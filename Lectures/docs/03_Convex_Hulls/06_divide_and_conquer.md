# Divide-and-Conquer Convex Hull

**Slides covered:** 235-244  

**Topic folder:** 03 Convex Hulls

## Motivation

This algorithm splits the points into left and right subsets, builds hulls recursively, and then merges the two hulls using upper and lower tangents.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 235: Divide-and-conquer design goal

- QUICKHULL recursively subdivides point set S, and assembles the convex hull H(S) by “merging”
- the subproblem results.
- Advantages:
- 1. Subdivision allows parallelization
- 2. Merge process is very simple (concatenation)
- Disadvantage:
- 1. Inability to control or guarantee subproblem size results in suboptimum worst case time performance.
- We seek a divide-and-conquer algorithm which divides the problem into subproblems of approximately equal size.

### Slide 236: Union of convex hulls, 1

- Suppose we have S and want to compute H(S).
- Further suppose S has been partitioned into S1 and S2, each containing half the points of S.
- If H(S1) and H(S2) are found separately (recursively), how much additional work is required to compute H(S1 ∪S2),
- i.e., H(S)?
- In other words, is it easier to find H(S) = H(S1 ∪S2) given H(S1) and H(S2) than to find H(S) directly?
- To do so, we use the relation:
- H(S1 ∪S2) = H(H(S1) ∪H(S2))
- The convex hull of the union of the two subsets is the same as
- the convex hull of the union of the convex hulls of the two subsets.

### Slide 237: Union of convex hulls, 2

- The relation is:  H(S1 ∪S2) = H(H(S1) ∪H(S2))
- Computing the convex hull of the union of convex hulls is made simpler because H(S1) and H(S2) are convex polygons
- and thus have an ordering on their vertices.
- HULL OF UNION OF CONVEX POLYGONS
- INSTANCE:  Convex polygons P1 and P2.
- QUESTION:  Find the convex hull of their union.
- This problem is the merge step of a divide-and-conquer algorithm for convex hull construction.
- An efficient algorithm for the merge is necessary for an efficient divide-and-conquer algorithm.
- H(S1)
- H(S2)

![Figure from slide 237](images/slide_237.png)

### Slide 238: Overview of divide-and-conquer algorithm

- 1. If |S|  k0 (k0 is a small integer), construct the convex hull
- directly by some method and stop, else go to step 2.
- (For example, for k0 = 3 the hull is a triangle, O(1).)
- 2. Partition the set S arbitrarily into two subsets S1 and S2
- of approximately equal sizes.
- 3. Recursively find the convex hulls H(S1) and H(S2).
- 4. Merge the two hulls together to form H(S).
- Let U(N) denote the time needed to find the hull of the union of
- two convex polygons (convex hulls), each with N/2 vertices.
- Let T(N) is the time required to find the convex hull of N points.
- T(N)  2T(N/2) + U(N) total time    subproblem time    merge time
- If U(N)  O(N), then T(N)  O(N log N) (by recurrence relation),
- so we seek an O(N) merge algorithm, i.e., an O(N) convex polygon union algorithm.

![Figure from slide 238](images/slide_238.png)

### Slide 239: Merge algorithm, 1

- This procedure finds the convex hull of the union of two convex polygons P1 and P2.
- 1. Find a point p that is internal to P1 (e.g. centroid).
- Note that this point p will be internal to H(P1  P2).
- 2. Determine whether or not p is internal to P2.
- This can be done in O(N) time (convex polygon inclusion).
- If p is not internal to P2, go to step 4.
- 3. Point p is internal to P2.  The vertices of both P1 and P2
- occur in sorted angular order about p.
- Merge the lists of vertices in O(N) time to obtain a sorted list of the vertices of both P1 and P2.
- Go to step 5.
- P1
- P2

![Figure from slide 239](images/slide_239.png)

### Slide 240: Merge algorithm, 2

- 4. Point p is not internal to P2.  Relative to p, polygon P2 lies in a wedge whose apex angle is ≤π.
- The wedge is delimited by two vertices of P2, call them u and v,
- which can be found in O(N) time by a single pass around P2.
- Vertices u and v partition P2 into two chains of vertices that are monotonic in polar angle w.r.t. p,
- with one chain increasing and the other decreasing.
- The chain convex towards p can be discarded, because its vertices will be internal to H(S1 ∪S2).
- The other chain of P2 and all of P1 constitute two lists of at most
- O(N) total vertices that occur in sorted angular order around p.
- This can be merged in O(N) time to form a list of vertices of
- P1 ∪P2, sorted about p.
- P1
- P2 u v

![Figure from slide 240](images/slide_240.png)

### Slide 241: Merge algorithm, 3

- 5. Use the Graham scan on the sorted list to construct the convex hull of the vertices on the list, which requires O(N) time.
- If polygon P1 has m vertices and polygon P2 has n vertices, this algorithm constructs H(P1 ∪P2) ∈O(m + n)∈O(N) time.
- As mentioned, an O(N) merge gives an O(N log N) divide-and-conquer algorithm for convex hull.

![Figure from slide 241](images/slide_241.png)

### Slide 242: Supporting lines, 1

- A by-product of the convex hull union algorithm is a method of determining supporting lines of two convex hulls.
- A supporting line of a convex polygon P is a straight line L
- passing through a vertex of P such that the interior of P lies entirely to one side of L.
- The idea is analogous to the notion of tangent for circles.
- L
- P

![Figure from slide 242](images/slide_242.png)

### Slide 243: Supporting lines, 2

- Two convex polygons P1 and P2, with n and m vertices, such that one is not entirely contained within the other,
- have common supporting lines.
- The number of common supporting lines is ≥2 and ≤2*min(n,m).
- (Maximum is achieved when convex polygons are partially overlapping.)
- P1
- P2

![Figure from slide 243](images/slide_243.png)

### Slide 244: Supporting lines, 3

- Once the convex hull of the union of P1 and P2 has been constructed, common supporting lines can be found.
- Scan the vertex list of H(P1 ∪P2); any pair of consecutive vertices where one originated in P1
- and the other in P2 defines a common supporting line.

![Figure from slide 244](images/slide_244.png)

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
