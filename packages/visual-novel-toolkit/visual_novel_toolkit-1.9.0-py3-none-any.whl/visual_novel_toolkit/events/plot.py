from collections import defaultdict
from pathlib import Path
from random import choice
from string import ascii_lowercase

from yaml import CSafeLoader
from yaml import load

from .types import EventName
from .types import Events
from .types import GroupName
from .types import Normalized


def plot_events() -> None:
    data = Path("data")
    events_file = data / "events.yml"

    events: Events = load(events_file.read_text(), Loader=CSafeLoader)

    docs = Path("docs")
    docs.mkdir(exist_ok=True)

    mermaid_file = docs / "events.mmd"
    mermaid_file.write_text(plot(events))


def plot(events: Events) -> str:
    normalized = normalize(events)

    ids = lookup()

    lines = ["flowchart BT"]

    for group_name, event_list in normalized["definitions"].items():
        lines.append(f"  subgraph {group_name}")
        lines.append("    direction BT")
        for event_name in event_list:
            lines.append(f"    {ids[event_name]}[{event_name}]")
        lines.append("  end")
        lines.append("")

    for left, right in normalized["pairs"]:
        lines.append(f"  {ids[left]} --> {ids[right]}")

    return "\n".join(lines)


def normalize(events: Events) -> Normalized:
    definitions: dict[GroupName, list[EventName]] = {}
    pairs: list[tuple[EventName, EventName]] = []

    for group_name, event_list in events.items():
        group = definitions[group_name] = []
        name = None
        for event_name in event_list:
            if isinstance(event_name, dict):
                name = list(event_name)[0]
                options = event_name[name]
            elif isinstance(event_name, str):
                options = {"previous": name}
                name = event_name
            else:
                raise RuntimeError
            group.append(name)
            if options["previous"]:
                pairs.append((options["previous"], name))

    return {"definitions": definitions, "pairs": pairs}


def lookup() -> dict[str, str]:
    return defaultdict(lambda: "".join(choice(ascii_lowercase) for i in range(12)))
