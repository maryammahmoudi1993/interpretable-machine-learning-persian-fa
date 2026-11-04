# Coverage control — Chapter 31 (Influential Instances)

Source: https://christophm.github.io/interpretable-ml-book/influential.html (accessed 2026-11-04)
Raw source: manuscript/influential.qmd, christophM/interpretable-ml-book (master), 572 lines
Persian: chapters/31-influential.md (+ src/chapters/31-influential.md)
Branch: translation/chapter-31-influential (base: origin/main)

| ID | Source item | Persian location | Status |
|----|-------------|------------------|--------|
| H1 | Intro, mean vs median income example | intro | complete |
| S1 | Outlier + Fig 31.1 (R plot, image from repo) | داده‌پرت | complete |
| S2 | Influential instance + Fig 31.2 | نمونهٔ تأثیرگذار | complete |
| S3 | Why influential instances help; learner Fig 31.3 (learner.jpg) | چرا ... | complete |
| S4 | Deletion diagnostics: DFBETA, Cook's distance, simple Influence formulas | تشخیص‌های حذفی | complete |
| S5 | Penguin random-forest example, callout, Fig 31.4 tree, instance 8, Fig 31.5 tree, retraining cost | مثال | complete |
| S6 | Influence functions dialogue, math (upweighting, Hessian, Newton step), Fig 31.6, I_up,loss | توابع تأثیر | complete |
| S7 | Applications: model behavior, domain mismatch, fixing training data | کاربرد | complete |
| S8 | Strengths | نقاط قوت | complete |
| S9 | Limitations | محدودیت‌ها | complete |
| S10 | Software and alternatives | نرم‌افزار | complete |

## Source observations flagged
- R inline values (number of training instances, max influence) are computed at build time and absent from the raw file: N=222 derived from Fig 31.4 leaf sizes (52+160+10); max influence ~0.012 read from the figure axis. The id of the top influential instance cannot be recovered and is omitted.
- Text says Fig 31.4 shows "support vector machine" while the model is a random forest (noted).
- Text says Fig 31.5 shows "high body mass and deep bills" but the tree only uses bill_length_mm and bill_depth_mm (noted).
- "whether a penguin's sex" is an incomplete sentence (noted).
- R code blocks have no Persian equivalent (figures come from the repo images).
- Worked examples (income mean/median, Cook's distance with 3 instances, gradient similarity) are translator illustrations.
- Cook 1977, Koh & Liang 2017, Koh et al. 2019 already in Appendix D.
