"""Check a portable course skill's basic structure; this does not test its behaviour."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


def check(folder: Path) -> list[str]:
    errors = []
    source = folder / "SKILL.md"
    if not source.is_file():
        return [f"Missing {source}"]
    text = source.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    if not match:
        return ["SKILL.md must start with --- frontmatter --- and a body."]
    fields = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator or key.strip() not in {"name", "description"}:
            errors.append("For this exercise use only name and description, each on one line.")
            continue
        value = value.strip()
        quoted = len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'"
        if not quoted and (": " in value or " #" in value or (value and value[0] in "[{}]!&*?|>@`")):
            errors.append("Quote a frontmatter value containing YAML punctuation; use a single-line string.")
        fields[key.strip()] = value[1:-1] if quoted else value
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z][a-z0-9-]{0,63}", name):
        errors.append("Use a lowercase name with letters, numbers and hyphens, maximum 64 characters.")
    if name != folder.name:
        errors.append("The skill folder and frontmatter name must match.")
    if len(fields.get("description", "")) < 20 or fields.get("description") in {"|", ">"}:
        errors.append("Write a meaningful one-line description saying when to use the skill.")
    if len(text[match.end():].strip()) < 80:
        errors.append("Write the workflow in the skill body.")
    if re.search(r"\b(?:TODO|YOUR[_ -]TEXT|FILL[_ -]THIS)\b", text):
        errors.append("Replace template placeholders before using the skill.")
    for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
        if re.match(r"(?:[a-z]+:|#)", target):
            continue
        if not (folder / target.split("#", 1)[0]).is_file():
            errors.append(f"Linked reference does not exist: {target}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/check_skill.py research-figure")
        print("Or pass the path to one skill folder.")
        return 2
    arg = Path(sys.argv[1])
    folder = arg if arg.is_dir() else PROJECT / "skills" / arg
    errors = check(folder)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {folder.name} has the required course structure and linked files.")
    print("Next, apply it to the two exercise inputs and inspect its behaviour and outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
