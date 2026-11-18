# Epicatechin COSY example data

These two files are unchanged copies from the **CENAPTNMR** collection,
[nmrXiv project P33](https://doi.org/10.57992/nmrxiv.p33),
[epicatechin sample S192](https://doi.org/10.57992/nmrxiv.p33.s192).
They support the raw-data and processed-spectrum examples in SpectroChemPy NMR.

## Source and licence

The project declares **Creative Commons Zero v1.0 Universal (CC0-1.0)**.
See the [project page](https://nmrxiv.org/P33) and
[CC0 terms](https://creativecommons.org/publicdomain/zero/1.0/legalcode).
This statement covers the measurement files listed below, not other datasets
in this repository. Please cite the original dataset identifiers when reusing them.

| Local file | Original dataset | Original filename |
| --- | --- | --- |
| `epicatechin_cosy.jdf` | [D875](https://doi.org/10.57992/nmrxiv.p33.s192.d875), raw JEOL JDF | `EpiCatechin_2880ug200uL_DMSOd6_COSY_400MHz_Jeol.jdf` |
| `epicatechin_cosy.jdx` | [D873](https://doi.org/10.57992/nmrxiv.p33.s192.d873), processed JCAMP-DX export | `EpiCatechin_2880ug200uL_DMSOd6_COSY_400MHz_JDX.jdx` |

Only the filenames were shortened. File contents and line endings are unchanged.
The raw file contains the acquired FIDs; the export already contains a processed
frequency-domain magnitude spectrum. They are used for different workflows.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `epicatechin_cosy.jdf` | 5271680 | `f109351f2102435faa7d302659e073b77ecc1184f1c3ef8817087ca91b9df3aa` |
| `epicatechin_cosy.jdx` | 8182161 | `b77cd1fe72cea1f6d820e40279d91cfdff3424333ca4d669e89b129c566c1152` |

Source archive: [nmrXiv S192](https://s3.uni-jena.de/nmrxiv-public/archive/S192/S192.zip).
Licence checked against the project page's structured licence metadata on
18 November 2026.


## Epicatechin proton 1D acquisition

`epicatechin_1h.jdf` is the proton 1D acquisition from the same public
[CENAPTNMR P33 epicatechin study](https://doi.org/10.57992/nmrxiv.p33.s192),
also under CC0-1.0. Original filename:
`EpiCatechin_2880ug200uL_DMSOd6_1H_400MHz_Jeol.jdf`.
The 1,081,024-byte file is unchanged and supports the JEOL 1D gallery example.
Its SHA-256 is
`6ab899b72d314f05d187e07c69389efae30572bae9b0c74fb0249cfa468ae7e0`.
