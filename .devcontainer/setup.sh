#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-tested.txt

# Pin the classroom CLI version. Rehearse before deliberately changing it.
npm install --global @openai/codex@0.169.0

git --version
codex --version
.venv/bin/python scripts/00_check_environment.py
.venv/bin/python scripts/check_data.py
.venv/bin/python scripts/01_first_output.py

cat <<'MESSAGE'

Course setup complete. Open outputs/01-first-output/age_distribution.png.
In a new terminal, sign into your own account:
  codex login --device-auth
Then run:
  codex

If device login is unavailable, see CODESPACES.md. Setup has not tested AI access.
MESSAGE
