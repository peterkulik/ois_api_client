from typing import Optional, Callable


def create_enum(enum: Callable, value: Optional[str]):
    return value and enum(value)
