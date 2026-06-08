# AGENTS.md — spectrochempy_data

**Purpose:** Test data & examples used by [SpectroChemPy](https://github.com/spectrochempy/spectrochempy).
Published as `spectrochempy_data` on the `spectrocat` conda channel.

## Structure

- `testdata/` — actual data files, organized by technique subdirectory (`irdata/`, `ramandata/`, etc.)
- `.conda/` — conda-build packaging (`meta.yaml` + `build.sh`)
- `scripts/` — two maintenance scripts (see below)

No source code, no tests, no linter, no typechecker.

## How to update

1. **Add or modify files** under `testdata/`.
2. **Run both scripts** from the repo root:
   ```bash
   python scripts/rename_without_space.py   # replaces spaces with _ in filenames
   python scripts/create_index_in_folder.py # regenerates __index__ YAML files
   ```
3. **Bump version** in `.conda/meta.yaml` (top-level `version` field, currently `1.8`).
4. Commit and PR.

## CI

- `.github/workflows/main.yml` builds via `conda-build .conda --output-folder out`
- On release: uploads to Anaconda (`anaconda upload`)
- On push to `develop`: uploads with `-l dev` label
- No tests run in CI.

## Release checklist (from PR template)

- [ ] Bump version in `.conda/meta.yaml`
- [ ] Run `scripts/rename_without_space.py` and `scripts/create_index_in_folder.py`
