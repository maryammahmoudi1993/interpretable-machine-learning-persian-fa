# Coverage control — Chapter 19 (Partial Dependence Plot)

Source: https://christophm.github.io/interpretable-ml-book/pdp.html (accessed 2026-10-22)
Raw source: manuscript/pdp.qmd, christophM/interpretable-ml-book (master), 347 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/19-pdp.md (+ src/chapters/19-pdp.md)
Branch: translation/chapter-19-pdp (base: main)

Status values: pending / complete / needs-fix / blocked

Note: the pre-existing Persian chapter was a condensed/reworded translation without in-image label translations, translator notes or worked examples, and with a few reworded sentences. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: PDP definition, linear/monotonic/complex, linear-regression remark (1-7) | intro | pending |
| S1 | ## Definition and estimation (9) | ## تعریف و برآورد | pending |
| M1 | PD function formula + symbols x_S, X_C, S, C (11-20) | definition | pending |
| M2 | Monte Carlo estimate formula + ICE average + symbols + correlation remark (22-30) | definition | pending |
| W1 | Callout warning: correlated features (32-38) | ⚠️ | pending |
| P1 | Classification, multiple classes (40-41) | definition | pending |
| P2 | PDP is a global method (44-45) | definition | pending |
| P3 | Categorical features, season/summer example (48-54) | ویژگی‌های طبقه‌ای | pending |
| S2 | ## Examples (57) + 1-2 features remark (59-60) | ## مثال‌ها | pending |
| P4 | Bike regression example, random forest, temperature trend (62-68) | examples | pending |
| F1 | Fig 19.1 PDPs temp/hum/wind + caption + in-image labels (70-90) | شکل ۱۹.۱ | pending |
| P5 | Humidity > 60%, wind, 25-35 km/h, author's expectation (92-95) | examples | pending |
| P6 | Categorical season example (97-98) | examples | pending |
| F2 | Fig 19.2 season + caption + in-image labels (100-108) | شکل ۱۹.۲ | pending |
| P7 | Penguin sex classification, RF vs logreg, body mass/bill depth (110-116) | examples | pending |
| F3 | Fig 19.3 + caption + in-image labels (118-174) | شکل ۱۹.۳ | pending |
| P8 | By-species PDP, Adelie/Chinstrap/Gentoo (176-183) | examples | pending |
| F4 | Fig 19.4 + caption + in-image labels (185-231) | شکل ۱۹.۴ | pending |
| P9 | Two-feature PDP, interaction (234-236) | examples | pending |
| F5 | Fig 19.5 + caption + in-image labels (238-249) | شکل ۱۹.۵ | pending |
| W2 | Callout tip: reduce interactions, Molnar 2020 (252-260) | 💡 | pending |
| S3 | ## PDP-based feature importance (262) | ## اهمیت ویژگی مبتنی بر PDP | pending |
| P10 | Greenwell 2018, motivation, numeric definition (264-266) | importance | pending |
| M3 | Numeric importance formula + K unique values (268-270) | importance | pending |
| M4 | Categorical importance formula (271-273) | importance | pending |
| P11 | Range rule, denominator four, 95% (275-280) | importance | pending |
| P12 | Cautions: main effect only, permutation importance, unique values (282-286) | importance | pending |
| S4 | ## Strengths (291): intuitive, clear interpretation, easy to implement, causal (293-307) | ## نقاط قوت | pending |
| S5 | ## Limitations (309): max features, distribution, independence, heterogeneity, regional (311-335) | ## محدودیت‌ها | pending |
| S6 | ## Software and alternatives (337-345) incl. 3 links | ## نرم‌افزار و جایگزین‌ها | pending |
| R1 | Citations: friedman2001, molnar2020, greenwell2018, zhao2019, herbinger2024/2022, britton2019, gkolemis2024 | refs → Appendix D | pending |
| X1 | Translator additions (notes / worked examples / figure label notes) | inline | pending |

## Source observations to flag
- Fig 19.1 caption/text: wind speed text says "25 to 35 km/h"; image shows a flat curve there (consistent).
- Source uses "j-th feature" in Strengths without defining j (flagged in a translator note).
- Source cites "Gkolemis 2024 (fast)" while Appendix D holds the 2023 RHALE entry (checked at the end).
