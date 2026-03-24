# Graham’s Scan

**Slides covered:** 206-219  

**Topic folder:** 03 Convex Hulls

## Motivation

Graham’s scan sorts points around a reference point and then removes right turns while scanning. It is one of the classic optimal planar convex hull algorithms.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 206: Concept

- A point within a triangle of S cannot be a vertex of the convex hull.
- Previous algorithm determined if a point p was within a triangle of S
- by trying (as many as) all of the triangles for each point p.
- Can we find out if p is within a triangle of S more efficiently?
- Graham’s scan does so.  This algorithm is from one of the first
- papers specifically concerned with finding an efficient geometric
- algorithm (1972).
- The essential idea:  if a point p is not a vertex of the convex hull,
- then it is internal to some triangle Op1p2, where O is an internal point and p1 and p2 are hull vertices.
- But if we are trying to find the hull vertices, where do p1 and p2 come from?
- We shall see.
- The algorithm consists of preparation and scan.
- Single shot algorithm (there is only one H(S) for a given S).

### Slide 207: Centroid

- The centroid of a finite set of points p1, p2, …, pN is their
- arithmetic mean (p1 + p2 + … + pN) / N.
- (Computed for each coordinate separately.)
- Lexicographic sort
- Sorting on multiple keys associated with objects to be sorted.
- Compare objects to be sorted on first key; and sort accordingly.
- If first keys are equal, sort on second key.
- If second keys are equal, … farther faster fastest father p1 = (-3,-1)
- p2 = (-2,1.5) p2 = (2,1) c = (-1,0.5)

### Slide 208: Polar angles

- The polar angle of a point p is the angle from the x axis through the origin to the point, ascending counterclockwise.

![Figure from slide 208](images/slide_208.png)

### Slide 209: Comparing polar angles

- Given two points p1 and p2 in the plane, which has the greater
- polar angle?  p2 forms a strictly small polar angle with the x axis
- than p1 iff triangle 0p2p1 has a positive signed area.
- Area(triangle 0p2p1) = (x0 y1 + x2 y0 + x1 y2 - x2 y1 - x0 y2 - x1 y0) / 2
- (See earlier slides on left-turn/right turn classification.)
- Equivalently, ... iff 0p2p1 is a left turn.
- Note that this means polar angles can be compared without actually computing them (the latter requires trig functions).

![Figure from slide 209](images/slide_209.png)

### Slide 210: Preparation

- The preparation for Graham’s scan is as follows:
- 1. Find a point O internal to H(S) (the centroid of S).  O(N)
- 2.  Transform the coordinates of the points in S so that
- O is the origin.  O(N)
- 2. Sort the N points of S lexicographically on
- (1)  polar angle and (2)  distance from O.  O(N log N)
- 3. Arrange the sorted points in a doubly-linked circular list. O(N)
- O

![Figure from slide 210](images/slide_210.png)

### Slide 211: Basic idea of the scan

- Recall that if a point p is not a vertex of the convex hull,
- then it is internal to some triangle Op1p2.
- The scan examines the points in sorted order (polar angle, distance from O), eliminating those not in the convex hull.
- Point p2 ∉H(S) and is eliminated when angle p1p2p3 is found to be reflex.
- Equivalently, eliminate p2 from H(S) iff p1p2p3 is not a left turn.
- O
- Point p2 is within triangle Op1p3 and is eliminated.

![Figure from slide 211](images/slide_211.png)

### Slide 212: Scan algorithm (informal)

- The scan begins at the rightmost smallest ordinate
- (minimum y coordinate) point; call it START.
- START is certainly a hull vertex (minimum y coordinate).
- Repeatedly examine consecutive triples of points p1p2p3.
- If p1p2p3 is a right turn, eliminate p2 from H(S) and backtrack to p0p1p3.
- If p1p2p3 is a left turn, advance to p2p3p4.
- What about p1p2p3 collinear?  Eliminate, p2 ∉H(S).
- O p0 p4
- Scan ends when it advances to start (i.e., p4 = START).
- START will never be eliminated because START ∈H(S).
- Backtracking will not go back beyond predecessor of START.

![Figure from slide 212](images/slide_212.png)

### Slide 213: Advancing and backtracking

- Backtracking may occur more than once in succession, eliminating a sequence of points.
- Backtracking sure to stop at START.
- No point can be eliminated more than once.
- O

![Figure from slide 213](images/slide_213.png)

### Slide 214: Algorithm

- (See Preparata, p. 108.)
- 1. Find an internal point O.
- 2. Using O as the coordinate origin, sort the N points of S lexicographically by polar angle and distance from O.
- Arrange the points into a doubly-linked circular list, with pointers NEXT and PRED for each entry,
- and with pointer START pointing to the starting point.
- 3.  Scan:
- begin v = START w = PRED[v]  /* w saves point just before START */
- f = FALSE  /* f indicates scan has returned to START */ while (NEXT[v] ≠START or f = FALSE)
- if
- (NEXT[v] = w) then f = TRUE endif if
- (Left(v, NEXT[v], NEXT[NEXT[v]])) then v = NEXT[v]  /* advance */
- else delete NEXT[v]  /* eliminate; list operation, O(1) */ v = PRED[v]  /* backtrack */
- endif endwhile
- 16 end

### Slide 215: Analysis

- Time:  O(N log N); see comments.
- Storage:  O(N) for circular linked list of points.
- Comments
- Preparation:
- Dominated by O(N log N) time required for sort.
- Scan:
- Left test requires O(1) time.
- After each test, either advance or backtrack.
- The scan will advance at most O(N) times, and will backtrack at most O(N) times.
- ⇒The entire scan requires O(N) time.

### Slide 216: Lower and upper hulls

- We introduce the notions of upper and lower hulls, which will be useful later, here in the context of Graham’s scan.
- Rather than comparing polar angles, x-coordinate values will be
- compared.
- Given set S of N points in the plane, find the points with minimum
- and maximum x coordinates (abscissa).
- Call those points l and r, and construct the line L through l and r.
- L partitions the remaining points S into two subsets, upper and lower,
- each of which include l and r.
- The lower (respectively, upper) subset will induce a polygonal
- chain monotone w.r.t. the x axis, called the lower (upper) hull.
- The concatenation of the two chains is the convex hull H(S).
- L
- Lower subset l r
- Upper subset

![Figure from slide 216](images/slide_216.png)

### Slide 217: Constructing the upper hull

- Sort the points of the upper subset of S on decreasing x coordinate.
- (Note error, text p. 109 says “increasing”.)
- Apply Graham’s scan from r to l.
- Specialization of the original method, where the reference point
- (called by O and q in the text) is at (0, -∞), so decreasing x coordinate is same as increasing polar angle.
- L l r
- Upper subset
- O

![Figure from slide 217](images/slide_217.png)

### Slide 218: Constructing the lower hull

- Sort the points of the lower subset of S on increasing x coordinate.
- Apply Graham’s scan from l to r.
- L
- Lower subset l r
- O

![Figure from slide 218](images/slide_218.png)

### Slide 219: Summary

- We have achieved best possible time for problem, O(N log N).
- But we will continue to examine additional algorithms.  Why?
- 1. The algorithm is optimal in the worst case, but we have not analyzed its expected case performance.
- 2. It does not generalize to d > 2.
- (Note that our lower bound proof also only applies to d = 2.)
- 3. The algorithm is static, in that all points must be given
- before the hull is constructed.
- 4. For a parallel environment, a recursive algorithm where the data is split into small subproblems
- (which this is not) might be preferable.
- 5. For other interesting insights and methods.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
