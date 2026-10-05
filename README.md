# spectrochempy_data

Test and example data for [SpectroChemPy](https://github.com/spectrochempy/spectrochempy).

[![CI](https://github.com/spectrochempy/spectrochempy_data/actions/workflows/main.yml/badge.svg)](https://github.com/spectrochempy/spectrochempy_data/actions/workflows/main.yml)
[![conda](https://img.shields.io/conda/v/spectrocat/spectrochempy_data)](https://anaconda.org/spectrocat/spectrochempy_data)

## Installation

```bash
mamba install -c spectrocat spectrochempy_data
```

## Data branches

This repository uses two branches to separate data by purpose:

| Branch | Content | Size |
|---|---|---|
| `master` | Test-essential data (used by CI and unit tests) | ~60 MB |
| `data-extra` | Extra datasets for reader development (agilent, jeol, bruker_3d, simpson, tecmag) | ~300 MB |

The `master` branch is downloaded automatically by SpectroChemPy at startup (via `scp.read()`).
Extra data must be fetched explicitly.

## Fetching extra data

```bash
# CLI
python scripts/fetch_extra.py

# Python
from spectrochempy.application.testdata import download_extra_testdata
download_extra_testdata()
```

Extra data is cloned into `~/.spectrochempy/testdata-extra/`.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for external contributors and [`MAINTENANCE.md`](MAINTENANCE.md) for maintainers.

## Issues

Report problems or request data via [GitHub Issues](https://github.com/spectrochempy/spectrochempy_data/issues).

## Data provenance and licensing

The LCS datasets explicitly listed in [`testdata/PROVENANCE.md`](testdata/PROVENANCE.md)
are licensed under **CC BY 4.0**, with attribution to LCS. That register defines
the covered files, attribution and licence links, and the datasets whose origin
or redistribution terms still need clarification, including SRS files.

There is no blanket licence covering all datasets in this repository.

## Credits

- `ramandata/wire` files — [py-wdf-reader](https://github.com/alchem0x2A/py-wdf-reader) (upstream repository: MIT; binary dataset licence coverage remains to be confirmed)
- `als2004dataset.mat` — [MCR datasets](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download_datasets.html)
- `dna_data.mat` — [CSIC DNA UV/CD dataset](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download_dataOligo.html); source archive match verified, data licence to clarify
- Original Galactic SPC collection — [hySpc.read.spc](https://github.com/r-hyperspec/hySpc.read.spc); source file matches verified, original SDK data rights to clarify (see the provenance register)
- `high_speed.srs` — provided by @Micsyl ([discussion #715](https://github.com/spectrochempy/spectrochempy/discussions/715))
