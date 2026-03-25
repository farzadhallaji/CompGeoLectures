# Supporting lines from hull union

## Scope
- **Slides:** pp. 242-244
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.27 11.1.txt, CS 564 - 02.27 11.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
Supporting lines are both a geometric concept and a merge primitive. They are the tangent lines that touch hulls without cutting through them.

## What you must know cold
- Definition of a supporting line for a convex polygon or two convex polygons.
- Upper and lower common tangents.
- Why the hull of a union reveals these lines.

## Core ideas and reasoning
- A common supporting line touches both polygons and leaves each polygon entirely on the same side.
- Finding upper/lower tangents is the key to linear-time hull merge.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 242
![Figure from slide p. 242](../images/convex-hulls/41_supporting-lines_p242.png)

### Figure from slide p. 243
![Figure from slide p. 243](../images/convex-hulls/41_supporting-lines_p243.png)

## Slide-by-slide digestion

### p. 242 - Divide-and-conquer
- Supporting lines, 1
- A by-product of the convex hull union algorithm is a method
- of determining supporting lines of two convex hulls.
- A supporting line of a convex polygon P is a straight line L
- passing through a vertex of P such that the interior of P
- lies entirely to one side of L.
- The idea is analogous to the notion of tangent for circles.

### p. 243 - Divide-and-conquer
- Supporting lines, 2
- Two convex polygons P1 and P2, with n and m vertices,
- such that one is not entirely contained within the other,
- have common supporting lines.
- The number of common supporting lines is ≥2 and ≤2*min(n,m).
- (Maximum is achieved when convex polygons are partially
- overlapping.)

### p. 244 - Divide-and-conquer
- Supporting lines, 3
- Once the convex hull of the union of P1 and P2 has been
- constructed, common supporting lines can be found.
- Scan the vertex list of H(P1 ∪P2);
- any pair of consecutive vertices where one originated in P1
- and the other in P2 defines a common supporting line.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Used as a linear-time merge primitive once hulls are already in cyclic order.

## Common mistakes and danger points
- Do not confuse supporting lines with arbitrary lines through hull vertices.

## Exam-style drills and answer skeletons
### Definition drill
**Question.** Give the precise definitions and the most important consequences from supporting lines from hull union.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Definition of a supporting line for a convex polygon or two convex polygons.
- Upper and lower common tangents.
- Why the hull of a union reveals these lines.
### Core test / key idea
- A common supporting line touches both polygons and leaves each polygon entirely on the same side.
- Finding upper/lower tangents is the key to linear-time hull merge.
### Complexity
- Used as a linear-time merge primitive once hulls are already in cyclic order.
### Common mistakes / danger points
- Do not confuse supporting lines with arbitrary lines through hull vertices.
## End-of-file summary
- Definition of a supporting line for a convex polygon or two convex polygons.
- Upper and lower common tangents.
- Why the hull of a union reveals these lines.
- Used as a linear-time merge primitive once hulls are already in cyclic order.
- Do not confuse supporting lines with arbitrary lines through hull vertices.

## Everything related to this topic
- **Previous file in reading order:** [Divide-and-conquer convex hulls and hull union](../03_Convex_Hulls/40_divide-and-conquer-hull.md)
- **Next file in reading order:** [Dynamic/on-line convex hull insertion: problem setting and core idea](../03_Convex_Hulls/42_dynamic-hull-core-idea.md)
- **Source slide range:** pp. 242-244 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.27 11.1.txt, CS 564 - 02.27 11.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead