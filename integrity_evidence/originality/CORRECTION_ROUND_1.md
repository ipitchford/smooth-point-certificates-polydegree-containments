# Stage 2.5 originality correction round 1

**Current-candidate verdict: PASS.** All three changed body paragraphs were
rechecked. None introduces a `CLOSE_MATCH` or `VERBATIM` issue; each remains
supported by the cited primary source. The boundary-factor proof remains
**PROVED**, including the repaired reflected logarithmic-mesh step. There is no
gray-zone finding or blocking defect.

Candidate: `work/irreducible-norms-ref-upgrade/stage2_5/candidate/MANUSCRIPT.md`  
Candidate version: `0.4.1-candidate`  
Candidate SHA-256: `5ff53d9074a4651940a12b432a7194baee1e078470d88d0ec5f22a7fe29ef762`  
Frozen Stage 2 manuscript SHA-256: `a9f06d035fe2ce1c4b4e1d9d7044f2dfd8006c9f2cab605e1cc34e4de8bf9bd8`  
Executed: `2026-08-09T20:15:39+0100`

## Scope and current Phase D coverage

The frozen-to-current diff contains three changes inside the established Phase
D body scope, Abstract through Conclusion:

1. Perry indexing clarification in Introduction paragraph `P006`.
2. Exact DLMF permalink sentence in Theorem 7.2 paragraph `P098`.
3. Removal of “not known necessary” in Discussion paragraph `P122`.

Later declaration changes are outside the established body scope and do not
enter the Phase D denominator.

Re-running the corrected paragraph enumerator under normal Python and
`python -O` produced byte-identical artifacts:

- Current eligible body paragraphs: **132**.
- Current sampled paragraphs: **40**.
- Current coverage: **40/132 = 30.303%**, above the 30% Mode 1 threshold.
- Major-section coverage: **12/12**.
- The 40 sample IDs are unchanged from the frozen audit.
- All three changed paragraphs are members of that sample and were rechecked
  in this round.

Recomputed inventory SHA-256:
`a9859bad0503116eb7b9c21e8278a43ec9e425fa154c0e40eb01e05f356d0483`  
Recomputed sample-plan SHA-256:
`cf06a5ad218c19fa69a90b74c8065d34bd1f7629de5e9a450f8a30911cf10876`

## Changed-paragraph originality and source checks

| Paragraph | Current lines | Quoted 8--12-word search | Unquoted search | Result | Grade |
|---|---:|---|---|---|---|
| `P006` | 77--82 | `"earlier thesis developed the same computational direction for the case later"` | `Perry thesis computational polydegree case e=3 Lewis Perry Straub indexing` | No exact or close wording hit. The unquoted search returned the primary thesis and LPS paper, which support the claim but use different prose. | `PARAPHRASE` |
| `P098` | 794--799 | `"Pfaff transformation DLMF 15.8.1 the Jacobi representation DLMF 18.5.7"` | `Pfaff transformation DLMF 15.8.1 Jacobi representation DLMF 18.5.7 strict ordering zeros DLMF 18.16.1` | Exact search returned no result. The unquoted search returned the relevant DLMF equations and secondary uses, with no matching manuscript sentence. | `PARAPHRASE` |
| `P122` | 962--964 | `"Lewis--Perry--Straub Theorem 4 gives a sufficient condition"` | `Lewis Perry Straub Theorem 4 sufficient condition Polydegree Conjecture smooth point` | Exact search returned no result. The unquoted search returned the cited primary paper and unrelated generic results, with no matching sentence. | `PARAPHRASE` |

No correction contains a `CLOSE_MATCH` or an uncited run of 20 or more source
words. The result is therefore `PASS` under the instructed gray-zone-fails
policy.

### Perry indexing clarification

The revised wording is technically supported and resolves the notation shift.
Perry's thesis describes its computer-assisted result as the `e=4` case and
states

`G_(d+3) intersect G_(d,4) != empty` for `2 <= d <= 45`.

It also records that the range was checked using a Gröbner basis in
Mathematica. Lewis--Perry--Straub later use `e` for the number of coefficient
variables in the implication

`G_(d+e) subset closure G_(d,e+1)`,

and call the corresponding computer-aided case `e=3`. Thus “the case later
indexed by Lewis--Perry--Straub as `e=3`” accurately distinguishes the two
conventions; it does not copy either source's wording.

Primary evidence:

- [Perry dissertation PDF](https://ir-api.ua.edu/api/core/bitstreams/e9dc277b-9b56-47c9-8c00-bd4de9bab2fc/content), PDF pp. 12 and 43.
- [Lewis--Perry--Straub primary PDF](https://arxiv.org/pdf/1809.09681), PDF pp. 2--3.

### Exact DLMF links

All three direct links resolve to the claimed authoritative equations:

- [DLMF 15.8.1](https://dlmf.nist.gov/15.8.E1) is the hypergeometric linear
  transformation used in the proof as Pfaff's transformation.
- [DLMF 18.5.7](https://dlmf.nist.gov/18.5.E7) is the Jacobi polynomial
  hypergeometric representation.
- [DLMF 18.16.1](https://dlmf.nist.gov/18.16.E1) strictly orders the Jacobi
  zeros between zero and pi, giving distinct zeros under the manuscript's
  already-verified Jacobi parameter hypotheses.

The new sentence is source metadata plus an independently worded deduction;
it is not a close textual match.

### Discussion qualification

[Lewis--Perry--Straub Theorem 4](https://arxiv.org/pdf/1809.09681) states
specialization hypotheses and concludes the required polydegree containment.
Calling it a sufficient condition is exact. Removing “not known necessary”
removes an unsupported literature-status modifier and leaves the theorem's
supported direction intact. No mathematical claim or proof depends on the
deleted phrase.

## Boundary-factor proof preservation

The only change within Theorem 7.2 is the replacement of a broad DLMF reference
sentence by the three exact equation links above. No formula, normalization,
Jacobi parameter pair, inequality, convolution definition, or low-degree case
changed.

In particular, the following load-bearing route is unchanged:

- arXiv:2404.11479v2 Theorem A supplies hypergeometric parameter
  concatenation, and Proposition 2.4(v) supplies half-line sign preservation.
- After reflection, both convolution factors are positive-rooted. For `M>=2`,
  simplicity of the reflected first factor gives logarithmic mesh greater than
  one; arXiv:2309.10970v3 Proposition 2.17 preserves that strict lower bound.
- Remark 2.12 reflects the result back; `M=0,1` remain separately constant and
  linear; scaling and reciprocation preserve simple positive roots.

Accordingly, the prior all-`n>=2` proof verdict remains **PROVED**.

## Defects

Blocking defects: **none**.  
Gray-zone findings: **none**.  
Correction-round verdict: **PASS**.

## Tool limitation

The originality component is a public-Web heuristic check, not Turnitin or
iThenticate. It cannot cover private, paywalled or cross-language corpora. This
focused round rechecked every changed body paragraph and relies on the frozen
40-paragraph sample for unchanged prose; its current unique coverage is
30.303%.
