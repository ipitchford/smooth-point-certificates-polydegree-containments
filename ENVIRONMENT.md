# Recorded build environment

The Stage 2 candidate was built and replayed on macOS arm64 on 9 August 2026
with:

- Python 3.14.6;
- SymPy 1.14.0;
- Singular 4.4.1;
- Pandoc 3.9;
- pdfTeX 1.40.29 from TeX Live 2026;
- Poppler `pdfinfo` 26.01.0.

The main verifier uses only the Python standard library. SymPy and Singular
are required for the exact geometry regeneration, Pandoc and TeX Live for the
paper build, and Poppler for the PDF structure check.
