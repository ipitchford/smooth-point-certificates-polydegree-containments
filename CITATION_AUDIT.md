# Citation audit

**Verification date:** 9 August 2026  
**Stage 2.5 final result:** 9/9 records PASS; 14/14 contexts PASS; 0
orphan and 0 dangling keys

The frozen Stage 2 bibliography was checked against primary or authoritative
records and initially failed closed on four exact-metadata records and one
unsupported context clause.  Correction round 1 repaired those defects and
the complete source and generated-PDF layers were rechecked.

| Key | Authoritative record and exact use | Final result |
|---|---|---|
| `lps2019` | [Publisher DOI](https://doi.org/10.1016/j.jpaa.2019.04.002) and [arXiv:1809.09681](https://arxiv.org/abs/1809.09681): definitions, Theorem 4, Theorems 13–14 | PASS. The discussion now attributes only sufficiency to Theorem 4. |
| `perry2016` | [University of Alabama repository](https://ir.ua.edu/items/f71aa1b3-0dbc-42a2-9f59-3f01eb1a5529): earlier computational direction | PASS. Text explicitly says the case is later indexed by LPS as `e=3`. |
| `edo2014` | [Publisher DOI](https://doi.org/10.1016/j.jalgebra.2013.09.011) and [arXiv:1304.3956](https://arxiv.org/abs/1304.3956): Strong Factorial antecedent | PASS. |
| `grochow2025` | [Publisher DOI](https://doi.org/10.1080/00029890.2024.2440297): multivariate Hensel lifting | PASS. Resolver, publisher record and Crossref identity agree. |
| `stacks00hp` | [Tag 00HP](https://stacks.math.columbia.edu/tag/00HP) and official cite page: faithful flatness | PASS. Official 2026 project record and exact lemma locator. |
| `stacks00fv` | [Tag 00FV](https://stacks.math.columbia.edu/tag/00FV) and official cite page: weak Nullstellensatz | PASS. Official 2026 project record and exact theorem locator. |
| `martinez2024zeros` | [arXiv:2404.11479v2](https://arxiv.org/abs/2404.11479v2): Theorem A and Proposition 2.4(v) | PASS. Official title punctuation and fixed v2 URL. |
| `martinez2024real` | [arXiv:2309.10970v3](https://arxiv.org/abs/2309.10970v3): Remark 2.12 and Proposition 2.17 | PASS. The 2024 year is the explicit v3 date, not the 2023 v1 date. |
| `dlmf` | [Release citation](https://dlmf.nist.gov/help/cite), [15.8.1](https://dlmf.nist.gov/15.8.E1), [18.5.7](https://dlmf.nist.gov/18.5.E7), [18.16.1](https://dlmf.nist.gov/18.16.E1) | PASS. Release 1.2.7/date/editors and all claim-specific permalinks are present. |

The detailed query, target, field-comparison and all-context ledgers are under
`integrity_evidence/citation/`.  This audit verifies the cited identities and
uses; it does not establish an exhaustive prior-art search.  Authenticated
MathSciNet, zbMATH and Scopus searches and original-author contact remain
future priority work.
