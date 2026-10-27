# Coverage control — Chapter 21 (Feature Interaction)

Source: https://christophm.github.io/interpretable-ml-book/interaction.html (accessed 2026-10-24)
Raw source: manuscript/interaction.qmd, christophM/interpretable-ml-book (master), 229 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/21-interaction.md (+ src/chapters/21-interaction.md)
Branch: translation/chapter-21-interaction (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against interaction.qmd on 2026-10-24; mdbook 0.4.40 build checked: internal links resolve, 11 translator-styled blocks, 2 tables, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

Note: the pre-existing Persian chapter was condensed (a stray Chinese token "做出" in the second paragraph, no label notes, no translator additions) and referenced `images/fig-interaction-penguins-1.png`, which has never existed in the repository. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: interaction definition, Aristotle quote (1-6) | intro | complete |
| S1 | ## What are feature interactions? (8) | ## تعامل ویژگی‌ها چیست؟ | complete |
| P1 | Decomposition into four terms (10-12) | S1 | complete |
| T1 | Table 21.1 house prices without interaction + caption (14-23) | جدول ۲۱.۱ | complete |
| P2 | Decomposition without interaction, 100,000 / 50,000 (25-30) | S1 | complete |
| T2 | Table 21.2 house prices with interaction + caption (32-42) | جدول ۲۱.۲ | complete |
| P3 | Decomposition with interaction term, 400,000 sum (45-49) | S1 | complete |
| P4 | H-statistic introduced, Friedman and Popescu (51-52) | S1 | complete |
| S2 | ## Friedman's H-statistic: two cases (55-60) | ## آمارهٔ H فریدمن | complete |
| M1 | PD_jk = PD_j + PD_k + symbols (62-66) | S2 | complete |
| M2 | f = PD_j + PD_-j + symbols (68-72) | S2 | complete |
| P5 | Variance explained, 0/1, >1 (74-81) | S2 | complete |
| M3 | H^2_jk formula (83-85) | S2 | complete |
| M4 | H^2_j formula (88-90) | S2 | complete |
| P6 | Cost 2n^2 / 3n^2, sampling (92-96) | S2 | complete |
| P7 | Test statistic, null hypothesis, model-specific (98-102) | S2 | complete |
| P8 | Classification with probabilities (104) | S2 | complete |
| S3 | ## Examples: penguin RF, body mass highest (106-113) | ## مثال‌ها | complete |
| F1 | Fig 21.1 top/bottom + caption (115-130) | شکل ۲۱.۱ | blocked (image + in-image labels unavailable) |
| P9 | Bonus by species (132-133) | S3 | complete |
| F2 | Fig 21.2 by species + caption + labels (135-157) | شکل ۲۱.۲ | complete |
| S4 | ## Strengths (160-171): theory, meaningful, dimensionless, all kinds, higher order | ## نقاط قوت | complete |
| S5 | ## Limitations (173-208) incl. H* formula (196) | ## محدودیت‌ها | complete |
| S6 | ## Software and alternatives (210-228) incl. 7 links, VIN, Greenwell | ## نرم‌افزار و جایگزین‌ها | complete |
| R1 | Citations: friedman2008predictive, inglis2022visualizing, hooker2004discovering, greenwell2018simple → Appendix D | refs | complete |
| X1 | Translator additions | inline | complete |

## Source observations to flag
- BLOCKED: Fig 21.1 (top/bottom H-statistic plots) has no local copy in the repository (the pre-existing chapter linked a file that never existed) and the source site/images were not reachable from the working environment. The chapter hotlinks the conventional Quarto path (`interaction_files/figure-html/fig-interaction-penguins-1.png`), which could not be verified; in-image labels for this figure are therefore not translated. To finish: download the figure from the website, save it as `chapters/images/fig-interaction-penguins-1.png` (+ `src/chapters/images/`), point the Markdown at it and add a label note like the one for Fig 21.2.
- The sentence "The statistic is 0 if there is no interaction at all, and 1 if all of the variance ... is explained by the sum of the partial dependence functions" disagrees with the formula (H^2 = 1 when everything is explained by the interaction); kept as in source and flagged in a translator note.
- All four citations (Friedman and Popescu 2008, Inglis 2022, Hooker 2004, Greenwell 2018) exist in Appendix D.
- The pre-existing Persian chapter contained a stray Chinese token in the second paragraph; removed by the re-translation.

## Translator additions (all marked, purple style)
Notes: terminology (interaction), notation (-j, centered PD), source slip on the 0/1 statement, missing Fig 21.1 explanation, Fig 21.2 labels. Worked examples: house-price interaction difference, two-level H workflow, cost with n samples, dimensionless comparison, spurious interaction vs H*, Greenwell partial-dependence interaction idea.
