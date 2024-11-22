from typing import NamedTuple


class Request(NamedTuple):
    key: str
    move: str
    value: int