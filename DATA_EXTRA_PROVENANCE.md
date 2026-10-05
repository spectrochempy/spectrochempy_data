# Provenance of the additional development corpus

This document applies to the 34 additional files introduced on `data-extra` by
commit `b429596af7fecfaa8ed2f514f401d9997249219c`. Files shared with the main data
branch are outside this inventory; their separate provenance work is tracked
in [spectrochempy_data PR #26](https://github.com/spectrochempy/spectrochempy_data/pull/26).

## Use the reviewed nmrglue-ng assessment

The reference assessment is
[nmrglue-ng PR #39](https://github.com/spectrochempy/nmrglue-ng/pull/39), its
[versioned manifest](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/maintainer/testdata-manifest.toml)
and [roadmap](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/maintainer/roadmap.md).
Use the **review-corrected conclusions**, not the initial PR summary:

- The historical nmrglue v0.5 release data has **UNRESOLVED redistribution
  rights**. BSD-3-Clause is the software repository licence; its application to
  contributed data was not established.
- The reference corpus distinguishes **29 original files** from **116 locally
  generated NMRPipe references**. Only the originals match this branch's
  identified additional files. The generated references are not present here.
- The five JEOL files on this branch are not accounted for by that historical
  manifest. nmrglue-ng's newer packaged JEOL fixtures are different files.

The original corpus archive is
[`test_data_v0.5-dev.zip`](https://github.com/jjhelmus/nmrglue/releases/download/v0.5/test_data_v0.5-dev.zip).
Its SHA-256, recorded in the reference roadmap, is
`dbff258fe08a19f1cd08f44b731d3d19e20e54fbb1415d904cd6d03f25209dae`.
This archive was not downloaded again for this comparison.

## Branch inventory

[`data-extra-manifest.json`](data-extra-manifest.json) records the exact path,
payload size, SHA-256, storage type and matching upstream path for each file.
All 34 entries have the common redistribution status `UNRESOLVED`; no data
licence is granted by the manifest.

| Group | Files | Result |
| --- | --- | --- |
| Agilent 1D / 2D / TPPI / 3D / 4D | 9 | Exact path-mapped size/hash match to original nmrglue corpus files |
| Bruker 1D / 2D / 3D | 16 | Exact path-mapped size/hash match to original nmrglue corpus files |
| SIMPSON input scripts | 2 | Exact path-mapped size/hash match to original nmrglue corpus files |
| Tecmag | 2 | Exact path-mapped size/hash match to original nmrglue corpus files |
| JEOL `13C.jdf`, `1H.jdf`, `COSY.jdf`, `HMBC.jdf`, `HSQC.jdf` | 5 | Original source and rights remain to be identified |

For the 21 ordinary Git blobs, size and SHA-256 were computed from the committed
contents. For the 13 LFS-backed entries, the manifest records the payload
`size` and `oid sha256` in the committed pointer: eight match the upstream
manifest and five are the unidentified JEOL files. Their remote payloads were
not downloaded or rehashed. A null `upstream_path` means no source match was
established; it does not mean the file is generated or freely licensed.

## Reuse the new licensed fixtures where they cover the required behavior

nmrglue-ng has separately introduced small, documented fixtures. These do not
retroactively change the licence or availability of the historical corpus.

| Reference work | Fixtures and documented terms | Application here |
| --- | --- | --- |
| [PR #40](https://github.com/spectrochempy/nmrglue-ng/pull/40), merged | JEOL fluorine/phosphorus (cheminfo MIT, notice required); Rutin 1H/13C (Harvard Dataverse `10.7910/DVN/ZAZDNM`, CC0 1.0) | Candidates for JEOL 1D reader development, under their own filenames and notices |
| [PR #41](https://github.com/spectrochempy/nmrglue-ng/pull/41), merged | Bruker sucrose 1D (NMRXiv P52), Ginsenoside Rg1 HSQC and Gossypol COSY (P33), CC0 1.0 | Candidates for 1D/2D reader coverage; not a substitute for 3D or Agilent-specific cases |
| [PR #42](https://github.com/spectrochempy/nmrglue-ng/pull/42), open at this assessment | Epicatechin JEOL HSQC and two JCAMP-DX spectra (NMRXiv P33), documented CC0 1.0 | Further candidates; follow the PR's review status and the per-file notices |

The per-file provenance, SHA-256 checksums and notices are maintained beside the
[JEOL](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/nmrglue/fileio/tests/data/jeol/README.md),
[Bruker](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/nmrglue/fileio/tests/data/bruker_pdata/README.md)
and [JCAMP-DX](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/nmrglue/fileio/tests/data/jcampdx/README.md)
fixtures. Prefer these reviewed records to reconstructing their provenance.

Any replacement must retain the required format, dimensionality and quadrature
coverage and be validated with its consumers. In particular, SpectroChemPy needs
the original Bruker indirect acquisition parameters (`acqu2`/`acqu2s`), omitted
from nmrglue-ng's reduced 2D selections. The source archives contain them, as
documented in PR #26. No verified like-for-like COSY/HMBC replacement for the
five legacy JEOL filenames has been established by this inventory.

## Keeping the inventory current

The JSON scope is the **additional corpus only**, at the pinned commit; it is
not a licence declaration for all of `testdata/`. `upstream_path` refers to an
exact entry in the pinned nmrglue-ng manifest and must agree in size, checksum
and `provenance_class = original`. Validate actual LFS payloads separately when
they are obtained. New data, replacements and new rights evidence require an
inventory and notice update; do not silently substitute different experiments
under the legacy filenames.
