# Coverage control — Chapter 23 (Permutation Feature Importance)

Source: https://christophm.github.io/interpretable-ml-book/feature-importance.html (accessed 2026-10-27)
Raw source: manuscript/feature-importance.qmd, christophM/interpretable-ml-book (master), 308 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/23-feature-importance.md (+ src/chapters/23-feature-importance.md)
Branch: translation/chapter-23-feature-importance (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against feature-importance.qmd on 2026-10-27; mdbook 0.4.40 build checked: 4 images resolve, internal links resolve, 20 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

Note: the pre-existing Persian chapter was condensed and had no in-image label notes or translator additions. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: PFI definition, important/unimportant (1-9) | intro | complete |
| S1 | ## Theory: Breiman 2001, Fisher 2019 model reliance (11-16) | ## نظریه | complete |
| A1 | Algorithm (Fisher 2019): input, steps 1-3, quotient/difference (18-27) | algorithm | complete |
| W1 | Callout tip: invert positive metrics (30-37) | 💡 | complete |
| P1 | Split-half swap, n(n-1) method (39-42) | theory | complete |
| W2 | Callout caution: use unseen data; SHAP/PDP importance (44-53) | ⚠️ | complete |
| P2 | Test data used in examples (55) | theory | complete |
| S2 | ## Example and interpretation (57) + bike SVM, MAE (68-71) | ## مثال و تفسیر | complete |
| F1 | Fig 23.1 bike importance + caption (73-80) | شکل ۲۳.۱ | complete |
| P3 | Penguin 3 logistic regressions, log loss, factor 1 (91-94) | S2 | complete |
| F2 | Fig 23.2 penguins + caption (95-103) | شکل ۲۳.۲ | complete |
| P4 | Most important feature, species question (105-111) | S2 | complete |
| S3 | ## Conditional feature importance (114-139) incl. 4 options and interpretation | ## اهمیت ویژگی شرطی | complete |
| W3 | Callout warning: correlated features lower conditional importance (141-147) | ⚠️ | complete |
| S4 | ## Group-wise PFI example (149-154) | ## مثال PFI گروهی | complete |
| F3 | Fig 23.3 correlation by species + caption + labels (156-177) | شکل ۲۳.۳ | complete |
| P5 | PFI by species text, caveats, other splits (179-189) | S4 | complete |
| F4 | Fig 23.4 PFI by species + caption + labels (191-209) | شکل ۲۳.۴ | complete |
| S5 | ## Strengths (213-235) | ## نقاط قوت | complete |
| S6 | ## Limitations (237-285) incl. rain/temperature example | ## محدودیت‌ها | complete |
| S7 | ## Software and alternatives (288-308) incl. PIMP link, Sobol, wei2015 | ## نرم‌افزار و جایگزین‌ها | complete |
| R1 | Citations: breiman2001, fisher2019, molnar2023modelagnostic, watson2021, strobl2008, debeer2020, wei2015 → Appendix D | refs | complete |
| X1 | Translator additions | inline | complete |

## Source observations to flag
- Debeer and Strobl (2020, `debeer2020conditional`) is cited in the source but has no entry in Appendix D; cited as plain name+year without a link, no entry invented. TODO for the maintainer (the scheduled Appendix D task also looks for it).
- The split-half paragraph cites "Fisher, Rudin, and Dominici (2018)" while the same paper is Fisher et al. 2019 in Appendix D (arXiv vs journal year); kept as in source and flagged.
- Fig 23.4 caption says results "are quite similar to overall PFI and don't differ much by species", while the text above and the figure show a large difference for body mass (about 10.6 Gentoo, 8.5 Adelie, 1 Chinstrap); caption translated as in source and mismatch flagged.
- Inline R values (most/least important feature in the bike example, the factor 15.4 for body mass) are computed at book build time; they were read off the figures (flagged in translator notes).
- Algorithm step uses e_perm without index j in the quotient; kept as in source and flagged.
- Citations present in Appendix D: Breiman 2001, Fisher et al. 2019, Molnar et al. 2023, Watson and Wright 2021, Strobl et al. 2008, Wei et al. 2015.

## Translator additions (all marked, purple style)
Notes: terminology (permutation, loss), notation, Fisher year, Debeer missing, knockoffs, Fig 23.1-23.4 label notes (incl. caption mismatch), inline R values. Worked examples: ratio vs difference, n(n-1) cost, unseen-data overfitting, bike error bars, conditional vs marginal importance with correlated temperatures, correlation by species, interactions double-counting, pairwise-correlation caveat, importance splitting, variance-based vs loss-based importance.
