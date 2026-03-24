# Geometric Search Overview and Polygon Inclusion

**Slides covered:** 66-79  

**Topic folder:** 02 Geometric Search

## Motivation

Geometric search asks: after preprocessing a geometric data set, how can we answer queries quickly? The first examples are polygon inclusion problems for convex, simple, and star-shaped polygons.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 66: In general terms a geometric query or search problem has this form:

- Given a set S of geometric objects and a distinct geometric object q
- which is the query object, the objective is to determine the subset
- of the objects in set S that are in some specified geometric
- relationship with the query object.
- Many variations are possible, depending on the specific problem.
- 1. S may have 1 or more elements.
- 2. The elements of S may be of the same type as q, or not.
- 3. The answer set may be constrained to have exactly one element,
- or it may vary from 0 to |S|.
- Topics of this section
- In this section, we will examine three specific problems of this type:
- 1. Polygon inclusion
- 2. Point location
- 3. Range searching

### Slide 67: Given polygon P and query point q, both in the plane, is q within P?

- P may be of different types (simple, convex, or star-shaped),
- which will affect the method.
- Methods
- Left test (convex)
- Intersection counting (Simple)
- Wedges (Convex and star-shaped)
- P q

![Figure from slide 67](images/slide_067.png)

### Slide 68: Given a partition of the geometric space into regions and a query

- point q, determine which region contains q.
- We will consider only d = 2, i.e., the plane.
- Methods
- Brute force
- Slab method
- Chain method
- Triangle refinement q f6 f1 f2 f3 f4 f5

![Figure from slide 68](images/slide_068.png)

### Slide 69: RANGE SEARCHING

- INSTANCE:  Set S = {p1, p2, ..., pN}, pi = (xi, yi) of points in the
- plane, and rectangle R = [lx, rx] × [ly, ry] in the plane.
- QUESTION:  Which points of S are within R?
- Methods
- Brute force
- Dominance
- Grid
- Quadtree k-D tree
- Direct access
- Range tree lx rx ly ry

![Figure from slide 69](images/slide_069.png)

### Slide 70: CONVEX POLYGON INCLUSION

- INSTANCE:  Convex polygon P = (e0 = v0v1, e1 = v1v2, ..., eN-1 = vN-1v0) with N edges and query point q, both in the plane.
- QUESTION:  Is q within P?
- Convex polygon inclusion by Left test
- P is the intersection of the half-planes defined by its edges.
- Query point q is within P iff q is to the left of or on all N edges of P.
- (This is true iff P is convex.) v0 v3 v1 v2 vN - 1
- ...
- P q1 q2

![Figure from slide 70](images/slide_070.png)

### Slide 71: Convex polygon inclusion by Left test procedure ConvexInclusion(P,q)

- begin for i = 0 to N /* Check each edge */ c = PointLineClassify(vi,v(i+1) mod N,q)
- if c = RIGHT return FALSE endif endfor return TRUE
- 10 end procedure ConvexInclusion(P,q) begin for i = 0 to N /* Check each edge */
- if
- Left(v(i+1) mod N,vi,q)  /* Backwards edge */ return FALSE endif
- endfor return TRUE end
- Analysis
- Time:  O(N);  N edges, O(1) each to classify.
- Space:  O(N);  N edges.

### Slide 72: SIMPLE POLYGON INCLUSION

- INSTANCE:  Simple polygon P = (e0 = v0v1, e1 = v1v2, ..., eN -1 = vN -1v0) with N edges and query point q, both in the plane.
- QUESTION:  Is q within P?
- Simple polygon inclusion by Intersection counting
- Query point q is within P iff a ray originating at q intersects
- the boundary of P an odd number of times.
- P

![Figure from slide 72](images/slide_072.png)

### Slide 73: Simple polygon inclusion by Intersection counting procedure SimpleInclusion(P,q)  /* Incomplete version */

- begin c = 0 for i = 0 to N /* Check each edge */ if edge vi,v(i+1) mod N ∩ray -∞,q
- c = (c + 1) mod 2 endif endfor if c = 1 return TRUE else return FALSE
- endif
- 14 end
- Analysis
- Time:  O(N);  N edges, O(1) each to test intersection.
- Space:  O(N);  N edges.

### Slide 74: Special cases, not explicitly handled by given procedure:

- 1.  Ray collinear with horizontal edge of P
- 2.  Ray intersects vertex of P
- 3.  Query point q on edge of P
- Resolving these special cases does not change complexity.
- See Preparata, p. 42 or O’Rourke, p. 233-236 for details.
- q2 Wrong q3 Right
- Ray intersects vertex of P q1 Right q2 Wrong
- Query point q on edge of P
- Ray collinear with horizontal edge of P q3 Right q3 Wrong

![Figure from slide 74](images/slide_074.png)

### Slide 75: CONVEX POLYGON INCLUSION

- INSTANCE:  Convex polygon P = (e0 = v0v1, e1 = v1v2, ..., eN -1 = vN -1v0) with N edges and query point q, both in the plane.
- QUESTION:  Is q within P?
- P convex ⇒ the vertices of P occur in angular order about any point within P.
- v0 v3 v1 v2 vN - 1
- ...
- P c q
- Rays from an internal point partition the plane into wedges.
- Convex polygon inclusion query has two steps:
- 1.  Determine wedge containing q
- 2.  Determine which side of edge for that wedge q is on

![Figure from slide 75](images/slide_075.png)

### Slide 76: 1. Find a point c internal to P (centroid of any three vertices).

- 2. Arrange the vertices into a data structure suitable for binary search (e.g., an array).
- Query
- Given query point q,
- 1. Find wedge containing q by binary search on the vertices.
- Point q lies within the wedge for vertices vi and vi+1 iff qcpi is a Right turn and qcpi+1 is a Left turn.
- 2. Once pi and pi+1 have been found, q is internal iff pi+1piq is a Left turn.
- v0 v3 v1 v2 vN - 1
- ...
- P c q q

![Figure from slide 76](images/slide_076.png)

### Slide 77: Preprocessing time:  O(N); to load vertices into data structure.

- Query time:  O(log N); binary search with O(1) time per comparison.
- Space:  O(N); for N edges.
- Comments
- Note that O(N) preprocessing enables O(log N) query.
- Since O(N) query exists, this method is useful for repetitive mode
- queries, not for single shot queries.
- Notation different in notes and text.
- This algorithm in text appears to be in error.
- Step 2, p. 43 seems to omit case of q on edge.
- Determinant (area of triangle) = 0 if q on edge.

### Slide 78: STAR-SHAPED POLYGON INCLUSION

- INSTANCE:  Star-shaped polygon P = (e0 = v0v1, e1 = v1v2, ...,
- eN-1 = vN-1v0) with N edges and query point q, both in the plane.
- QUESTION:  Is q within P?
- A simple polygon P is star-shaped if ∃ a point c within
- P ∋ for all points p within P the segment cp lies within P. The
- locus of those points is the kernel of P.
- (Note that convex polygons are star-shaped, and that for a convex polygon the entire polygon is the kernel.)
- ∈kernel
- ∉kernel c
- P

![Figure from slide 78](images/slide_078.png)

### Slide 79: P star-shaped ⇒ the vertices of P occur in angular order about any point in

- the kernel of P ⇒
- The convex polygon inclusion algorithm can be used, once a point in the kernel of P has been found.
- This can be done in O(N) time ⇒
- Preprocessing remains O(N).
- c
- P

![Figure from slide 79](images/slide_079.png)

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
