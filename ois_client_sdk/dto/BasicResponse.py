from dataclasses import dataclass
from typing import Union


@dataclass
class BasicResult:
    func_code: str
    error_code: Union[str, None]
    message: Union[str, None]


@dataclass
class BasicResponse:
    result: BasicResult
