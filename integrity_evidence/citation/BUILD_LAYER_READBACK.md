# Citation build-layer readback

## Verdict

**FULL CITATION-INTEGRITY PASS: source layer PASS; generated layer PASS.**

The rebuilt `build/main.tex`, `build/main.txt`, and `build/main.pdf` faithfully carry the nine corrected bibliography records and all fourteen corrected citation contexts. The prior stale wording and records are absent. This verdict is limited to citation integrity; the package manifest is separately stale and still blocks an overall frozen-package/release-integrity PASS.

## Scope and artifact identity

- Readback completed: **2026-08-09T20:16:20+01:00 (BST)**.
- Candidate inspected read-only: `/Users/admin/Documents/Codex/2026-08-09/the-0processed-folder-on-the-mac/work/irreducible-norms-ref-upgrade/stage2_5/candidate`.
- Coverage: 9/9 rendered bibliography records and 14/14 rendered citation contexts in TeX, extracted text, and PDF; no sampling.
- Gray-zone policy: FAIL. No citation gray zone remained.

| Artifact | SHA-256 | Modified (BST) |
|---|---|---|
| `MANUSCRIPT.md` | `5ff53d9074a4651940a12b432a7194baee1e078470d88d0ec5f22a7fe29ef762` | 2026-08-09 20:04:21 |
| `references.bib` | `47a9074f428cdf60b712ced79c67928d0df1addb0679d03fdf79fd09863dde2d` | 2026-08-09 20:09:59 |
| `build/main.tex` | `a5548f66d6fdc0928411f7cb34472d00c34d76ee21cbd7782ad9bbc1c018f973` | 2026-08-09 20:10:09 |
| `build/main.txt` | `f2d5015ca05a1f74e25bd5ec3affe4267069013c9aefdc0290d3c1430d1ae0cc` | 2026-08-09 20:10:11 |
| `build/main.pdf` | `a93b3f92e6762123bae5edae0cdec8696541ea9082139cc95a8fde169fa02d16` | 2026-08-09 20:10:11 |

The generated files postdate both corrected sources. A fresh `pdftotext -layout` extraction from `main.pdf` is byte-identical to `build/main.txt` and has the same SHA-256. `qpdf --check` reports no syntax or stream-encoding errors.

## Stale-defect phrase checks

Case-insensitive exact searches over `MANUSCRIPT.md`, `references.bib`, `build/main.tex`, `build/main.txt`, and a fresh PDF extraction returned zero matches for:

- `not known necessary`;
- the old synthetic Stacks title/lemma forms and `n.d.` records;
- the old composite DLMF title `Hypergeometric Transformations, Jacobi Representations and Zeros`;
- DLMF Release 1.2.6;
- the incorrect colon form `finite free convolution: Applications`;
- a 2023 rendering of the version-pinned `2309.10970v3` record.

The corrected C14 sentence renders on PDF page 15 as: “Lewis–Perry–Straub Theorem 4 gives a sufficient condition (Lewis et al. 2019).”

## All nine rendered bibliography records

| Key | TeX | Text | PDF | Rendered-field result |
|---|---:|---:|---:|---|
| `edo2014` | 1345–1349 | 903–905 | 17 | Authors, 2014, exact title, *Journal of Algebra* 397, 443–456, and DOI all render correctly. PASS |
| `grochow2025` | 1350–1355 | 906–908 | 17 | Author, 2025, exact title, *American Mathematical Monthly* 132(4), 350–355, and DOI render correctly. PASS |
| `lps2019` | 1356–1361 | 909–912 | 17 | Three authors, 2019, exact title, *JPAA* 223(12), 5346–5359, and DOI render correctly. PASS |
| `martinez2024real` | 1362–1366 | 913–915 | 17 | Three authors, 2024a, exact title, Version 3, and immutable `/2309.10970v3` URL render correctly. PASS |
| `martinez2024zeros` | 1367–1372 | 916–919 | 17 | Three authors, 2024b, exact period before “Applications”, Version 2, and immutable `/2404.11479v2` URL render correctly. PASS |
| `dlmf` | 1373–1378 | 920–922 | 17 | Standard style abbreviation “Olver et al., eds.”, 2026, official title, Release 1.2.7 of 2026-06-15, and official root render correctly. PASS |
| `perry2016` | 1379–1383 | 923–925 | 17 | Author, 2016, exact title, doctoral-dissertation type, University of Alabama, and repository URL render correctly. PASS |
| `stacks00hp` | 1384–1388 | 926–928 | 17 | Official author/title, 2026a, official root, and exact Tag 00HP URL render correctly. PASS |
| `stacks00fv` | 1389–1393 | 929–931 | 17 | Official author/title, 2026b, official root, and exact Tag 00FV URL render correctly. PASS |

There are exactly nine `\\bibitem` blocks in `main.tex` and nine rendered record starts in `main.txt`. Citation-style author truncation for DLMF is expected and does not remove the all-ten-editor source record in `references.bib`. The Stacks tag URLs are exact locators even though the CSL style suppresses the optional note text.

## All fourteen rendered citation contexts

| ID | Key | TeX lines | Text lines | PDF page | Rendered citation/context | Verdict |
|---|---|---:|---:|---:|---|---|
| C01 | `lps2019` | 183–184 | 80 | 2 | Computer-aided `e=3,4,5` ranges; `(Lewis et al. 2019)` | PASS |
| C02 | `perry2016` | 184–186 | 80–81 | 2 | Earlier thesis direction, explicitly indexed as LPS `e=3`; `(Perry 2016)` | PASS |
| C03 | `edo2014` | 186–188 | 81–83 | 2 | Strong Factorial/rigidity framework; `(Edo and Essen 2014)` | PASS |
| C04 | `lps2019` | 190–192 | 84–85 | 2 | “presently unmotivated”; `(Lewis et al. 2019)` | PASS |
| C05 | `lps2019` | 255–265 | 131–137 | 3 | Theorems 13–14 ranges/divisibility; `(Lewis et al. 2019)` | PASS |
| C06 | `lps2019` | 349–350 | 192 | 4 | Definitions of the coefficient and determinant data; `(Lewis et al. 2019)` | PASS |
| C07 | `grochow2025` | 645 | 409 | 8 | Simple-root multivariate Hensel setting; `(Grochow 2025)` | PASS |
| C08 | `stacks00hp` | 661 | 417 | 8 | Faithful flatness/nonzero tensor; `(Stacks project authors 2026a)` | PASS |
| C09 | `stacks00fv` | 664–665 | 419 | 8 | Weak Nullstellensatz/complex point; `(Stacks project authors 2026b)` | PASS |
| C10 | `lps2019` | 666–668 | 420–421 | 8 | Theorem 4 yields containment; `(Lewis et al. 2019)` | PASS |
| C11 | `martinez2024zeros` | 1007 | 650 | 12 | Hypergeometric concatenation; `(Martínez-Finkelshtein et al. 2024b)` | PASS |
| C12 | `dlmf` | 1008–1021 | 650–656 | 12 | Three named DLMF equations plus `(Olver et al. 2026)` | PASS |
| C13 | `martinez2024real` | 1034 | 671 | 13 | Logarithmic-mesh preservation; `(Martínez-Finkelshtein et al. 2024a)` | PASS |
| C14 | `lps2019` | 1208–1209 | 801 | 15 | Theorem 4 is stated only as sufficient; `(Lewis et al. 2019)` | PASS |

Normalized-whitespace counts agree in `main.tex`, `main.txt`, and the fresh PDF extraction:

- `Lewis et al. 2019`: 6;
- each other cited work: 1;
- total rendered source citations: 14;
- unique works: 9;
- orphan records: 0;
- dangling citations: 0.

## PDF link and visual readback

`pdfinfo -url` confirms distinct embedded annotations for all three exact DLMF claim locations on PDF page 12:

- `https://dlmf.nist.gov/15.8.E1`;
- `https://dlmf.nist.gov/18.5.E7`;
- `https://dlmf.nist.gov/18.16.E1`.

It also confirms the three DOI targets, both immutable arXiv version URLs, the Perry repository URL, DLMF root, and both Stacks tag URLs on page 17.

PDF pages 2, 3, 4, 8, 12, 13, 15, and 17 were rendered at 144 dpi and visually inspected. These pages cover every one of the fourteen citation contexts and every bibliography record. No missing text, clipped record, overlapping line, broken glyph, or out-of-page URL was found. Normal line wrapping and hyphenation do not alter any metadata or claim.

## Separate package-integrity caveat

The citation layers pass, but `MANIFEST.sha256` was not refreshed. A read-only run of `python3 scripts/verify_manifest.py --root .` returns exit 1 with 23 unmanifested files and 21 digest mismatches, including `MANUSCRIPT.md`, `references.bib`, and all three rebuilt citation artifacts. This is **not** a citation-content failure, but it prevents an overall frozen-package or publication-ready integrity PASS until the package boundary is reconciled and the manifest is regenerated and verified.

## Final gate

- Source citation layer: **PASS**.
- Generated TeX/text/PDF citation layer: **PASS**.
- Combined citation-integrity gate: **PASS**.
- Overall frozen-package/release-integrity gate: **NOT PASSING YET — stale manifest**.

