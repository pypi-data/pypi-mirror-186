from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class UserSummaryWithTypeType(Enums.KnownString):
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "UserSummaryWithTypeType":
        if not isinstance(val, str):
            raise ValueError(f"Value of UserSummaryWithTypeType must be a string (encountered: {val})")
        newcls = Enum("UserSummaryWithTypeType", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(UserSummaryWithTypeType, getattr(newcls, "_UNKNOWN"))
