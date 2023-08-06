from http import HTTPStatus
import io
import json
import urllib

import requests
from requests.auth import HTTPBasicAuth

from autumn8.lib.api_creds import retrieve_api_creds
from autumn8.cli.cli_environment import CliEnvironment
from autumn8.common.config.s3 import init_s3_client, init_s3

import appdirs
import os
from pathlib import Path
import pickle

from tqdm import tqdm

APP_NAME = "autumn8"
APP_AUTHOR = "autumn8"

data_dir = appdirs.user_data_dir(APP_NAME, APP_AUTHOR)


def retrieve_pending_uploads():
    path = os.path.join(data_dir, "uploads.pickle")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    return {}


def update_upload(run_id, resume_args):
    path = os.path.join(data_dir, "uploads.pickle")
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = pickle.load(f)

        data[run_id] = resume_args

        with open(path, "wb") as f:
            pickle.dump(data, f)
    else:
        data_path = Path(data_dir)
        data_path.mkdir(parents=True, exist_ok=True)
        data = {run_id: resume_args}

        with open(path, "wb") as f:
            pickle.dump(data, f)


def remove_upload(run_id):
    path = os.path.join(data_dir, "uploads.pickle")
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = pickle.load(f)

        resume_args = data[run_id]
        environment = resume_args["environment"]
        if (
            "model_file_upload_id" in resume_args
            and resume_args["model_file_upload_id"] is not None
        ):
            abort_upload(environment, resume_args["model_file_upload_id"])

        if (
            "input_file_upload_id" in resume_args
            and resume_args["input_file_upload_id"] is not None
        ):
            abort_upload(environment, resume_args["input_file_upload_id"])

        data.pop(run_id)

        with open(path, "wb") as f:
            pickle.dump(data, f)


def abort_upload(environment, id):
    s3 = init_s3_client(environment.value["s3_host"])
    s3_bucket_name = environment.value["s3_bucket_name"]
    mpus = s3.list_multipart_uploads(Bucket=s3_bucket_name)
    if "Uploads" in mpus:
        for upload in mpus["Uploads"]:
            upload_id = upload["UploadId"]
            key = upload["Key"]
            if upload_id == id:
                s3.abort_multipart_upload(
                    Bucket=s3_bucket_name, Key=key, UploadId=upload_id
                )


def url_with_params(url, params):
    url_parse = urllib.parse.urlparse(url)
    url_new_query = urllib.parse.urlencode(params)
    url_parse = url_parse._replace(query=url_new_query)

    new_url = urllib.parse.urlunparse(url_parse)
    return new_url


def require_ok_response(response):
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise Exception(
            f"Received response {response.status_code}:\n{response.text}\n\nUser not authenticated; please run `autumn8-cli login` to authorize your CLI"
        )
    if response.status_code != HTTPStatus.OK:
        raise Exception(
            f"Received response {response.status_code}:\n{response.text}"
        )


def fetch_user_data(environment: CliEnvironment):
    user_id, api_key = None, None
    autodl_host = environment.value["host"]
    try:
        user_id, api_key = retrieve_api_creds()
    except:
        raise Exception(
            f"API key is missing! To configure API access, please visit {autodl_host}/profile and generate an API key, then run `autumn8-cli login`"
        )

    user_api_route = f"{autodl_host}/api/user"
    response = requests.get(
        user_api_route,
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(user_id, api_key),
    )

    require_ok_response(response)
    return json.loads(response.text)["user"]


def post_model(environment, organization_id, model_config):
    autodl_host = environment.value["host"]
    api_route = f"{autodl_host}/api/lab/model"
    print("Submitting model to", api_route)
    response = requests.post(
        url_with_params(api_route, {"organization_id": organization_id}),
        headers={"Content-Type": "application/json"},
        data=json.dumps(model_config),
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )

    require_ok_response(response)
    return response.json()["id"]


def delete_model(environment, organization_id, model_id):
    autodl_host = environment.value["host"]
    new_url = url_with_params(
        f"{autodl_host}/api/lab/model",
        {"model_id": model_id, "organization_id": organization_id},
    )
    response = requests.delete(
        new_url,
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )
    require_ok_response(response)


def normal_or_multipart_upload(
    environment,
    S3,
    s3_bucket_name,
    s3_file_url,
    f,
    resume_args,
    id_key,
    mpu_id=None,
):
    f.seek(0, 2)  # seek to end of file
    total_bytes = f.tell()
    f.seek(0)
    # AWS dissallow multipart upload of files under 5MB
    if total_bytes < 6 * 1024**2:
        normal_upload(environment, s3_bucket_name, s3_file_url, f)
    else:
        multipart_upload(
            S3, s3_bucket_name, s3_file_url, f, resume_args, id_key, mpu_id
        )


def normal_upload(environment, s3_bucket_name, s3_file_url, f):
    S3 = init_s3(environment.value["s3_host"])
    S3.Bucket(s3_bucket_name).Object(s3_file_url).upload_fileobj(f)


def get_uploaded_parts(S3, s3_bucket_name, s3_file_url, upload_id):
    parts = []
    res = S3.list_parts(
        Bucket=s3_bucket_name, Key=s3_file_url, UploadId=upload_id
    )
    if "Parts" in res:
        for p in res["Parts"]:
            parts.append(p)
    return parts


def multipart_upload(
    S3, s3_bucket_name, s3_file_url, f, resume_args, id_key, mpu_id=None
):
    f.seek(0, 2)  # seek to end of file
    total_bytes = f.tell()
    f.seek(0)  # seek to start of file
    part_bytes = 10 * 1024**2  # minimum part size on aws is 5MB
    uploaded_bytes = 0

    if mpu_id != None:
        print(f"Resuming upload with id {mpu_id}")
        parts = get_uploaded_parts(S3, s3_bucket_name, s3_file_url, mpu_id)
    else:
        parts = []
        mpu = S3.create_multipart_upload(Bucket=s3_bucket_name, Key=s3_file_url)
        mpu_id = mpu["UploadId"]
        print(f"Created new multipart upload with id {mpu_id}")

    resume_args[id_key] = mpu_id
    update_upload(resume_args["run_id"], resume_args)

    for i in tqdm(range(1, total_bytes // part_bytes + 2)):
        data = f.read(part_bytes)
        if not len(data):
            break

        if len(parts) >= i:
            print("Part already uploaded")
            part = parts[i - 1]
            if len(data) != part["Size"]:
                raise Exception(
                    "Size mismatch: local "
                    + str(len(data))
                    + ", remote: "
                    + part["Size"]
                )
            parts[i - 1] = {k: part[k] for k in ("PartNumber", "ETag")}
        else:
            part = S3.upload_part(
                Body=data,
                Bucket=s3_bucket_name,
                Key=s3_file_url,
                UploadId=mpu_id,
                PartNumber=i,
            )
            parts.append({"PartNumber": i, "ETag": part["ETag"]})

        uploaded_bytes += len(data)
        i += 1

    S3.complete_multipart_upload(
        Bucket=s3_bucket_name,
        Key=s3_file_url,
        UploadId=mpu_id,
        MultipartUpload={"Parts": parts},
    )


def post_model_file(
    environment,
    bytes_or_filepath,
    s3_file_url,
    resume_args,
    id_key,
    upload_id=None,
):
    S3 = init_s3_client(environment.value["s3_host"])
    s3_bucket_name = environment.value["s3_bucket_name"]
    if isinstance(bytes_or_filepath, io.BytesIO):
        f = bytes_or_filepath
        normal_or_multipart_upload(
            environment,
            S3,
            s3_bucket_name,
            s3_file_url,
            f,
            resume_args,
            id_key,
            upload_id,
        )
    else:
        with open(bytes_or_filepath, "rb") as f:
            normal_or_multipart_upload(
                environment,
                S3,
                s3_bucket_name,
                s3_file_url,
                f,
                resume_args,
                id_key,
                upload_id,
            )


def async_prediction(environment, organization_id, model_id):
    autodl_host = environment.value["host"]
    new_url = url_with_params(
        f"{autodl_host}/api/lab/model/async_prediction",
        {
            "model_id": model_id,
            "organization_id": organization_id,
        },
    )
    response = requests.post(
        new_url,
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )
    require_ok_response(response)
    return response
