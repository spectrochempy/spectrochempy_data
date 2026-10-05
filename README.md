# spectrochempy_data

Test and example data for [SpectroChemPy](https://github.com/spectrochempy/spectrochempy).

[![CI](https://github.com/spectrochempy/spectrochempy_data/actions/workflows/main.yml/badge.svg)](https://github.com/spectrochempy/spectrochempy_data/actions/workflows/main.yml)
[![conda](https://img.shields.io/conda/v/spectrocat/spectrochempy_data)](https://anaconda.org/spectrocat/spectrochempy_data)

## Data-extra development corpus

This is the `data-extra` development-corpus branch. The conda package below
contains the main test/example corpus, not these additional development files.

## Additional-data provenance

See [DATA_EXTRA_PROVENANCE.md](DATA_EXTRA_PROVENANCE.md) and the
[per-file manifest](data-extra-manifest.json) for the 34 additional files.
Their data redistribution rights remain unresolved under the reviewed
`nmrglue-ng` assessment. The notice also identifies the newer licensed fixtures
selected by that project and the remaining migration requirements.

## Main-corpus installation

```bash
mamba install -c spectrocat spectrochempy_data
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for external contributors and [`MAINTENANCE.md`](MAINTENANCE.md) for maintainers.

## Issues

Report problems or request data via [GitHub Issues](https://github.com/spectrochempy/spectrochempy_data/issues).

## Credits

- `ramandata/wire` files — [py-wdf-reader](https://github.com/alchem0x2A/py-wdf-reader) (upstream repository: MIT; binary dataset licence coverage remains to be confirmed)
- `als2004dataset.mat` — [MCR datasets](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download_datasets.html)
- `high_speed.srs` — provided by @Micsyl ([discussion #715](https://github.com/spectrochempy/spectrochempy/discussions/715))
