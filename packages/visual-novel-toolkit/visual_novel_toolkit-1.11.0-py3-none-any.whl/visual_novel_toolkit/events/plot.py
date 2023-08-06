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

    for group_name, event_list in normalized["groups"].items():
        lines.append(f"  subgraph {group_name}")
        lines.append("    direction BT")
        for event_name in event_list:
            if normalized["definitions"][event_name]:
                left, right = "{{", "}}"
            else:
                left, right = "[", "]"
            lines.append(f"    {ids[event_name]}{left}{event_name}{right}")
        lines.append("  end")
        lines.append("")

    for left, right, decision in normalized["pairs"]:
        sep = f"-- {decision} " if decision is not None else ""
        lines.append(f"  {ids[left]} {sep}--> {ids[right]}")

    return "\n".join(lines)


def normalize(events: Events) -> Normalized:
    definitions: dict[EventName, bool] = {}
    groups: dict[GroupName, list[EventName]] = {}
    pairs: list[tuple[EventName, EventName, str | None]] = []

    for group_name, event_list in events.items():
        group = groups[group_name] = []
        for event_name in event_list:
            if isinstance(event_name, dict):
                name = list(event_name.keys())[0]
                options = list(event_name.values())[0]
                if "previous" not in options:
                    previous = [group[-1]] if group else []
                elif isinstance(options["previous"], str):
                    previous = [options["previous"]]
                elif isinstance(options["previous"], list):
                    previous = options["previous"]
                else:
                    raise RuntimeError
            elif isinstance(event_name, str):
                name = event_name
                options = {}
                previous = [group[-1]] if group else []
            else:
                raise RuntimeError
            definitions[name] = False
            group.append(name)
            if previous:
                if "decision" in options:
                    for each in previous:
                        definitions[each] = True
                    decision = options["decision"]
                else:
                    decision = None
                for each in previous:
                    pairs.append((each, name, decision))

    return {"definitions": definitions, "groups": groups, "pairs": pairs}


def lookup() -> dict[str, str]:
    return defaultdict(lambda: "".join(choice(ascii_lowercase) for i in range(12)))
