# Convex Hull Overview, Definitions, and Lower Bounds

**Slides covered:** 181-201  

**Topic folder:** 03 Convex Hulls

## Motivation

The convex hull is one of the central objects in computational geometry. These slides explain what it is, give many equivalent definitions, and show how lower bounds are argued using problem transformations.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 181: Topic overview

- Chapter 3 in Preparata, Chapter 3 in O’Rourke.
- Chapter 1 and 11 in  Berg et.al. (This book was not out when these slides were prepared.)
- Seq Src Subtopic
- Preparata O’Rourke
- O+P Preliminaries and definitions
- P
- Problem definition, convex hull
- P
- Problem definition, extreme points 99
- P
- Lower bound, convex hull
- *
- Lower bound, extreme points
- P
- Convex hull by extreme points
- P
- Graham’s scan
- P

### Slide 182: -useful to construct other structures

- -many applications: robot motion planning, shape analysis etc.
- - a beautiful object, one of the early success stories in computational
- geometry that sparked interest among Computer Scientists by the invention of O(nlogn) algorithm
- rather than a O(n**3) algorithm.
- - intimately related to sorting algorithm for both lower and upper bound.

### Slide 183: Intuitive definition

- Given a set S = {p1, p2, …, pN} of points in the plane, the convex hull H(S) is the smallest convex polygon in the plane
- that contains all of the points of S.
- Imagine nails pounded halfway into the plane at the points of S.
- The convex hull corresponds to a rubber band stretch around them.

![Figure from slide 183](images/slide_183.png)

### Slide 184: Convex polygon

- A polygon is convex iff for any two points in the polygon
- (interior ∪boundary) the segment connecting the points is entirely within the polygon.
- convex not convex

![Figure from slide 184](images/slide_184.png)

### Slide 185: Vertices

- A polygon vertex is convex if its interior angle ≤ π (180°).
- It is reflex if its interior angle > π (180°).
- convex reflex
- In a convex polygon, all the vertices are convex.
- In other words, any polygon with a reflex vertex is not convex.

![Figure from slide 185](images/slide_185.png)

### Slide 186: Parametric equation of a line

- Recall the following equation of a line:
- {α(p0) + (1 - α)(p1) }, where α ∈ ℜ(real numbers) where p0 and p1 are the points determining the line.
- p0 = (x0, y0) p1 = (x1, y1)
- Substituting gives
- {α(x0, y0) + (1 - α)(x1, y1) }
- Multiplying through gives the coordinates of points
- {αx0 + (1 - α)x1, αy0 + (1 - α)y1 }
- If 0 <=  α <= 1, the points are between p0 and p1.
- p1 p0 α > 1 α = 1 α = 0 α < 0
- 1 < α < 0

![Figure from slide 186](images/slide_186.png)

### Slide 187: Convex combination

- We generalize from the parametric equation of a line, which suggests the idea of a convex combination.
- A convex combination of points p1, p2, …, pk is a sum of the form α1p1 + α2p2 + … + αkpk
- where αi ≥0 for 1 ≤i ≤k and α1 + α2 + … + αk = 1.
- Such a convex combination is a point.
- As we saw, a line segment consists of all convex combinations
- of its endpoints(k=2).  (The same is not true of a line, why not?)
- A triangle consists of convex combinations of its three corners (k=3).
- For k = 4, a tetrahedron consists of all convex combinations
- of its four corners.
- These objects are all convex.
- A convex set is the set of all convex combinations of its defining points.

![Figure from slide 187](images/slide_187.png)

### Slide 188: Convex hull, definition 4

- The convex hull H(S) of a set of points S is the set of all convex combinations of the points of S.
- It should be intuitively clear that a hull defined in this way
- can not have a “dent” (reflex vertex).

![Figure from slide 188](images/slide_188.png)

### Slide 189: Convex hull, definition 5

- The convex hull H(S) of a set of points S in d dimensions is the set of all convex combinations of d + 1 or fewer points of S.
- This is different from definition 4 in that only d + 1 or fewer
- points are needed to get any point of H(S).
- For example, in the plane d = 2, convex polygons can be composed as the union of all points
- contained by the  triangles of the given points, which are the convex combination of all d + 1 = 3 points.

![Figure from slide 189](images/slide_189.png)

### Slide 190: Convex hull, definition 6

- The convex hull H(S) is the intersection of all convex sets that contain S.

![Figure from slide 190](images/slide_190.png)

### Slide 191: Convex hull, definition 7

- The convex hull H(S) is the intersection of all halfspaces
- (for d = 2, halfplanes) that contain S.

![Figure from slide 191](images/slide_191.png)

### Slide 192: Convex hull, definition 8

- The convex hull H(S) of a set of points S in the plane is the smallest convex polygon P that encloses S,
- smallest in the sense that there is no other polygon P′ such that P ⊃P′ ⊇S.
- P
- P′

![Figure from slide 192](images/slide_192.png)

### Slide 193: Convex hull, definition 9

- The convex hull H(S) of a set of points S in the plane is the enclosing convex polygon P with the smallest area.
- Convex hull, definition 10
- The convex hull H(S) of a set of points S in the plane is the enclosing convex polygon P with the smallest perimeter.
- Extreme Points E
- A point p of a convex set is an extreme point if no two points
- a,b∈
- S exist such that p is between the line segment ab.
- Thus, in Definition 5 example, the points (1, 2, 3, 4, 5, 6, 7) are
- extreme points but 8 and 9 and others are not.
- Alternately, the extreme points of S is the smallest subset of  S
- having the property that H(E)=H(S).
- Thus, E defines the vertices on H(S) but does not define the
- convex hull H(S), which requires the sequence of points on the
- hull viz. (1, 3, 4, 2, 6, 7, 5) for our example. Thus, there are two
- distinct problems.

### Slide 194: Convex hull, definition 11

- The convex hull H(S) of a set of points S in the plane is the union of all the triangles defined by points in S.
- This is a restatement of definition 5.
- Many triangles are not shown in the figure.

![Figure from slide 194](images/slide_194.png)

### Slide 195: Problem definitions

- CONVEX HULL
- INSTANCE.  A set S = {p1, p2, …, pN} of d-dimensional points.
- QUESTION.  Construct the convex hull H(S) for S.
- (The construction must give the vertices and their sequence,
- that is, obtain a description of the boundary which is a convex
- polygon.)
- EXTREME POINTS
- INSTANCE.  A set S = {p1, p2, …, pN} of d-dimensional points.
- QUESTION.  Identify the points of S that are vertices of the convex hull H(S).  (Here, the ordering is not required.)
- We will assume d = 2 unless otherwise noted.
- It turns out that both have the same asymptotic complexity θ(nlogn) for d=2. Thus the second problem is not any easier
- than the first problem.

### Slide 196: Transformation of problems

- We would like to establish lower bounds for performance measures (time and space) for problems (not algorithms!).
- One reason:  to avoid a futile search for an algorithm faster than
- the theoretical lower bound for the problem.
- Generally, proving a lower (or upper) is difficult, because it is a proof about all algorithms to solve the problem.
- There is a technique to do so, useful in some cases:
- transformation of problems.
- Suppose there are two problems A and B, which are related so that every instance of A can be solved as follows:
- 1. Convert the instance of A to a suitable instance of B.
- 2. Solve problem B.
- 3. Convert the answer to B to a correct answer to the original
- instance of A.
- We say:  A has been transformed to B.
- If the transformation steps 1 and 3 can be performed in a total of
- O(τ(N)) time, we say that A is τ(N)-transformable to B, written
- A ατ(N) B
- Transformability is not necessarily symmetric.
- If problems A and B are mutually transformable, they are equivalent.

### Slide 197: Lower and upper bounds via transformation

- Under the assumption that the transformation preserves the order of the instance size, the transformation has two properties:
- Property 1 (Lower bound via transformation).  If problem A is
- known to require at least T(N) time and A is τ(N)-transformable to B,
- then B requires at least T(N) - O(τ(N)) time.
- Otherwise, you could use the transformation to solve A too fast.
- Property 2 (Upper bound via transformation).  If problem B can be
- solved in T(N) time and A is τ(N)-transformable to B, then A requires at most T(N) + O(τ(N)) time.
- You can always solve A via the transformation.
- Problem A
- Problem B τ(N)-transformable
- Upper bound O(f(N))
- Lower bound Ω(f(N))

![Figure from slide 197](images/slide_197.png)

### Slide 198: A known problem

- Note that the technique assumes that there is a problem with a
- known lower bound (to use property 1).
- We have such a problem:  SORTING requires Ω(N log N).
- Problem A
- Problem B τ(N)-transformable
- Upper bound O(f(N))
- Lower bound Ω(f(N))

![Figure from slide 198](images/slide_198.png)

### Slide 199: Lower bound for CONVEX HULL

- Can we get a lower bound for time for CONVEX HULL?
- Recall that that the constructed hull H(S) must be given in order.
- This suggest a connection to SORTING.
- Theorem.  SORTING is linear-time transformable to CONVEX
- HULL;  SORTING αO(N) CONVEX HULL.
- Therefore, CONVEX HULL requires at least Ω(N log N) time.
- Proof.  We show the transformation.  Suppose the instance of
- SORTING is the set of N real numbers {x1, x2, …, xN}.
- Transform that set to an instance of CONVEX HULL by converting each real number xi to the point (xi,xi
- 2).  O(N)
- All of these points lie on the parabola y = x2.

![Figure from slide 199](images/slide_199.png)

### Slide 200: Lower bound for CONVEX HULL

- The convex hull of the converted instance will consist of a list of points, sorted by abscissa.  At most one pass through the list
- will find the smallest and the answer to SORTING can be read off from there in one pass.  O(N)

![Figure from slide 200](images/slide_200.png)

### Slide 201: Lower bound for CONVEX HULL

- Note that the O(N) transformation is dominated by the O(N log N)
- complexity of the problem.
- As a consequence of this transformation, we know that CONVEX HULL requires at least Ω(N log N) time.
- SORTING
- CONVEX HULL
- O(N)-transformable
- Upper bound O(N log N)
- Lower bound Ω(N log N)
- Can we find an algorithm for CONVEX HULL that requires
- O(N log N) time, which will be the best we can do?

![Figure from slide 201](images/slide_201.png)

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
