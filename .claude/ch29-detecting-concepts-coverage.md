# Coverage control — Chapter 29 (Detecting Concepts)

Source: https://christophm.github.io/interpretable-ml-book/detecting-concepts.html (accessed 2026-11-02)
Raw source: manuscript/detecting-concepts.qmd, christophM/interpretable-ml-book (master), 170 lines
Persian: chapters/29-detecting-concepts.md (+ src/chapters/29-detecting-concepts.md)
Branch: translation/chapter-29-detecting-concepts (base: origin/main)

| ID | Source item | Persian location | Status |
|----|-------------|------------------|--------|
| H1 | Title, author line (Fangzhou Li), intro on feature-based limits, concept-based approach | intro | complete |
| S1 | TCAV overview + callout "Carefully define concept" | TCAV | complete |
| S2 | CAV definition, S_{C,k,l} formula, sign/angle interpretation | بردار فعال‌سازی مفهوم | complete |
| S3 | TCAV score formula, zebra/striped example, significance test (3 steps), t-test callout, Bonferroni | آزمون با CAVها | complete |
| S4 | Example: InceptionV3, Fig 29.1 (tcav.jpg) + label note, callout "Use more than 50 images" | مثال | complete |
| S5 | Strengths (3 paragraphs) | نقاط قوت | complete |
| S6 | Limitations (4) | محدودیت‌ها | complete |
| S7 | Other approaches: ACE, CBM, CW | رویکردهای دیگر | complete |
| S8 | Software | نرم‌افزار | complete |

## Source observations flagged
- Subscript Q in TCAV_{Q,C,k,l} not defined; k used for class index and target class; "unit CAV" vs "coefficient vector" (noted).
- Bar values in Fig 29.1 estimated from the plot (labeled as such).
- Worked examples (2-D angle, 40/50 = 0.8, Bonferroni 0.05/3) are translator illustrations.
- All references (Kim 2018, Szegedy 2016, Alain 2018, Ghorbani 2019, Koh 2020, Chen 2020) already in Appendix D.
