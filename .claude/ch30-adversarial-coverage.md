# Coverage control — Chapter 30 (Adversarial Examples)

Source: https://christophm.github.io/interpretable-ml-book/adversarial.html (accessed 2026-11-03)
Raw source: manuscript/adversarial.qmd, christophM/interpretable-ml-book (master), 231 lines
Persian: chapters/30-adversarial.md (+ src/chapters/30-adversarial.md)
Branch: translation/chapter-30-adversarial (base: origin/main)

| ID | Source item | Persian location | Status |
|----|-------------|------------------|--------|
| H1 | Definition, link to counterfactuals, three attack scenarios | intro | complete |
| S1 | Methods and examples intro | روش‌ها و مثال‌ها | complete |
| S2 | Szegedy et al.: loss + c|r|, box-constrained L-BFGS, Fig 30.1 (ostrich) + note | بخش اول | complete |
| S3 | Fast gradient sign method, formula, linearity, transferability, adversarial training | پاندا | complete |
| S4 | 1-pixel attack, differential evolution, formula, Fig 30.2 + note | حمله‌های تک‌پیکسلی | complete |
| S5 | Adversarial patch (toaster), Fig 30.3 + note | وصلهٔ خصمانه | complete |
| S6 | 3D-printed turtle, EOT, 3 formulas, Fig 30.4 + note | لاک‌پشت | complete |
| S7 | Black box attack: 7 steps, 84% figure | حملهٔ جعبه‌سیاه | complete |
| S8 | Cybersecurity perspective: three golden rules, defenses, white/gray/black box | دیدگاه امنیت سایبری | complete |

## Source observations flagged
- d used for both dimension (in [0,1]^d) and distance function (noted).
- r1, r2, r3 described as "random numbers" (noted as distinct random members).
- Heading translated as "مثال‌های خصمانه" to match SUMMARY.md (old file used "نمونه‌های متخاصم").
- Worked examples (3-pixel FGSM, c trade-off) are translator illustrations.
- All references (Szegedy 2014, Goodfellow 2015, Su 2019, Brown 2018, Athalye 2018, Papernot 2017, Biggio 2018) already in Appendix D.
