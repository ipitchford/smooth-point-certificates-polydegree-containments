# Citation correction round 1: source and build-layer re-audit

## Outcome

**FULL CITATION-INTEGRITY PASS: SOURCE LAYER PASS; BUILD LAYER PASS.**

Every defect from the first audit is resolved in the corrected `references.bib` and `MANUSCRIPT.md`:

- all 9/9 bibliography records pass existence, metadata, and current target checks;
- all 14/14 in-text citation contexts pass against the cited primary or official source;
- all nine bibliography keys are cited, with no orphan or dangling key;
- the two Stacks records now use the official 2026 citation with exact tag locators;
- the `martinez2024zeros` title now has the official period and both Martínez records use version-pinned URLs;
- the DLMF record now matches the official Release 1.2.7 citation and the manuscript links all three exact permalinks;
- the unsupported “not known necessary” clause has been removed.

The source-layer result is **PASS**, not provisional. The rebuilt TeX, extracted text, and PDF also pass complete readback. The combined citation-integrity gate is therefore **PASS**. A separate stale package manifest still prevents an overall frozen-package/release-integrity PASS.

## Audit scope

- Source audit time: **2026-08-09T20:07:16+01:00 (BST)**; build readback completed **2026-08-09T20:16:20+01:00 (BST)**.
- Candidate inspected read-only: `/Users/admin/Documents/Codex/2026-08-09/the-0processed-folder-on-the-mac/work/irreducible-norms-ref-upgrade/stage2_5/candidate`.
- Source files:
  - `references.bib`, SHA-256 `47a9074f428cdf60b712ced79c67928d0df1addb0679d03fdf79fd09863dde2d`;
  - `MANUSCRIPT.md`, SHA-256 `5ff53d9074a4651940a12b432a7194baee1e078470d88d0ec5f22a7fe29ef762`.
- Generated files:
  - `build/main.tex`, SHA-256 `a5548f66d6fdc0928411f7cb34472d00c34d76ee21cbd7782ad9bbc1c018f973`;
  - `build/main.txt`, SHA-256 `f2d5015ca05a1f74e25bd5ec3affe4267069013c9aefdc0290d3c1430d1ae0cc`;
  - `build/main.pdf`, SHA-256 `a93b3f92e6762123bae5edae0cdec8696541ea9082139cc95a8fde169fa02d16`.
- Coverage: all nine records and all fourteen citation occurrences, not a sample.
- Evidence policy: publisher, DOI/Crossref, institutional repository, official arXiv API/versioned PDF, official Stacks tag/cite pages, author paper, and official NIST DLMF only.
- Gray-zone policy: FAIL. No gray-zone exception was needed in this round.

## Prior-defect closure

| Prior defect | Corrected source evidence | Result |
|---|---|---|
| `stacks00hp` synthetic title and missing year | `author = The Stacks project authors`; `title = The Stacks project`; official root; `year = 2026`; note and URL identify Tag 00HP/Lemma 10.39.15 | **RESOLVED** |
| `stacks00fv` synthetic stand-alone record and missing year | Same official 2026 entry pattern; note and URL identify Tag 00FV/Theorem 10.34.1 | **RESOLVED** |
| `martinez2024zeros` colon instead of official period | Title now exactly uses “convolution. Applications”; URL is pinned to `2404.11479v2` | **RESOLVED** |
| DLMF composite title/authorship, missing release/editors/locators | Official title, Release 1.2.7 of 2026-06-15, all ten editors, official root, and direct 15.8.1/18.5.7/18.16.1 links | **RESOLVED** |
| Unsupported “not known necessary” clause | `MANUSCRIPT.md:963-964` now says only that Theorem 4 gives a sufficient condition | **RESOLVED** |
| Advisory: unpinned `martinez2024real` URL | URL now targets `2309.10970v3`; 2024 retained as the correct v3 artifact year | **RESOLVED** |

## Record-by-record re-verification

### Summary

| Key | Primary/official authority | Metadata | Target | Verdict |
|---|---|---|---|---|
| `lps2019` | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022404919300933), [DOI](https://doi.org/10.1016/j.jpaa.2019.04.002) | Authors/year/title/venue/223(12)/5346–5359/DOI all match | DOI → matching Elsevier PII, HTTP 200 | PASS |
| `perry2016` | [University of Alabama PDF](https://ir-api.ua.edu/api/core/bitstreams/e9dc277b-9b56-47c9-8c00-bd4de9bab2fc/content) | Author/year/title/dissertation/institution all match | Repository item HTTP 200 | PASS |
| `edo2014` | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021869313005000), [DOI](https://doi.org/10.1016/j.jalgebra.2013.09.011) | Authors/year/title/venue/397/443–456/DOI all match | DOI → matching Elsevier PII, HTTP 200 | PASS |
| `grochow2025` | [Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/00029890.2024.2440297), [author PDF](https://home.cs.colorado.edu/~jgrochow/hensel-notes.pdf) | Author/year/title/venue/132(4)/350–355/DOI all match | DOI resolves to matching publisher path; publisher blocks automated HEAD 403 but identity is independently confirmed | PASS |
| `stacks00hp` | [Tag 00HP](https://stacks.math.columbia.edu/tag/00HP), [official cite page](https://stacks.math.columbia.edu/tag/00HP/cite) | Official title/author/year/root plus exact tag locator | Exact tag HTTP 200 | PASS |
| `stacks00fv` | [Tag 00FV](https://stacks.math.columbia.edu/tag/00FV), [official cite page](https://stacks.math.columbia.edu/tag/00FV/cite) | Official title/author/year/root plus exact tag locator | Exact tag HTTP 200 | PASS |
| `martinez2024zeros` | [arXiv v2](https://arxiv.org/abs/2404.11479v2), [v2 PDF](https://arxiv.org/pdf/2404.11479v2) | Authors/year/exact title/eprint/class/version all match | Versioned URL HTTP 200 | PASS |
| `martinez2024real` | [arXiv v3](https://arxiv.org/abs/2309.10970v3), [v3 PDF](https://arxiv.org/pdf/2309.10970v3) | Authors/title/eprint/class/version match; 2024 is correct for the explicit v3 artifact | Versioned URL HTTP 200 | PASS |
| `dlmf` | [DLMF How to Cite](https://dlmf.nist.gov/help/cite) | Official title, Release 1.2.7 date, root, and all ten editors match | Root and three permalinks HTTP 200 | PASS |

### Exact correction checks

#### Stacks

The official tag cite pages prescribe:

- author: `The Stacks project authors`;
- title: `The Stacks project`;
- root: `https://stacks.math.columbia.edu`;
- year: `2026`.

The corrected records reproduce those fields and add the exact locators in `note` and `url`. Tag 00HP states the nonzero-tensor characterization in Lemma 10.39.15(2); Tag 00FV is Theorem 10.34.1, Hilbert Nullstellensatz. Both records and both contexts pass.

#### Martínez title and version dates

The official arXiv API currently identifies `2404.11479v2` with the title:

> *Zeros of generalized hypergeometric polynomials via finite free convolution. Applications to multiple orthogonality*

The corrected title uses the same period. The URL is now pinned to v2.

For `2309.10970`, v1 was submitted in 2023, but the record explicitly cites v3. ArXiv reports the v3 update on 2 May 2024, and the v3 PDF masthead/date are May 2024. Therefore `year = 2024`, `version = 3`, and the corrected `/v3` URL form a coherent artifact-level citation and pass.

#### DLMF

The candidate now follows [DLMF's current recommended citation](https://dlmf.nist.gov/help/cite):

- title: *NIST Digital Library of Mathematical Functions*;
- Release 1.2.7 of 2026-06-15;
- F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds.;
- official root URL.

The manuscript also now links the exact claim locations:

- [DLMF 15.8.1](https://dlmf.nist.gov/15.8.E1), Pfaff transformation;
- [DLMF 18.5.7](https://dlmf.nist.gov/18.5.E7), Jacobi hypergeometric representation;
- [DLMF 18.16.1](https://dlmf.nist.gov/18.16.E1), strict ordering of Jacobi zeros.

The bibliographic and locator defects are fully resolved at source level.

## Complete citation-context re-audit

| ID | Source line | Key | Claim | Exact source location | Verdict |
|---|---:|---|---|---|---|
| C01 | 78 | `lps2019` | Computer-aided ranges for `e=3,4,5` | LPS Theorem 13, arXiv p. 9 / journal p. 5354 | PASS |
| C02 | 80 | `perry2016` | Earlier computational direction for LPS parameter `e=3` | Perry Theorem 1.3.2 and Chapter 3 conclusion, PDF pp. 7 and 38 | PASS |
| C03 | 82 | `edo2014` | Rigidity and Strong Factorial framework | Edo–van den Essen §§2.2–2.3 and 5.1–5.2, PDF pp. 4–7 and 14–15 | PASS |
| C04 | 85 | `lps2019` | Determinant described as “presently unmotivated” | LPS p. 3 after the `a_{d,e}` definition | PASS |
| C05 | 150 | `lps2019` | Theorem 13 ranges and Theorem 14 divisibility family | LPS pp. 9–10 / journal pp. 5354–5355 | PASS |
| C06 | 216 | `lps2019` | Definitions of `g`, `alpha`, and `a` | LPS §1.1, pp. 2–3 | PASS |
| C07 | 476 | `grochow2025` | Invertible-Jacobian square-system Hensel lifting | Grochow Theorem 1, author PDF p. 1 | PASS |
| C08 | 492 | `stacks00hp` | Faithful flatness preserves a nonzero tensor | Tag 00HP, Lemma 10.39.15(2) | PASS |
| C09 | 495 | `stacks00fv` | Weak Nullstellensatz gives a complex point | Tag 00FV, Theorem 10.34.1(1) and finite-type sentence | PASS |
| C10 | 497 | `lps2019` | Theorem 4 yields containment | LPS Theorem 4, p. 3 | PASS |
| C11 | 794 | `martinez2024zeros` | Hypergeometric concatenation under multiplicative finite free convolution | v2 Theorem A, p. 7 | PASS |
| C12 | 807 | `dlmf` | Pfaff transformation, Jacobi representation, and distinct Jacobi roots | DLMF 15.8.1, 18.5.7, 18.16.1, directly linked at lines 795–797 | PASS |
| C13 | 820 | `martinez2024real` | Reflection identity and logarithmic-mesh preservation | v3 Remark 2.12 and Proposition 2.17, pp. 14–15 | PASS |
| C14 | 964 | `lps2019` | Theorem 4 gives a sufficient condition | LPS Theorem 4, p. 3 | **PASS** |

The first-round C14 defect is gone. The corrected sentence no longer makes a negative state-of-literature claim; it states exactly the implication Theorem 4 supplies.

The corrected Perry sentence now explicitly says “the case later indexed by Lewis--Perry--Straub as `e=3`”, so the prior notation ambiguity is resolved. In the local LPS convention `e=3` means `(d,e+1)=(d,4)`, which is Perry's second-degree `e=4` computation.

## Closure

Citation frequencies in the corrected manuscript:

| Key | Count |
|---|---:|
| `lps2019` | 6 |
| each of the other eight keys | 1 |
| Total | 14 |

- Bibliography keys: 9.
- Unique cited keys: 9.
- Orphans: 0.
- Dangling citations: 0.
- Source-layer closure: **PASS**.

## Build-layer readback completed

The rebuilt artifacts postdate the corrected sources. Complete readback found:

- 9/9 rendered bibliography records PASS in TeX, extracted text, and PDF;
- 14/14 rendered citation contexts PASS, with the expected six LPS occurrences and one occurrence for each other work;
- the removed “not known necessary” phrase, old Stacks synthetic/`n.d.` records, old DLMF composite title, wrong Martínez punctuation, and stale release/version forms are absent;
- `build/main.txt` is byte-identical to a fresh `pdftotext -layout` extraction from the rebuilt PDF;
- all three exact DLMF equation permalinks survive as PDF link annotations;
- visual inspection of PDF pages 2, 3, 4, 8, 12, 13, 15, and 17 covers all citation contexts and all bibliography entries and found no clipping, overlap, missing glyphs, or broken record layout.

The complete receipt, record table, context table, hashes, and link checks are in `BUILD_LAYER_READBACK.md`.

Separate caveat: `MANIFEST.sha256` remains stale. The read-only manifest verifier returns exit 1 with 23 unmanifested files and 21 digest mismatches. This does not reverse the citation-integrity PASS, but it blocks an overall frozen-package/release-integrity PASS.

## Final correction-round verdict

**PASS — full citation integrity.** All prior citation defects are resolved in the corrected sources and in the rebuilt TeX/text/PDF.

**NOT PASSING — overall package integrity.** The manifest must be reconciled and refreshed before the candidate can claim a frozen-package or release-integrity PASS.

Machine-readable companion: `corrected_citation_ledger.json`; detailed generated-layer receipt: `BUILD_LAYER_READBACK.md`.
