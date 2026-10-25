# Coverage control — Chapter 22 (Functional Decomposition)

Source: https://christophm.github.io/interpretable-ml-book/decomposition.html (accessed 2026-10-25)
Raw source: manuscript/decomposition.qmd, christophM/interpretable-ml-book (master), 426 lines
Author: Christoph Molnar — CC BY-NC-SA 4.0
Persian: chapters/22-decomposition.md (+ src/chapters/22-decomposition.md)
Branch: translation/chapter-22-decomposition (base: main)

Status values: pending / complete / needs-fix / blocked (all items checked against decomposition.qmd on 2026-10-25; mdbook 0.4.40 build checked: 2 images resolve, internal links resolve, 24 translator-styled blocks, MathJax renders without errors on desktop and 390px mobile, no page-level horizontal scroll)

Note: the pre-existing Persian chapter was condensed and altered the opening example (it used f = x1*e^x1 - x2 + x1*x2 instead of the source's 2 + e^x1 - x2 + x1*x2) and had no in-image label notes or translator additions. It is replaced section by section by a sentence-level translation.

| ID | Source item (qmd lines) | Persian location | Status |
|----|-------------------------|------------------|--------|
| H1 | Title + intro: model as function, functional decomposition, foundation (1-7) | intro | complete |
| M1 | Example function 2 + e^x1 - x2 + x1*x2 (10-15) | intro | complete |
| F1 | Fig 22.1 prediction surface + caption + labels (16-35) | شکل ۲۲.۱ | complete |
| P1 | Describing the function, interaction visible (38-40) | intro | complete |
| M2 | 4-term decomposition + main effects, interaction, intercept (43-52) | intro | complete |
| F2 | Intercept 3.18, Fig 22.2 components + caption + labels (54-83) | شکل ۲۲.۲ | complete |
| P2 | Pringles / hyperbolic paraboloid, spoiler ALE (86-90) | intro | complete |
| P3 | Naive approach, two problems, x1*x2 example (93-106) | intro | complete |
| P4 | Solutions needed: method + axioms (108-110) | intro | complete |
| S1 | ## Decomposing a function (113): p features, full decomposition formula, subsets S (116-154) | ## تجزیه یک تابع | complete |
| P5 | Number of components 2^p, 10 features example (157-163) | S1 | complete |
| P6 | Non-uniqueness, shifting effects, 3D shoes example (165-178) | S1 | complete |
| L1 | Four approaches list (181-187) | S1 | complete |
| S2 | ## Functional ANOVA (190): definition, formulas, intercept, f1, f12 (192-248) | ## آنالیز واریانس تابعی | complete |
| L2 | Three axioms (250-255) + discussion of each (257-273) | S2 | complete |
| P7 | Correlated features problem (275-276) | S2 | complete |
| S3 | ## Generalized Functional ANOVA (278-310): extrapolation, argmin formula, hierarchical orthogonality, weight function, estimation | ## آنالیز واریانس تابعی تعمیم‌یافته | complete |
| S4 | ## Accumulated Local Effects (313-343): operator H_S, pseudo-orthogonality, PDP not a decomposition | ## اثرات محلی انباشته | complete |
| S5 | ## Decomposing tree ensembles (345-364) | ## تجزیه مجموعه‌درختان | complete |
| S6 | ## Statistical regression models (366-394) | ## مدل‌های رگرسیون آماری | complete |
| S7 | ## Strengths (396-412) | ## نقاط قوت | complete |
| S8 | ## Limitations (414-425) | ## محدودیت‌ها | complete |
| R1 | Citations: hooker2004discovering, hooker2007generalized, apley2020, yang2024inherently, caruana2015intelligible → Appendix D | refs | complete |
| X1 | Translator additions | inline | complete |

## Source observations to flag
- The pre-existing Persian chapter changed the opening example to x1*e^x1 - x2 + x1*x2; the source function is 2 + e^x1 - x2 + x1*x2 (restored; intercept 3.18 = 2 + sinh(1) verified in a worked example).
- Fig 22.2 caption says "top row: main effects f1 and f2; bottom: interaction f12", but the image layout is f1 (top-left), interaction (top-right), f2 (bottom-left); caption translated as in source and mismatch flagged.
- The subset sentence uses |S| >= 1 for interactions (should be >= 2); the next sentence uses |S| > 1. Flagged.
- The "10 features" example lists 90 two-way and 720 three-way terms, which are ordered counts (10*9, 10*9*8); the combination counts are 45 and 120 (total 1024 is correct). Flagged.
- Intercept formula uses S = {emptyset} (set containing the empty set); meant S = emptyset. Flagged. The 1,2 interaction example assumes four features (integral over X_3, X_4). Flagged.
- Hooker (2007), "generalized functional ANOVA", is cited in the source (`hooker2007generalized`) but has no entry in Appendix D (only Hooker 2004). Linked to Appendix D without inventing an entry. TODO for the maintainer: add the Hooker 2007 reference to Appendix D.
- Citations present in Appendix D: Hooker 2004, Apley and Zhu 2020, Yang et al. 2024, Caruana et al. 2015.
- "Apley and Zhu (2020)" appears once in the source without a citation link; same paper as the linked one.

## Translator additions (all marked, purple style)
Notes: terminology, three-line formula, |S| >= 1 slip, 90/720 counts, S={emptyset}/four-feature assumption, Hooker 2007 reference, axioms, projections and entanglement, GA2M/MARS/splines, exponential explosion. Worked examples: interaction visible in f, intercept = 2 + sinh(1), 2^p components for p = 3, non-uniqueness (all effect in interaction), recursive ANOVA components, axioms check, hierarchical orthogonality, operator H_S as a filter, tree depth vs interaction order, linear model as decomposition, Shapley split of interaction. Figure label notes for Fig 22.1-22.2.
