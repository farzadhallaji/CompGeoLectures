# Convex combinations and dimension-sensitive definitions

## Scope
- **Slides:** pp. 186-189
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.20 9.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This is the algebraic definition of convex hull, and it is one of the cleanest pieces of theory in the block.

## What you must know cold
- Convex combination: coefficients are nonnegative and sum to 1.
- Hull as the set of all convex combinations of input points.
- Dimension-sensitive idea that only up to d+1 points are needed in d-space.

## Core ideas and reasoning
- Affine combinations give the full affine span; convex combinations restrict you to the convex region.
- In the plane, every hull point can be represented using at most 3 input points.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 188
![Figure from slide p. 188](../images/convex-hulls/32_convex-combinations-and-dimension_p188.png)

### Figure from slide p. 189
![Figure from slide p. 189](../images/convex-hulls/32_convex-combinations-and-dimension_p189.png)

## Slide-by-slide digestion

### p. 186 - Preliminaries and definitions
- Parametric equation of a line
- Recall the following equation of a line:
- {α(p0) + (1 - α)(p1) }, where α ∈ ℜ(real numbers)
- where p0 and p1 are the points determining the line.
- p0 = (x0, y0)
- p1 = (x1, y1)
- Substituting gives
- {α(x0, y0) + (1 - α)(x1, y1) }
- Multiplying through gives the coordinates of points
- {αx0 + (1 - α)x1, αy0 + (1 - α)y1 }

### p. 187 - Preliminaries and definitions
- Convex combination
- We generalize from the parametric equation of a line,
- which suggests the idea of a convex combination.
- A convex combination of points p1, p2, …, pk
- is a sum of the form α1p1 + α2p2 + … + αkpk
- where αi ≥0 for 1 ≤i ≤k and α1 + α2 + … + αk = 1.
- Such a convex combination is a point.
- As we saw, a line segment consists of all convex combinations
- of its endpoints(k=2). (The same is not true of a line, why not?)
- A triangle consists of convex combinations of its three corners (k=3).

### p. 188 - Preliminaries and definitions
- Convex hull, definition 4
- The convex hull H(S) of a set of points S
- is the set of all convex combinations of the points of S.
- It should be intuitively clear that a hull defined in this way
- can not have a “dent” (reflex vertex).

### p. 189 - Preliminaries and definitions
- Convex hull, definition 5
- The convex hull H(S) of a set of points S in d dimensions
- is the set of all convex combinations of d + 1 or fewer points of S.
- This is different from definition 4 in that only d + 1 or fewer
- points are needed to get any point of H(S).
- For example, in the plane d = 2,
- convex polygons can be composed as the union of all points
- contained by the triangles of the given points,
- which are the convex combination of all d + 1 = 3 points.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
No algorithm yet; this is representational theory used in later equivalence proofs.

## Common mistakes and danger points
- Nonnegative coefficients and sum-to-1 are both required. Drop either condition and you leave the convex hull.

## Exam-style drills and answer skeletons
### Definition drill
**Question.** Give the precise definitions and the most important consequences from convex combinations and dimension-sensitive definitions.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Convex combination: coefficients are nonnegative and sum to 1.
- Hull as the set of all convex combinations of input points.
- Dimension-sensitive idea that only up to d+1 points are needed in d-space.
### Core test / key idea
- Affine combinations give the full affine span; convex combinations restrict you to the convex region.
- In the plane, every hull point can be represented using at most 3 input points.
### Complexity
- No algorithm yet; this is representational theory used in later equivalence proofs.
### Common mistakes / danger points
- Nonnegative coefficients and sum-to-1 are both required. Drop either condition and you leave the convex hull.
## End-of-file summary
- Convex combination: coefficients are nonnegative and sum to 1.
- Hull as the set of all convex combinations of input points.
- Dimension-sensitive idea that only up to d+1 points are needed in d-space.
- No algorithm yet; this is representational theory used in later equivalence proofs.
- Nonnegative coefficients and sum-to-1 are both required. Drop either condition and you leave the convex hull.

## Everything related to this topic
- **Previous file in reading order:** [Convex hull intuition and preliminaries](../03_Convex_Hulls/31_convex-hull-intuition.md)
- **Next file in reading order:** [Equivalent formulations and problem statement](../03_Convex_Hulls/33_convex-hull-equivalent-formulations.md)
- **Source slide range:** pp. 186-189 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.20 9.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead