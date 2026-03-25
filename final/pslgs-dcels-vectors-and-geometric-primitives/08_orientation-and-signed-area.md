# Orientation tests and signed-area interpretation

## Scope
- **Slides:** pp. 58-62
- **Major topic folder:** pslgs-dcels-vectors-and-geometric-primitives
- **Recording files touching this material:** CS 564 - 01.23 1.2.txt, CS 564 - 01.30 3.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This is one of the most important files in the whole pack. Orientation is the primitive behind convex hulls, polygon inclusion, sweep-line ordering, and half-plane tests. Break this and the course collapses in an impressively efficient way.

## What you must know cold
- Orientation determinant for three points a, b, c.
- Positive sign means c is to the left of directed edge ab; negative means right; zero means collinear.
- Determinant equals twice the signed area of triangle abc.
- Cycle interpretation: counterclockwise vs clockwise.

## Core ideas and reasoning
- Translate so a is at the origin. Then orient(a,b,c) = (b_x-a_x)(c_y-a_y) - (b_y-a_y)(c_x-a_x).
- The sign tells relative turning direction without computing any angle.
- Signed area explains why the same formula appears in both combinatorial and geometric arguments.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 58
![Figure from slide p. 58](../images/pslgs-dcels-vectors-and-geometric-primitives/08_orientation-and-signed-area_p58.png)

### Figure from slide p. 59
![Figure from slide p. 59](../images/pslgs-dcels-vectors-and-geometric-primitives/08_orientation-and-signed-area_p59.png)

## Slide-by-slide digestion

### p. 58 - LEFT-RIGHT-ABOVE-BELOW
- A geometric primitive operation: triangle orientation
- Given three non-collinear points p0, p1, p2, the triangle Δ p0p1p2
- is positively oriented if p2 lies to the left of p0p1,
- and negatively oriented if p2 lies to the right of p0p1.
- Let vector a = p1 - p0 and vector b = p2 - p0 .
- θab
- 0 < θab < 180
- positive orientation
- 180 < θab < 360
- negative orientation

### p. 59 - translations of the line segments at the origin.
- Vectors a and b can be in one of four possible configurations:
- In cases 1 and 3, 0 < θab < 180.
- In cases 2 and 4, 180 < θab < 360.
- In cases 1 and 2, the positive x axis pierces θab.
- In cases 3 and 4, it does not.
- We introduce the value Q = θb - θa (note that Q ≠θab).
- Case
- Range of Q = θb - θa
- Orientation of Δ p0p1p2
- -360 < Q < -180

### p. 60 - Observe from the table that sin(Q) has the same sign as the
- orientation of Δ p0p1p2.
- sin(Q) = sin(θb - θa)
- by definition of Q
- = sin θb cos θa - cos θb sin θa
- by trig. identity
- We know that
- cos θa = xa / |a| sin θa = ya / |a|
- cos θb = xb / |b| sin θb = yb / |b|
- by definition of sine and cosine. Then, by substitution
- sin(θb - θa) = (yb / |b|)(xa / |a|) - (xb / |b|)(ya / |a|)

### p. 61 - Another way of reaching the same expression is with the
- determinant of the coordinates of the points:
- | x0 y0 1 |
- D =
- | x1 y1 1 |
- | x2 y2 1 |
- Evaluating this determinant gives the expression
- x0 y1 + x2 y0 + x1 y2 - x2 y1 - x0 y2 - x1 y0
- which is the expansion of the final expression previously derived.
- Observe that the determinant is equivalent to the cross product
- (in 2 dimensions).

### p. 62 - Area Interpretation
- The value of the determinant D is twice
- the signed area of the triangle Δ p0p1p2 . The
- signed area is positive if p0p1p2 form a counter clockwise
- sequence, it is negative if this sequence is clockwise. If the
- area is zero, then D is 0.
- Generalization
- The three points p0 p1 and p2 form a plane in
- 3-d with a positive normal. A fourth point p3 is on the
- upside if p3 falls on the positive side of the plane and
- on the downside if p3 falls on the negative side of the plane.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Constant-time primitive. Entire algorithms are built by repeating this test.

## Common mistakes and danger points
- Direction matters. orient(a,b,c) = -orient(b,a,c).
- Zero means collinear; if an algorithm assumes general position, say so explicitly.
- Boundary handling is where many exam solutions die.

## Exam-style drills and answer skeletons
Existing drill reminders from the earlier pack:
- Use the orientation test to compare angular order of points around a query point without trigonometric functions.
- Explain how left/right tests implement half-plane membership in convex-polygon inclusion.
- Adapted from HW1-Q1: Given a circular linked list of points and a point P outside the list, decide whether the points are in counterclockwise order around P.

### HW1-Q1 adapted
**Question.** Given a circular linked list of points around P, test whether the list is in counterclockwise order around P without using trigonometric angles.

**How to answer.** Use a half-plane test plus the orientation determinant as an angle comparator. Pure determinant sign on consecutive pairs is not enough because the cyclic order can wrap past π.

### Definition drill
**Question.** Give the precise definitions and the most important consequences from orientation tests and signed-area interpretation.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Orientation determinant for three points a, b, c.
- Positive sign means c is to the left of directed edge ab; negative means right; zero means collinear.
- Determinant equals twice the signed area of triangle abc.
- Cycle interpretation: counterclockwise vs clockwise.
### Core test / key idea
- Translate so a is at the origin. Then orient(a,b,c) = (b_x-a_x)(c_y-a_y) - (b_y-a_y)(c_x-a_x).
- The sign tells relative turning direction without computing any angle.
- Signed area explains why the same formula appears in both combinatorial and geometric arguments.
### Complexity
- Constant-time primitive. Entire algorithms are built by repeating this test.
### Common mistakes / danger points
- Direction matters. orient(a,b,c) = -orient(b,a,c).
- Zero means collinear; if an algorithm assumes general position, say so explicitly.
- Boundary handling is where many exam solutions die.
## End-of-file summary
- Orientation determinant for three points a, b, c.
- Positive sign means c is to the left of directed edge ab; negative means right; zero means collinear.
- Determinant equals twice the signed area of triangle abc.
- Constant-time primitive. Entire algorithms are built by repeating this test.
- Direction matters. orient(a,b,c) = -orient(b,a,c).
- Zero means collinear; if an algorithm assumes general position, say so explicitly.

## Everything related to this topic
- **Previous file in reading order:** [Vector algebra and trigonometric groundwork](../pslgs-dcels-vectors-and-geometric-primitives/07_vectors-and-trig-groundwork.md)
- **Next file in reading order:** [Primitive formulas and summary](../pslgs-dcels-vectors-and-geometric-primitives/09_primitive-formulas-summary.md)
- **Source slide range:** pp. 58-62 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 01.23 1.2.txt, CS 564 - 01.30 3.1.txt
- **Related homework-derived exam prompts included here:** HW1-Q1 adapted