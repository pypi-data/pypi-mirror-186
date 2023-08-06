import logging
from ..aws_operations import (
    get_secret_binary as get_secret_binary,
    s3_get_object_bytes as s3_get_object_bytes,
    s3_put_object_bytes as s3_put_object_bytes,
    ses_send_email as ses_send_email,
)
from ..custom_types import (
    AuthClients as AuthClients,
    AuthConfig as AuthConfig,
    CategorySummaries as CategorySummaries,
    CategorySummary as CategorySummary,
    CustomError as CustomError,
    EmailDomainAndOrgId as EmailDomainAndOrgId,
    EmptyEvaluation as EmptyEvaluation,
    EvaluationSummaries as EvaluationSummaries,
    EvaluationSummary as EvaluationSummary,
    HttpError as HttpError,
    HttpSuccess as HttpSuccess,
    JwtParam as JwtParam,
    LoginHash as LoginHash,
    MagicLinkDomain as MagicLinkDomain,
    MagicLinkDto as MagicLinkDto,
    MagicLinkInternal as MagicLinkInternal,
    RoleEnum as RoleEnum,
    UserEmailAndId as UserEmailAndId,
    WhoAmI as WhoAmI,
)
from ..eid import (
    get_eval_eid as get_eval_eid,
    get_org_eid as get_org_eid,
    get_user_eid as get_user_eid,
)
from ..http_return import (
    http_200_json as http_200_json,
    http_400_json as http_400_json,
    http_403_json as http_403_json,
    http_500_json as http_500_json,
    http_error as http_error,
    http_error_to_json_response as http_error_to_json_response,
)
from botocore.client import Config as Boto3Config
from ecdsa import SigningKey as SigningKey, VerifyingKey as VerifyingKey
from fastapi import APIRouter, Request as Request
from fastapi.responses import JSONResponse as JSONResponse
from mypy_boto3_s3.type_defs import PutObjectOutputTypeDef
from mypy_boto3_secretsmanager import SecretsManagerClient
from pydantic import EmailStr
from typing import Any, Dict, List, Union

LOG: logging.Logger

class Auth:
    default_algorithm: str
    default_boto3_config: Boto3Config
    clients: AuthClients
    config: AuthConfig
    boto3_config: Boto3Config
    router: APIRouter
    def __init__(self, config: AuthConfig, boto3_config=...) -> None: ...
    @staticmethod
    def get_signing_key(
        secrets_manager_client: SecretsManagerClient, secret_id: str
    ) -> Union[SigningKey, HttpError]: ...
    @staticmethod
    def create_jwt(
        jwt_param: JwtParam,
        signing_key: SigningKey,
        audience: str,
        issuer: str,
        exp_days: int,
        algorithm: str = ...,
    ) -> Union[str, CustomError]: ...
    @staticmethod
    def decode_jwt(
        jwt_string: str,
        verifying_key: VerifyingKey,
        audience: str,
        algorithm: str = ...,
    ) -> Union[Dict[str, Any], CustomError]: ...
    @staticmethod
    def get_jwt_token_from_cookies(
        cookies: Dict[str, Any], jwt_name: str
    ) -> Union[str, CustomError]: ...
    @staticmethod
    def get_jwt_field_from_cookies(
        cookies: Dict[str, Any],
        jwt_name: str,
        verifying_key: VerifyingKey,
        audience: str,
        jwt_field_name: str,
    ) -> Union[str, CustomError]: ...
    @staticmethod
    def get_jwt_fields_from_cookies(
        cookies: Dict[str, Any],
        jwt_name: str,
        verifying_key: VerifyingKey,
        audience: str,
        jwt_field_names: List[str],
    ) -> Union[List[str], List[CustomError]]: ...
    @staticmethod
    def get_user_email_from_cookies(
        cookies: Dict[str, Any],
        jwt_name: str,
        verifying_key: VerifyingKey,
        audience: str,
    ) -> Union[str, CustomError]: ...
    @staticmethod
    def get_user_role_from_cookies(
        cookies: Dict[str, Any],
        jwt_name: str,
        verifying_key: VerifyingKey,
        audience: str,
    ) -> Union[str, CustomError]: ...
    @staticmethod
    def get_cookie_domain_from_cors(cors_allow_origin: str) -> str: ...
    def convert_magic_link_domain_to_internal(
        self, magic_link: MagicLinkDomain, source_ip: str
    ) -> MagicLinkInternal: ...
    def save_magic_link_internal_to_s3(
        self, magic_link_internal: MagicLinkInternal, utc_now_str: str
    ) -> Union[HttpSuccess, HttpError]: ...
    def render_email_body(
        self, magic_link_internal: MagicLinkInternal
    ) -> Union[str, CustomError]: ...
    def get_hash_from_s3(
        self, login_hash: LoginHash
    ) -> Union[MagicLinkInternal, HttpError]: ...
    @staticmethod
    def magic_link_dto_to_domain(
        magic_link_dto: MagicLinkDto,
    ) -> Union[MagicLinkDomain, CustomError]: ...
    async def send_magic_link(
        self, magic_link_dto: MagicLinkDto, request: Request
    ) -> JSONResponse: ...
    def set_cookie_with_domain_on_response(
        self,
        cookie_domain: str,
        http_response: JSONResponse,
        jwt_token: str,
        max_age: int,
    ) -> JSONResponse: ...
    def verify_email_domain(
        self, email_address: EmailStr
    ) -> Union[bool, CustomError]: ...
    def get_organization_id_for_user(
        self, email_address: EmailStr
    ) -> Union[str, CustomError]: ...
    def put_user_email_and_id(
        self, email_address: EmailStr, user_id: str, org_id: str
    ) -> Union[PutObjectOutputTypeDef, CustomError]: ...
    def put_category_summaries(
        self, user_id: str
    ) -> Union[PutObjectOutputTypeDef, CustomError]: ...
    def put_favorite_drinks_eval_summary(
        self, user_id: str, eval_id: str
    ) -> Union[PutObjectOutputTypeDef, CustomError]: ...
    def put_favorite_drinks_eval(
        self, eval_id: str
    ) -> Union[PutObjectOutputTypeDef, CustomError]: ...
    def put_empty_eval_summaries(self, user_id: str) -> Union[None, CustomError]: ...
    def create_user(self, email_address: EmailStr, user_id: str, org_id: str): ...
    def get_user_id_for_user(
        self, org_id: str, email_address: EmailStr
    ) -> Union[str, CustomError]: ...
    async def login(self, login_hash: LoginHash) -> JSONResponse: ...
    async def logout(self) -> JSONResponse: ...
    async def get_who_am_i(self, request: Request) -> JSONResponse: ...
