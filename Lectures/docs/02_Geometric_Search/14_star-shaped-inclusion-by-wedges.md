# Star-shaped polygon inclusion by wedges

## Scope
- **Slides:** pp. 78-79
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 01.30 3.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This extends the wedge idea from convex polygons to star-shaped polygons. The cost is that you now rely on a kernel point rather than arbitrary interior structure.

## What you must know cold
- Definition of a star-shaped polygon and its kernel.
- Why a kernel point sees the entire boundary.
- How wedge partitioning around a kernel point supports inclusion testing.

## Core ideas and reasoning
- Pick a point in the kernel. Every boundary point is visible from it.
- Order vertices around that point, find the wedge containing the query direction, then test locally.
- The method is an extension of the convex fan idea but requires star-shaped visibility.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 78
![Figure from slide p. 78](../images/geometric-search/14_star-shaped-inclusion-by-wedges_p78.png)

### Figure from slide p. 79
![Figure from slide p. 79](../images/geometric-search/14_star-shaped-inclusion-by-wedges_p79.png)

## Slide-by-slide digestion

### p. 78 - Star-shaped polygon inclusion by Wedges
- STAR-SHAPED POLYGON INCLUSION
- INSTANCE: Star-shaped polygon P = (e0 = v0v1, e1 = v1v2, ...,
- eN-1 = vN-1v0) with N edges and query point q, both in the plane.
- QUESTION: Is q within P?
- A simple polygon P is star-shaped if ∃ a point c within
- P ∋ for all points p within P the segment cp lies within P. The
- locus of those points is the kernel of P.
- (Note that convex polygons are star-shaped, and that for a
- convex polygon the entire polygon is the kernel.)
- ∈kernel

### p. 79 - Star-shaped polygon inclusion by Wedges
- P star-shaped ⇒
- the vertices of P occur in angular order about any point in
- the kernel of P ⇒
- The convex polygon inclusion algorithm can be used,
- once a point in the kernel of P has been found.
- This can be done in O(N) time ⇒
- Preprocessing remains O(N).

## What you must be able to say or do in an exam
- State the input, output, preprocessing, and query/update model precisely.
- Explain the invariant or ordering that makes the method work.
- Trace the method by hand on a small example.
- Give the exact time and space bounds.
- Mention one edge case, degeneracy, or limitation.

## Complexity and performance facts
After suitable preprocessing, queries can be handled similarly to wedge-based convex inclusion.

## Common mistakes and danger points
- An arbitrary interior point is not enough; it must lie in the kernel.
- Do not claim this works for every simple polygon.
- Boundary case matters: when the query point lies exactly on an edge (orientation/determinant = 0), handle it according to the problem's inside/boundary policy; do not skip the determinant-zero branch.

## Exam-style drills and answer skeletons
### Core exam drill
**Question.** State the problem solved by star-shaped polygon inclusion by wedges, describe preprocessing/query/update steps if any, and give the time and space bounds.

**How to answer.** An excellent answer names the input, the output, the invariant or ordering exploited by the method, and the exact asymptotic costs.

### Hand-trace drill
**Question.** Trace star-shaped polygon inclusion by wedges on a small example by hand and explain each comparison or structural change.

**How to answer.** On this course, being able to run the method on a picture matters more than writing vague slogans.

## Recap
### What you must know cold
- Definition of a star-shaped polygon and its kernel.
- Why a kernel point sees the entire boundary.
- How wedge partitioning around a kernel point supports inclusion testing.
### Core test / key idea
- Pick a point in the kernel. Every boundary point is visible from it.
- Order vertices around that point, find the wedge containing the query direction, then test locally.
- The method is an extension of the convex fan idea but requires star-shaped visibility.
### Complexity
- After suitable preprocessing, queries can be handled similarly to wedge-based convex inclusion.
### Common mistakes / danger points
- An arbitrary interior point is not enough; it must lie in the kernel.
- Do not claim this works for every simple polygon.
- Boundary case matters: when the query point lies exactly on an edge (orientation/determinant = 0), handle it according to the problem's inside/boundary policy; do not skip the determinant-zero branch.
## End-of-file summary
- Definition of a star-shaped polygon and its kernel.
- Why a kernel point sees the entire boundary.
- How wedge partitioning around a kernel point supports inclusion testing.
- After suitable preprocessing, queries can be handled similarly to wedge-based convex inclusion.
- An arbitrary interior point is not enough; it must lie in the kernel.
- Do not claim this works for every simple polygon.

## Everything related to this topic
- **Previous file in reading order:** [Convex polygon inclusion by wedges](../02_Geometric_Search/13_convex-inclusion-by-wedges.md)
- **Next file in reading order:** [Point location by slab decomposition](../02_Geometric_Search/15_point-location-slab-method.md)
- **Source slide range:** pp. 78-79 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 01.30 3.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead