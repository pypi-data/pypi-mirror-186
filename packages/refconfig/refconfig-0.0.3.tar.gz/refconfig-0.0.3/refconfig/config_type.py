from enum import Enum
from typing import Union


class CType(Enum):
    YAML = 1
    JSON = 2
    RAW = 3
    SMART = -1


CType_str = []
CType_int = []
CType_CType = []

for item in CType.__members__.items():
    CType_str.append(item[0])
    CType_CType.append(item[1])
    CType_int.append(item[1].value)

error = ValueError(f'Config type is restricted in {CType_str}')


def parse_type(t: Union[str, int, CType]):
    if isinstance(t, str):
        assert t.upper() in CType_str, error
        return CType.__getitem__(t.upper())
    if isinstance(t, int):
        assert t in CType_int, error
        return CType(t)
    if isinstance(t, CType):
        return t
    raise error


if __name__ == '__main__':
    print(parse_type(-2))
