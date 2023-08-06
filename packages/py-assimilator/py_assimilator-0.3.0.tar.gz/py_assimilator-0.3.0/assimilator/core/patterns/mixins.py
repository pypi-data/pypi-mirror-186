import json
from typing import Type, TypeVar

from pydantic import ValidationError, BaseModel

from assimilator.core.exceptions import ParsingError


T = TypeVar("T", bound=BaseModel)


class JSONParsedMixin:
    @classmethod
    def from_json(cls: Type[T], data: str) -> T:
        try:
            return cls(**json.loads(data))
        except ValidationError as exc:
            raise ParsingError(exc)


__all__ = [
    'JSONParsedMixin',
]
