# Coverage control — Chapter 20 (Accumulated Local Effects)

Source: https://christophm.github.io/interpretable-ml-book/ale.html (accessed 2026-10-23)
Raw source: manuscript/ale.qmd, christophM/interpretable-ml-book (master), 671 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/20-ale.md (+ src/chapters/20-ale.md)
Branch: translation/chapter-20-ale (base: main)

Status values: pending / complete / needs-fix / blocked

Note: the pre-existing Persian chapter was condensed, had no in-image label translations or translator additions, and its figure numbering was shifted (the 2D-ALE figure was unnumbered). It is replaced section by section by a sentence-level translation; figures are numbered 20.1-20.9 in source order.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: ALE definition, faster/unbiased alternative to PDP (1-6) | intro | pending |
| P1 | Read PDP chapter first; PDP problem with correlated features (10-12) | intro | pending |
| S1 | ## Motivation and intuition (15) | ## انگیزه و شهود | pending |
| P2 | PDP unreliable under correlation; house example, PDP recipe (17-28) | motivation | pending |
| F1 | Fig 20.1 motivation1 + caption + in-image labels (29-60) | شکل ۲۰.۱ | pending |
| P3 | Conditional distribution, M-Plots, why they fail (62-71) | motivation | pending |
| F2 | Fig 20.2 motivation2 + caption + in-image labels (73-113) | شکل ۲۰.۲ | pending |
| P4 | ALE differences instead of averages, 29/31 m2 (115-120) | motivation | pending |
| F3 | Fig 20.3 computation + caption + in-image labels (123-157) | شکل ۲۰.۳ | pending |
| L1 | Three-way summary PDP / M-Plots / ALE quotes (159-163) | motivation | pending |
| S2 | ## Theory intro (165-169) | ## نظریه | pending |
| M1 | PDP formula + explanation (171-193) | theory | pending |
| M2 | M-plot formula + neighborhood (195-219) | theory | pending |
| M3 | ALE formula (221-241) | theory | pending |
| M4 | Three differences, derivative formula, integral, constant, no-gradient problem (244-265) | theory | pending |
| S3 | ## Estimation (268-272) | ## تخمین | pending |
| M5 | Uncentered ALE formula + term-by-term breakdown (274-288) | estimation | pending |
| M6 | Centered ALE formula + interpretation example (290-295) | estimation | pending |
| P5 | Quantile grid, drawbacks (297-300) | estimation | pending |
| P6 | **ALE for two features**, formulas referral (303-312) | estimation | pending |
| F4 | Fig 20.4 2D computation + caption (a,b,c,d; 2nd-order difference) + labels (314-340) | شکل ۲۰.۴ | pending |
| P7 | Empty cells, second-order interpretation, linear example, PDP vs ALE order, higher orders (342-355) | estimation | pending |
| P8 | **ALE for categorical features**, ordering, KS distance, MDS, season/weather example (358-380) | estimation | pending |
| W1 | Callout tip: utilize natural order (382-388) | 💡 | pending |
| S4 | ## ALE versus PDP: scenario (390-396) | ## ALE در برابر PDP | pending |
| F5 | Fig 20.5 correlation-problem + caption + labels (398-425) | شکل ۲۰.۵ | pending |
| P9 | Realistic scenario, extrapolation, adversarial link (427-433) | ale-vs-pdp | pending |
| F6 | Fig 20.6 PDP vs ALE + caption + labels (434-447) | شکل ۲۰.۶ | pending |
| P10 | Is odd behaviour interesting; recommendation (449-453) | ale-vs-pdp | pending |
| W2 | Callout tip: produce both PDP and ALE (456-462) | 💡 | pending |
| S5 | ## Examples: bike wind speed/weather (467-474) | ## مثال‌ها | pending |
| F7 | Fig 20.7 ale-bike + caption + labels (476-495) | شکل ۲۰.۷ | pending |
| P11 | Humidity/temperature 2nd-order, interaction (498-504) | examples | pending |
| F8 | Fig 20.8 ale-bike-2d + caption + labels (506-533); hidden PDP chunk (eval: false, not shown) (536-546) | شکل ۲۰.۸ | pending |
| P12 | Total vs second-order effect (548-552) | examples | pending |
| P13 | Penguin example (554-561) | examples | pending |
| F9 | Fig 20.9 ale-penguin + caption + labels (563-589) | شکل ۲۰.۹ | pending |
| S6 | ## Strengths (592-609): unbiased, faster O(n), clear, centred, 2D interaction only, decomposition, prefer ALE | ## نقاط قوت | pending |
| S7 | ## Limitations (611-662): across intervals, linear coefficients (Gromping), shaky, number of intervals (RHALE), no ICE, stability, 2nd-order interpretation, implementation, strongly correlated, PDP preferable, rule of thumb | ## محدودیت‌ها | pending |
| S8 | ## Software and alternatives (665-671) incl. 5 links | ## نرم‌افزار و جایگزین‌ها | pending |
| R1 | Citations: apley2020visualizingeffects, gromping2020model, gkolemis2023rhale → Appendix D | refs | pending |
| X1 | Translator additions (notes / worked examples / figure label notes) | inline | pending |

## Source observations to flag
(filled in at the end)
