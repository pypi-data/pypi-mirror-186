from ..aws_operations import (
    s3_put_object_bytes as s3_put_object_bytes,
    sqs_send_message_fifo as sqs_send_message_fifo,
)
from ..custom_types import HttpError as HttpError
from mypy_boto3_s3 import S3Client
from mypy_boto3_sqs import SQSClient
from typing import Union

def save_to_s3_and_send_sqs_update(
    s3_client: S3Client,
    s3_bucket: str,
    s3_key: str,
    s3_body_bytes: bytes,
    sqs_client: SQSClient,
    sqs_queue_url: str,
    sqs_message_body: str,
    sqs_message_group_id: str,
) -> Union[bool, HttpError]: ...
