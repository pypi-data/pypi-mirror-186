from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class TeamSummaryWithTypeType(Enums.KnownString):
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "TeamSummaryWithTypeType":
        if not isinstance(val, str):
            raise ValueError(f"Value of TeamSummaryWithTypeType must be a string (encountered: {val})")
        newcls = Enum("TeamSummaryWithTypeType", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(TeamSummaryWithTypeType, getattr(newcls, "_UNKNOWN"))
