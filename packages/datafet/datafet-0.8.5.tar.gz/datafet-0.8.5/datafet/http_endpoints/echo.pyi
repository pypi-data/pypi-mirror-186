from _typeshed import Incomplete
from fastapi import Request as Request
from fastapi.responses import JSONResponse

def get_echo(request: Request) -> JSONResponse: ...
