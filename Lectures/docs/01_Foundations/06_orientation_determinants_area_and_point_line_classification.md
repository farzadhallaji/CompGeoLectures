# Orientation, Determinants, Area, and Point-Line Classification

**Slides covered:** 58-65  

**Topic folder:** 01 Foundations

## Motivation

This is the heart of many geometry algorithms. The orientation test tells left versus right, determinants turn that into a formula, and the signed area view explains why the test works.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 58: A geometric primitive operation:  triangle orientation

- Given three non-collinear points p0, p1, p2, the triangle Δ p0p1p2
- is positively oriented if p2 lies to the left of p0p1, and negatively oriented if p2 lies to the right of p0p1.
- Let vector a = p1 - p0 and vector b = p2 - p0  .
- p0 p1 p2 a b p0 p1 p2 a b θab θab
- 0 < θab < 180 positive orientation
- 180 < θab < 360 negative orientation
- p0, p1, p2 form a counter-clockwise cycle p0, p1, p2 form a clockwise cycle

![Figure from slide 58](images/slide_058.png)

### Slide 59: Vectors a and b can be in one of four possible configurations:

- In cases 1 and 3, 0 < θab < 180.
- In cases 2 and 4, 180 < θab < 360.
- In cases 1 and 2, the positive x axis pierces θab.
- In cases 3 and 4, it does not.
- We introduce the value Q = θb - θa (note that Q ≠θab).
- Case
- Range of Q = θb - θa sin Q
- Orientation of Δ p0p1p2
- -360 < Q < -180
- -180 < Q < 0
- 0 < Q < 180
- 180 < Q < 360
- (Equality holds if a and b are collinear.)
- With this information, we could compute Q = θb - θa and then use the table to give the orientation of Δ p0p1p2.
- But computing θa and θb require expensive trig. functions.
- Can we do better?

![Figure from slide 59](images/slide_059.png)

### Slide 60: sin(Q) = sin(θb - θa) by definition of Q

- = sin θb cos θa - cos θb sin θa by trig. identity
- We know that cos θa = xa / |a|        sin θa = ya / |a| cos θb = xb / |b|        sin θb = yb / |b|
- by definition of sine and cosine.  Then, by substitution sin(θb - θa) = (yb / |b|)(xa / |a|) - (xb / |b|)(ya / |a|)
- = (1 / |a| |b|) (ybxa - xbya).
- |a| and |b| are positive constants, so sign(sin(θb - θa)) = sign(ybxa - xbya).
- By definition, xa = (x1 - x0)        ya = (y1 - y0) xb = (x2 - x0)        yb = (y2 - y0)
- so sign(sin(θb - θa)) = sign((y2 - y0)(x1 - x0) - (x2 - x0)(y1 - y0)).
- The latter expression can be used to find the orientation of Δ p0p1p2
- from the coordinates of p0, p1, p2 in constant time.

### Slide 61: | x0 y0 1 |

- D =
- | x1 y1 1 |
- | x2 y2 1 |
- Evaluating this determinant gives the expression x0 y1 + x2 y0 + x1 y2 - x2 y1 - x0 y2 - x1 y0
- which is the expansion of the final expression previously derived.
- Observe that the determinant is equivalent to the cross product
- (in 2 dimensions).
- Left turn/Right Turn Test
- If the sign of the determinant D is positive then Δ p0p1p2  is counterclockwise (p2 is left of p0p1 ) and if D is negative then Δ p0p1p2 is
- clockwise (p2 is right of p0p1 ). If D=0, then the three points are
- collinear.
- p0 p1 p2 p2 left right

![Figure from slide 61](images/slide_061.png)

### Slide 62: The value of the determinant D is twice the signed area of the triangle Δ p0p1p2 . The

- signed area is positive if p0p1p2 form a counter clockwise sequence, it is negative if this sequence is clockwise. If the
- area is zero, then D is 0.
- Generalization
- The three points p0   p1 and p2  form a plane in
- 3-d with a positive normal. A fourth point p3 is on the upside if p3 falls on the positive side of the plane and
- on the downside if  p3 falls on the negative side of the plane.
- The test for this is with respect to the sign of the determinant.
- |  x0  y0  z0   1 |
- |  x1  y1  z1   1 |
- D =    |  x2  y2  z2   1 |
- |  x3  y3  z3   1 |
- This D represents the signed volume of the polyhedron.
- The formulation extends to n-dimensional space.
- (Reading Assignment: Section 1:3(p.17) to Section 1:5 (p.35),
- in O’Rourke text).

### Slide 63: We use the following equation of a line:

- line = {α(p0) + (1 - α)(p1) }, where α ∈ ℜ(real numbers) where p0 and p1 as usual are the points determining the line.
- p0 = (x0, y0) p1 = (x1, y1)
- Substituting gives
- {α(x0, y0) + (1 - α)(x1, y1) }
- Multiplying through gives the coordinates
- {αx0 + (1 - α)x1, αy0 + (1 - α)y1 } p1 p0 α > 1 α = 1 α = 0 α < 0
- 1 < α < 0

![Figure from slide 63](images/slide_063.png)

### Slide 64: Point-Line classification

- We now consider the geometric primitive operation of classifying a point w.r.t. a line (both in the plane).
- A directed line segment partitions the plane into 7 non-overlapping regions.  The possibilities are shown below.
- The problem, given p0, p1, and p2, is to determine which region p2 lies in.
- p0 p1 terminus origin beyond right left behind between

![Figure from slide 64](images/slide_064.png)

### Slide 65: We have seen the following primitives:

- 1. Triangle orientation
- 2. Left test
- 3. Point-line classification
- Others I have implemented:
- 1. Point-on-plane test
- 2. Segment-segment intersection
- 3. Segment-triangle intersection
- All require constant time (if d is fixed).
- There are many others.  If in doubt, ask.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
