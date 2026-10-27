# Coverage control — Chapter 20 (Accumulated Local Effects)

Source: https://christophm.github.io/interpretable-ml-book/ale.html (accessed 2026-10-23)
Raw source: manuscript/ale.qmd, christophM/interpretable-ml-book (master), 671 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/20-ale.md (+ src/chapters/20-ale.md)
Branch: translation/chapter-20-ale (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against ale.qmd on 2026-10-23; mdbook 0.4.40 build checked: 9 images resolve, internal links resolve, 36 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

Note: the pre-existing Persian chapter was condensed, had no in-image label translations or translator additions, and its figure numbering was shifted (the 2D-ALE figure was unnumbered). It is replaced section by section by a sentence-level translation; figures are numbered 20.1-20.9 in source order.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: ALE definition, faster/unbiased alternative to PDP (1-6) | intro | complete |
| P1 | Read PDP chapter first; PDP problem with correlated features (10-12) | intro | complete |
| S1 | ## Motivation and intuition (15) | ## انگیزه و شهود | complete |
| P2 | PDP unreliable under correlation; house example, PDP recipe (17-28) | motivation | complete |
| F1 | Fig 20.1 motivation1 + caption + in-image labels (29-60) | شکل ۲۰.۱ | complete |
| P3 | Conditional distribution, M-Plots, why they fail (62-71) | motivation | complete |
| F2 | Fig 20.2 motivation2 + caption + in-image labels (73-113) | شکل ۲۰.۲ | complete |
| P4 | ALE differences instead of averages, 29/31 m2 (115-120) | motivation | complete |
| F3 | Fig 20.3 computation + caption + in-image labels (123-157) | شکل ۲۰.۳ | complete |
| L1 | Three-way summary PDP / M-Plots / ALE quotes (159-163) | motivation | complete |
| S2 | ## Theory intro (165-169) | ## نظریه | complete |
| M1 | PDP formula + explanation (171-193) | theory | complete |
| M2 | M-plot formula + neighborhood (195-219) | theory | complete |
| M3 | ALE formula (221-241) | theory | complete |
| M4 | Three differences, derivative formula, integral, constant, no-gradient problem (244-265) | theory | complete |
| S3 | ## Estimation (268-272) | ## تخمین | complete |
| M5 | Uncentered ALE formula + term-by-term breakdown (274-288) | estimation | complete |
| M6 | Centered ALE formula + interpretation example (290-295) | estimation | complete |
| P5 | Quantile grid, drawbacks (297-300) | estimation | complete |
| P6 | **ALE for two features**, formulas referral (303-312) | estimation | complete |
| F4 | Fig 20.4 2D computation + caption (a,b,c,d; 2nd-order difference) + labels (314-340) | شکل ۲۰.۴ | complete |
| P7 | Empty cells, second-order interpretation, linear example, PDP vs ALE order, higher orders (342-355) | estimation | complete |
| P8 | **ALE for categorical features**, ordering, KS distance, MDS, season/weather example (358-380) | estimation | complete |
| W1 | Callout tip: utilize natural order (382-388) | 💡 | complete |
| S4 | ## ALE versus PDP: scenario (390-396) | ## ALE در برابر PDP | complete |
| F5 | Fig 20.5 correlation-problem + caption + labels (398-425) | شکل ۲۰.۵ | complete |
| P9 | Realistic scenario, extrapolation, adversarial link (427-433) | ale-vs-pdp | complete |
| F6 | Fig 20.6 PDP vs ALE + caption + labels (434-447) | شکل ۲۰.۶ | complete |
| P10 | Is odd behaviour interesting; recommendation (449-453) | ale-vs-pdp | complete |
| W2 | Callout tip: produce both PDP and ALE (456-462) | 💡 | complete |
| S5 | ## Examples: bike wind speed/weather (467-474) | ## مثال‌ها | complete |
| F7 | Fig 20.7 ale-bike + caption + labels (476-495) | شکل ۲۰.۷ | complete |
| P11 | Humidity/temperature 2nd-order, interaction (498-504) | examples | complete |
| F8 | Fig 20.8 ale-bike-2d + caption + labels (506-533); hidden PDP chunk (eval: false, not shown) (536-546) | شکل ۲۰.۸ | complete |
| P12 | Total vs second-order effect (548-552) | examples | complete |
| P13 | Penguin example (554-561) | examples | complete |
| F9 | Fig 20.9 ale-penguin + caption + labels (563-589) | شکل ۲۰.۹ | complete |
| S6 | ## Strengths (592-609): unbiased, faster O(n), clear, centred, 2D interaction only, decomposition, prefer ALE | ## نقاط قوت | complete |
| S7 | ## Limitations (611-662): across intervals, linear coefficients (Gromping), shaky, number of intervals (RHALE), no ICE, stability, 2nd-order interpretation, implementation, strongly correlated, PDP preferable, rule of thumb | ## محدودیت‌ها | complete |
| S8 | ## Software and alternatives (665-671) incl. 5 links | ## نرم‌افزار و جایگزین‌ها | complete |
| R1 | Citations: apley2020visualizingeffects, gromping2020model, gkolemis2023rhale → Appendix D | refs | complete |
| X1 | Translator additions (notes / worked examples / figure label notes) | inline | complete |

## Source observations to flag
- Fig 20.2 image title shows the raw text `mathbbP` (a rendering slip in the source figure); kept and flagged in a translator note.
- The formulas appear in the qmd in an `align*` (HTML/PDF) and a two-equation (EPUB) version; the two-line EPUB form is used. In the ALE formula the conditional-expectation subscript uses `x_S` while the bracket uses `z_S`; translated as in source and flagged.
- Second-order section: "You can subtract the lower-order effects in a partial dependence plot ..." is kept as in the source and flagged.
- Fig 20.8 text says "cold and humid weather increases the prediction" while the brightest cell in the image is around 30 degrees and humidity ~90 (a lighter band also at ~10-13 degrees); flagged without changing the text. The hidden PDP chunk (`eval: false`) is not shown on the website and was not reproduced.
- "total effect ... is simply the product of the two main effects" (source wording) is flagged.
- Tip callout "If you ALE and PDP show ..." has a typo in the source (likely "your"); flagged.
- Figure numbering: the old Persian file had an unnumbered 2D-ALE figure and shifted numbers; now 20.1-20.9 in source order.
- All three citations (Apley and Zhu 2020, Gromping 2020, Gkolemis 2023) exist in Appendix D.

## Translator additions (all marked, purple style)
Notes: intro terms, formula notation and source slips, estimation symbols, KS/MDS, second-order wording, tip callout, regional notes. Worked examples: Fig 20.1 unrealistic pairs, M-Plot mixing effect, local effect averaging, derivative vs M-plot, accumulation and centering (numeric), 2nd-order difference, additive model 2D ALE, category ordering via MDS, PDP vs ALE jump, weather ALE reading, interaction vs main effects, penguin species, cost O(n), interval-wise interpretation, number of intervals, rule of thumb. Figure label notes for Fig 20.1-20.9.
