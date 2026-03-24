# Feedback and fixes

## What was good

- The lecture set is organized clearly by topic and subtopic.
- Slide coverage is stated explicitly, which makes the notes easy to audit.
- The summaries are generally accurate, concise, and useful for revision.
- The split into **Foundations**, **Geometric Search**, and **Convex Hulls** is logical and easy to navigate.

## Main issue I fixed

The original extracted figure images were inconsistent. A number of them were clipped too tightly, so labels or border text were cut off. In some cases the image captured only a fragment of the intended slide figure.

## What I changed

- Replaced **all 168 figure image files** with fresh renders taken directly from the source PDF.
- Each replacement keeps the full slide content visible, then trims only the outer blank margin.
- Updated both the `docs/` source image copies and the built `site/` image copies so the package stays consistent.

## Text review

The written notes were already in decent shape, so I did **not** do a heavy rewrite. That was the right call, because rewriting everything just to look busy would be stupid.
I left the structure intact and focused on the real defect: broken figure extraction.

## Recommendation for the next iteration

If you want a cleaner second pass later, the best improvements would be:

1. Replace generic captions like “Figure from slide X” with short descriptive captions.
2. Add one compact worked example for each major algorithm section.
3. Add one small complexity summary table at the end of each chapter.
