# Convex hull intuition and preliminaries

## Scope
- **Slides:** pp. 183-185
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.20 9.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
These slides fix the geometric meaning of convex hull before the algorithms start. If you cannot state what the hull is in three different ways, later proofs feel like spellcasting.

## What you must know cold
- Rubber-band intuition.
- Convex vs reflex vertices.
- The hull as the smallest convex polygon containing the set.

## Core ideas and reasoning
- Interior points do not appear as hull vertices.
- Reflex behavior belongs to non-convex polygons; the hull itself is convex.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 184
![Figure from slide p. 184](../images/convex-hulls/31_convex-hull-intuition_p184.png)

### Figure from slide p. 185
![Figure from slide p. 185](../images/convex-hulls/31_convex-hull-intuition_p185.png)

## Slide-by-slide digestion

### p. 183 - Preliminaries and definitions
- Intuitive definition
- Given a set S = {p1, p2, …, pN} of points in the plane,
- the convex hull H(S) is the smallest convex polygon in the plane
- that contains all of the points of S.
- Imagine nails pounded halfway into the plane at the points of S.
- The convex hull corresponds to a rubber band stretch around them.

### p. 184 - Preliminaries and definitions
- Convex polygon
- A polygon is convex iff for any two points in the polygon
- (interior ∪boundary) the segment connecting the points is
- entirely within the polygon.
- convex
- not convex

### p. 185 - Preliminaries and definitions
- Vertices
- A polygon vertex is convex if its interior angle ≤ π (180°).
- It is reflex if its interior angle > π (180°).
- convex
- In a convex polygon, all the vertices are convex.
- In other words, any polygon with a reflex vertex is not convex.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Definition stage.

## Common mistakes and danger points
- Do not confuse the hull of the input point set with a polygon formed by connecting points in arbitrary order.

## Exam-style drills and answer skeletons
### HW2-Q5 adapted
**Question.** Given the vertices of a non-convex simple polygon in clockwise order, explain how to obtain its convex hull in linear time.

**How to answer.** Use the boundary order to avoid a global sort. The answer should maintain a hull-like stack while scanning the polygonal chain.

### Definition drill
**Question.** Give the precise definitions and the most important consequences from convex hull intuition and preliminaries.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Rubber-band intuition.
- Convex vs reflex vertices.
- The hull as the smallest convex polygon containing the set.
### Core test / key idea
- Interior points do not appear as hull vertices.
- Reflex behavior belongs to non-convex polygons; the hull itself is convex.
### Complexity
- Definition stage.
### Common mistakes / danger points
- Do not confuse the hull of the input point set with a polygon formed by connecting points in arbitrary order.
## End-of-file summary
- Rubber-band intuition.
- Convex vs reflex vertices.
- The hull as the smallest convex polygon containing the set.
- Definition stage.
- Do not confuse the hull of the input point set with a polygon formed by connecting points in arbitrary order.

## Everything related to this topic
- **Previous file in reading order:** [Convex hull motivation and why the topic matters](../convex-hulls/30_convex-hull-motivation.md)
- **Next file in reading order:** [Convex combinations and dimension-sensitive definitions](../convex-hulls/32_convex-combinations-and-dimension.md)
- **Source slide range:** pp. 183-185 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.20 9.1.txt
- **Related homework-derived exam prompts included here:** HW2-Q5 adapted