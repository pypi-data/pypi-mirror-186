import os

import boto3
import boto3.session

AUTODL_S3_REGION = "us-east-1"


def init_s3(s3_host):
    # TODO - we need to somehow include these in CLI without hardcoding

    # AWS_ACCESS_KEY_ID = os.environ["NEXT_PUBLIC_AWS_ACCESS_KEY_ID"]
    # AWS_SECRET_ACCESS_KEY = os.environ["NEXT_PUBLIC_AWS_SECRET_KEY"]
    AWS_ACCESS_KEY_ID = "AKIASO72NKUYW7ONNRFO"
    AWS_SECRET_ACCESS_KEY = "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"

    return boto3.resource(
        "s3",
        region_name=AUTODL_S3_REGION,
        endpoint_url=s3_host,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )


def init_s3_client(s3_host):
    # AWS_ACCESS_KEY_ID = os.environ["NEXT_PUBLIC_AWS_ACCESS_KEY_ID"]
    # AWS_SECRET_ACCESS_KEY = os.environ["NEXT_PUBLIC_AWS_SECRET_KEY"]
    AWS_ACCESS_KEY_ID = "AKIASO72NKUYW7ONNRFO"
    AWS_SECRET_ACCESS_KEY = "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"

    return boto3.session.Session().client(
        "s3",
        region_name=AUTODL_S3_REGION,
        endpoint_url=s3_host,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )


_S3 = None

# TODO flatten and reorganize our S3 structure
# right now, there's three places that attempt to determine the target bucket
# and all of these stack upon each other in the resulting url:
# - this endpoint already includes the bucket name, so the bucket is predetermined for this endpoint
# - when calling S3.Bucket(name), we also provide another bucket name for the url
# - finally, the bucket name is appended to the s3_file_url attribute somewhere during the upload
def get_s3_client():
    global _S3
    if _S3 is None:
        _S3 = init_s3(os.environ.get("NEXT_PUBLIC_AWS_S3_ENDPOINT"))

    return _S3
