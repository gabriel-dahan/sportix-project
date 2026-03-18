from abc import ABC
import datetime

from .base_match import _Match


class _Player(ABC):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birthdate: datetime.date | None,
                 height: float | None,
                 weight: float | None,
                 country: str | None,
                 sport: str
                 ) -> None:

        self.first_name = first_name
        self.last_name = last_name

        self._birthdate = birthdate
        self._height = height
        self._weight = weight
        self._country = country

        self.sport = sport

        self._matches: list[_Match] = []

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def birthdate(self) -> datetime.date | None:
        return self._birthdate

    @property
    def height(self) -> float | None:
        return self._height

    @property
    def weight(self) -> float | None:
        return self._weight

    @property
    def country(self) -> str | None:
        return self._country

    @property
    def matches(self, _sorted: bool = True, key: str = "birthdate") -> list["_Match"]:
        if _sorted:
            return sorted(self._matches)
        return self._matches

    def add_matches(self, matches: list["_Match"]) -> None:
        """ Adds a list of matches to the player's played matches (sorts the ) """

        ...

    def matches_history(self) -> list["_Match"]:
        ...

    def show_last_matches(self, n: int = 5) -> None:
        lines = [
            "--------------- LAST MATCHES ---------------",
            "|                                          |",
        ]
        return "\n".join(lines)

    def get_winrate(self) -> float:
        ...

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return ""
