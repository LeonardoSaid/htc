from typing import Optional, Union
from starlette.responses import JSONResponse


def json_response(data: Optional[Union[dict, list]] = None, messages: list = [], status_code: int = 200):
    return JSONResponse({
        "data": data,
        "messages": messages
    }, status_code=status_code)
