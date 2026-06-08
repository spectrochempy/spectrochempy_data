# Contributing to spectrochempy_data

## For external contributors (via Pull Request)

**1. Fork the repository**

**2. Add your data files**

Place them in the appropriate directory under `testdata/`:

| Directory | Technique |
|---|---|
| `testdata/irdata/` | Infrared spectroscopy |
| `testdata/ramandata/` | Raman spectroscopy |
| `testdata/nmrdata/` | NMR spectroscopy |
| `testdata/msdata/` | Mass spectrometry |
| `testdata/agirdata/` | AGIR data |
| `testdata/dscdata/` | DSC data |
| `testdata/galacticdata/` | Galactic (Spectral) data |
| `testdata/matlabdata/` | MATLAB data files |

**3. Commit and open a Pull Request**

```bash
git add testdata/
git commit -m "Add <technique> data: <description>"
git push
# Open a PR on GitHub
```

**4. The maintainer merges your PR**

On merge to `master`, an automatic workflow:
- Runs maintenance scripts (renames files with spaces, regenerates `__index__` files)
- Bumps the version number
- Creates a GitHub Release and a conda package
- Publishes to Anaconda (`spectrocat` channel)

> **You don't need to run the scripts or bump the version yourself — the CI does it automatically.**

## For maintainers (direct push to master)

See `MAINTENANCE.md` for the complete procedure.
