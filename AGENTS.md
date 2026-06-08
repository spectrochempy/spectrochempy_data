# AGENTS.md — spectrochempy_data

**Rules for OpenCode agents:**
- **Never commit, push, or create PRs unless explicitly instructed.**
- Always wait for explicit approval before staging/committing any change.
- This includes `git add`, `git commit`, `git push`, and `gh pr create`.
- Only act when the user's prompt clearly requests it (e.g. "commit this").
- If in doubt, show the diff and ask.

**Purpose:** Test data & examples used by [SpectroChemPy](https://github.com/spectrochempy/spectrochempy).
Published as `spectrochempy_data` on the `spectrocat` conda channel.

## Structure

- `testdata/` — actual data files, organized by technique subdirectory (`irdata/`, `ramandata/`, etc.)
- `.conda/` — conda-build packaging (`meta.yaml` + `build.sh`)
- `scripts/` — two maintenance scripts (see below)

No source code, no tests, no linter, no typechecker.

## How to add data (maintainer, quick path)

Push new data files to `master` under `testdata/` — the release workflow handles the rest. See `audit/RELEASE_AUTOMATION_PLAN.md`.

## Manual update (if not pushing to master)

1. **Add or modify files** under `testdata/`.
2. **Run both scripts** from the repo root:
   ```bash
   python scripts/rename_without_space.py   # replaces spaces with _ in filenames
   python scripts/create_index_in_folder.py # regenerates __index__ YAML files
   ```
3. **Bump version** in `.conda/meta.yaml` (top-level `version` field).
4. Commit and PR.

## CI

- `.github/workflows/main.yml` — builds via `conda-build .conda --output-folder out`; on release publishes to Anaconda; on push to `develop` publishes with `-l dev` label.
- `.github/workflows/release.yml` — auto-release when data files are pushed to `master`:
  - Runs maintenance scripts
  - Bumps patch version
  - Creates tag and GitHub Release
  - Supports `workflow_dispatch` with `dry-run: true` for testing<!-- end list -->
- No tests run in CI.
