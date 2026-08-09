# Stage 2.5 Phase A/B citation-integrity audit

## Verdict

**FAIL under the requested fail-closed policy.**

All nine cited sources exist, and all three supplied DOIs resolve to the correct works. The package nevertheless fails strict citation integrity because four bibliography records have exact-metadata defects and one of fourteen citation contexts is not fully supported by its cited source.

| Gate | Result |
|---|---:|
| Bibliography records | 9 |
| Source existence | 9 PASS / 0 FAIL |
| Strict record metadata | 5 PASS / 4 FAIL |
| DOI targets | 3 PASS / 0 FAIL |
| In-text citation occurrences audited | 14/14 (100%) |
| Citation context | 13 PASS / 1 FAIL |
| Orphan bibliography keys | 0 |
| Dangling citation keys | 0 |
| Hallucinated sources | 0 |
| Overall publication gate | **FAIL** |

The strict record failures are `stacks00hp`, `stacks00fv`, `martinez2024zeros`, and `dlmf`. The context failure is the uncited state-of-knowledge clause “not known necessary” at `MANUSCRIPT.md:960`.

## Scope, timestamp, and method

- Audit date/time: **2026-08-09T19:52:50+01:00 (BST)**.
- Frozen package audited read-only: `/Users/admin/Documents/Codex/2026-08-09/the-0processed-folder-on-the-mac/outputs/smooth-point-certificates-polydegree-stage2-2026-08-09`.
- Bibliography corpus: all nine records in `references.bib`.
- Citation-context corpus: all fourteen `[@key]` occurrences in `MANUSCRIPT.md`; the generated `build/main.tex` bibliography was also checked for closure and rendering.
- Source policy: publisher pages, DOI/Crossref registry, official institutional repository, official arXiv API and versioned PDFs, official Stacks tag/cite pages, author-hosted paper copy where needed for theorem text, and official NIST DLMF pages only. No metadata conclusion relies on memory, an aggregator, the package's pre-existing citation audit, or a secondary bibliography.
- Fail rule: an unresolved or ambiguous supplied field is a FAIL. Optional fields that were not supplied, such as a dissertation's total extent, are reported but are not converted into defects.
- Exactness rule: case normalization is accepted; a changed title delimiter is not accepted where both the official API and the pinned PDF agree on the original punctuation.
- DOI target rule: identity must match at the publisher and in the official DOI registry. An automated publisher block does not fail a DOI where the resolver destination and publisher article page independently match.

Frozen source hashes:

| File | SHA-256 |
|---|---|
| `references.bib` | `19c866aa5f089171eea7bc1e9ab99409dd2039e3948cf8192ab9db5c99819a05` |
| `MANUSCRIPT.md` | `a9f06d035fe2ce1c4b4e1d9d7044f2dfd8006c9f2cab605e1cc34e4de8bf9bd8` |
| `build/main.tex` | `de55d7e5c22dc5e2e02914735b11b72136e666269f6f5e60ca995d15734f9ecf` |

## Search log and record-level verification

### 1. `lps2019` — PASS

- Exact discovery query: `"10.1016/j.jpaa.2019.04.002"`
- Top authoritative record: [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0022404919300933)
- Official alternates: [DOI](https://doi.org/10.1016/j.jpaa.2019.04.002), [arXiv 1809.09681](https://arxiv.org/abs/1809.09681)
- Existence: **PASS**. Publisher, Crossref, and arXiv identify the same work.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Authors | Drew Lewis; Kaitlyn Perry; Armin Straub | Same | PASS |
| Year | 2019 | 2019 | PASS |
| Title | *An algorithmic approach to the Polydegree Conjecture for plane polynomial automorphisms* | Same | PASS |
| Venue | *Journal of Pure and Applied Algebra* | Same | PASS |
| Volume/issue | 223(12) | 223(12) | PASS |
| Pages | 5346–5359 | 5346–5359 | PASS |
| DOI | 10.1016/j.jpaa.2019.04.002 | Same | PASS |
| URL | arXiv abstract | Official alternate for the same article, current v1 | PASS |

DOI target check: `https://doi.org/10.1016/j.jpaa.2019.04.002` returned a final HTTP 200 at Elsevier PII `S0022404919300933`, which is the matching article. Hallucination-pattern check: no phantom DOI, author, title, or venue collision.

Exact claim locations used below: definitions and Theorem 4 on arXiv PDF pages 2–3; Theorem 13 on page 9; Theorem 14 on page 10. These correspond to journal pages 5347–5348 and 5354–5355.

### 2. `perry2016` — PASS

- Exact discovery query: `"Polydegree properties of polynomial automorphisms" Perry`
- Top authoritative record: [University of Alabama repository item](https://ir.ua.edu/items/f71aa1b3-0dbc-42a2-9f59-3f01eb1a5529)
- Official full metadata: [repository full item page](https://ir.ua.edu/items/f71aa1b3-0dbc-42a2-9f59-3f01eb1a5529/full)
- Existence: **PASS**.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Author | Kaitlyn Anne Perry | Same | PASS |
| Year | 2016 | 2016 | PASS |
| Title | *Polydegree properties of polynomial automorphisms* | Same | PASS |
| Type | Doctoral dissertation | Dissertation submitted for the degree of Doctor of Philosophy | PASS |
| School/venue | The University of Alabama | The University of Alabama | PASS |
| Volume | Not applicable | Not applicable | N/A |
| Pages | Not supplied | Repository extent 57 pages | Optional omission |
| DOI | None | None reported | N/A |
| URL | Repository item UUID | Same official item | PASS |

The PDF title page confirms the author, title, PhD status, Department of Mathematics, institution, and 2016 date. Hallucination-pattern check: clean.

### 3. `edo2014` — PASS

- Exact discovery query: `"10.1016/j.jalgebra.2013.09.011"`
- Top authoritative record: [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0021869313005000)
- Official alternates: [DOI](https://doi.org/10.1016/j.jalgebra.2013.09.011), [arXiv 1304.3956](https://arxiv.org/abs/1304.3956)
- Existence: **PASS**.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Authors | Eric Edo; Arno van den Essen | Same | PASS |
| Year | 2014 | 2014 | PASS |
| Title | *The Strong Factorial Conjecture* | Same | PASS |
| Venue | *Journal of Algebra* | Same | PASS |
| Volume/issue | 397; no issue | 397; no issue reported | PASS |
| Pages | 443–456 | 443–456 | PASS |
| DOI | 10.1016/j.jalgebra.2013.09.011 | Same | PASS |
| URL | arXiv abstract | Official alternate, current v2 | PASS |

DOI target check: final HTTP 200 at Elsevier PII `S0021869313005000`, identity matched. Hallucination-pattern check: clean.

### 4. `grochow2025` — PASS

- Exact discovery query: `"10.1080/00029890.2024.2440297"`
- Top authoritative record: [Taylor & Francis article](https://www.tandfonline.com/doi/abs/10.1080/00029890.2024.2440297)
- Official content copy: [author-hosted PDF](https://home.cs.colorado.edu/~jgrochow/hensel-notes.pdf)
- Existence: **PASS**.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Author | Joshua A. Grochow | Same | PASS |
| Year | 2025 | 2025 | PASS |
| Title | *Multivariate Hensel lifting without assuming as many variables as equations* | Same, with headline capitalization | PASS |
| Venue | *The American Mathematical Monthly* | Same | PASS |
| Volume/issue | 132(4) | 132(4) | PASS |
| Pages | 350–355 | 350–355 | PASS |
| DOI | 10.1080/00029890.2024.2440297 | Same | PASS |
| URL | Publisher full-text path | Correct publisher work | PASS |

DOI target check: the resolver led to the correct Taylor & Francis full-text path. Automated `HEAD` received HTTP 403 at the final publisher page, but this is not an identity ambiguity: the publisher article page and Crossref both independently report the exact record. The DOI's `2024` substring is a registration identifier, not a publication-year mismatch. Hallucination-pattern check: clean.

### 5. `stacks00hp` — FAIL

- Exact discovery query: `site:stacks.math.columbia.edu/tag/00HP "Lemma 10.39.15"`
- Top authoritative record: [Stacks Project Tag 00HP](https://stacks.math.columbia.edu/tag/00HP)
- Official citation instructions: [How to cite Tag 00HP](https://stacks.math.columbia.edu/tag/00HP/cite)
- Existence: **PASS**. Strict metadata: **FAIL**.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Author | The Stacks Project Authors | The Stacks project authors | PASS after case normalization |
| Year | Omitted | 2026 in official BibTeX | **FAIL** |
| Title | *Lemma 10.39.15 (Tag 00HP): Faithfully flat modules* | Generic BibTeX title *The Stacks project*; tag header *Lemma 10.39.15 (00HP)*; slogan “A flat module is faithfully flat iff it has nonzero fibers” | **FAIL** |
| Venue | The Stacks Project | The Stacks project | PASS |
| Volume/pages | N/A | N/A | N/A |
| DOI | None | None | N/A |
| URL | Exact tag | Exact tag | PASS |

The problem is not source existence. It is a genuine tag wrapped in a non-official bibliographic title. The missing year causes the generated bibliography to print `n.d.` even though the official cite page supplies 2026. This is a synthetic-metadata pattern, not a hallucinated theorem.

### 6. `stacks00fv` — FAIL

- Exact discovery query: `site:stacks.math.columbia.edu/tag/00FV "Theorem 10.34.1"`
- Top authoritative record: [Stacks Project Tag 00FV](https://stacks.math.columbia.edu/tag/00FV)
- Official citation instructions: [How to cite Tag 00FV](https://stacks.math.columbia.edu/tag/00FV/cite)
- Existence: **PASS**. Strict metadata: **FAIL**.

| Field | Supplied | Official | Verdict |
|---|---|---|---|
| Author | The Stacks Project Authors | The Stacks project authors | PASS after case normalization |
| Year | Omitted | 2026 in official BibTeX | **FAIL** |
| Title | *Theorem 10.34.1 (Tag 00FV): Hilbert Nullstellensatz* | Generic BibTeX title *The Stacks project*; tag header *Theorem 10.34.1 (00FV): Hilbert Nullstellensatz* | Tag locator substantively exact, but **FAIL** against the official generic entry under the strict policy |
| Venue | The Stacks Project | The Stacks project | PASS |
| Volume/pages | N/A | N/A | N/A |
| DOI | None | None | N/A |
| URL | Exact tag | Exact tag | PASS |

Again, the mathematical source is real and exact. The failure is bibliographic construction plus the missing official year, rendered as `n.d.`.

### 7. `martinez2024zeros` — FAIL

- Exact discovery query: `site:arxiv.org/abs/2404.11479 "Zeros of generalized hypergeometric polynomials"`
- Top authoritative record: [arXiv 2404.11479v2](https://arxiv.org/abs/2404.11479v2)
- Pinned primary artifact: [v2 PDF](https://arxiv.org/pdf/2404.11479v2)
- Existence: **PASS**. Strict metadata: **FAIL**.

| Field | Supplied | Official v2 | Verdict |
|---|---|---|---|
| Authors | Andrei Martínez-Finkelshtein; Rafael Morales; Daniel Perales | Same; accents visible in PDF | PASS |
| Year | 2024 | First submitted 2024-04-17; v2 2024-06-03; PDF dated 2024-06-04 | PASS |
| Title | *... finite free convolution: Applications to multiple orthogonality* | *... finite free convolution. Applications to multiple orthogonality* | **FAIL** |
| Venue | arXiv | arXiv | PASS |
| Volume/pages | Not supplied | No volume; v2 has 53 pages | N/A / optional omission |
| DOI | None | None reported | N/A |
| eprint/class/version | 2404.11479; math.CA; v2 | Same | PASS |
| URL | Unversioned abstract | Currently resolves to v2 | PASS-current; pin `/v2` for durability |

Both the official arXiv API title and the v2 PDF use a **period**, not a colon, before “Applications”. Under an exact-field, gray-zone-fails rule this is a record failure, though it is plainly a punctuation normalization rather than a fabricated source. The version field is correct; the URL should still be made version-specific.

### 8. `martinez2024real` — PASS, with version-date rationale

- Exact discovery query: `site:arxiv.org/abs/2309.10970 "Real roots of hypergeometric polynomials"`
- Top authoritative record: [arXiv 2309.10970v3](https://arxiv.org/abs/2309.10970v3)
- Pinned primary artifact: [v3 PDF](https://arxiv.org/pdf/2309.10970v3)
- Existence: **PASS**. Strict metadata: **PASS**.

| Field | Supplied | Official v3 | Verdict |
|---|---|---|---|
| Authors | Andrei Martínez-Finkelshtein; Rafael Morales; Daniel Perales | Same; accents visible in PDF | PASS |
| Year | 2024 | v1 submitted 2023-09-19; v3 updated 2024-05-02; v3 masthead says 2 May 2024 and PDF date is 3 May 2024 | **PASS for the explicitly cited v3 artifact** |
| Title | *Real roots of hypergeometric polynomials via finite free convolution* | Same | PASS |
| Venue | arXiv | arXiv | PASS |
| Volume/pages | Not supplied | No volume; v3 has 47 pages | N/A / optional omission |
| DOI | None | None reported | N/A |
| eprint/class/version | 2309.10970; math.CA; v3 | Same | PASS |
| URL | Unversioned abstract | Currently resolves to v3 | PASS-current; pin `/v3` for durability |

This edge case is not failed. `year = 2024` would be wrong if the record purported to date the base arXiv submission, which began in 2023. But the record explicitly says `version = 3`, and the targeted v3 artifact is dated May 2024 in both arXiv history and the PDF itself. The year is therefore a defensible and exact **version year**. A versioned URL would remove the remaining durability risk.

### 9. `dlmf` — FAIL

- Exact discovery queries:
  - `site:dlmf.nist.gov/15.8 Pfaff transformation DLMF 15.8.1`
  - `site:dlmf.nist.gov/18.5 "Jacobi" "18.5.7" zeros 18.16`
- Top authoritative metadata page: [DLMF: How to Cite](https://dlmf.nist.gov/help/cite)
- Claim-specific official permalinks: [15.8.1](https://dlmf.nist.gov/15.8.E1), [18.5.7](https://dlmf.nist.gov/18.5.E7), [18.16.1](https://dlmf.nist.gov/18.16.E1)
- Existence: **PASS**. Strict metadata: **FAIL**.

| Field | Supplied | Official recommended citation | Verdict |
|---|---|---|---|
| Author | NIST Digital Library of Mathematical Functions | No corporate-author field in recommended BibTeX; ten named editors are given in `note` | **FAIL** |
| Year/release | No year; access date only | Release 1.2.7 of 2026-06-15 | **FAIL** |
| Title | *Hypergeometric transformations, Jacobi representations and zeros* | *NIST Digital Library of Mathematical Functions* | **FAIL** |
| Venue/locator | “Sections 15.8, 18.5 and 18.16” in `howpublished` | Root URL plus release; specific equations/sections should use permalinks | **FAIL** |
| Volume/pages | N/A | N/A | N/A |
| DOI | None | None | N/A |
| URL | DLMF root | Same root URL as the recommended bibliographic entry | PASS; locator precision fails separately |

The supplied record has synthesized a composite work title from the three topics. DLMF's official citation on the audit date is:

> *NIST Digital Library of Mathematical Functions*, https://dlmf.nist.gov/, Release 1.2.7 of 2026-06-15, followed by the named editors.

The official instructions also explicitly recommend equation/section permalinks. The generated bibliography currently renders the source as `n.d.` and omits the release and editors. This is the clearest metadata-integrity failure in the set. The cited mathematical content itself is real and is evaluated separately below.

## DOI and URL target ledger

| Key | Identifier/URL check | Result |
|---|---|---|
| `lps2019` | DOI → Elsevier PII `S0022404919300933`, HTTP 200 | PASS |
| `edo2014` | DOI → Elsevier PII `S0021869313005000`, HTTP 200 | PASS |
| `grochow2025` | DOI → matching Taylor & Francis full-text path; final automated HEAD blocked 403; publisher page + Crossref identity agree | PASS |
| `perry2016` | Official University of Alabama UUID item | PASS |
| `stacks00hp` | Exact official Tag 00HP page | PASS target; FAIL metadata |
| `stacks00fv` | Exact official Tag 00FV page | PASS target; FAIL metadata |
| `martinez2024zeros` | Official arXiv base URL currently resolves to v2 | PASS target; version-pin advised |
| `martinez2024real` | Official arXiv base URL currently resolves to v3 | PASS target; version-pin advised |
| `dlmf` | Official root URL; specific claims resolved at three official permalinks | PASS existence; FAIL record precision |

## Complete in-text citation-context audit

All fourteen occurrences were audited, not a sample.

| ID | Line | Key | Citation context | Exact primary location | Verdict |
|---|---:|---|---|---|---|
| C01 | 78 | `lps2019` | Computer-aided ranges for `e=3,4,5` | LPS Theorem 13, arXiv p. 9 / journal p. 5354 | PASS |
| C02 | 80 | `perry2016` | Perry's earlier computational direction for LPS parameter `e=3` | Dissertation Theorem 1.3.2 and Chapter 3 conclusion, PDF pp. 7, 38 | PASS, with indexing note |
| C03 | 81 | `edo2014` | Rigidity/Strong Factorial framework for inverse-coefficient polynomials | Edo–van den Essen §§2.2–2.3, 5.1–5.2, PDF pp. 4–7, 14–15 | PASS |
| C04 | 84 | `lps2019` | Determinant described as “presently unmotivated” | LPS p. 3, immediately after `a_{d,e}` definition | PASS |
| C05 | 149 | `lps2019` | Theorem 13 ranges and Theorem 14 divisibility family | LPS pp. 9–10 / journal pp. 5354–5355 | PASS |
| C06 | 215 | `lps2019` | Definitions of `g`, `alpha`, and `a` | LPS §1.1, pp. 2–3 | PASS |
| C07 | 475 | `grochow2025` | Invertible-Jacobian square-system Hensel lift | Grochow Theorem 1, author PDF p. 1 | PASS |
| C08 | 491 | `stacks00hp` | Faithfully flat extension preserves nonzero tensor | Tag 00HP, Lemma 10.39.15, condition (2) | PASS |
| C09 | 494 | `stacks00fv` | Weak Nullstellensatz gives a complex point | Tag 00FV, Theorem 10.34.1, part (1) and finite-type sentence | PASS |
| C10 | 496 | `lps2019` | Theorem 4 yields containment | LPS Theorem 4, p. 3 | PASS |
| C11 | 793 | `martinez2024zeros` | Hypergeometric concatenation under multiplicative finite free convolution | v2 Theorem A, p. 7 | PASS |
| C12 | 803 | `dlmf` | Pfaff transform, Jacobi representation, and distinct Jacobi roots | DLMF 15.8.1, 18.5.7, 18.16.1 | PASS substantively |
| C13 | 816 | `martinez2024real` | Reflection plus logarithmic-mesh preservation | v3 Remark 2.12 and Proposition 2.17, pp. 14–15 | PASS |
| C14 | 960 | `lps2019` | “Theorem 4 gives a sufficient, not known necessary, condition” | LPS Theorem 4, p. 3 | **FAIL** |

### Context notes

1. **Perry notation.** The manuscript is using Lewis–Perry–Straub's parameter `e`: their `e=3` problem concerns `(d,e+1)=(d,4)`. Perry's thesis describes the same second degree as the `e=4` case and gives the bounded Gröbner computation through `d=45`. The sentence is supportable in its local notation but would benefit from “in the later LPS indexing” to prevent a reader from thinking Perry called it `e=3`.

2. **DLMF substance versus record metadata.** Equation 15.8.1 supplies the Pfaff transformation; 18.5.7 supplies the hypergeometric Jacobi representation; 18.16.1 orders the `n` Jacobi zeros strictly between `0` and `π`, hence gives distinct roots in `(-1,1)` for the orthogonality range. The claim is supported even though the `dlmf` bibliography record fails.

3. **The sole context failure.** LPS Theorem 4 is plainly a sufficient implication. The paper does not state that the condition is “not known necessary”, and a single sufficient theorem cannot certify that negative state-of-literature claim. Under the requested rule this occurrence fails. The cleanest repair is either to remove the state-of-knowledge clause or support it with an explicit primary statement/current bounded literature audit; the latter still should be worded as an audit result, not as universal absence.

## Orphan and dangling closure

Bibliography keys:

`lps2019`, `perry2016`, `edo2014`, `grochow2025`, `stacks00hp`, `stacks00fv`, `martinez2024zeros`, `martinez2024real`, `dlmf`.

Citation frequencies:

| Key | Occurrences |
|---|---:|
| `lps2019` | 6 |
| each of the other eight keys | 1 each |
| Total | 14 |

- Unique cited keys: 9/9.
- Orphan bibliography records: none.
- Dangling citation keys: none.
- Generated `build/main.tex` bibliography items: 9/9.
- Closure verdict: **PASS**.

The generated bibliography also exposes the metadata failures: `stacks00hp`, `stacks00fv`, and `dlmf` render as `n.d.`, and DLMF's release and editors disappear.

## Blocking defects and safe corrections

1. **`martinez2024zeros` exact title:** replace the colon with the official period before “Applications”. Prefer the versioned URL `https://arxiv.org/abs/2404.11479v2`.

2. **Stacks records:** use the Stacks Project's official 2026 entry and tag locators, or at minimum add `year = {2026}` and make the tag title exact. The official pattern is one generic *The Stacks project* record plus explicit `[Tag 00HP]` and `[Tag 00FV]` locators.

3. **DLMF:** replace the composite title/author construction with DLMF's recommended Release 1.2.7 citation, include the ten editors, and cite the exact permalinks 15.8.1, 18.5.7, and 18.16.1.

4. **Line 960:** do not use LPS Theorem 4 to support “not known necessary”. Safe wording from the verified source alone is: “Lewis–Perry–Straub Theorem 4 gives a sufficient condition.” Any stronger state-of-knowledge sentence needs separate current evidence and calibrated bounded-search wording.

5. **Advisory, not counted as a current failure:** pin both arXiv URLs to `/v2` and `/v3`. For `martinez2024real`, retain 2024 if the record continues to identify v3 explicitly; use 2023 only if switching to an unversioned/base-work citation convention.

## Bottom line

This is **not a hallucinated bibliography**: source existence is 9/9 and DOI identity is 3/3. It is nevertheless a **citation-integrity FAIL** under exact, fail-closed review. Publication should remain gated until the four record defects and the one unsupported context clause are corrected and the generated bibliography is rebuilt/read back.

The machine-readable companion is `citation_integrity_ledger.json` in this directory.
