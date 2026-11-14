# Take the course in GitHub Codespaces

This route runs Python, Git and Codex CLI on a cloud computer. You use VS Code and its terminal in your browser; you do not need to install these programs on your laptop. You need a GitHub account with available Codespaces usage and your own eligible Codex account. Computing usage and AI usage have separate allowances.

Use the [student starter template repository](https://github.com/J-R-Paul/Agentic-Coding). Its root contains this file, `AGENTS.md`, `requirements-tested.txt`, `.devcontainer/`, `scripts/` and `data/`.

## Create your own project

1. Open the instructor's template repository on GitHub. Choose **Use this template → Create a new repository** and create a copy under your own account. Choose private visibility if you do not want to publish your work.
2. In your new repository, choose **Code → Codespaces → Create codespace on main** (or the repository's default branch). A two-core machine is sufficient for the supplied analyses. Wait for the setup command to finish; the first build can take several minutes.
3. Check that the setup log ends with `Course setup complete`. It installs Python packages and Codex CLI, checks the environment and data, and creates the first saved figure.
4. In the file explorer, open `outputs/01-first-output/age_distribution.png`.

If setup fails, save the exact error and tell the instructor. Once the problem is resolved, the setup command can be rerun in the terminal:

```bash
bash .devcontainer/setup.sh
```

## Sign into Codex

Open **Terminal → New Terminal** and run:

```bash
codex --version
python scripts/00_check_environment.py
codex login --device-auth
```

Open the sign-in link printed in the terminal, sign into **your own** ChatGPT account, and enter the one-time code. Device-code login may first need enabling in your ChatGPT security settings or by your workspace administrator. If this login method is unavailable, tell the instructor before class so they can verify another supported route for your account.

After login, run:

```bash
codex
```

Begin with a small read-only task, such as: “Read AGENTS.md and tell me which interpreter and commands to use for the course checks.” A successful setup log alone does not establish AI access or sufficient allowance. Review permission requests and keep the course's normal approval settings.

The workspace is configured to put `.venv/bin` on the remote command path. `python` should therefore use the course environment; the explicit `.venv/bin/python` commands in the main README also work. Codex runs in this cloud project and can use its files and Python environment.

## Save and resume

Save your files, then commit and push the project changes you want to keep to your own repository. The supplied `.gitignore` excludes `outputs/`, so download figures, tables and other output files separately if you want copies outside the codespace. Download a file using its context menu in the file explorer.

Stop the codespace when you finish, and reopen the same one from <https://github.com/codespaces> to continue. Stopping releases compute; storage continues to count towards your allowance. Codespaces can be deleted after inactivity. Before deleting one, push source changes and download any outputs you need.

Do not share Codex credentials or add them to your repository. If you need to end your login, use `codex logout`. A rebuilt or new container may require another login.

## Start the capstone

When the instructor releases the capstone, create an empty folder outside the starter project, for example:

```bash
mkdir -p /workspaces/northbridge-capstone
cd /workspaces/northbridge-capstone
codex
```

Put the separately supplied client pack in this new project and configure it intentionally, following `START-HERE.md`. Do not copy the whole starter project. The starter's Python environment remains on the command path in this codespace; your project files, instructions and Git repository should be separate. `/workspaces` persists across container rebuilds, but files outside your starter repository are not included when you push that repository. Save or publish the capstone separately before deleting the codespace.

## Official references

- [Codespaces configuration](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
- [Codespaces usage and billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
- [Codex CLI installation](https://github.com/openai/codex#quickstart)
- [Codex remote and device-code authentication](https://learn.chatgpt.com/docs/auth#login-on-headless-devices)
