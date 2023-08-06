from typing import NewType
from typing import TypeAlias
from typing import TypedDict


# Input.


GroupName = NewType("GroupName", str)


EventName = NewType("EventName", str)


class EventOptions(TypedDict):
    previous: EventName | None


Events: TypeAlias = dict[GroupName, list[EventName | dict[EventName, EventOptions]]]


# Internal.


class Normalized(TypedDict):
    definitions: dict[GroupName, list[EventName]]
    pairs: list[tuple[EventName, EventName]]
