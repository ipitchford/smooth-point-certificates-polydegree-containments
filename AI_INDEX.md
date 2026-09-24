# AI index — smooth-point-certificates-polydegree-containments

## Identity and version

Documentation addendum: 2026-09-24. Indexes [source commit bba54b9a1667](https://github.com/ipitchford/smooth-point-certificates-polydegree-containments/tree/bba54b9a1667bfc9a9e88657aa495816812182bc) and candidate tag `v0.4.1-candidate`. This index was added after that release: it is **not** part of the original tag, DOI archive or frozen manifest. Existing release files and checksums remain unchanged. For historical manifest/allow-list checks, use a clean checkout of that tag, not this documentation-enriched branch. The addendum is authenticated by Git history.

[Release identity and DOI](README.md) · [Evidence Press context](https://evidencepress.org/releases/smooth-point-certificates-polydegree-containments/)

## Exact scope

Candidate Jacobian identity, integral Euler syzygy, sharpened Hensel criterion, curve bridge and uniform squarefreeness of individual boundary factors. Recorded finite computation covers the full affine statement for 2≤d≤20 and adjacent boundary coprimality through d=200.

The linked manuscript and claim register control all hypotheses and quantifiers; this index is a navigation aid, not a substitute proof.

## Claim and evidence map

- [MANUSCRIPT.md](MANUSCRIPT.md) — Precise statements and proofs.
- [CLAIM_STATUS.json](CLAIM_STATUS.json) — Claim register.
- [ASSURANCE.md](ASSURANCE.md) — Assurance.
- [BUILD.md](BUILD.md) — Full replay and environment.
- [CITATION_AUDIT.md](CITATION_AUDIT.md) — Sources.
- [PROVENANCE.md](PROVENANCE.md) — Provenance.
- [LICENSES.md](LICENSES.md) — Rights.

## Reproduce

From the indexed release root, after inspecting the commands and installing the documented environment:

```sh
python3 -m pip install -r requirements.txt
python3 -B scripts/verify_jacobian_refactor.py --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
python3 -B scripts/test_mutations.py --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
```

Singular is also required for the complete checks. BUILD.md includes package validation and extended affine/boundary checks. Recorded package totals are 10 symbolic gates, 51 witness relations and 17 mutation/regression controls, not a fresh index-time rerun.

## Trust boundary and safe reuse

Finite ranges do not prove uniform adjacent coprimality or the all-d affine statement. Historical open-status statements in this package are version-scoped, not a current literature determination.

No new mathematical validation, formalisation, independent reproduction or novelty audit was performed for this documentation repair. Preserve the anonymous attribution and existing citation metadata. Distinguish producer checks, finite formal results, universal written arguments and external review. Before downstream reuse, match the exact statement and dependency scope and check subsequent corrections; a DOI or successful command alone is not proof of correctness.

## Licence and provenance

Use the rights/provenance sources linked above and [README](README.md); cited and third-party material retains its own terms. This new index is dedicated under CC0-1.0, without changing any existing licence or attribution.

