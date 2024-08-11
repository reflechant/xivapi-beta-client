from enum import Enum


class LanguageString(str, Enum):
    CHS = "chs"
    CHT = "cht"
    DE = "de"
    EN = "en"
    FR = "fr"
    JA = "ja"
    KR = "kr"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
