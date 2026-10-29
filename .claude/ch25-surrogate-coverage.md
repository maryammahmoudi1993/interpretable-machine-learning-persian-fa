# Coverage control — Chapter 25 (Surrogate Models)

Source: https://christophm.github.io/interpretable-ml-book/global.html (accessed 2026-10-29)
Raw source: manuscript/global.qmd, christophM/interpretable-ml-book (master), 158 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/25-surrogate.md (+ src/chapters/25-surrogate.md)
Branch: translation/chapter-25-surrogate (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against global.qmd on 2026-10-29; mdbook 0.4.40 build checked: 2 images resolve, internal links resolve, 13 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: global surrogate definition (1-7) | intro | complete |
| S1 | ## Theory (9): surrogate models in engineering, synonyms (11-16) | ## نظریه | complete |
| P1 | f vs g, any interpretable model (18-21) | S1 | complete |
| M1 | Linear model formula; decision tree formula (23-29) | S1 | complete |
| P2 | Model-agnostic, decoupled choice (31-33) | S1 | complete |
| L1 | Seven steps (35-45) + variants remark (47) | S1 | complete |
| M2 | R-squared formula + symbols, interpretation (49-58) | S1 | complete |
| P3 | Black box performance irrelevant to surrogate (60-63) | S1 | complete |
| P4 | Subset/re-weighting, local surrogate (66-68) | S1 | complete |
| S2 | ## Example: intro (70-82) | ## مثال | complete |
| P5 | Bike SVM + CART surrogate, R2 (inline R), 13 degrees (84-88) | S2 | complete |
| F1 | Fig 25.1 bike surrogate tree + caption + labels (90-94) | شکل ۲۵.۱ | complete |
| P6 | Penguin RF surrogate depth 2, R2 (inline R) (97-109) | S2 | complete |
| F2 | Fig 25.2 penguin surrogate + caption + labels (111-117) | شکل ۲۵.۲ | complete |
| S3 | ## Strengths (119-132) | ## نقاط قوت | complete |
| S4 | ## Limitations (134-151) | ## محدودیت‌ها | complete |
| S5 | ## Software (153-157) | ## نرم‌افزار | complete |
| X1 | Translator additions | inline | complete |

## Source observations to flag
- The source prints the R-squared values of the bike and penguin surrogate trees through inline R code (computed at book-build time), so no number appears in the source text; the Persian text says "the value computed when the book was built" and a translator note explains it. No number was invented.
- The text says the tree predicts more bikes "when temperature is above 13 degrees and when the count two days before was higher"; in Fig 25.1 the temperature split (13.7375) appears only in the branch with count two days before <= 4570. Noted.
- The pre-existing Persian header gave the original title as "Global Surrogate Models"; the source chapter title is "Surrogate Models" (fixed).
- The local-surrogate sentence has no link to LIME in the source; a translator note adds the link and says so.
- No citations in this chapter; Appendix D needs no change.

## Translator additions (all marked, purple style)
Notes: terminology (surrogate, black box, global), formula symbols, inline R values, Fig 25.1/25.2 label notes, LIME link. Worked examples: seven-step walkthrough, R-squared by hand (4 predictions), reading a surrogate tree, penguin leaf confidence, flexibility with two audiences, subset-fidelity warning, Python sketch.
