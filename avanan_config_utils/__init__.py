import json

import boto3


def get_config_dict(file_path, bucket_name=None):
    """Reads file, loads JSON from it and return

    :param file_path: This can be a local file path or name of key stored in S3 bucket
    :param bucket_name: If this parameter is passed, file is downloaded from given bucket
    """
    if not bucket_name:
        file_content = open(file_path).read()
        return json.loads(file_content)
    s3 = boto3.resource('s3')
    s3_obj = s3.Object(bucket_name, file_path)
    body = s3_obj.get()['Body'].read()
    return json.loads(body)
