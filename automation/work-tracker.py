#!/usr/bin/env python3
"""
Work Tracker - Hold styr på hvad du arbejder på
================================================
Brug:
  python work-tracker.py                        # Vis dashboard
  python work-tracker.py add "Projekt" "Hvad"  # Tilføj nyt arbejde
  python work-tracker.py update "Projekt" "Ny status note"
  python work-tracker.py done "Projekt"         # Markér som færdig
  python work-tracker.py hold "Projekt"         # Sæt på pause
  python work-tracker.py resume "Projekt"       # Genoptag
  python work-tracker.py remove "Projekt"       # Fjern helt
  python work-tracker.py log "Projekt" "Note"   # Tilføj lognotat
"""

import json
import argparse
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_FILE = REPO_ROOT / ".work-data.json"
DASHBOARD_FILE = REPO_ROOT / "WORK-STATUS.md"

STATUS_ACTIVE = "aktiv"
STATUS_HOLD = "pause"
STATUS_DONE = "færdig"


# ── Data layer ──────────────────────────────────────────────────────────────

def load_data() -> dict:
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {"projects": []}


def save_data(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def find_project(data: dict, name: str) -> dict | None:
    name_lower = name.lower()
    for p in data["projects"]:
        if p["name"].lower() == name_lower:
            return p
    return None


def today() -> str:
    return date.today().strftime("%d %b %Y")


# ── Dashboard renderer ───────────────────────────────────────────────────────

def render_dashboard(data: dict) -> str:
    active = [p for p in data["projects"] if p["status"] == STATUS_ACTIVE]
    on_hold = [p for p in data["projects"] if p["status"] == STATUS_HOLD]
    done = [p for p in data["projects"] if p["status"] == STATUS_DONE]

    lines = [
        "# Work Status Dashboard",
        f"*Sidst opdateret: {today()}*",
        "",
    ]

    def table(projects: list) -> list[str]:
        rows = ["| Projekt | Hvad arbejder jeg på | Sidst opdateret |",
                "|---------|----------------------|-----------------|"]
        for p in projects:
            note = p.get("current_note", p["description"])
            rows.append(f"| **{p['name']}** | {note} | {p['last_updated']} |")
        return rows

    # Active
    lines.append("## Aktive projekter")
    if active:
        lines.extend(table(active))
    else:
        lines.append("*Ingen aktive projekter*")

    # On hold
    lines += ["", "## På pause"]
    if on_hold:
        lines.extend(table(on_hold))
    else:
        lines.append("*Ingen projekter på pause*")

    # Done (last 5)
    lines += ["", "## Nyligt afsluttet"]
    recent_done = sorted(done, key=lambda p: p["last_updated"], reverse=True)[:5]
    if recent_done:
        rows = ["| Projekt | Afsluttet |", "|---------|-----------|"]
        for p in recent_done:
            rows.append(f"| {p['name']} | {p['last_updated']} |")
        lines.extend(rows)
    else:
        lines.append("*Ingen afsluttede projekter endnu*")

    # Log entries (newest 10 across all projects)
    all_logs = []
    for p in data["projects"]:
        for entry in p.get("log", []):
            all_logs.append((entry["date"], p["name"], entry["note"]))
    all_logs.sort(reverse=True)

    if all_logs:
        lines += ["", "## Seneste aktivitet"]
        lines += ["| Dato | Projekt | Note |", "|------|---------|------|"]
        for d, name, note in all_logs[:10]:
            lines.append(f"| {d} | {name} | {note} |")

    lines.append("")
    lines.append("---")
    lines.append("*Opdater med: `python automation/work-tracker.py`*")

    return "\n".join(lines) + "\n"


def write_dashboard(data: dict) -> None:
    DASHBOARD_FILE.write_text(render_dashboard(data), encoding="utf-8")


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_show(data: dict) -> None:
    print(render_dashboard(data))


def cmd_add(data: dict, name: str, description: str) -> None:
    if find_project(data, name):
        print(f"Projekt '{name}' findes allerede. Brug 'update' for at ændre status.")
        sys.exit(1)
    data["projects"].append({
        "name": name,
        "description": description,
        "current_note": description,
        "status": STATUS_ACTIVE,
        "added": today(),
        "last_updated": today(),
        "log": [{"date": today(), "note": f"Startet: {description}"}],
    })
    save_data(data)
    write_dashboard(data)
    print(f"Tilføjet: '{name}' som aktivt projekt.")


def cmd_update(data: dict, name: str, note: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    p["current_note"] = note
    p["status"] = STATUS_ACTIVE
    p["last_updated"] = today()
    p.setdefault("log", []).append({"date": today(), "note": note})
    save_data(data)
    write_dashboard(data)
    print(f"Opdateret '{name}': {note}")


def cmd_log(data: dict, name: str, note: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    p["last_updated"] = today()
    p.setdefault("log", []).append({"date": today(), "note": note})
    save_data(data)
    write_dashboard(data)
    print(f"Log tilføjet til '{name}': {note}")


def cmd_done(data: dict, name: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    p["status"] = STATUS_DONE
    p["last_updated"] = today()
    p.setdefault("log", []).append({"date": today(), "note": "Markeret som færdig"})
    save_data(data)
    write_dashboard(data)
    print(f"'{name}' markeret som færdig.")


def cmd_hold(data: dict, name: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    p["status"] = STATUS_HOLD
    p["last_updated"] = today()
    p.setdefault("log", []).append({"date": today(), "note": "Sat på pause"})
    save_data(data)
    write_dashboard(data)
    print(f"'{name}' sat på pause.")


def cmd_resume(data: dict, name: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    p["status"] = STATUS_ACTIVE
    p["last_updated"] = today()
    p.setdefault("log", []).append({"date": today(), "note": "Genoptaget"})
    save_data(data)
    write_dashboard(data)
    print(f"'{name}' genoptaget.")


def cmd_remove(data: dict, name: str) -> None:
    p = find_project(data, name)
    if not p:
        print(f"Projekt '{name}' ikke fundet.")
        sys.exit(1)
    data["projects"].remove(p)
    save_data(data)
    write_dashboard(data)
    print(f"'{name}' fjernet.")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Work Tracker - hold styr på dine projekter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="Vis dashboard (standard)")

    p_add = sub.add_parser("add", help="Tilføj nyt projekt")
    p_add.add_argument("name", help="Projektnavn")
    p_add.add_argument("description", help="Hvad arbejder du på?")

    p_update = sub.add_parser("update", help="Opdater status")
    p_update.add_argument("name")
    p_update.add_argument("note", help="Hvad er status nu?")

    p_log = sub.add_parser("log", help="Tilføj lognotat uden at ændre status")
    p_log.add_argument("name")
    p_log.add_argument("note")

    p_done = sub.add_parser("done", help="Markér som færdig")
    p_done.add_argument("name")

    p_hold = sub.add_parser("hold", help="Sæt på pause")
    p_hold.add_argument("name")

    p_resume = sub.add_parser("resume", help="Genoptag projekt")
    p_resume.add_argument("name")

    p_remove = sub.add_parser("remove", help="Fjern projekt helt")
    p_remove.add_argument("name")

    args = parser.parse_args()
    data = load_data()

    match args.command:
        case "add":
            cmd_add(data, args.name, args.description)
        case "update":
            cmd_update(data, args.name, args.note)
        case "log":
            cmd_log(data, args.name, args.note)
        case "done":
            cmd_done(data, args.name)
        case "hold":
            cmd_hold(data, args.name)
        case "resume":
            cmd_resume(data, args.name)
        case "remove":
            cmd_remove(data, args.name)
        case _:
            cmd_show(data)


if __name__ == "__main__":
    main()
