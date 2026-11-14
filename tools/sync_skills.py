"""Copy canonical project skills to the two supported client discovery directories."""
from __future__ import annotations

import shutil
from pathlib import Path

from check_skill import check

PROJECT = Path(__file__).resolve().parents[1]


def main() -> int:
    sources = sorted(path.parent for path in (PROJECT / "skills").glob("*/SKILL.md"))
    for source in sources:
        errors = check(source)
        if errors:
            raise SystemExit(f"Fix {source.name} before syncing: {'; '.join(errors)}")
        if any(path.is_symlink() for path in source.rglob("*")):
            raise SystemExit(f"Use ordinary files in this portable release: {source}")
    for source in sources:
        for directory in (".agents/skills", ".claude/skills"):
            target = PROJECT / directory / source.name
            if not target.resolve().is_relative_to(PROJECT):
                raise SystemExit(f"Destination escapes the project: {target}")
            if target.exists() and any(p.is_symlink() for p in target.rglob("*")):
                raise SystemExit(f"Replace symlinks with ordinary project files: {target}")
            shutil.copytree(source, target, dirs_exist_ok=True)
            print(f"Copied {source.name} -> {directory}/{source.name}")
    print("Edit skills/ as the canonical source, then run this command again.")
    print("No home-directory skills, accounts, or global settings were changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
