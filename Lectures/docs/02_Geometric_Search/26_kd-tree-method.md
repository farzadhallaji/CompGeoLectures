# k-d tree method

## Scope
- **Slides:** pp. 152-160
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 02.13 7.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
The k-d tree is the first range-search structure in this block that subdivides based on the data rather than the ambient space. That is why its worst-case story is better.

## What you must know cold
- Alternate vertical and horizontal splits.
- Choose splitting points/medians so subproblems are roughly balanced.
- Query recursively visits only subtrees whose regions intersect the search range.

## Core ideas and reasoning
- Each node stores a point and induces an axis-aligned region for its subtree.
- Balance comes from splitting by median coordinate, not by a fixed background grid.
- This is why the structure supports logarithmic-style search behavior in the balanced case.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 154
![Figure from slide p. 154](../images/geometric-search/26_kd-tree-method_p154.png)

### Figure from slide p. 158
![Figure from slide p. 158](../images/geometric-search/26_kd-tree-method_p158.png)

## Slide-by-slide digestion

### p. 152 - k-D tree method
- Concept
- Grid and Quadtree methods subdivide plane based on space, not
- data set, leading to poor worst case performance. Following
- methods subdivide plane based on points in data set.
- A k-dimensional binary tree (k-D tree) recursively subdivides the
- plane into half-planes, in alternating orthogonal directions, at lines
- determined by the points of S. Each subdivision results in
- approximately equal numbers of points on either side of the
- bisecting line, allowing bisecting (binary) search.
- Th

### p. 153 - A two-dimensional binary search tree is constructed associated
- with the given set of points S (pre-processing step).
- A node v in the tree is associated with a point P(v) of S and a
- line l(v) [ parallel to x- or y-axis] is assumed to pass through it.
- A rectangle R(v) is associated with v. The line l(v) divides R(v)
- into two regions R1 and R2.
- Search continues in region
- R2 since R2 covers D∩R(v).
- D may or may not contain P(v).
- Search must continue in both R1
- and R2.

### p. 154 - k-D tree method
- P(v)=p6
- t(v)=vert
- M(v)=x6
- P(v)=p10
- t(v)=horz
- M(v)=y10
- P(v)=p3
- M(v)=y3
- P(v)=p2
- M(v)=x2

### p. 155 - k-D tree method
- Preprocessing
- Data associated with each node v of k-D tree:
- Explicit
- P(v) Point through which plane is bisected.
- t(v)
- Direction of bisection, t(v) ∈{horz, vert}.
- M(v) x (or y) value of bisecting line.
- Implicit
- R(v) Rectangle (half-plane) on P(v)’s side of
- the bisecting line associated with Parent(v).

### p. 156 - k-D tree method
- Preprocessing

```text
procedure CreatekDNode(S,t) /* S is set of points, t is direction. */
begin
S = ∅then
return NULL /* Leaf nodes are NULL pointers. */
Allocate new node v
t = vert then
Find pi ∈S ∋xi is median for all x ∈S
M(v) = xi /* x coordinate of bisecting line */
SL = {pj ∈S - {pi} xj < xi}
```

### p. 157 - Analysis
- The preprocessing time is O(nlogn) for d=2. The argument goes
- as follows:
- 1. Using O(nlogn) time sort the points along x- and y-axis.
- For our example, this will produce two lists:
- L1= (1,2,3,4,5,6,7,8,9,10,11)
- L2= (5,7,2,8,10,3,4,1,11,9,6)
- 2. Pick the median element point 6 to be the root vertex v. This takes
- O(1) time.
- 3.Search L2 with x-coordinate value of point 6..say xm,from left to right.
- If the x-coordinate of the element is less than xm then put the element

### p. 158 - k-D tree method
- Query
- range
- P(v)=p6
- t(v)=vert
- M(v)=x6
- P(v)=p10
- t(v)=horz
- M(v)=y10
- P(v)=p3
- M(v)=y3

### p. 159 - k-D tree method
- Query
- SearchkDTree(root(T),R)

```text
/* T is k-D tree. */
/* R = [lx, rx] × [ly, ry] is search range. */
procedure SearchkDTree(v,R) /* v is a tree node, R is range. */
begin
(v ≠NULL) then
(t(v) = vert) then
[l, r] = [lx, rx]
[l, r] = [ly, ry]
```

### p. 160 - k-D tree method
- Analysis
- Very complex; algorithm appeared in 1975, analysis not
- until 1977. See Preparata pp. 77-79 or Laszlo p. 248 for details.
- Preprocessing: θ(dN log N); d is number of dimensions.
- Both presort (for median finding) and recurrence for algorithm
- recursion are O(N log N).
- Query: O(dN1-1/d + K); e.g. for d = 2, O(√N + K).
- Storage: O(dN).

## What you must be able to say or do in an exam
- State the input, output, preprocessing, and query/update model precisely.
- Explain the invariant or ordering that makes the method work.
- Trace the method by hand on a small example.
- Give the exact time and space bounds.
- Mention one edge case, degeneracy, or limitation.

## Complexity and performance facts
Balanced construction supports efficient range searching with query time depending on visited nodes plus reported points.

## Common mistakes and danger points
- The split direction alternates by level. The recordings mention a common coding/slide confusion exactly here.
- Do not describe it as a quadtree with two children. The construction principle is different.

## Exam-style drills and answer skeletons
### Core exam drill
**Question.** State the problem solved by k-d tree method, describe preprocessing/query/update steps if any, and give the time and space bounds.

**How to answer.** An excellent answer names the input, the output, the invariant or ordering exploited by the method, and the exact asymptotic costs.

### Hand-trace drill
**Question.** Trace k-d tree method on a small example by hand and explain each comparison or structural change.

**How to answer.** On this course, being able to run the method on a picture matters more than writing vague slogans.

## Recap
### What you must know cold
- Alternate vertical and horizontal splits.
- Choose splitting points/medians so subproblems are roughly balanced.
- Query recursively visits only subtrees whose regions intersect the search range.
### Core test / key idea
- Each node stores a point and induces an axis-aligned region for its subtree.
- Balance comes from splitting by median coordinate, not by a fixed background grid.
- This is why the structure supports logarithmic-style search behavior in the balanced case.
### Complexity
- Balanced construction supports efficient range searching with query time depending on visited nodes plus reported points.
### Common mistakes / danger points
- The split direction alternates by level. The recordings mention a common coding/slide confusion exactly here.
- Do not describe it as a quadtree with two children. The construction principle is different.
## End-of-file summary
- Alternate vertical and horizontal splits.
- Choose splitting points/medians so subproblems are roughly balanced.
- Query recursively visits only subtrees whose regions intersect the search range.
- Balanced construction supports efficient range searching with query time depending on visited nodes plus reported points.
- The split direction alternates by level. The recordings mention a common coding/slide confusion exactly here.
- Do not describe it as a quadtree with two children. The construction principle is different.

## Everything related to this topic
- **Previous file in reading order:** [Quadtree method](../02_Geometric_Search/25_quadtree-method.md)
- **Next file in reading order:** [Direct access methods](../02_Geometric_Search/27_direct-access-methods.md)
- **Source slide range:** pp. 152-160 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.13 7.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead
