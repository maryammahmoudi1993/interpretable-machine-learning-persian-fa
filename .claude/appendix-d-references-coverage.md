# Coverage control — Appendix D (References)

Source bibliography: manuscript/references.bib (140 entries, raw.githubusercontent.com, accessed 2026-11-14); manuscript/references.qmd only contains the citeproc placeholder (`::: {#refs}`).
Persian: chapters/appendix-D-references.md (+ src/chapters/appendix-D-references.md)
Branch: translation/appendix-d-references (base: origin/main)

## Comparison of references.bib with Appendix D (by title)
- 136 of 140 entries already in Appendix D.
- Added (cited in the source): Debeer & Strobl (2020), "Conditional Permutation Importance Revisited", BMC Bioinformatics 21 (1): 307 (cited in feature-importance.qmd as @debeer2020conditional). Placed alphabetically (between "Deb, K." and "DeLMA").
- Present in the .bib but NOT cited in any manuscript chapter that could be fetched, therefore not added (citeproc would not list them): lipton2018mythos (Lipton 2018), aamodt1994casebased (Aamodt and Plaza 1994), molnar2022general (Molnar et al. 2022). Four manuscript pages (about-book, overview-methods, preface, taxonomy) returned 404, so they could not be searched. TODO for the maintainer if these are cited there.
- Hooker 2007 and Gkolemis et al. (2024, "n.d.") were already in Appendix D (written with the em-dash repeated-author style), contrary to older notes; the notes were updated and the Gkolemis citation in chapters/19-pdp.md is now linked.

## In-text citation check (Persian chapters)
- All linked citations `[Author (year)](appendix-D-references.md)` in chapters/[0-9]*.md resolve to an Appendix D entry (7 apparent misses were repeated-author "———" entries: Ribeiro 2018, Štrumbelj 2011/2014, Hooker 2007).
- Plain-text citations without links are not exhaustively checked (heuristic would be noisy).

## Structure checks
- src/SUMMARY.md lists the cover, about page, chapters 1-37 and appendices A-D (43 entries).
- chapters/ and src/chapters/ are byte-identical (diff -rq empty).
- All local image links resolve.
- mdbook build passes; Playwright render check on 16 pages at 1000 px and 390 px: no horizontal scroll, no MathJax errors, no broken images.

## Open items
- Package references of Appendix C are listed inside Appendix C, not in Appendix D (by design of the generated page).
- Fig 21.1 image (blocked earlier) still unresolved (see summary).
