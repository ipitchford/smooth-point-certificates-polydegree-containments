# Build and validation

From this directory:

```sh
pandoc MANUSCRIPT.md --standalone --citeproc \
  --bibliography references.bib \
  --from markdown+tex_math_dollars --to latex \
  --output build/main.tex

python3 /Users/admin/.codex/plugins/cache/openai-bundled/latex/0.2.4/scripts/compile_latex.py \
  "$PWD/build/main.tex" --compiler texlive --output-directory "$PWD/build"

python3 -B scripts/validate_candidate.py --root "$PWD" \
  --report build/validation_report.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" \
  --report build/validation_report_optimized.json
cmp build/validation_report.json build/validation_report_optimized.json
```

`--publication-ready` is a deliberately stricter negative control. Run it in
both modes; it must fail while the metadata remains a pre-deposit template
with no DOI, licence or public URLs:

```sh
python3 -B scripts/validate_candidate.py --root "$PWD" \
  --publication-ready --report build/publication_ready_expected_failure.json
python3 -B -O scripts/validate_candidate.py --root "$PWD" \
  --publication-ready \
  --report build/publication_ready_expected_failure_optimized.json
cmp build/publication_ready_expected_failure.json \
  build/publication_ready_expected_failure_optimized.json
```

The Stage 1/Stage 2 witness reconciliation is directly replayable:

```sh
cmp source_records/stage1_v0.2/polydegree_e3_witnesses_50_100.json \
  evidence/upstream/polydegree_e3_witnesses_50_100.json
```

## Evidence replay

The standard-library verifier and its controls need only Python 3.14 or a
compatible Python 3 implementation:

```sh
python3 -B scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
python3 -B -O scripts/verify_jacobian_refactor.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json

python3 -B scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
python3 -B -O scripts/test_mutations.py \
  --witness-data evidence/upstream/polydegree_e3_witnesses_50_100.json
```

The exact affine and boundary regenerations additionally require SymPy 1.14.0
and Singular 4.4.1:

```sh
python3 -B scripts/explore_geometry.py --d-min 2 --d-max 20
python3 -B -O scripts/explore_geometry.py --d-min 2 --d-max 20
python3 -B scripts/boundary_sweep.py --d-min 2 --d-max 200
python3 -B -O scripts/boundary_sweep.py --d-min 2 --d-max 200
```

The uniform boundary-factor proof has an exact hypergeometric replay:

```sh
python3 -B scripts/verify_boundary_hypergeom.py \
  --d-max 300 --factor-max 300 --interlace-max 120
python3 -B -O scripts/verify_boundary_hypergeom.py \
  --d-max 300 --factor-max 300 --interlace-max 120
```

Supplementary toric and triple-disjointness attacks have their own commands
and boundaries in `proof_search/*/STATUS_MEMO.md` or `PROOF_MEMO.md`. They are
not prerequisites for the core manuscript validator.

After unpacking a frozen release directory, check its complete inventory in
both modes:

```sh
python3 -B scripts/verify_manifest.py --root "$PWD"
python3 -B -O scripts/verify_manifest.py --root "$PWD"
```
