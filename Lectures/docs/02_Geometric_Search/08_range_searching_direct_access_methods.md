# Range Searching by Direct Access Methods

**Slides covered:** 161-173  

**Topic folder:** 02 Geometric Search

## Motivation

Direct access methods trade a lot of preprocessing and storage for very fast queries. The single-stage version is simple but expensive in space; the multistage version reduces that space.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 161: p10 p11 ly ry

- Concept
- Points of S partition plane into (N + 1)2 cells.
- Given range R = [lx, rx] × [ly, ry], points (lx, ly) and (rx, ry) each lie in
- a particular cell.  Moving one of those points within a cell does not
- change the answer (the subset of S within R).  Thus a pair of cells
- forms an equivalence class of ranges.
- ⇒The number of distinct ranges is bounded above by
- N + 1   2  ∈O(N4).
- rx lx
- (     )

![Figure from slide 161](images/slide_161.png)

### Slide 162: Preprocessing

- Compute and save answer for each of O(N4) different pairs of cells.
- Query
- 1.  Given R = [lx, rx] × [ly, ry], map points (lx, ly) and (rx, ry) to cells.
- 2.  Access and report answer stored for the pair of cells.
- Analysis
- Preprocessing:  O(N5); O(N4) cells, O(N) linear processing for each.
- Query: O(log N + K); O(log N) to find cells for range corners
- Query:  O(log N + K); O(log N) to find cells for range corners.
- Storage:  O(N5); O(N4) cells, O(N) elements for each cell.
- An interesting idea, but too much storage.

### Slide 163: Normalization of coordinates

- It will be useful to have available normalized coordinates for both
- ranges and points.  For points ∈ S, normalized x coordinate is
- in [1, N], assigned in order of increasing x coordinate.
- For range R = [lx, rx] × [ly, ry], normalized range is obtained by
- mapping range extents to normalized coordinates for points.  Range
- normalized x coordinates are in [1, N + 1].  For example, if xi-1 ≤lx ≤ xi, lx normalized is i.
- x points ∈ S normalized coordinates
- {
- N + 1
- . . .
- p1 p2 p3 pN
- Normalization usually implies an O(N log N) sort in preprocessing
- and O(log N) normalization search in query.

### Slide 164: Concept

- One-dimensional binary search is optimal in storage θ(N) and
- time O(log N + K).  Combine direct access on one coordinate (x)
- with one-dimensional binary search on the other (y).
- Combination is single stage direct access.
- Given range R = [lx, rx] × [ly, ry], normalize [lx, rx] to (i, j);
- normalized range will have 1 ≤i ≤j ≤N + 1.
- Use x-range (i, j) to access entry in direct access array.
- Each array entry points to a binary search tree which holds points
- of S with normalized coordinates in [i, j], stored in ascending
- y order.  Leaves are threaded to allow traversal in ascending y order.
- O t f h ibl (i j)
- One tree for each possible (i, j).
- Direct access finds points in [lx, rx].
- Tree search finds points in [ly, ry].

### Slide 165: p10 p11 x-range y-range p4 p8 p3 p2 p7 p5 p6

- 2, 9
- 2, 8
- 2, 7
- . . .
- x-range array
- Pointer to binary search tree for y-range

![Figure from slide 165](images/slide_165.png)

### Slide 166: Direct access method (single stage)

### Slide 167: Preprocessing

- For each pair of normalized x coordinates (i, j), build a threaded
- binary tree storing the subset of S with normalized x coordinates
- in the interval [i, j] in ascending y coordinate order.
- Query
- 1. Normalize x-range of R = [lx, rx] × [ly, ry].  O(log N)
- 2. Access x-range array to get tree pointer.  O(1)
- 3. Search tree for y ≥ ly.  O(log N)
- 4. Report points within y-range by following threads in tree
- until y ≥ ry.  O(K)
- Analysis
- Preprocessing:  O(N3 log N); O(N2) trees, O(N log N) each.
- Query:  O(log N + K).
- Storage:  O(N3); O(N2) trees, O(N) each.

### Slide 168: Concept

- We would like to improve the O(N3) storage of single stage direct
- access method.  Instead of precomputing answers for all possible
- x-ranges, do so for a smaller set of fixed x-ranges.  For a query
- x-range, find a set of the fixed ranges that cover it, and combine
- their precomputed answers.
- N + 1
- . . .
- division gauge
- Point set S x-ranges
- “coarse” gauge
- N + 1 division gauge
- . . .
- Coarse interval
- Fine interval 2
- Fine interval 1
- Query x-range
- Point set S x-ranges
- “fine” gauges

### Slide 169: Data structure

- Multiple direct access arrays, one for each gauge
- ⇒1 array for coarse level, multiple at fine level.
- Each array contains an entry for each possible interval in that gauge.
- As in the single stage version, each entry is a pointer to a threaded
- binary tree containing the points of S located within the x-range of
- the interval, stored in ascending y order.
- Preprocessing
- For each level (coarse and fine) for each gauge at the level
- f h ibl i t l i th for each possible interval in the gauge build a threaded binary tree.
- Query
- 1. Normalize query x-range.  O(log N)
- 2. Determine intervals that compose the query x-range.  O(1)
- 3. For each interval
- 3.1 Access the appropriate direct access array to get the tree pointer.  O(1)
- 3.2 Search tree for point with y ≥left end of y-range.  O(log N)
- 3.3 Follow threads reporting points until point with y ≥right end of y-range.  O(K)

### Slide 170: Query (Explanation)

- • Find the beginning and end of the query x-range. This will
- correspond to three intervals: one in the coarse gauge and two in the fine gauges (O log (N)).
- • There is a direct access array for the coarse division, whose
- elements are pointing to the threaded binary trees for each possible coarse x-range.
- • After we identify the query x-range with two normalization
- (binary searches), go to the direct access array for the coarse subdivision and follow the array element to access
- the corresponding binary search tree for the coarse subdivision part of the query x-range. Find the beginning
- of the y-range in this tree and follow the threads to report
- the points in the r-range (O log (N)+K).
- • There are direct access arrays for each subdivision of the
- coarse gauge with a threaded binary tree for each possible range in the fine division. Go to the direct access arrays for
- the beginning and ending parts of the query x-range in the fine subdivision and follow the array elements to access
- the corresponding binary search trees for these parts in the
- fine subdivision. Find the beginning of the y-ranges in these two binary search trees and follow the threads to
- report the points in the y-range (O log (N)+K).

### Slide 171: Direct access method (multistage)

![Figure from slide 171](images/slide_171.png)

### Slide 172: Example (storage and query cost):

- N = 100,  = 0.5, coarse gauge contains N 0.5 =10 divisions.  N
- (100) possible coarse-gauge intervals. N (100) binary trees each with N (100) points. The total storage cost is 100 x 100 =
- 10,000 (O(N 2)).
- Each fine gauge contains N 1-0.5 = N 0.5 = 10 divisions. There are
- N 0.5 = 10 such structures. Each fine division contains 10 points
- and the storage cost of the binary search trees of a single structure in the fine division is N 0.5 x 2 =100. For a total storage
- of N 0.5 x N 0.5 x 2 x N 0.5 = 10,000 points. Total storage cost for
- both divisions is O(N 2). Query cost is O(log (N )+K) with the
- search cost three times the search cost of the single stage direct access method.

![Figure from slide 172](images/slide_172.png)

### Slide 173: Analysis

- Preprocessing:  O(N2 log N); O(N) trees, O(N log N) each.
- Query:  O(log N + K); see comments.
- Storage: O(N2); see below.
- Storage analyis details
- Level
- Coarse
- Fine
- Gauges per level
- Nα
- Divisions per gauge
- Nα
- N1−α
- Possible intervals per gauge
- (Nα)2 = N2α
- (N1−α)2 = N2−2α
- Points per tree
- O(N)
- O(N1−α)

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
