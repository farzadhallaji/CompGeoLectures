# Primitive formulas and summary

## Scope
- **Slides:** pp. 63-65
- **Major topic folder:** pslgs-dcels-vectors-and-geometric-primitives
- **Recording files touching this material:** CS 564 - 01.23 1.2.txt, CS 564 - 01.30 3.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This range compresses the earlier primitives into a small toolkit. Treat it as your local formula sheet for the rest of the midterm.

## What you must know cold
- Parametric line equation and segment restriction.
- Point-line classification in terms of left, right, behind, beyond, between, origin, destination if your notes use that extended vocabulary.
- How these formulas combine in intersection and inclusion tests.

## Core ideas and reasoning
- Given a directed segment ab and point q, first use orientation to classify left/right/collinear.
- If collinear, parameter values or dot-product style comparisons decide whether q is behind a, beyond b, or on the segment.
- Most later algorithms are just structured uses of these formulas.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 63
![Figure from slide p. 63](../images/pslgs-dcels-vectors-and-geometric-primitives/09_primitive-formulas-summary_p63.png)

### Figure from slide p. 64
![Figure from slide p. 64](../images/pslgs-dcels-vectors-and-geometric-primitives/09_primitive-formulas-summary_p64.png)

## Slide-by-slide digestion

### p. 63 - Parametric equation of a line
- We use the following equation of a line:
- line = {α(p0) + (1 - α)(p1) }, where α ∈ ℜ(real numbers)
- where p0 and p1 as usual are the points determining the line.
- p0 = (x0, y0)
- p1 = (x1, y1)
- Substituting gives
- {α(x0, y0) + (1 - α)(x1, y1) }
- Multiplying through gives the coordinates
- {αx0 + (1 - α)x1, αy0 + (1 - α)y1 }
- α > 1

### p. 64 - Point-Line classification
- We now consider the geometric primitive operation of
- classifying a point w.r.t. a line (both in the plane).
- A directed line segment partitions the plane into 7
- non-overlapping regions. The possibilities are shown below.
- The problem, given p0, p1, and p2, is to determine which
- region p2 lies in.
- terminus
- origin
- beyond
- right

### p. 65 - Summary of geometric primitives
- We have seen the following primitives:
- 1. Triangle orientation
- 2. Left test
- 3. Point-line classification
- Others I have implemented:
- 1. Point-on-plane test
- 2. Segment-segment intersection
- 3. Segment-triangle intersection
- All require constant time (if d is fixed).
- There are many others. If in doubt, ask.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Constant-time primitives.

## Common mistakes and danger points
- Do not stop at collinear. Many algorithms need the follow-up between/behind/beyond logic.
- Maintain a consistent directed-edge convention.

## Exam-style drills and answer skeletons
Existing drill reminders from the earlier pack:
- Adapted from HW1-Q1: Given a circular linked list of points and a point P outside the list, decide whether the points are in counterclockwise order around P.

### Definition drill
**Question.** Give the precise definitions and the most important consequences from primitive formulas and summary.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Parametric line equation and segment restriction.
- Point-line classification in terms of left, right, behind, beyond, between, origin, destination if your notes use that extended vocabulary.
- How these formulas combine in intersection and inclusion tests.
### Core test / key idea
- Given a directed segment ab and point q, first use orientation to classify left/right/collinear.
- If collinear, parameter values or dot-product style comparisons decide whether q is behind a, beyond b, or on the segment.
- Most later algorithms are just structured uses of these formulas.
### Complexity
- Constant-time primitives.
### Common mistakes / danger points
- Do not stop at collinear. Many algorithms need the follow-up between/behind/beyond logic.
- Maintain a consistent directed-edge convention.
## End-of-file summary
- Parametric line equation and segment restriction.
- Point-line classification in terms of left, right, behind, beyond, between, origin, destination if your notes use that extended vocabulary.
- How these formulas combine in intersection and inclusion tests.
- Constant-time primitives.
- Do not stop at collinear. Many algorithms need the follow-up between/behind/beyond logic.
- Maintain a consistent directed-edge convention.

## Everything related to this topic
- **Previous file in reading order:** [Orientation tests and signed-area interpretation](../01_Foundations/08_orientation-and-signed-area.md)
- **Next file in reading order:** [Search problem taxonomy and inclusion basics](../02_Geometric_Search/10_search-taxonomy.md)
- **Source slide range:** pp. 63-65 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 01.23 1.2.txt, CS 564 - 01.30 3.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead