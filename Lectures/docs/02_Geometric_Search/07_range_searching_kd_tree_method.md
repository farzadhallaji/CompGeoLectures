# Range Searching by the k-D Tree Method

**Slides covered:** 152-160  

**Topic folder:** 02 Geometric Search

## Motivation

The k-D tree splits by the data, not by a fixed grid. In 2D it alternates x-splits and y-splits, giving a binary search tree for multidimensional point searching.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 152: Grid and Quadtree methods subdivide plane based on space, not

- data set, leading to poor worst case performance.  Following
- methods subdivide plane based on points in data set.
- A k-dimensional binary tree (k-D tree) recursively subdivides the
- plane into half-planes, in alternating orthogonal directions, at lines
- determined by the points of S.  Each subdivision results in approximately equal numbers of points on either side of the
- bisecting line, allowing bisecting (binary) search.
- .
- Th t i l t d i th l ill b t t ll
- The material presented in the class will be totally based on Chapter 5 ( Orthogonal Range Searching)
- from Berg-Kreveld-Overmars-Schwarzkopf, pp. 93-117).
- Some of the older slides will still be used but a set of new slides based on this chapter will be presented here
- without having PowerPoint slides on this web pages.

### Slide 153: with the given set of points S (pre-processing step).

- A node v in the tree is associated with a point P(v) of S and a
- line l(v) [ parallel to x- or y-axis] is assumed to pass through it.
- A rectangle R(v) is associated with v. The line l(v) divides R(v)
- into two regions R1 and R2.
- D
- D v
- D
- Search  continues in region
- R2 since R2 covers D∩R(v).
- D may or may not contain P(v).
- Search must continue in both R1 and R2.
- R(v)
- R(v) v v l(v) l(v)
- R1
- D is the search range rectangle

![Figure from slide 153](images/slide_153.png)

### Slide 154: P(v)=p6 t(v)=vert

- M(v)=x6
- P(v)=p10 t(v)=horz
- M(v)=y10
- P(v)=p3 t(v)=horz
- M(v)=y3
- P(v)=p2 t(v)=vert
- M(v)=x2
- P(v)=p9 t(v)=vert
- M(v)=x9
- P(v)=p7 t(v)=vert
- M(v)=x7
- P(v)=p1 t(v)=vert
- M(v)=x1
- P(v)=p11 t(v)=horz
- M(v)=y11
- P(v)=p8 t(v)=horz
- M(v)=y8
- P(v)=p4 t(v)=horz

![Figure from slide 154](images/slide_154.png)

### Slide 155: Data associated with each node v of k-D tree:

- Explicit
- P(v) Point through which plane is bisected.
- t(v)
- Direction of bisection, t(v) ∈{horz, vert}.
- M(v) x (or y) value of bisecting line.
- Implicit
- R(v) Rectangle (half-plane) on P(v)’s side of the bisecting line associated with Parent(v).
- S(v)
- Subset of S within R(v).
- The implicit data R(v) and S(v) are not represented in the tree, but
- can be inferred from other data in the tree.
- Th k D t i b ilt b th ll
- The k-D tree is built by the call:
- T = CreatekDNode(S,vert)
- /* T is k-D tree, S is point data set, vert is bisection direction. */

### Slide 156: begin if

- S = ∅then return NULL  /* Leaf nodes are NULL pointers. */ endif
- Allocate new node v if t = vert then
- Find pi ∈S ∋xi is median for all x ∈S
- M(v) = xi /* x coordinate of bisecting line */
- SL = {pj ∈S - {pi} xj < xi}
- SR = {pj ∈S - {pi} xj ≥ xi}  /* i.e. SR = (S - {pi}) - SL */
- t h t = horz else  /* t = horz */
- Find pi ∈S ∋yi is median for all y ∈S.
- M(v) = yi /* y coordinate of bisecting line */
- SL = {pj ∈S - {pi} yj < yi}
- SR = {pj ∈S - {pi} yj ≥ yi}  /* i.e. SR = (S - {pi}) - SL */
- t = vert endif
- P(v) = pi t(v) = t
- Lchild(v) = CreatekDNode(SL,t)
- Rchild(v) = CreatekDNode(SR,t) return v end

### Slide 157: as follows:

- 1. Using O(nlogn) time sort the points along  x- and y-axis.
- For our example, this will produce two lists:
- L1= (1,2,3,4,5,6,7,8,9,10,11)
- L2= (5,7,2,8,10,3,4,1,11,9,6)
- 2. Pick the median element point 6 to be the root vertex v. This takes
- O(1) time.
- 3.Search L2 with x-coordinate value of point 6..say xm,from left to right.
- If the x-coordinate of the element is less than  xm then put the element
- i li t L3 th i t i li t L4 Thi t t k
- O( ) ti in list L3; otherwise put in list L4. This step takes O(n) time.
- For our example, the new lists are L3 and L4:
- L3= (5,2,3,4,1)    and L4 = (7,8,10,11,9)
- 4. Recurse the process until a single element node is reached.
- For example, pick 3 and 10 for the sublists etc.
- So, this is classic divide and conquer strategy
- T(n) <=  2T(n/2)  +  O(n)
- T(n)= O(n logn)

### Slide 158: Query range

- P(v)=p6 t(v)=vert
- M(v)=x6
- P(v)=p10 t(v)=horz
- M(v)=y10
- P(v)=p3 t(v)=horz
- M(v)=y3
- P(v)=p2 t(v)=vert
- M(v)=x2
- P(v)=p9 t(v)=vert
- M(v)=x9
- P(v)=p7 t(v)=vert
- M(v)=x7
- P(v)=p1 t(v)=vert
- M(v)=x1
- P(v)=p11 t(v)=horz
- M(v)=y11
- P(v)=p8 t(v)=horz
- M(v)=y8

![Figure from slide 158](images/slide_158.png)

### Slide 159: SearchkDTree(root(T),R)

- /* T is k-D tree. */
- /* R = [lx, rx] × [ly, ry] is search range. */ procedure SearchkDTree(v,R)  /* v is a tree node, R is range. */
- begin if
- (v ≠NULL) then if
- (t(v) = vert) then
- [l, r] = [lx, rx] else
- [l, r] = [ly, ry] dif endif if
- (l ≤M(v) ≤r and P(v) ∈R) then report P(v) endif if
- (l < M(v)) then
- SearchkDTree(Lchild(v),R) endif if
- (M(v) < r) then
- SearchkDTree(Rchild(v),R) endif endif end

### Slide 160: Analysis

- Very complex; algorithm appeared in 1975, analysis not until 1977.  See Preparata pp. 77-79 or Laszlo p. 248 for details.
- Preprocessing:  θ(dN log N); d is number of dimensions.
- Both presort (for median finding) and recurrence for algorithm
- recursion are O(N log N).
- Query:  O(dN1-1/d + K); e.g. for d = 2, O(√N + K).
- Storage:  O(dN).

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
