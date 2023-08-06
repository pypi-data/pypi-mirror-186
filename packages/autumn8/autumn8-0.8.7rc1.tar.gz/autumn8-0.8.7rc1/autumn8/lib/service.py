import io
import os
import uuid
from pathlib import Path
from typing import Optional

from autumn8.lib import api


def resume_upload_model(upload_task):
    return upload_model(**upload_task)


def upload_model(
    environment,
    organization_id,
    model_config,
    model_file,
    input_file_path: Optional[str],
    model_file_upload_id: Optional[str] = None,
    input_file_upload_id: Optional[str] = None,
    run_id: Optional[str] = None,
    **kwargs,
):
    if run_id is None:  # used for resuming upload
        run_id = str(uuid.uuid4())
    function_args = locals()
    autodl_host = environment.value["host"]
    if type(model_file) == io.BytesIO:
        model_file.seek(0)
        model_file_name = model_config["name"]  # TODO add extension?
    else:
        model_file_name = os.path.basename(model_file)

    s3_bucket_name = environment.value["s3_bucket_name"]
    model_type = "" if "model_type" not in kwargs else kwargs["model_type"]

    if "s3_file_url" not in kwargs:
        additional_extension = (
            f".{model_type}" if model_type is not None else ""
        )
        s3_file_url = f"{s3_bucket_name}/models/{organization_id}-{uuid.uuid4()}-{model_file_name}{additional_extension}"
        function_args["s3_file_url"] = s3_file_url
    else:
        s3_file_url = kwargs["s3_file_url"]

    print("Uploading the model files...")
    api.lab.post_model_file(
        environment,
        model_file,
        s3_file_url,
        function_args,
        "model_file_upload_id",
        model_file_upload_id,
    )
    model_config["s3_file_url"] = s3_file_url

    if input_file_path != None and len(input_file_path) > 0:
        filename = Path(input_file_path).name
        if "s3_input_file_url" not in kwargs:
            s3_input_file_url = f"{s3_bucket_name}/inputs/{organization_id}-{uuid.uuid4()}-{filename}"
            function_args["s3_input_file_url"] = s3_input_file_url
        else:
            s3_input_file_url = kwargs["s3_input_file_url"]
        print("Uploading the input files...")
        api.lab.post_model_file(
            environment,
            input_file_path,
            s3_input_file_url,
            function_args,
            "input_file_upload_id",
            input_file_upload_id,
        )
        model_config["s3_input_file_url"] = s3_input_file_url

    print("Creating the model entry in AutoDL...")
    model_id = api.lab.post_model(environment, organization_id, model_config)
    api.lab.remove_upload(run_id)

    print("Starting up performance predictor...")
    api.lab.async_prediction(environment, organization_id, model_id)
    return f"{autodl_host}/{organization_id}/performancePredictor/dashboard/{model_id}"
