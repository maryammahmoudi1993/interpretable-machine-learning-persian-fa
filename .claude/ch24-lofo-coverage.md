# Coverage control — Chapter 24 (LOFO Importance)

Source: https://christophm.github.io/interpretable-ml-book/lofo.html (accessed 2026-10-28)
Raw source: manuscript/lofo.qmd, christophM/interpretable-ml-book (master), 257 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/24-lofo.md (+ src/chapters/24-lofo.md)
Branch: translation/chapter-24-lofo (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against lofo.qmd on 2026-10-28; mdbook 0.4.40 build checked: 3 images resolve, internal links resolve, 3 footnotes render, 13 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: LOFO definition, footnote loco (1-5) | intro | complete |
| P1 | Intuition, negative importance, conditional on other features (7-10) | intro | complete |
| P2 | p retrainings, simple algorithm (12-14) | intro | complete |
| A1 | Algorithm: input, steps 1-4, three formulas (16-42) | algorithm | complete |
| P3 | Positive metrics: sign/quotient swap; train vs test data (45-46) | algorithm | complete |
| S1 | ## Examples: bike RF 2/3 data, holiday negative (49-54) | ## مثال‌ها | complete |
| F1 | Fig 24.1 bike LOFO + caption (57-87) | شکل ۲۴.۱ | complete |
| P4 | Duplicate temperature experiment (90-94) | S1 | complete |
| F2 | Fig 24.2 correlated bike LOFO + caption (96-131) | شکل ۲۴.۲ | complete |
| P5 | Interpretation, footnote not-same-lofo, conclusions list with footnote learner-ability (133-143) | S1 | complete |
| P6 | Penguin RF 2/3 data; bill depth most important (145-147) | S1 | complete |
| F3 | Fig 24.3 penguins + caption (149-177) | شکل ۲۴.۳ | complete |
| P7 | Accuracy sign flip; species/flipper_length removable (179-181) | S1 | complete |
| S2 | ## LOFO versus PFI (183-202) | ## LOFO در برابر PFI | complete |
| S3 | ## Strengths (204-223) | ## نقاط قوت | complete |
| S4 | ## Limitations (225-239) | ## محدودیت‌ها | complete |
| S5 | ## Software and alternatives (241-250) | ## نرم‌افزار و جایگزین‌ها | complete |
| FN | Footnotes loco (252), learner-ability (254), not-same-lofo (257) | footnotes | complete |
| R1 | Citation lei2018distributionfree → Appendix D | refs | complete |
| X1 | Translator additions | inline | complete |

## Source observations to flag
- The captions of Fig 24.1 and Fig 24.2 are swapped in the source: the caption of the first figure mentions the duplicated `temp_copy` feature, but that image has no `temp_copy`; the second image (with `temp_copy`) carries the generic caption. Captions translated as in source, mismatch flagged under Fig 24.1.
- The source text says LOFO shows `species` and `flipper_length` can be safely removed; in Fig 24.3 `species` is negative but `flipper_length_mm` is small positive (about 0.009, same as `bill_length_mm`). Flagged.
- One sentence says "LOCO importance" (the original name) where the chapter otherwise says LOFO. Flagged.
- Lei et al. 2018 (`lei2018distributionfree`) exists in Appendix D.
- Source uses three footnotes (loco, learner-ability, not-same-lofo); kept as markdown footnotes.

## Translator additions (all marked, purple style)
Notes: LOCO/LOFO wording, notation, Fig 24.1-24.3 label notes (incl. caption swap), species/flipper mismatch, learner terminology. Worked examples: LOFO difference/quotient and negative importance, negative importance meaning, duplicated-temperature mechanism, LOFO vs conditional PFI with trees, sequential selection, cost of p retrainings, simple implementation.
