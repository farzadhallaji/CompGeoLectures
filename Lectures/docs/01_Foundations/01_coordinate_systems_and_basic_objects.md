# Coordinate Systems and Basic Geometric Objects

**Slides covered:** 9-19  

**Topic folder:** 01 Foundations

## Motivation

This file introduces the language of computational geometry: coordinates, dimensions, points, lines, segments, rays, planes, and rectangles. The goal is to know exactly what the basic objects are before any algorithm starts doing clever things.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 9: The objects considered in Computational Geometry are points,

- lines, line segments, polygons,  polyhedron,  hyper-rectangles,
- etc.
- A coordinate system provides a means to specify positions or points in space.
- The Cartesian coordinate system labels a d-dimensional space
- with d mutually perpendicular (orthogonal) coordinate axes, one per dimension.
- d-dimensional space (d-space)
- Notation d defined as number of dimensions of space or a geometric object.
- As a pre prefifix x on on the he na name of of an n obj object, d- de
- denot notes the he num numbe ber r of of dimensions of the object, e.g. d-rectangle or 2-rectangle.
- We will most often work in d = 2 (plane), which is the default,
- sometimes in d = 1 or d > 2.
- x y x y z d = 2 d = 3
- Right-handed coordinate system

![Figure from slide 9](images/slide_009.png)

### Slide 10: Object with d dimensions and 0 extent.

- Location in d-space.
- Given as an ordered sequence of d coordinates.
- d = 1
- (x) or x d = 2
- (x, y) d = 3
- (x, y, z) d ≥4
- (x1, x2, ..., xd) or (x0, x1, ..., xd-1) p0
- Line
- Infinite “straight” 1-dimensional set of points, determined by two points p0, p1 ∋p0 ≠p1.

![Figure from slide 10](images/slide_010.png)

### Slide 11: Finite 1-dimensional subset of a line, determined by two endpoints p0, p1.

- Ray
- Infinite 1-dimensional subset of a line determined by two points p0, p1 ∋p0 ≠p1,
- where one point is denoted as the endpoint.

![Figure from slide 11](images/slide_011.png)

### Slide 12: Point-Line classification

- We now consider the geometric primitive operation of classifying a point w.r.t. a line (both in the plane).
- A directed line segment partitions the plane into 7 non-overlapping regions.  The possibilities are shown below.
- The problem, given p0, p1, and p2, is to determine which region p2 lies in.
- p1 beyond left p0 terminus origin right behind between

![Figure from slide 12](images/slide_012.png)

### Slide 13: We use the following equation of a line:

- line = {α(p0) + (1 - α)(p1) }, where α ∈ ℜ(real numbers) where p0 and p1 as usual are the points determining the line.
- p0 = (x0, y0) p1 = (x1, y1)
- Substituting gives
- {α(x0, y0) + (1 - α)(x1, y1) }
- Multiplying through gives the coordinates
- {αx0 + (1 - α)x1, αy0 + (1 - α)y1 }
- W k t l ith i t (4 3) d (7 5) th t
- Work out an example with points (4,3) and (7,5) as the two end points with values of α as 0, 1, 0.5, 2 and -3.
- p1 p0 α > 1 α = 1 α = 0 α < 0
- 1 < α < 0

![Figure from slide 13](images/slide_013.png)

### Slide 14: A line segment is a closed subset of a line contained between two points which are

- called the end points. The subset is closed in the sense that it includes the end points.
- The equation of the line segment is the same as the parametric equation of a line with the
- as the parametric equation of a line with the restriction  that α has the value 0<=α<=1.
- This is also called the convex combination of the two end points.

### Slide 15: made by the line with positive x-axis c=intercept of the line with the y-axis.

- Vertical line  with x=k cannot be represented since these lines have infinite slopes.
- Expressed in terms of the coordinates of two points  on the line (x1,y1) and (x2,y2), we can
- write y=[(y2-y1)/(x2-x1)] x  + (y1x2 -y2x1)/(x2-x1)
- Or     (x2-x1)(y-y1)= (y2-y1)(x-x1)
- This is called an implicit form of an equation of a line. Now, x2=x1 and y2≠y1 means a
- vertical line with equation x=x1.
- θ m=tanθ c x y

![Figure from slide 15](images/slide_015.png)

### Slide 16: Note the coefficients are not unique; for a given constant k, kA, kB and kC will

- Note the coefficients are not unique; for a given constant k, kA, kB and kC will
- give the same line.
- In general, in a d-dimension, given a set of k points p1, p2, .., pk, the set of points
- p= α1 p1+ α2 p2+….+ ακ pk such that the α−coefficients are real and
- their sum equals 1, is called an affine combination of the given set of k points.
- For k=2, this set defines a straight line through two points; for k=3, it is a plane,
- and for higher k values, it is called a hyperplane.

### Slide 17: Plane

- Infinite 2-dimensional subset of space, determined by three points p0, p1, p2, ∋ p0 ≠ p1 ≠ p2 ≠ p0;
- (p0, p1, and p2 must be non-collinear).
- Interval
- Pair of coordinate values.
- Often treated like a segment on a coordinate axis.
- [l, r] closed; x ∋l ≤x ≤r is within interval
- (l, r) open; x ∋l < x < r is within interval r l closed r l open

![Figure from slide 17](images/slide_017.png)

### Slide 18: Rectangle

- Quadrilateral with opposite sides parallel and only right angles.
- 90° π/2
- We will use degrees or radians, as convenient.
- Rectilinear or axis parallel rectangle
- Cartesian product of d intervals.
- 2-rectangle or simply rectangle

![Figure from slide 18](images/slide_018.png)

### Slide 19: No prefix “d-” means usual or expected number of dimensions for the object.

- rectangle = 2-rectangle cube = 3-cube
- Prefix “hyper-” means d is unspecified and it may be more than
- the usual number of dimensions for that object.
- hyper-rectangle = d-rectangle, d unspecified
- “d-dimensional rectilinear hyper-rectangle”

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
