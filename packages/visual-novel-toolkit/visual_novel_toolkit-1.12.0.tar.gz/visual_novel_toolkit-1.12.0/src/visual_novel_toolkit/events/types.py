from typing import NewType
from typing import TypeAlias
from typing import TypedDict


# Input.


GroupName = NewType("GroupName", str)


EventName = NewType("EventName", str)


class EventOptions(TypedDict, total=False):
    decision: str | None
    previous: EventName | list[EventName]


Events: TypeAlias = dict[GroupName, list[EventName | dict[EventName, EventOptions]]]


# Internal.


class Normalized(TypedDict):
    definitions: dict[EventName, bool]
    groups: dict[GroupName, list[EventName]]
    pairs: list[tuple[EventName, EventName, str | None]]
