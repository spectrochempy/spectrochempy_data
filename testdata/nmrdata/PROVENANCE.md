# Provenance of the NMR example additions

This notice covers only the exact files listed in `example-data.sha256`.
It assigns no licence to other measurements already in this repository.
The checksums identify unchanged source bytes; directory names may be shorter
than the archived paths. Generated `__index__` files are navigation metadata.

## Public CENAPTNMR data — CC0 1.0

| Files relative to this directory | Source |
| --- | --- |
| `jeol/epicatechin_1h.jdf` | Epicatechin proton 1D, nmrXiv P33/S192 |
| `jeol/epicatechin_cosy.jdf` | Epicatechin COSY FIDs, nmrXiv P33/S192/D875 |
| `jeol/epicatechin_cosy.jdx` | Epicatechin processed COSY export, nmrXiv P33/S192/D873 |
| `nmrpipe/nmrpipe_2d_cosy_example.ft2` | Processed Gossypol COSY, P33/S213, converted to NMRPipe |

Source: [nmrXiv CENAPTNMR project P33](https://doi.org/10.57992/nmrxiv.p33).
The project's structured licence metadata declares
[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/legalcode),
verified on 18 November 2026. Please cite the original study identifiers.
The JEOL and NMRPipe subdirectory notices give filenames and conversion details.

## Archived measurements — CC BY 4.0

Christian Fernandez explicitly confirmed provenance and authorised
redistribution of the following five acquisitions under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
on 18 November 2026. This statement does not assign individual experimental
authorship beyond that confirmation.

| Included paths relative to this directory | Archived acquisition | Use |
| --- | --- | --- |
| `bruker/tests/nmr/RbNO3/15/` | RbNO3, experiment 15 | States STMAS; explicit TDeff selection |
| `bruker/tests/nmr/RbNO3/206/` | RbNO3, experiment 206 | Multiplex 3Q MQMAS comparison with STMAS |
| `bruker/tests/nmr/MULTIPLEX/3/` | MULTIPLEX, experiment 3, 27Al | 3Q/5Q selection; incomplete final phase cycle |
| `bruker/tests/nmr/MULTIPLEX/4/` | MULTIPLEX, experiment 4, 87Rb | Main Multiplex gallery workflow |
| `bruker/tests/nmr/alumina_800C/12/` | 27Al, experiment 12, title “Alumine 800 C” | Processed spectrum overlay for the Czjzek example |

Only the acquisition binaries and parameters listed by checksum are included.
For alumina, the selection is `acqus`, `pdata/1/procs`, and `pdata/1/1r`.
Pulse-program text, third-party includes, AU code, logs and other files from
the archives are excluded. The confirmation does not relicense such code.

Suggested attribution:

> NMR measurements: archived RbNO3/15, RbNO3/206, MULTIPLEX/3, MULTIPLEX/4
> and Alumine 800 C/12; supplied with permission by Christian Fernandez,
> distributed through spectrochempy_data under CC BY 4.0.

Include the dataset path and repository revision when citing a particular
acquisition; retain the licence link and indicate any later modifications.
The present measurement bytes are unchanged.

The archived alumina parameters disagree about the MAS rate (MASR versus
CNST31); its example uses an illustrative model rather than a quantitative
validation. MULTIPLEX/3 needs explicit handling of its partial phase cycle.
These limitations do not alter the archived data.

The original RbNO3/15 indirect status header reports `NUC1=1H`, whereas
the direct acquisition reports `87Rb`. Those archived parameters are kept
unchanged. For STMAS, the observed F2 nucleus determines the physical spin
and shear geometry; the unused default isotope in the F1 header is not a
constraint. The indirect time increment still determines the F1 frequency
spacing. Supplying these data alone does not certify scientific referencing.

## PEG 600 PFG — provenance clarification, 24 November 2026

This clarification concerns `bruker/tests/nmr/relax/102`, already present
before the additions covered by the checksum notice above. Christian
Fernandez states that he did not create this measurement and identifies
Cassandre Kouvatas as its author. The archive records acquisition
on 16 June 2023 under `nmr@lcs175n`, in a path containing
`Cassandre/13C_PEG600_8mm_diff/102`, and F2 reprocessing on 30 June under
the Windows account `Cassandre`. The maintainer confirms Cassandre Kouvatas
as the measurement author.

Christian Fernandez imported the files through
[data PR #22](https://github.com/spectrochempy/spectrochempy_data/pull/22)
on 5 July 2023. Repository contribution does not establish measurement
authorship. The maintainer confirms CC BY 4.0 for this acquisition,
the same licence as his files. Credit **Cassandre Kouvatas** as the measurement author and
retain the [CC BY 4.0 licence link](https://creativecommons.org/licenses/by/4.0/).
Pulse-program text is excluded. Raw metadata and measurement bytes are unchanged.
