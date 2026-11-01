# Coverage control — Chapter 27 (Learned Features)

Source: https://christophm.github.io/interpretable-ml-book/cnn-features.html (accessed 2026-11-01)
Raw source: manuscript/cnn-features.qmd, christophM/interpretable-ml-book (master), 317 lines
Persian: chapters/27-cnn-features.md (+ src/chapters/27-cnn-features.md)
Branch: translation/chapter-27-cnn-features (base: origin/main)

| ID | Source item | Persian location | Status |
|----|-------------|------------------|--------|
| H1 | Intro: feature visualization / network dissection | intro | complete |
| P1 | Why deep features matter, SVM comparison, four layer-type bullets | intro | complete |
| F1 | Fig 27.1 (cnn-features.jpg) + caption + in-image labels | شکل ۲۷.۱ | complete |
| S1 | Feature visualization: units | بخش تجسم ویژگی | complete |
| F2 | Fig 27.2 (units.jpg, newly added image) + labels A–F | شکل ۲۷.۲ | complete |
| S2 | Optimization: formulas for neuron and channel, negative direction | بهینه‌سازی | complete |
| F3 | Fig 27.3 (a484.jpg) | شکل ۲۷.۳ | complete |
| P2 | Training data vs. generated images, regularization (GAN, denoising AE) | بهینه‌سازی | complete |
| F4 | Fig 27.4 (activation-optim.jpg) + step labels | شکل ۲۷.۴ | complete |
| P3 | Distill.pub recommendations | بهینه‌سازی | complete |
| S3 | Connection to adversarial examples | ارتباط با مثال‌های خصمانه | complete |
| S4 | Text and tabular data (Karpathy RNN) | داده‌های متنی و جدولی | complete |
| S5 | Network Dissection intro, disentanglement question, husky/wolf, bias | تشریح شبکه | complete |
| S6 | Algorithm: 3 steps, Broden numbers, step 2 list, IoU formula, 0.04 threshold | الگوریتم | complete |
| F5-7 | Figs 27.5–27.7 + captions + in-image labels | شکل‌های ۲۷.۵–۲۷.۷ | complete |
| S7 | Experiments: all 12 findings, rotated basis, GANs | آزمایش‌ها | complete |
| S8 | Strengths (6 items) | نقاط قوت | complete |
| S9 | Limitations (illusion, too many units, pixel labels, negative activations) | محدودیت‌ها | complete |
| S10 | Software (Lucid, tf_cnnvis, Keras Filters, DeepVis, netdissect) | نرم‌افزار | complete |

## Source observations flagged
- Source sentence "The function h one particular the activation" is missing a verb (noted).
- IoU formula is written per image, but the procedure computes it over the dataset (noted); L_c not defined in source.
- Fig 27.2 image (units.jpg) was missing from the repo and was added from the upstream repository.
- Worked IoU example (0.45) is the translator's illustration, clearly labeled, not from the book.
