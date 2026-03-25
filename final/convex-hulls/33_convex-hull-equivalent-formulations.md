# Equivalent formulations and problem statement

## Scope
- **Slides:** pp. 190-195
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.20 9.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
The course gives several equivalent ways to think about the hull because different algorithms and proofs use different one-liners: smallest convex set, intersection of half-planes, union of triangles, and so on.

## What you must know cold
- Hull as the intersection of all convex sets containing S.
- Hull as the intersection of all containing half-planes / half-spaces.
- Hull as smallest enclosing convex polygon.
- Formal problem statement: given S, construct H(S).

## Core ideas and reasoning
- These equivalences justify multiple algorithm paradigms: half-plane tests, supporting-line arguments, or combinatorial constructions.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 190
![Figure from slide p. 190](../images/convex-hulls/33_convex-hull-equivalent-formulations_p190.png)

### Figure from slide p. 191
![Figure from slide p. 191](../images/convex-hulls/33_convex-hull-equivalent-formulations_p191.png)

## Slide-by-slide digestion

### p. 190 - Preliminaries and definitions
- Convex hull, definition 6
- The convex hull H(S) is the intersection of all convex sets
- that contain S.

### p. 191 - Preliminaries and definitions
- Convex hull, definition 7
- The convex hull H(S) is the intersection of all halfspaces
- (for d = 2, halfplanes) that contain S.

### p. 192 - Preliminaries and definitions
- Convex hull, definition 8
- The convex hull H(S) of a set of points S in the plane
- is the smallest convex polygon P that encloses S,
- smallest in the sense that there is no other polygon P′
- such that P ⊃P′ ⊇S.
- P′

### p. 193 - Preliminaries and definitions
- Convex hull, definition 9
- The convex hull H(S) of a set of points S in the plane
- is the enclosing convex polygon P with the smallest area.
- Convex hull, definition 10
- is the enclosing convex polygon P with the smallest perimeter.
- Extreme Points E
- A point p of a convex set is an extreme point if no two points
- a,b∈
- S exist such that p is between the line segment ab.
- Thus, in Definition 5 example, the points (1, 2, 3, 4, 5, 6, 7) are

### p. 194 - Preliminaries and definitions
- Convex hull, definition 11
- The convex hull H(S) of a set of points S in the plane
- is the union of all the triangles defined by points in S.
- This is a restatement of definition 5.
- Many triangles are not shown in the figure.

### p. 195 - Preliminaries and definitions
- Problem definitions
- CONVEX HULL
- INSTANCE. A set S = {p1, p2, …, pN} of d-dimensional points.
- QUESTION. Construct the convex hull H(S) for S.
- (The construction must give the vertices and their sequence,
- that is, obtain a description of the boundary which is a convex
- polygon.)
- EXTREME POINTS
- QUESTION. Identify the points of S that are vertices of
- the convex hull H(S). (Here, the ordering is not required.)

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Pre-algorithm theory.

## Common mistakes and danger points
- Equivalent formulations are not separate definitions of different objects; they describe the same hull.

## Exam-style drills and answer skeletons
### Definition drill
**Question.** Give the precise definitions and the most important consequences from equivalent formulations and problem statement.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Hull as the intersection of all convex sets containing S.
- Hull as the intersection of all containing half-planes / half-spaces.
- Hull as smallest enclosing convex polygon.
- Formal problem statement: given S, construct H(S).
### Core test / key idea
- These equivalences justify multiple algorithm paradigms: half-plane tests, supporting-line arguments, or combinatorial constructions.
### Complexity
- Pre-algorithm theory.
### Common mistakes / danger points
- Equivalent formulations are not separate definitions of different objects; they describe the same hull.
## End-of-file summary
- Hull as the intersection of all convex sets containing S.
- Hull as the intersection of all containing half-planes / half-spaces.
- Hull as smallest enclosing convex polygon.
- Pre-algorithm theory.
- Equivalent formulations are not separate definitions of different objects; they describe the same hull.

## Everything related to this topic
- **Previous file in reading order:** [Convex combinations and dimension-sensitive definitions](../convex-hulls/32_convex-combinations-and-dimension.md)
- **Next file in reading order:** [Lower bound for convex hull via reduction from sorting](../convex-hulls/34_convex-hull-lower-bound.md)
- **Source slide range:** pp. 190-195 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.20 9.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead