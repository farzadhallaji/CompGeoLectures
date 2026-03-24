# Range Searching Overview and the Grid Method

**Slides covered:** 135-141  

**Topic folder:** 02 Geometric Search

## Motivation

Range searching asks which points lie inside a query rectangle. The grid method is the first space decomposition idea: divide space into cells, preprocess counts or lists, then answer queries from those cells.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 135: Range searching example

- Given N points in the plane, how many lie in a given rectangle with
- sides parallel to the coordinate axes?  That is, how many points
- (x, y) satisfy lx ≤x ≤rx, ly ≤y ≤ry, for given lx, rx, ly, ry?
- ry lx rx ly
- Answer:  6

![Figure from slide 135](images/slide_135.png)

### Slide 136: General range searching problem

- Given a data set of N objects, each consisting of an ordered d-tuple
- of values (x1, x2, ..., xd), and a query domain consisting of d ranges
- [li, ri] for 1 ≤i ≤d, count or report the objects whose values are
- within the query domain (i.e., where li ≤xi ≤ri for 1 ≤i ≤d).
- The domain is itself often called the query range, hence the term
- range searching.
- It is natural to view the d-tuples as points in d-dimensional
- Cartesian space (d-space) and the range as a region in that space.
- For example, in 2-space the objects and the range are points and
- t l ti l a rectangle, respectively.

### Slide 137: pi = (xi, yi) for 1 ≤i ≤N, and rectangular range R = [lx, rx] × [ly, ry],

- also in the plane.
- QUESTION:  Report the points of S located within R, i.e. points pi ∈S where lx ≤xi ≤rx and ly ≤yi ≤ry.
- Range searching assumptions
- Unless otherwise noted, we will assume the following for all
- range searching problems and algorithms.
- 1. Two dimensional, all points and range within plane.
- 2 All i t d i iti d t
- Geometric Search, Range Searching
- Introduction to range searching
- 2. All points and range in positive quadrant.
- 3. Repetitive mode (single data set, multiple queries).
- 4. Static data set S (no changes to S after preprocessing).
- 5. Reporting (points in R must be identified).

### Slide 138: Concept p1 p5 p2 p3 p7 p6 p4 p8 p9 p12 p11 p10 y x

- Point data set S = {p1, p2, ..., pN}, pi = (xi, yi)
- Subdivision of plane into m × m grid (m is grid parameter)

### Slide 139: Preprocessing procedure ConstructGrid begin

- Initialize m × m array of lists g to NULL.
- for i = 1 to N add pi to list g[xi /size(m)][yi /size(m)]
- end
- Quantity size(m) is the coordinate distance represented by one grid interval.
- m × m array of pointers to lists p1 p2 p5 p3 p7 p4 p10 p6 p8
- Lists associated with grid cells
- Points on cell edges are placed in cell to right or above.
- All three points are in the cell shown.

![Figure from slide 139](images/slide_139.png)

### Slide 140: Query procedure QueryGrid begin for i = lx/size(m) to rx/size(m) 

- for j = ly/size(m) to ry/size(m)  for each point pk on list g[i][j]
- if lx ≤xk ≤rx and ly ≤yk ≤ry report pk endif endfor endfor endfor
- d end

### Slide 141: Analysis

- Preprocessing:  O(m2 + N).
- Query: O(m2 + N).
- Storage: O(m2 + N).
- Analysis comments
- Query not O(m2N) because each point only checked once.
- Not O(m2 + K) because some points are checked that are not reported. O(m2 + K) is better than O(m2 + N) and the former
- is allowed only when only points to be reported are checked.
- Al ith ti d t d d t id t
- Algorithm time and storage are dependent on grid parameter m.
- m too large ⇒small cells, many empty.
- m too small ⇒large cells, many containing numerous points.
- Degenerate case, m = 1, equivalent to linear scan of data set.
- Best value for m depends on application.
- This method is substantially suboptimal in worst-case analysis.
- However, in practice runs in O(K) time in average case, if points are uniformly distributed.  See Laszlo, p. 231.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
