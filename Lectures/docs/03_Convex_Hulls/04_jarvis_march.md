# Jarvis’ March

**Slides covered:** 220-224  

**Topic folder:** 03 Convex Hulls

## Motivation

Jarvis’ march, also called gift wrapping in 2D, walks from one hull vertex to the next by always choosing the most counterclockwise candidate. It is output-sensitive because its time depends on the number of hull vertices.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 220: Concept

- Graham’s scan found the vertices of H(S).
- Given a point p ∈ S, the algorithm would determine whether p ∈ H(S), with some possible backtracking.
- Conceptually, Jarvis’ march instead finds the edges of H(S).
- Given two points p and q, it is possible to determine if segment pq is an edge of H(S).
- Theorem.  The line segment l defined by two points is an edge
- of the convex hull iff all other points of the set lie on the line defined by l or to one side of it.
- (Note, text omits “the line defined by”.
- p q q′ p′
- Segment pq is an edge of H(S).
- Segment p′q′ is not an edge of H(S).

![Figure from slide 220](images/slide_220.png)

### Slide 221: Naïve approach

- There are O(N2) lines determined by all pairs of points.
- For each of those lines, it is possible to test all the remaining
- N - 2  points (Point-line classification) and determine if the line meets the criteria of the theorem as an edge of H(S).
- This simple process requires O(N3) time to find the edges of H(S).
- The edges must then be arranged in order in O(N) time.
- Improving on the naïve approach
- To improve on this, observe that once it is established that
- some segment pq is a edge of H(S), then another edge must exist with q as an endpoint.
- This fact can be used to reduce the time required to O(N2).

![Figure from slide 221](images/slide_221.png)

### Slide 222: Marching (up)

- Assume that the rightmost smallest ordinate point p1 has been found.
- Point p1 is certainly ∈H(S).
- We wish to find the next vertex on H(S), call it p2.
- Point p2 is the point ∈S with the smallest polar angle ≤0 w.r.t. p1.
- Likewise, the next point p3 has the smallest polar angle ≤0 w.r.t. p2.
- Each successive vertex of H(S) can be found in linear time O(N)
- by checking each p ∈S to find the point with the least polar angle.
- In this manner, H(S) can be constructed from the lowest point
- to the highest point (p1 to p4 in the example).
- We are finding edges by looking for the other endpoint.
- Note errors in test in Figure 3.9, p. 111.

![Figure from slide 222](images/slide_222.png)

### Slide 223: Marching (down)

- When marching down, the least polar angle is found w.r.t. to the point as usual, but relative to the negative x axis,
- because relative to the x axis will give erroneous results.

![Figure from slide 223](images/slide_223.png)

### Slide 224: Analysis

- Time: O(N2); O(N) points in hull, N comparisons at each to find least polar angle.
- Storage:  O(N); for the points.
- However, only the vertices of the hull H(S) are actually processed
- (that is, if there are actually h points on the hull, hN left/right
- comparisons are necessary) to find the next vertex.
- Let h be |H(S)|; of course h ∈O(N), but often h << N.
- Expected time for Jarvis’ march algorithm is O(hN), which compares favorably with Graham’s scan O(N log N)
- when h < log N.
- Furthermore, when we know the hull H(S) has C sides, C a constant,
- then the expected time is linear O(N).
- Jarvis’ march concluding comments
- Finding the hull vertices by repeatedly turning angles has the
- feeling of “wrapping” the set S.
- We will generalize this approach for d > 2 later, in the “gift wrapping” algorithm.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
