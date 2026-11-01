# Coverage control — Chapter 28 (Saliency Maps)

Source: https://christophm.github.io/interpretable-ml-book/pixel-attribution.html (accessed 2026-11-01)
Raw source: manuscript/pixel-attribution.qmd, christophM/interpretable-ml-book (master), 359 lines
Persian: chapters/28-saliency-maps.md (+ src/chapters/28-saliency-maps.md)
Branch: translation/chapter-28-saliency-maps (base: origin/main)

| ID | Source item | Persian location | Status |
|----|-------------|------------------|--------|
| H1 | Intro, Fig 28.1 (vanilla.jpg) + label note | intro | complete |
| P1 | Other names, feature attribution, notation S(x), R^c | intro | complete |
| P2 | Occlusion- vs gradient-based; gradient-only vs path-attribution; callout "Pick reference image" | intro | complete |
| S1 | Vanilla Gradient: recipe, Taylor expansion, ReLU ambiguity, 2x2 example, saturation | Vanilla Gradient | complete |
| S2 | DeconvNet: formula, 2x2 example | DeconvNet | complete |
| S3 | Grad-CAM: intuition, localization-map formula, 9-step recipe | Grad-CAM | complete |
| S4 | Guided Grad-CAM | Guided Grad-CAM | complete |
| S5 | SmoothGrad: 3 steps, formula, noise 10-20%, n=50 | SmoothGrad | complete |
| S6 | Examples: VGG-16, Figs 28.2 and 28.3 + label notes, discussion | مثال‌ها | complete |
| S7 | Strengths (3) | نقاط قوت | complete |
| S8 | Limitations: Ghorbani, Kindermans, callout warning, Adebayo, Tomsett | محدودیت‌ها | complete |
| S9 | Software: tf-keras-vis, iNNvestigate, DeepExplain | نرم‌افزار | complete |

## Source observations flagged
- Image written as "I" then x; output index S_C vs S_c (noted).
- Indicator I(x>0) vs text "positive or zero" (noted).
- Number of samples N vs n; "20k classes" vs 1,000 classes (noted).
- Z in Grad-CAM weight formula is not defined in the source (noted).
- All References (Simonyan, Selvaraju, Sundararajan, Shrikumar, Zeiler, Smilkov, Ghorbani, Kindermans, Adebayo, Tomsett, Alber, Bach) already exist in Appendix D.
- Worked numeric examples (reference-image 0.6, Grad-CAM alpha weights) are translator illustrations, labeled as such.
