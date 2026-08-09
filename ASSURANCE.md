# Assurance statement

## Publication-integrity disposition

- The frozen Stage 2 ancestor failed closed on citation/declaration/metadata
  semantics, not on a discovered theorem or computational defect.
- Correction round 1 produced `0.4.1-candidate`; all 9 references and all 14
  citation contexts pass current source and build readback.
- All 16 ledger claims were audited.  Unsafe novelty/assurance polarity was
  rewritten; no major distortion or unverifiable core claim remains.
- Forty of 132 eligible body paragraphs were screened (30.303%), covering all
  12 major sections: 20 original, 10 common knowledge, 10 cited paraphrase,
  and zero close/verbatim matches.  Self-plagiarism screening was not
  executable for an anonymous author without an identity corpus.
- All seven AI research failure modes are CLEAR after the provenance
  correction.  Mode 6 was initially suspected because the ancestor's
  `aiGenerated:false` conflicted with its drafting disclosure.
- No unsupported funding, competing-interest or contributor-role claim is
  made. Scholarly attribution is Anonymous; the human direction and
  publication role is recorded in `PROVENANCE.md`.
- The corrected pre-publication verdict is PASS WITH NOTES. The notes are
  visible assurance boundaries, not waived integrity defects.

## Completed at Stage 2

- Written proof chain from the Lewis--Perry--Straub definitions through the
  Jacobian, Euler, Hensel and curve statements.
- Current upstream v0.3.0 archive reconciled with the audited v0.2.0 witness
  corpus; the witness JSON is byte-identical.
- v0.3.0 internal manifest: 38/38.
- Upstream witness verifier: 51/51 under ordinary and optimised Python.
- No-import standard-library verifier: 10/10 symbolic gates and 51/51 witness
  relations in both modes; reports byte-identical.
- Sixteen mutation or negative controls plus one positive
  bad-characteristic regression in both modes.
- Exact (\mathbf Q)/Singular affine sweep for (2\le d\le20).
- Exact boundary sweep through (d=200).
- Written all-index proof that every individual one-variable boundary factor
  has simple positive roots, with its hypergeometric normalization and
  convolution factorization replayed exactly through index 301.
- Independent referee audit replaced an inapplicable strict-interlacing step
  with the verified logarithmic-mesh argument before manuscript integration.
- LaTeX compilation and rendered-PDF visual inspection.
- Citation-closure and authoritative-record audit for all nine cited records.

## Fresh Stage 2.5 replay

- Corrected candidate validator: PASS in ordinary and optimized Python;
  byte-identical reports.
- Replacement verifier: 10/10 symbolic gates and 51/51 witnesses in both
  modes; byte-identical reports.
- Mutation/regression controls: 17/17 in both modes; reports differ only in
  the recorded optimization level.
- Affine `d=2..20`, boundary `d=2..200`, and hypergeometric identity/evidence
  replays all pass in both modes; each ordinary/optimized pair is
  byte-identical.
- The v0.2 and v0.3 witness files are now both included, hash to
  `b659a8bccea30df4f800df526319bcbe01f429c3bee2ee8146983933da9cb38b`,
  and compare byte-for-byte.
- Publication-ready validation is rerun only after the real DOI, immutable
  release URLs, date and licence are coupled into the package.

## Supplementary proof-search receipts

- A raising-operator identity reduces every hypothetical affine triple zero
  to a non-transverse intersection and proves the entire (Y=0) slice; the
  remaining all-index triple-disjointness statement is open.
- A toric face ledger and mixed-volume formula are proved uniformly, while
  the full affine computation extends exactly through (d=30) and face tests
  through (d=250). The remaining face and interior unit-ideal theorems are
  open, so these extensions are not promoted into the manuscript cutoff.
- The supplementary normal and optimized receipts are byte-identical in the
  checks where byte identity is expected.

## Retained defect

The upstream verifier uses a proof-critical Python `assert` at its coefficient
divisibility guard. Optimised Python removes the guard. An injected invalid
numerator demonstrates the fail-open behaviour; current unmodified rows still
pass, and the replacement verifier uses explicit errors. This is a robustness
defect, not evidence that a current certificate is false.

## What the checks do not establish

They do not establish uniform adjacent boundary coprimality, the uniform
all-(d) affine theorem, priority, novelty,
independent reproduction, proof-assistant verification, external specialist
acceptance, journal acceptance, peer review, a REF grade or real-world impact.
