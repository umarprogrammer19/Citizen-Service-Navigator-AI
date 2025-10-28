# Contributing to Citizen‑Service‑Navigator‑AI

Thanks for your interest in improving **Citizen‑Service‑Navigator‑AI**! 🎉
This guide explains how to set up your environment, make changes, and submit a high‑quality pull request.

> This is a Python project managed with **[uv](https://docs.astral.sh/uv/)** (fast package/dependency manager). All commands below use `uv`.


## 📜 Code of Conduct
We follow a **Contributor Code of Conduct** to keep this community open and welcoming. By participating, you agree to uphold it.

- If the repository contains `CODE_OF_CONDUCT.md`, please read it.
- If it doesn’t exist yet, we follow the Contributor Covenant 2.1 by default.

For violations, please open a confidential issue or email the maintainers.

---

## 🧰 Prerequisites
- **Python**: 3.11+ recommended (project uses `uv`, which manages virtual envs automatically)
- **uv**: v0.4+ → `curl -LsSf https://astral.sh/uv/install.sh | sh` (or see docs)
- **Git**: for version control
- **Make** (optional): convenient shortcuts if a `Makefile` exists

> `uv` creates and pins virtual environments automatically per project, no `venv` manual work needed.

---

## ⚡ Quick Start (5 minutes)
```bash
# 1) Fork the repo (on GitHub), then clone your fork
git clone https://github.com/<your-username>/Citizen-Service-Navigator-AI.git
cd Citizen-Service-Navigator-AI

# 2) Sync dependencies (creates a venv under .venv or uv cache)
uv sync

# 3) Activate shell (optional; uv can run without activation)
uv venv --seed  # ensures pip/setuptools/wheel are present

# 4) Run the app (adjust entrypoints as needed)
uv run python -m app               # or
uv run python src/main.py          # or
uv run streamlit run app.py        # if using Streamlit

# 5) Run tests & linters
uv run pytest -q
uv run ruff check .
uv run ruff format .               # or: uv run black .
uv run mypy src\ n```

> If the project uses a `.env`, copy and fill:
```bash
cp .env.example .env
```

---

## 🗂️ Project Layout (convention)
```
Citizen-Service-Navigator-AI/
├─ src/                      # Python source (preferred "src" layout)
│  └─ citizen_service_navigator_ai/  # package module(s)
├─ tests/                    # unit/integration tests (pytest)
├─ pyproject.toml            # tool config: uv, ruff, black, mypy, pytest, etc.
├─ .pre-commit-config.yaml   # git hooks
├─ .env.example              # sample environment variables
└─ README.md
```
> Actual paths may differ; update commands accordingly.

---

## 🪄 Using `uv` like a pro
Common tasks:

```bash
# Add a runtime dependency
uv add fastapi

# Add a dev-only dependency
uv add --dev pytest ruff mypy black

# Remove a dependency
uv remove fastapi

# Update locked deps (respecting constraints)
uv lock --upgrade

# Install from lock (reproducible)
uv sync

# Run scripts/CLI without activating venv
uv run python -m citizen_service_navigator_ai

# Inspect dependency tree
uv tree

# Export requirements.txt (if needed for deployment)
uv export --format requirements-txt > requirements.txt
```

---

## 🔁 Development Workflow
1. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/<short-description>
   # or: fix/<bug>, chore/<task>, docs/<topic>
   ```
2. **Sync deps**: `uv sync`
3. **Write code + tests** (TDD encouraged)
4. **Run quality checks** before committing:
   ```bash
   uv run ruff check .
   uv run ruff format .
   uv run mypy src
   uv run pytest
   ```
5. **Commit with Conventional Commits** (see below)
6. **Push** and open a **Pull Request** against `main`

---

## ✍️ Commit Message Style (Conventional Commits)
Use one of: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

Examples:
```
feat(api): add endpoint to fetch nearby services
fix(nlp): correct language detection for Urdu text
chore(deps): bump uv lock and refresh ruff to 0.6.x
```

> Scope (in parentheses) is optional but helpful.

---

## ✅ Pull Request Checklist
- [ ] PR title follows Conventional Commits
- [ ] Description explains **what** & **why**
- [ ] Tests added/updated; `uv run pytest` passes
- [ ] Lint/format clean: `uv run ruff check .` and `uv run ruff format .`
- [ ] Types clean: `uv run mypy src`
- [ ] No unrelated file changes
- [ ] If applicable, docs updated (README/docs)

Maintainers will review for clarity, scope, tests, and architectural fit.

---

## 🧪 Testing
- Framework: **pytest**
- Run tests: `uv run pytest -q`
- Coverage (if configured): `uv run pytest --cov=src --cov-report=term-missing`
- Add test files under `tests/` with names like `test_*.py`

---

## 🧹 Linting & Formatting
- **ruff** for linting & (optionally) formatting
- **black** for formatting (if preferred)
- Config lives in `pyproject.toml`. Typical commands:

```bash
uv run ruff check .
uv run ruff format .
# or, if using black
uv run black .
```

---

## 🔎 Static Types
- **mypy** is recommended for type checking
- Run: `uv run mypy src`
- Add gradual types in critical modules first, then expand

---

## 🧩 Environment & Secrets
- Duplicate `.env.example` → `.env` and fill values
- **Do not** commit real secrets. If needed, use GitHub Actions secrets or a vault
- Use `python-dotenv` or similar to load envs in dev

---

## 🧭 Local Run Recipes (examples)
Choose what the project actually uses and update as needed:

```bash
# FastAPI/UVicorn
uv run uvicorn citizen_service_navigator_ai.api:app --reload

# Streamlit
uv run streamlit run app.py

# CLI module
uv run python -m citizen_service_navigator_ai --help
```

---

## 🧷 Pre-commit Hooks (highly recommended)
```bash
uv run pre-commit install     # installs git hooks
uv run pre-commit run --all-files
```
This ensures your commits are linted/formatted and pass basic checks.

---

## 🏗️ CI (GitHub Actions) — Example
Create `.github/workflows/ci.yml` similar to:
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v2
      - run: uv sync --all-extras --dev
      - run: uv run ruff check .
      - run: uv run ruff format --check .
      - run: uv run mypy src
      - run: uv run pytest --maxfail=1 --disable-warnings -q
```

---

## 🚀 Releasing (if applicable)
- Ensure `pyproject.toml` version is bumped (`feat`/`fix` changes)
- Tag: `git tag -a vX.Y.Z -m "release vX.Y.Z" && git push --tags`
- If packaging, you can build with `uv build` and upload with `uv publish` (requires config)

---

## 🐛 Reporting Bugs & 💡 Proposing Features
- **Bugs**: open an issue with steps to reproduce, expected vs actual, logs, screenshots
- **Features**: explain the use case and alternatives considered; small PRs welcome
- Use labels like `bug`, `enhancement`, `good first issue`, `help wanted`

---

## 🔐 Security
Please do **not** open public issues for sensitive vulnerabilities. Instead, email the maintainers privately with reproduction details. We will respond and coordinate a fix.

---

## 🙌 Acknowledgements
Thank you for contributing to Citizen‑Service‑Navigator‑AI! Your time and ideas help make public‑service navigation more accessible for everyone.

