from typing import List, Union

from botocore.response import StreamingBody
from mypy_boto3_s3 import S3Client
from mypy_boto3_s3.type_defs import DeleteObjectOutputTypeDef, PutObjectOutputTypeDef
from mypy_boto3_secretsmanager import SecretsManagerClient
from mypy_boto3_ses import SESClient
from mypy_boto3_ses.type_defs import SendEmailResponseTypeDef
from mypy_boto3_sqs import SQSClient
from mypy_boto3_sqs.type_defs import SendMessageResultTypeDef
from pydantic import EmailStr as EmailStr

from ..custom_types import HttpError as HttpError
from ..http_return import http_error as http_error

e: List[str]

def get_secret_string(
    secrets_manager_client: SecretsManagerClient, secret_id: str
) -> Union[str, HttpError]: ...
def get_secret_binary(
    secrets_manager_client: SecretsManagerClient, secret_id: str
) -> Union[bytes, HttpError]: ...
def s3_get_object_stream(
    s3_client: S3Client, s3_bucket: str, s3_key: str
) -> Union[StreamingBody, HttpError]: ...
def s3_get_object_bytes(
    s3_client: S3Client, s3_bucket: str, s3_key: str
) -> Union[bytes, HttpError]: ...
def s3_put_object_bytes(
    s3_client: S3Client, s3_bucket: str, s3_key: str, s3_body_bytes: bytes
) -> Union[PutObjectOutputTypeDef, HttpError]: ...
def s3_delete_object(
    s3_client: S3Client, s3_bucket: str, s3_key: str
) -> Union[DeleteObjectOutputTypeDef, HttpError]: ...
def sqs_send_message_fifo(
    sqs_client: SQSClient,
    sqs_queue_url: str,
    sqs_message_body: str,
    sqs_message_group_id: str,
) -> Union[SendMessageResultTypeDef, HttpError]: ...
def ses_send_email(
    ses_client: SESClient,
    ses_from_email: EmailStr,
    ses_to_emails: List[EmailStr],
    ses_email_subject: str,
    ses_email_body: str,
) -> Union[SendEmailResponseTypeDef, HttpError]: ...
