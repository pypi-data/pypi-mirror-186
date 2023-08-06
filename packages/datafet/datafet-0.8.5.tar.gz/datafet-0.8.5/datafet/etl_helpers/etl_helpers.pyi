import datetime
from jinja2 import Template as Template
from mypy_boto3_athena.client import AthenaClient
from mypy_boto3_s3.service_resource import (
    Bucket,
    ObjectSummary,
    S3ServiceResource as S3ServiceResource,
)
from typing import Callable, Dict, Generator, List, Tuple

def chunks(lst: List, n: int) -> List[List]: ...
def get_args(argv: List) -> Dict: ...
def get_arg_or_def(args: Dict, arg_name: str, def_val: str) -> str: ...
def now() -> str: ...
def utc_now() -> str: ...
def get_min_max(
    dt: datetime.datetime,
) -> Tuple[datetime.datetime, datetime.datetime]: ...
def set_boto_session(
    logger: Callable[[str], Tuple[int, str]],
    is_cloud: bool = ...,
    profile_name: str = ...,
    region_name: str = ...,
): ...
def create_query_exectution_with_athena(
    logger: Callable[[str], Tuple[int, str]],
    athena_client: AthenaClient,
    query: str,
    catalog: str,
    database: str,
    workgroup: str,
): ...

LOOP_COUNTER_TO_SLOW_DOWN: int
SHORT_SLEEP: int
LONG_SLEEP: int

def wait_for_query_results(
    logger: Callable[[str], Tuple[int, str]],
    athena_ui_base_url: str,
    athena_client: AthenaClient,
    query_execution: Dict,
): ...
def get_previous_day(n: int) -> datetime.datetime: ...
def get_first_and_last_moment_of_a_day(
    dt: datetime.datetime,
) -> Tuple[datetime.datetime, datetime.datetime]: ...
def get_all_objects_generator(
    bucket: Bucket, logs_prefix: str
) -> Generator[ObjectSummary, None, None]: ...
def is_object_created_at(
    s3_object: ObjectSummary, day_min_max: Tuple[datetime.datetime, datetime.datetime]
) -> bool: ...
def get_filtered_objects_generator(
    objects_generator: Generator[ObjectSummary, None, None],
    day_min_max: Tuple[datetime.datetime, datetime.datetime],
) -> Generator: ...
def get_downloaded_unzipped_content_generator(
    s3_objects_generator: Generator[ObjectSummary, None, None]
) -> Generator[bytes, None, None]: ...
def get_split_lines_generator(
    file_content_generator: Generator[bytes, None, None]
) -> Generator[List[str], None, None]: ...
def get_split_fields_generator(
    split_lines_generator: Generator[List[str], None, None]
) -> Generator[List[str], None, None]: ...
def get_all_objects_with_predicate_generator(
    bucket: Bucket, prefix: str, predicate_fn: Callable[[ObjectSummary], bool]
): ...
