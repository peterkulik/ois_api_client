from collections import Callable
from typing import Optional


def create_enum(enum: Callable, value: Optional[str]):
    return value and enum(value)
