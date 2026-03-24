# Complexity Basics and Segment Trees

**Slides covered:** 29-44  

**Topic folder:** 01 Foundations

## Motivation

This file explains how geometric algorithms are measured, what counting versus reporting means, and why preprocessing matters. It also introduces the segment tree, a basic data structure used later.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 29: RANGE SEARCHING

- Given N points in the plane, how many lie in a given rectangle with
- sides parallel to the coordinate axes?  That is, how many points
- (x, y) satisfy lx ≤x ≤rx, ly ≤y ≤ry, for given lx, rx, ly, ry?
- ry lx rx ly
- The range searching problem is (informally) defined above.
- In this example, the instance of the range searching problem is a
- particular set of points and a particular range.
- In an instance like this, the points are the data set.

![Figure from slide 29](images/slide_029.png)

### Slide 30: We are interested in efficient algorithms for geometric problems.

- Efficiency is evaluated in terms of computational cost, given as a function of the size of the instance of the problem.
- By convention, notation N denotes input instance size.
- To determine the computational cost of an algorithm, we must know what primitive operations are available and
- what they cost.  This is a model of computation.
- Turing machine:  too primitive
- C language on Unix workstation:  too specific
- We will use a highly abstract model, the familiar random-access
- machihine ne from from [A
- [Aho, ho,1974]
- 1974]. We us use a slight ghtly modi odifified d  realal RAM
- model.
- These operations are available at unit cost:
- 1. arithmetic; +, -, *, /
- 2. comparisons; <, ≤, =, ≠, ≥, >
- 3. memory access
- 4. analytic functions; root, trig, exp, log
- Numbers are assumed to be real, with infinite precision.
- This is considerably abstracted; in a real machine:

### Slide 31: Order notation

- We are interested in the amount of time and memory used by algorithms, as a function of the input instance size N.
- “Worst case” or Upper bound
- O(f(N)) denotes the set of all functions g(N) such that there exist
- positive constants C and N0 with g(N) ≤Cf(N) for all N ≥ N0.
- “Best case” or Lower Bound
- Ω(f(N)) denotes the set of all functions g(N) such that there exist
- positive constants C and N0 with g(N) ≥Cf(N) for all N ≥ N0.
- “Optimal case” Or Optimal Bound θ(f(N)) denotes the set of all functions g(N) such that there exist
- positive constants C1, C2, and N0 with
- C1f(N) ≤g(N) ≤ C2f(N) for all N ≥ N0.
- Notes:
- These notations denote sets:  f(N) ∈O(log N), not f(N) = O(log N).
- Larger terms dominate the order, e.g.,
- (4N + 20 log N + 100) ∈O(N)
- We will use the notation for both time and memory.
- Most of our attention will be towards “worst case”.

### Slide 32: SEGMENT INTERSECTION COUNTING

- INSTANCE:  Set S = {s1, s2, ..., sN} of line segments in the plane.
- QUESTION:  Count the number of intersections of segments in S.

![Figure from slide 32](images/slide_032.png)

### Slide 33: SEGMENT INTERSECTION COUNTING

- INSTANCE:  Set S = {s1, s2, ..., sN} of line segments in the plane.
- QUESTION:  Count the number of intersections of segments in S.
- procedure SegmentIntersectionCounting(S) begin count = 0 for i = 1 to N
- for j = 1 to N if  i ≠j and si ∩sj ≠∅ count = count + 1 dif endif
- endfor endfor print count
- 11 end
- Storage:  O(N), for set S
- Time:  O(N2), for nested loops
- Notice the assumed primitive operation:  segment intersection.
- What geometric operations are primitive?

### Slide 34: Preprocessing. Time spent organizing the data set, usually into

- some data structure.  Less important than query and storage.
- Query. Time spent producing the answer for a query relative to
- the data set.
- Storage. Memory required for static and dynamic data structures
- used by the query algorithm.
- Single shot vs. repetitive-mode
- Single shot.  Given a single data set and a single query, produce an
- answer one time.  Almost always best handled by scan of data
- set; no preprocessing, query O(N), storage O(N).
- Repetitive-mode. Given a single data set and a sequence of queries,
- produce the answer for each query relative to the data set.  Here, we
- are willing to spend time preprocessing to enable query time
- better than O(N).

### Slide 35: satisfy the query.

- Reporting. Report (list, identify) the objects that satisfy the
- query.
- For example, consider the standard range search problem:
- RANGE SEARCHING.
- INSTANCE:  Set S = {p1, p2, ..., pN}, pi = (xi, yi) of points in the
- plane, and rectangle R = [lx, rx] × [ly, ry] in the plane.
- Preliminaries p
- , g
- [ x, x]
- [ y, y] p
- QUESTION (counting):  How many points of S are within R?
- QUESTION (reporting):  Which points of S are within R?

### Slide 36: problems can have query time complexity that is output sensitive.

- Output-sensitive example
- INTERVAL ENCLOSURE
- INSTANCE:  Set S = {x1, x2, ..., xN} of points on the number line (x-axis), and an interval Q = [l, r].
- QUESTION: Which points of S are within Q, i.e. l ≤xi ≤ r?
- Naive repetitive mode algorithm and analysis.
- Preliminaries
- Preprocessing:
- 1. Sort S into an array A.  O(N log N)
- Query:
- 1. Binary search A for xi ≥l.  O(log N)
- 2. Binary search A for xj ≤ r.  O(log N)
- 3. Report points from xi to xj in A.  ?
- There can be O(N) points from l to r ⇒step 3 is O(N)
- ⇒query is O(N).
- Without reporting, query is O(log N), with reporting O(N).
- Time complexity of this type is usually written O(log N + K),
- where N is input size and K is output size.

### Slide 37: Pre-processing Cost: trade-off between space and time complexity with or without

- Pre-processing Cost: trade-off between space and time complexity with or without
- pre-processing.
- Amortized Cost: average  over expensive and inexpensive operations.
- Normalization
- It will sometimes be useful to have available normalized values for coordinates.  For a coordinate value x, its
- normalized x coordinate is in [1, N], assigned in order of increasing x coordinate, relative to the set from which
- the coordinates are/will be drawn.
- Normalization usually implies an O(N log N) sort in preprocessing and O(log N) normalization search in query.

### Slide 38: the real line whose extremes (endpoints) belong to a fixed set of

- N abscissae (x-values).  It is the set of x-values from which the
- endpoints are chosen that is fixed, not the intervals themselves.
- The tree structure in which the intervals are stored is defined for
- a scope interval [l, r].  For a given [l, r] there is exactly one
- segment tree structure. The data intervals are stored within the
- fixed tree.  We will assume WLOG that the data interval endpoints
- have been normalized to [1, N] and the tree has been built for
- scope interval [1, N].
- Preliminaries
- T(l, r) = Segment tree over scope interval [l, r].
- Each node v of T(l, r) is associated with a scope interval ⊆[l, r].
- A node v has these parameters:
- B(v)
- Beginning of scope interval associated with this node.
- E(v)
- End of scope interval associated with this node.
- Lchild(v)
- Left subtree = T(B(v), (B(v) + E(v)) / 2)

### Slide 39: [6,12]

- [3,6)
- [1,3)
- [6,9)
- [9,12]
- Example
- The structure of the segment tree T(1,12) is shown.
- Each node is labeled with its associated interval [B(v), E(v)).
- Preliminaries
- [1,2)
- [10,12]
- [6,7)
- [7,9)
- [9,10)
- [4,6)
- [3,4)
- [2,3)
- [5,6)
- [4,5)

![Figure from slide 39](images/slide_039.png)

### Slide 40: intervals with endpoints ∈{l, l + 1, l + 2, ..., r},  in

- O(log N) time per operation.
- For r - l > 3, an arbitrary interval [b, e] inserted into T(l, r) will
- be partitioned into and “allocated” as a collection of standard
- intervals of T(l, r).
- There will be at most ( log2(r – 1)+ log2(r – 1)- 2) ∈ O(log N)
- standard intervals in the partition.
- Preliminaries
- To insert interval [b, e] into segment tree T:
- InsertSegmentTree(b, e, root(T)) procedure InsertSegmentTree(b, e, v)
- begin if
- (b ≤B(v) and E(v) ≤e) then add [b, e] to A(v) else if (b < (B(v) + E(v)) / 2) then
- InsertSegmentTree(b, e, Lchild(v)) if ((B(v) + E(v)) / 2< e) then
- InsertSegmentTree(b, e, Rchild(v)) end end

### Slide 41: [1,12]

- [1,6)
- [6,12]
- [1,3)
- [6,9)
- [9,12]
- (B(v) + E(v)) / 2
- [3,6)
- Preliminaries
- [1,2)
- [10,12]
- [7,9)
- [9,10)
- [3,4)
- [4,6)
- [5,6)
- [4,5)
- [11,12]
- [10,11)

![Figure from slide 41](images/slide_041.png)

### Slide 42: Insertion

![Figure from slide 42](images/slide_042.png)

### Slide 43: Insertion

![Figure from slide 43](images/slide_043.png)

### Slide 44: To delete interval [b, e] from segment tree T:

- DeleteSegmentTree(b, e, root(T)) procedure DeleteSegmentTree(b, e, v)
- begin if
- (b ≤B(v) and E(v) ≤e) then remove [b, e] from A(v) else if (b < (B(v) + E(v)) / 2) then
- D l t S tT
- (b
- L hild( ))
- Preliminaries
- DeleteSegmentTree(b, e, Lchild(v)) if ((B(v) + E(v)) / 2< e) then
- DeleteSegmentTree(b, e, Rchild(v)) end end

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
