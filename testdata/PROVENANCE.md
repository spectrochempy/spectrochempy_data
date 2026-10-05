# Data provenance and licensing

This repository contains datasets from multiple sources. Licences apply to the
specific datasets identified below, not to the repository as a whole.
An unresolved entry means that provenance or permission still needs documenting;
it is not a determination that reuse is prohibited.

## LCS datasets — CC BY 4.0

Christian Fernandez has confirmed LCS provenance for the IR/OMNIC, Raman LabSpec,
AGIR, DSC, MS and CP NMR datasets, subsequently also confirming OPUS and
`wodger.spg` and the `topspin_1d`, `topspin_2d` and `relax` measurements, and
selected the
[Creative Commons Attribution 4.0 International licence (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
for the LCS data. The covered scope is defined below. SRS files are pending
clarification and are excluded from this grant.

The LCS datasets in this scope are licensed under CC BY 4.0. You may share and
adapt them, including for commercial purposes, subject to the licence terms.
Give appropriate credit, link to the licence, and indicate any changes. See the
[full legal terms](https://creativecommons.org/licenses/by/4.0/legalcode.en).

### Attribution

Suggested attribution for the covered datasets:

> Data: LCS, distributed through spectrochempy_data
> (https://github.com/spectrochempy/spectrochempy_data), licensed under
> CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

When citing an individual dataset, also identify its path and repository version.
Retain any supplied author and attribution notices. If you modify the data,
describe the modifications; the attribution above does not claim that a derived
dataset is unchanged. Except where noted below, individual measurement authors
have not yet been recorded in this register; the collective LCS attribution
does not assign authorship to the person who committed the files.

For the `topspin_1d`, `topspin_2d` and `relax` measurements, Christian Fernandez
has explicitly confirmed that he created them. Attribute these measurements to
**Christian Fernandez, LCS**, with the repository and CC BY 4.0 links above.

### Covered files

Paths below are relative to this `testdata/` directory. This initial register
covers files tracked at repository revision
`08bb9b0cbff8f4363c48b6bff7ccb743f8140e0a` that match the following entries.
Directory entries include their descendants, with the exclusions stated below.
New files and replacements need their own provenance review and a register
update; placing a file in one of these directories does not establish its rights.

| Dataset | Included paths | Exclusions |
| --- | --- | --- |
| AGIR | `agirdata/` | Generated `__index__` files |
| DSC | `dscdata/` | Generated `__index__` files |
| Mass spectrometry | `msdata/` | Generated `__index__` files |
| Raman LabSpec | `ramandata/labspec/` | Generated `__index__` files |
| CP NMR | `nmrdata/bruker/tests/nmr/CP/` | Generated `__index__` files |
| TopSpin 1D NMR measurements and parameters | `nmrdata/bruker/tests/nmr/topspin_1d/` | Generated `__index__` files and `1/pulseprogram` |
| TopSpin 2D NMR measurements and parameters | `nmrdata/bruker/tests/nmr/topspin_2d/` | Generated `__index__` files and `1/pulseprogram` |
| NMR relaxation/diffusion measurements and parameters | `nmrdata/bruker/tests/nmr/relax/` | Generated `__index__` files and all `pulseprogram` files |
| IR spectra | `irdata/CO@Mo_Al2O3.SPG`, `irdata/IR.CSV`, `irdata/nh4y-activation.spg` | None |
| IR carroucell measurements | `irdata/carroucell_samp/` | Generated `__index__` files |
| IR interferograms and spectra | `irdata/interferogram/` | Generated `__index__` files |
| IR spectra in subdirectories | `irdata/subdir/` | All `.srs` files and generated `__index__` files |
| OPUS reader fixtures | `irdata/OPUS/` | Generated `__index__` files |
| OMNIC spectrum group | `wodger.spg` | None |

`agirdata/P350/FTIR/FTIR.zip` is included as an LCS data archive. Its internal
members have not yet been inventoried individually in this register.

The confirmation of IR/OMNIC provenance has not been extended to PerkinElmer
files without an explicit scope confirmation. Copies of `wodger.spg` embedded
in SpectroChemPy tests must also carry the attribution. The copy at
`tests/test_core/test_readers/ressources/omnic/wodger.spg` in SpectroChemPy revision
`f49dd8d4fe77a0811037417ab7dd12fb250d5ccb` is byte-identical to this dataset
(SHA-256 `c0caef3b5603a6920c3fbd0bad976718b9af5e32e098492b01704ef9ddd0ce15`).
No licence is assigned here to index files, repository scripts or documentation.

## SRS files — clarification requested

The following files are **not covered by the LCS CC BY 4.0 grant above**.

| Path | Current evidence | Remaining question |
| --- | --- | --- |
| `irdata/omnic_series/GC_Demo.srs` | Origin not confirmed | LCS measurement, vendor demonstration, or another source? |
| `irdata/omnic_series/TGA_demo.srs` | Origin not confirmed | LCS measurement, vendor demonstration, or another source? |
| `irdata/omnic_series/rapid_scan.srs` | Origin not confirmed | Producer and redistribution terms? |
| `irdata/omnic_series/rapid_scan_reprocessed.srs` | Origin not confirmed | Original dataset, processing steps and redistribution terms? |
| `irdata/omnic_series/high_speed.srs` | Provided by @Micsyl; [discussion #715](https://github.com/spectrochempy/spectrochempy/discussions/715) records the sample exchange and addition to this repository | Explicit licence or redistribution permission? |
| `irdata/subdir/TGAIR-unreadable.srs` | Origin not confirmed | Producer, any alterations and redistribution terms? |

Arnaud Travert (@atravert) is asked to clarify these entries during PR review.

## Other datasets — initial provenance register

These entries are not covered by the LCS licence grant above. Source credits
are evidence to investigate, not a substitute for applicable licence terms.

| Scope | Known source or evidence | Next step |
| --- | --- | --- |
| `ramandata/wire/` | All six WDF files match the py-wdf-reader binary release by SHA-256; see evidence below | Confirm that the upstream MIT grant covers the separately released measurement files and preserve notices |
| `matlabdata/als2004dataset.MAT` | Byte-identical to `ex_data.MAT` in the CSIC `data_gui2004.zip` archive | Obtain explicit data reuse terms; scientific citation identified below |
| `matlabdata/dna_data.mat` | Byte-identical to the CSIC `dna_data.zip` member; contributed here through [PR #25](https://github.com/spectrochempy/spectrochempy_data/pull/25) | Obtain explicit data reuse terms; do not classify as LCS based on contributor identity |
| `matlabdata/METING9.MAT` | SpectroChemPy's kinetics example cites the University of Amsterdam Biosystems Data Analysis Group | Recover original archive and reuse terms; cited download page currently returns HTTP 404 |
| `matlabdata/dso.mat` | Embedded metadata records an SPG import by `traverta`, with Mo/SiO2 spectra acquired in 2016 | Ask Arnaud to confirm LCS origin and the source/transformations |
| `nmrdata/bruker/tests/nmr/cadmium/`, `nmrdata/bruker/tests/nmr/h3po4/` | Readmes cite Tübingen; both `acqus` files contain `OWNER= PUBLIC DOMAIN` | Confirm the scope of that declaration for the whole experiment; source site timed out |
| `nmrdata/bruker/tests/nmr/topspin_1d/1/pulseprogram` | Christian Fernandez confirms authorship of the experiment; the stored program names `zg.lcs`, `Author: C.FERNANDEZ`, and includes Bruker support code | Review rights in the combined program text separately from the now-confirmed LCS measurements |
| `nmrdata/bruker/tests/nmr/topspin_2d/1/pulseprogram`, `nmrdata/bruker/tests/nmr/relax/100/pulseprogram`, `nmrdata/bruker/tests/nmr/relax/102/pulseprogram` | Measurements confirmed as Christian Fernandez's LCS data; included program text contains third-party references | Review program rights separately from the measurement licence |
| `nmrdata/bruker/tests/nmr/exam2d_HC/`, `nmrdata/bruker/tests/nmr/exam2d_HH/` | Christian Fernandez confirms these examples came with TopSpin; original distribution terms are unavailable | Replacement by the CC0 NMRXiv candidates below is preferred, subject to reader/test validation; existing files are not relicensed |
| `galacticdata/`, except `2024-11-22-SPC_1661.spc` | 23 SPC files match same-named hySpc.read.spc Git blobs; source and conflicting licence descriptions detailed below | Resolve rights for original SDK/example data, rather than assigning a software licence automatically |
| `galacticdata/2024-11-22-SPC_1661.spc` | Added in commit `83381ea`; not matched to the examined hySpc.read.spc files | Ask Christian for the source and permission |
| `irdata/perkinelmer/` | Not yet established | Confirm whether LCS or external data and document terms |
| `data-extra`: Agilent, additional Bruker, SIMPSON and Tecmag files | 29 file hashes/LFS object IDs match the nmrglue-ng manifest of the original nmrglue v0.5 corpus | Data redistribution terms remain unresolved in that manifest; see comparison below |
| `data-extra`: five JEOL `.jdf` files | No match in the examined nmrglue-ng corpus manifest | Ask Christian for the original source and permission; do not confuse these with the newer NMRXiv fixtures |

## Source evidence

Checks below compare committed data at `08bb9b0cbff8f4363c48b6bff7ccb743f8140e0a`
against the named sources. A content match establishes file identity with that
source; it does not on its own establish ownership or a redistribution grant.

### WiRE binary examples

Source archive:
[`spectra_files.zip`, release tag `binary`](https://github.com/alchem0x2A/py-wdf-reader/releases/tag/binary).
Archive SHA-256:
`110832b8c68527546d963fbfb47f6246a2dab77b559799d5a66e59903abc368a`.
All six local WDF files match archive members under `spectra_files/`:

| Local file under `ramandata/wire/` | SHA-256 (also the upstream member checksum) |
| --- | --- |
| `Streamline.wdf` | `857acee66c0c4fa7b009cb68f1eb6ac2493769271de0e0ef81902e64a0890f80` |
| `depth.wdf` | `2f6558d5ec3695ed1046152fe5e0e8acea8485c63fd8d676c83d178df15fc0de` |
| `line.wdf` | `bb4a978504587fc37760df303f8380f141cdeac9089121ad5162ae9a700aea78` |
| `mapping.wdf` | `4ebeae5f5ebe8045d7537769445242c5775670463e15144819f799595aba17e7` |
| `sp.wdf` | `5ca8c55848b4bdbe73fa2ca44f3e211613b52c65bf2aaaf5b14e8858f4e3f565` |
| `undefined.wdf` | `05ce6a9d5f477ac122b980a16e4dbc2ca4f08d08d310299f67d4830ddce87cee` |

The archive also contains `streamline.wdf`, identical to `Streamline.wdf`.
It contains no licence or README. The upstream
[example README](https://github.com/alchem0x2A/py-wdf-reader/blob/e22fa62add9a080d9eb80863a8b9fa426eb573dd/examples/spectra_files/README.md)
directs users to this archive; the main README describes personal measurements.
The repository's
[MIT licence](https://github.com/alchem0x2A/py-wdf-reader/blob/e22fa62add9a080d9eb80863a8b9fa426eb573dd/LICENSE)
states `Copyright (c) 2022 T.Tian`. This is strong provenance evidence; an explicit
confirmation that this grant includes the binary measurements remains to be
recorded. No separate licence is assigned to those measurements here.

### CSIC MATLAB datasets

The source pages supply scientific citations and download links, but no explicit
data licence was found on the examined pages or inside these two archives.

| Local file | Original archive member | File SHA-256 |
| --- | --- | --- |
| `matlabdata/als2004dataset.MAT` | `data_gui2004.zip` → `ex_data.MAT` | `4d0557572f37ac1632f8de33b403dc882ef85adc92b2298f3d82bf0a6cb8797d` |
| `matlabdata/dna_data.mat` | `dna_data.zip` → `dna_data.mat` | `f458d15325c93ebe973c66ab31d0331130da127cca9dfd60fd2f9ced024c5bbc` |

- [MCR-ALS GUI source page](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download_dataALS2004.html):
  J. Jaumot, R. Gargallo, A. de Juan and R. Tauler, *A graphical user-friendly
  interface for MCR-ALS: a new tool for multivariate curve resolution in MATLAB*,
  Chemometrics and Intelligent Laboratory Systems **76**, 101–110 (2005).
  [Archive](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download/datasets/data_gui2004.zip)
  SHA-256: `8ac3a9e6de5c9b15afdfd2a6316cb902b34b07e01460bdccc388eee014bc2b1e`.
- [DNA UV/CD source page](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download_dataOligo.html):
  J. Jaumot, N. Escaja, R. Gargallo, C. Gonzalez, E. Pedroso and R. Tauler,
  *Multivariate curve resolution: a powerful tool for the analysis of
  conformational transitions in nucleic acids*, Nucleic Acids Research
  **30**(17), e92 (2002).
  [Archive](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/download/datasets/dna_data.zip)
  SHA-256: `47565567668bc1f818c5753867579610db1ace61e09fe5e457ec264305365caa`.

The [MCR contact page](https://www.cid.csic.es/homes/rtaqam/tmp/WEB_MCR/contact.htm)
identifies Romà Tauler, Anna de Juan and Joaquim Jaumot as contacts. Ask for the
applicable data licence or permission covering redistribution and adaptations
for open-source tests and examples; citation alone does not settle those terms.

For `METING9.MAT`, the source is documented in SpectroChemPy's
`src/spectrochempy/examples/analysis/a_decomposition/plot_mcrals_kinetics.py`:
the [Biosystems Data Analysis Group dataset page](https://www.bdagroup.nl/content/Downloads/datasets/datasets.php)
(HTTP 404 during this investigation), with citation key `bijlsma:2001`.
The original file has not yet been retrieved and compared.

### Galactic SPC files

[PR #5](https://github.com/spectrochempy/spectrochempy_data/pull/5) identifies
hySpc.read.spc as the source and describes it as GPLv3. Its accompanying
`README.txt` is empty, including in the introduction commit `965537f`.

All 23 SPC files in `galacticdata/` other than `2024-11-22-SPC_1661.spc` have
identical Git blob IDs to their same-named counterparts under
[`inst/extdata/spc/`](https://github.com/r-hyperspec/hySpc.read.spc/tree/722567e1452ab544e8559ce63673d087ae743439/inst/extdata/spc).
This comparison includes `barbsvd.spc` and `LC_DIODE_ARRAY.SPC`.

The upstream
[DESCRIPTION](https://github.com/r-hyperspec/hySpc.read.spc/blob/722567e1452ab544e8559ce63673d087ae743439/DESCRIPTION)
and [LICENSE](https://github.com/r-hyperspec/hySpc.read.spc/blob/722567e1452ab544e8559ce63673d087ae743439/LICENSE)
declare MIT, copyright 2020– by the hySpc.read.spc authors. The
[DESCRIPTION at a revision preceding PR #5](https://github.com/r-hyperspec/hySpc.read.spc/blob/629194f054996885db70c66225d53b1f7c5f533d/DESCRIPTION)
also declares MIT. Therefore the discrepancy with PR #5 is not evidence of a
subsequent licence change.

The upstream
[`R/read_spc.R`](https://github.com/r-hyperspec/hySpc.read.spc/blob/722567e1452ab544e8559ce63673d087ae743439/R/read_spc.R)
refers to sample files from `ftirsearch.com` and an “SPC SDK example files” test
group. This adds an earlier source to investigate: the package's software
licence alone does not resolve the terms of the original SDK data. Access to
`https://www.ftirsearch.com/` timed out. Ask the upstream maintainers for the
original distribution/permission, and ask Arnaud what GPLv3 evidence was used
in PR #5. The separately added `2024-11-22-SPC_1661.spc` still needs its own source.

### NMR experiments outside CP

Paths here are relative to `nmrdata/bruker/tests/nmr/`:

- `cadmium/100/acqus` and `h3po4/4/acqus` contain
  `ORIGIN= WSolids (C) 1995-2007 Klaus Eichele` and `OWNER= PUBLIC DOMAIN`.
  Their readmes name
  [Klaus Eichele's Tübingen processing examples](https://anorganik.uni-tuebingen.de/klaus/nmr/processing/index.php?p=dcoffset/dcoffset).
  The public-domain statement is a useful embedded indication, but its scope
  (parameter file versus all experiment files) has not been established. The
  source page timed out; do not convert that indication into a CC0 declaration.
- `topspin_1d/1/pulseprogram` names `zg.lcs`, `Author: C.FERNANDEZ`, and
  modifications in 2013. Christian Fernandez subsequently confirmed that he
  created the `topspin_1d` measurements; those measurements and parameters are
  now included in the LCS scope above. The stored pulse program includes Bruker
  support code and remains outside that grant pending a separate scope review.
- `topspin_2d/1/pdata/1/title` reads `HMQC simple PST-5`; its pulse program
  credits `D. Massiot 24/08/95` and includes Bruker support code.
  Christian Fernandez confirms that he created the measurements, now included
  in the LCS scope; the pulse-program text remains excluded.
- `exam2d_HH/1/pdata/1/title` reads `COSY Cyclosporin`. The `exam2d_HH` and
  `exam2d_HC` acquisition files refer to TopSpin 2.1 example-style paths.
  Christian Fernandez confirms that both datasets came from examples distributed
  with TopSpin and that he no longer has that software copy. Their source is
  therefore identified by the contributor, but the original distribution and
  example-data licence have not been recovered. Ask Bruker for the applicable
  redistribution terms or explicit permission covering these files. Distribution
  with TopSpin does not by itself establish permission to redistribute them in
  an open-source data repository. These datasets remain outside the LCS grant.
- `relax/100` and `relax/102` contain pulse programs with multiple author or
  vendor references. Christian Fernandez confirms that he created the
  measurements, now included in the LCS scope. The pulse programs remain
  excluded pending clarification of their own redistribution terms.

For these experiments, distinguish rights in measurement data from rights in
included pulse-program code; an LCS measurement confirmation alone should not
silently relicense third-party program text.

### Additional NMR data on data-extra

The 34 files added under `testdata/` on branch `data-extra`, revision
`b429596af7fecfaa8ed2f514f401d9997249219c`, were compared with the
[nmrglue-ng corpus manifest](https://github.com/spectrochempy/nmrglue-ng/blob/8db4649d4c2a1905a0a6f137cedf76b2a32eac24/maintainer/testdata-manifest.toml).
That manifest identifies the matched files as originals from the **nmrglue v0.5
release archive**. It distinguishes the repository's BSD-3-Clause software
licence from the release data's still-`UNRESOLVED` redistribution status.

| Paths under `testdata/nmrdata/` on data-extra | Matched files | Comparison |
| --- | --- | --- |
| `agilent/agilent_{1d,2d,2d_tppi,3d,4d}/` | 9 | Four parameter-file SHA-256 hashes and five LFS object IDs |
| `bruker/bruker_{1d,2d,3d}/` | 16 | Thirteen parameter/program-file SHA-256 hashes and three LFS object IDs |
| `simpson/simpson_1d/rr.in`, `simpson/simpson_2d/2d.in` | 2 | SHA-256 hashes |
| `tecmag/LiCl_ref1.tnt`, `tecmag/LiCl_ref1.txt` | 2 | SHA-256 hashes |

For LFS-backed files this comparison uses the `oid sha256` stored in the Git
pointer, not a new download and rehash of the remote binary. The other 21 files
were hashed directly from Git blobs. The matching manifest provides a traceable
source lead; no new licence is assigned on the strength of the match.

The five `jeol/` files have no counterpart in that manifest:

| File | LFS SHA-256 object ID |
| --- | --- |
| `13C.jdf` | `97bb17a0633b2770bb411ef4529f2e45972eaa20c4babb72c0cb447d47270945` |
| `1H.jdf` | `d546be0d05b89ddf5951e58a98a1d47ddefcf7670dab47a91529223d4b245430` |
| `COSY.jdf` | `266d923f6170bd33f8cafd24c56495d5e63152beb6872ff6ffc8c1d82ddc2bc0` |
| `HMBC.jdf` | `db8783c809df754e5ff2b4d132e671a397167e9196c5b68ac9a360729fb7282e` |
| `HSQC.jdf` | `e2f7ab502c33e293bcaa9bede2e284e8ee852822fb14bea915a6cea3b3af52db` |

Their source and permission must be supplied or independently recovered. The
CC0 declaration for NMRXiv datasets discussed below does not apply to these
unidentified files merely because they use the same instrument format.

### Replacement candidates for the TopSpin exam2d examples

The maintainer proposes replacing the vendor examples using the NMRXiv fixtures
already selected in `nmrglue-ng`. These are candidates, **not yet installed or
validated with the SpectroChemPy reader**.

#### Current consumers

At SpectroChemPy revision `f49dd8d4fe77a0811037417ab7dd12fb250d5ccb`:

- `plugins/spectrochempy-nmr/tests/test_read_topspin.py:46–49` reads
  `exam2d_HC/3/pdata/1/2rr` and asserts a quaternion dataset of shape
  `(1024, 1024)`, with corresponding axis sizes. It has no assertions specific
  to cyclosporin peak positions.
- `docs/sources/userguide/processing/fourier2d.py_to_fix:184` uses raw
  `exam2d_HC` for an Echo-AntiEcho HSQC processing example; line 216 uses
  `exam2d_HH` for QF processing. The file is a deferred tutorial, not a normal
  `.py` example. Replacing its datasets requires updating sample descriptions,
  processing choices and plot ranges, not just paths.
- There are no other explicit `exam2d` references in the searched tracked files,
  including notebooks. Directory-based reads in `test_read_topspin.py` may also
  discover the experiments, so their selection behavior must be checked during
  migration.

#### Source and licence

The [NMRXiv CENAPTNMR project P33](https://nmrxiv.org/P33),
DOI [10.57992/nmrxiv.p33](https://doi.org/10.57992/nmrxiv.p33), explicitly declares
**CC0 1.0** in its public page's structured data (`props.project.data.license`,
SPDX `CC0-1.0`, [legal terms](https://creativecommons.org/publicdomain/zero/1.0/legalcode)).
This declaration was checked on the project and both study pages; the DataCite
record itself has an empty `rightsList`, so the licence evidence is the NMRXiv
record rather than an assumption based on the DOI.

| Replaces | Candidate | Source experiment | Relevant characteristics |
| --- | --- | --- | --- |
| `exam2d_HC` | Ginsenoside Rg1 HSQC, [S208 / D1068](https://nmrxiv.org/S208), DOI `10.57992/nmrxiv.p33.s208.d1068` | `Ginsenoside_3110ug200uL_HSQC_600MHz_Bruker/` | `acqu2s`: `FnMODE=6`, `NUC1=13C`, `TD=256`; all four processed components `2rr`, `2ri`, `2ir`, `2ii`; processed shape `(256, 4096)` in nmrglue-ng |
| `exam2d_HH` | Gossypol COSY, [S213 / D1145](https://nmrxiv.org/S213), DOI `10.57992/nmrxiv.p33.s213.d1145` | `Gossypol_3650ug200uL_CDCl3_COSY_600MHz_JDX/` | Bruker directory despite the name ending in JDX; `acqu2s`: `FnMODE=1`, `NUC1=1H`, `TD=128`; processed `2rr` shape `(512, 2048)` in nmrglue-ng |

The source encodings preserve the intended examples: Echo-AntiEcho for the
HSQC candidate and QF for the COSY candidate. These values were read from
original archive members, not inferred from experiment names.

Both study archives were inspected in memory. All 11 HSQC files and all eight
COSY files committed in `nmrglue-ng` revision
`24372441f6b09ca4f1807a25bf48cf9b2fa550c2` under
`nmrglue/fileio/tests/data/bruker_pdata/exp2d_hsqc/` and `exp2d_cosy/` match
original archive members by SHA-256. That repository's adjacent README records
the per-file checksums and `tests/test_bruker_pdata.py` records independently
decoded reference values. Those tests have been inspected, not rerun here.

| Original study archive | Bytes | SHA-256 |
| --- | --- | --- |
| [Ginsenoside Rg1](https://s3.uni-jena.de/nmrxiv/production/archive/eadafe70-541c-4b20-838f-036e0e91326b/Ginsenoside%20Rg1%20600%20MHz%20in%20CD3OD%20NMR%20data.zip) | 28252039 | `eb936e46b3a3d2b455eae290ec142f57e6d2cb1431a05a6b9ee3969186b3c4ab` |
| [Gossypol](https://s3.uni-jena.de/nmrxiv/production/archive/86d3cf29-d858-4d18-be13-4fe834a916ea/%20Gossypol%20600%20MHz%20CDCl3%20DMSOd6%20NMR%20data%20.zip) | 63896152 | `5751ca6afe23f067d9f0ced782e5f7f5a3a6fbc34afefd7d3c5b2356a26e085c` |

#### Required adaptation

The reduced nmrglue-ng fixtures omit `acqu2` and `acqu2s`; both files are
present in the original archives. SpectroChemPy uses indirect acquisition
metadata for encoding, frequencies and axes, so copying the reduced fixtures
unchanged is insufficient. Recover the original parameters, retaining their
checksums, and use a numeric experiment directory (e.g. `<dataset>/1/`), as the
current reader converts the experiment number to an integer.

Additional original parameter checksums, relative to each source experiment:

| Candidate | File | SHA-256 |
| --- | --- | --- |
| HSQC | `acqu2` | `de9f07b4a3266dd95310d8dd964b0b86826a557253485c86215cec7e2399a5c3` |
| HSQC | `acqu2s` | `56e1c35e751517c21c15ede0e85d89d7be4b2e9d88d7467dc9bcef2791ecfd1c` |
| COSY | `acqu2` | `adcfdeb25947e2d0698f5187cf078740d5fa30dade5b442b07df4ac934e0d1f8` |
| COSY | `acqu2s` | `a39fa6f1202eca0b5a1ddffd649721346cd20a96fda9de0bfa87b3fc159221bd` |

Before removing the vendor examples, validate processed HSQC quaternion
components and coordinates, raw HSQC/COSY encoding, and directory discovery in
SpectroChemPy. New shape/value assertions must follow the source files and
reader normalization, not merely be adjusted until the old test passes.
The single data-repository PR can include the replacement data and provenance;
consumer changes are in the separate SpectroChemPy repository and must be
coordinated before retiring the old paths.

## Maintaining this register

For each new or clarified dataset, record the exact file scope, producer/source,
source version or persistent link, applicable licence or permission, required
attribution, and any transformations. Preserve supporting notices. Do not infer
data ownership from a Git commit author or licensing from an instrument format.

This is a family-level register with checksums for the externally matched
archives and files, not yet a complete per-file checksum manifest.
