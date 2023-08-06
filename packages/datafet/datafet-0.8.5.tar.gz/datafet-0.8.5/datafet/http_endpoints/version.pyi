from typing import Union

from _typeshed import Incomplete
from pydantic import BaseModel

def get_current_version() -> Union[str, None]: ...

class Version(BaseModel):
    version: str

async def get_version(): ...
