# Coverage control — Chapter 19 (Partial Dependence Plot)

Source: https://christophm.github.io/interpretable-ml-book/pdp.html (accessed 2026-10-22)
Raw source: manuscript/pdp.qmd, christophM/interpretable-ml-book (master), 347 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/19-pdp.md (+ src/chapters/19-pdp.md)
Branch: translation/chapter-19-pdp (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against pdp.qmd on 2026-10-22; mdbook 0.4.40 build checked: 5 images resolve, internal links resolve, 17 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile with no page-level horizontal scroll)

Note: the pre-existing Persian chapter was a condensed/reworded translation without in-image label translations, translator notes or worked examples, and with a few reworded sentences. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: PDP definition, linear/monotonic/complex, linear-regression remark (1-7) | intro | complete |
| S1 | ## Definition and estimation (9) | ## تعریف و برآورد | complete |
| M1 | PD function formula + symbols x_S, X_C, S, C (11-20) | definition | complete |
| M2 | Monte Carlo estimate formula + ICE average + symbols + correlation remark (22-30) | definition | complete |
| W1 | Callout warning: correlated features (32-38) | ⚠️ | complete |
| P1 | Classification, multiple classes (40-41) | definition | complete |
| P2 | PDP is a global method (44-45) | definition | complete |
| P3 | Categorical features, season/summer example (48-54) | ویژگی‌های طبقه‌ای | complete |
| S2 | ## Examples (57) + 1-2 features remark (59-60) | ## مثال‌ها | complete |
| P4 | Bike regression example, random forest, temperature trend (62-68) | examples | complete |
| F1 | Fig 19.1 PDPs temp/hum/wind + caption + in-image labels (70-90) | شکل ۱۹.۱ | complete |
| P5 | Humidity > 60%, wind, 25-35 km/h, author's expectation (92-95) | examples | complete |
| P6 | Categorical season example (97-98) | examples | complete |
| F2 | Fig 19.2 season + caption + in-image labels (100-108) | شکل ۱۹.۲ | complete |
| P7 | Penguin sex classification, RF vs logreg, body mass/bill depth (110-116) | examples | complete |
| F3 | Fig 19.3 + caption + in-image labels (118-174) | شکل ۱۹.۳ | complete |
| P8 | By-species PDP, Adelie/Chinstrap/Gentoo (176-183) | examples | complete |
| F4 | Fig 19.4 + caption + in-image labels (185-231) | شکل ۱۹.۴ | complete |
| P9 | Two-feature PDP, interaction (234-236) | examples | complete |
| F5 | Fig 19.5 + caption + in-image labels (238-249) | شکل ۱۹.۵ | complete |
| W2 | Callout tip: reduce interactions, Molnar 2020 (252-260) | 💡 | complete |
| S3 | ## PDP-based feature importance (262) | ## اهمیت ویژگی مبتنی بر PDP | complete |
| P10 | Greenwell 2018, motivation, numeric definition (264-266) | importance | complete |
| M3 | Numeric importance formula + K unique values (268-270) | importance | complete |
| M4 | Categorical importance formula (271-273) | importance | complete |
| P11 | Range rule, denominator four, 95% (275-280) | importance | complete |
| P12 | Cautions: main effect only, permutation importance, unique values (282-286) | importance | complete |
| S4 | ## Strengths (291): intuitive, clear interpretation, easy to implement, causal (293-307) | ## نقاط قوت | complete |
| S5 | ## Limitations (309): max features, distribution, independence, heterogeneity, regional (311-335) | ## محدودیت‌ها | complete |
| S6 | ## Software and alternatives (337-345) incl. 3 links | ## نرم‌افزار و جایگزین‌ها | complete |
| R1 | Citations: friedman2001, molnar2020, greenwell2018, zhao2019, herbinger2024/2022, britton2019, gkolemis2024 | refs → Appendix D | complete |
| X1 | Translator additions (notes / worked examples / figure label notes) | inline | complete |

## Source observations to flag
- Strengths uses "j-th feature" without defining j; flagged in a translator note (j = the index in S = {j}).
- The citation `gkolemis2024fast` has no matching entry in Appendix D (only RHALE 2023); it is cited as plain "Gkolemis و همکاران (۲۰۲۴)" without a link, flagged in a translator note, and no reference was invented.
- `molnar2020quantifying` is Appendix D "2020b" (Quantifying Model Complexity via Functional Decomposition).
- Hidden R chunks in the qmd produce the 5 figures; code is not shown on the website and was not reproduced (figure labels are translated in translator notes).
- Orphan image `fig-correlation-pdp-ale-plot-1.png` exists in images/ but is not part of this chapter's source.

## Translator additions (all marked, purple style)
Notes: intro terms, bike units/author expectation, "surprise, surprise"/regression-to-mean wording, range rule, "j-th feature", Gkolemis citation. Worked examples: PD computation, categorical PD, 2D PDP, PDP importance, causal-for-model vs. world, heterogeneous effects/regional PDP. Figure label notes for Fig 19.1-19.5.
