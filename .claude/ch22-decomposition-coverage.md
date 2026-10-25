# Coverage control — Chapter 22 (Functional Decomposition)

Source: https://christophm.github.io/interpretable-ml-book/decomposition.html (accessed 2026-10-25)
Raw source: manuscript/decomposition.qmd, christophM/interpretable-ml-book (master), 426 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/22-decomposition.md (+ src/chapters/22-decomposition.md)
Branch: translation/chapter-22-decomposition (base: main)

Status values: pending / complete / needs-fix / blocked

Note: the pre-existing Persian chapter was condensed and altered the opening example (it used f = x1*e^x1 - x2 + x1*x2 instead of the source's 2 + e^x1 - x2 + x1*x2) and had no in-image label notes or translator additions. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: model as function, functional decomposition, foundation (1-7) | intro | pending |
| M1 | Example function 2 + e^x1 - x2 + x1*x2 (10-15) | intro | pending |
| F1 | Fig 22.1 prediction surface + caption + labels (16-35) | شکل ۲۲.۱ | pending |
| P1 | Describing the function, interaction visible (38-40) | intro | pending |
| M2 | 4-term decomposition + main effects, interaction, intercept (43-52) | intro | pending |
| F2 | Intercept 3.18, Fig 22.2 components + caption + labels (54-83) | شکل ۲۲.۲ | pending |
| P2 | Pringles / hyperbolic paraboloid, spoiler ALE (86-90) | intro | pending |
| P3 | Naive approach, two problems, x1*x2 example (93-106) | intro | pending |
| P4 | Solutions needed: method + axioms (108-110) | intro | pending |
| S1 | ## Decomposing a function (113): p features, full decomposition formula, subsets S (116-154) | ## تجزیه یک تابع | pending |
| P5 | Number of components 2^p, 10 features example (157-163) | S1 | pending |
| P6 | Non-uniqueness, shifting effects, 3D shoes example (165-178) | S1 | pending |
| L1 | Four approaches list (181-187) | S1 | pending |
| S2 | ## Functional ANOVA (190): definition, formulas, intercept, f1, f12 (192-248) | ## آنالیز واریانس تابعی | pending |
| L2 | Three axioms (250-255) + discussion of each (257-273) | S2 | pending |
| P7 | Correlated features problem (275-276) | S2 | pending |
| S3 | ## Generalized Functional ANOVA (278-310): extrapolation, argmin formula, hierarchical orthogonality, weight function, estimation | ## آنالیز واریانس تابعی تعمیم‌یافته | pending |
| S4 | ## Accumulated Local Effects (313-343): operator H_S, pseudo-orthogonality, PDP not a decomposition | ## اثرات محلی انباشته | pending |
| S5 | ## Decomposing tree ensembles (345-364) | ## تجزیه مجموعه‌درختان | pending |
| S6 | ## Statistical regression models (366-394) | ## مدل‌های رگرسیون آماری | pending |
| S7 | ## Strengths (396-412) | ## نقاط قوت | pending |
| S8 | ## Limitations (414-425) | ## محدودیت‌ها | pending |
| R1 | Citations: hooker2004discovering, hooker2007generalized, apley2020, yang2024inherently, caruana2015intelligible → Appendix D | refs | pending |
| X1 | Translator additions | inline | pending |

## Source observations to flag
(filled in at the end)
