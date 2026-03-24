# Range Searching by the Quadtree Method

**Slides covered:** 142-151  

**Topic folder:** 02 Geometric Search

## Motivation

Quadtrees recursively split the plane into four equal parts. They adapt space decomposition through recursion and are useful when point distribution is uneven.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 142: Definitions

- A quadtree subdivision is a recursive subdivision of the plane into
- four equal sized quadrants.  A quad is a quadrant or subquadrant
- at any level of the subdivision, including the plane itself.
- Each quad is represented by a node in a four-way branching tree
- called a quadtree.  (The root represents the plane.)  Each node of
- a quadtree has either 0 or 4 children, depending on whether the
- corresponding quad is subdivided.  Each non-root node represents
- one subquadrant of its parent’s quad.
- Subdivision of a quad recurses until:
- Th d t i
- ≤M i t f S i t
- M i th ll
- 1. The quad contains ≤M points of S; integer M is the cell occupancy target.
- 2. The node corresponding to the quad is at depth D in the quadtree; integer D is the cutoff depth.
- M and D are the quadtree construction parameters.
- Attached to each leaf node in the quadtree is a list of the points
- located in the corresponding quad.

### Slide 143: Point data set S.

- Quadtree subdivision for S with M = 2 and
- D = 3.
- Quad where D = 3 cut off further subdivision.

![Figure from slide 143](images/slide_143.png)

### Slide 144: Quadtree subdivision for S with M = 2 and

- D = 3.
- Quad where D = 3 cut off further subdivision.
- Corresponding quadtree.
- Branch numbering convention
- Attached point list (showing number of points)
- Level 2
- Level 1
- Level 0
- Level 3

![Figure from slide 144](images/slide_144.png)

### Slide 145: Construction

- A quadtree is built over a square subset of the plane, or domain,
- defined to include all points of S; domain = [Lx, Rx] × [Ly, Ry].
- Domain subdivided into a regular m × m grid of square cells,
- each containing a list of points of S located in that cell; m = 2D + 1.
- Conceptually, the overall quadtree is built bottom-up from the grid.
- Associate with each cell a one-node quadtree, at level D + 1.
- To construct a quadtree with root at level λ, the four quadtrees at
- level λ + 1 that represent its subquadrants are “combined”.
- To “combine” quadtrees q0, q1, q2, q3 at level λ + 1:
- if t th t i ≤M i t λ + 1 > D th if q0, q1, q2, q3 together contain ≤M points or λ + 1 > D then
- merge q0, q1, q2, q3 into a new single node at level λ else link q0, q1, q2, q3 as children of a new node at level λ
- Notation
- M
- Cell occupancy target m
- Grid parameter for smallest quads, m = 2D + 1
- D
- Cutoff (maximum) quadtree depth d
- Dimensions (2 in this case)

### Slide 146: Level 4.

- Level 3.

### Slide 147: Level 2.

- Levels 1 and 0.

### Slide 148: Preprocessing

- Quadtree node q q.points
- List of points of S within quad for this node; NULL if not leaf.
- q.child[4] Pointers to subtrees, NULL if leaf.
- q.size
- Number of points within quads represented by the subtree rooted at this node.
- q.quad
- Boundaries of the quad represented by this node; format [lx, rx] × [ly, ry].
- Q = ConstructQuadtree(G, M, D, 0, 0, m-1, 0,  m-1, domain) procedure ConstructQuadtree(G, M, D, level, imin, imax, jmin, jmax, quad)
- begin
- Allocate new quadtree node q.
- if imin = imax  /* Lowest level, single grid cell. */ q.points = G[imin][jmin].points  /* Node’s point list comes from grid cell. */
- q.child[0] = q.child[1] = q.child[2] = q.child[3] = NULL q.size =  G[imin][jmin]
- q.quad = quad else q points = NULL q.points = NULL imid = (imin + imax) / 2
- jmid = (jmin + jmax) / 2
- [lx, rx] × [ly, ry] = quad q.child[0] = ConstructQuadtree(G, M, D, level+1, imid+1, imax, jmid+1, jmax,
- [(lx+ rx ) / 2, rx] × [(ly+ ry ) / 2, ry]) q.child[1] = ConstructQuadtree(G, M, D, level+1, imid+1, imax, jmin, jmid,
- [(lx+ rx ) / 2, rx] × [(ly, (ly+ ry ) / 2]) q.child[2] = ConstructQuadtree(G, M, D, level+1, imin, imid, jmin, jmid,
- [(lx, (lx+ rx ) / 2]] × [(ly, (ly+ ry ) / 2]) q.child[3] = ConstructQuadtree(G, M, D, level+1, imin, imid, jmid+1, jmax,

### Slide 149: (l + r ) / 2 rx

- (lx + rx) / 2 lx
- Geometry of recursive calls in CreateQuadtree jmid jmin imid
- İmid+1 imax imin ly
- (ly + ry) / 2

![Figure from slide 149](images/slide_149.png)

### Slide 150: Query

- QueryQuadtree(root(Q),R)
- /* Q is quadtree, R = [lx, rx] × [ly, ry] is range. */ procedure QueryQuadtree(q, R)
- begin if
- (q.quad ∩R) then  /* Query range overlaps node’s quad. */ if
- (q.child[0] = NULL) then  /*Node q is a leaf. */ for each point pi on q.points  /* Scan the point list. */
- if
- (pi within R) then report pi endif df endfor else  /* Node q is not a leaf. */
- for i = 0 to 3
- QueryQuadtree(q.child[i],R)  /* Query subtrees. */ endfor endif
- endif end

### Slide 151: Analysis

- Preprocessing:  O(m2 + N); recall that m = 2D + 1.
- Query:  O(2D + N).
- Storage:  O(m2 + N).
- Analysis comments
- Note that ConstructQuadtree is O(m2), not O(m2 + N), because
- point lists rather than points are handled (appending 4 lists can be
- done in constant time).  However, constructing the grid G, input to
- ConstructQuadtree, is O(m2 + N).
- Th ti
- O(2D + N) i t
- The query time O(2D + N) is worst case.
- O(2D) is the largest number of nodes that might be visited; it is O(2D) instead of O(4D) based on an analysis of the types of
- possible range/quad intersections and a trick of storing points
- at non-leaf as well as leaf nodes (see Laszlo pp. 239-242).
- O(N) is the largest number of points that might be tested for
- inclusion in the range.
- Average case query performance can be much better, depending on
- point distribution.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
