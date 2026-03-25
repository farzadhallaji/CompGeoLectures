# Triangle refinement: hierarchy, query, storage, and analysis

## Scope
- **Slides:** pp. 123-134
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 02.11 6.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This is the operative part of triangle refinement: how you descend the DAG, what you store, and why the path length stays logarithmic or near-logarithmic in the course analysis.

## What you must know cold
- How to test which child triangle contains the query point.
- Why each level narrows the search region.
- Storage and search-graph size issues.

## Core ideas and reasoning
- Start from a top-level triangle covering the subdivision.
- At each level, perform point-in-triangle tests on the few candidate children and move to the unique containing child.
- Stop at a leaf triangle and recover the face in the original PSLG.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 125
![Figure from slide p. 125](../images/geometric-search/22_triangle-refinement-query-and-analysis_p125.png)

### Figure from slide p. 128
![Figure from slide p. 128](../images/geometric-search/22_triangle-refinement-query-and-analysis_p128.png)

## Slide-by-slide digestion

### p. 123 - Sequence of triangulations
- We have triangulation G with N vertices. Construct a sequence of
- triangulations S1, S2, ..., Sh(N), where S1 = G and Si is obtained from
- Si-1 as follows:
- (1) Remove a maximal independent set of nonboundary vertices of
- Si-1 and their incident edges. A set of vertices of a graph (in our
- case a planar graph) is said to be independent if no two pair of
- vertices are adjacent in the graph. A maximal set is one such that
- adding one more vertex will make at least one pair of vertices to
- become adjacent. How this set is chosen will determine the
- performance of the algorithm.

### p. 124 - Notation
- The notation Rj denotes a triangle.
- A triangle Rj may appear in more than one triangulation in
- the sequence, but is said to belong to triangulation Si
- if Rj was created in step (2) while constructing Si.
- Search data structure
- We now build a search data structure T, an acyclic directed graph.
- The nodes of T represent triangles.
- When discussing T, we say “triangle Rj” or just “Rj”
- when “the node of T that represents Rj” is meant.
- In T, there is an arc from triangle Rk to triangle Rj if,

### p. 125 - Geometric Search, Point location, Triangle refinement method
- This slide is mainly visual. Use the figure crop in this file and make sure you can explain what the diagram is showing.

### p. 126 - Triangle refinement method
- PSLG G
- Directed acyclic
- search graph T
- Triangulated PSLG G
- Triangulate PSLG G
- (To be covered later)
- Construct sequence of triangulations
- and directed acyclic search graph T
- (PS pp. 56-58)
- Queries

### p. 127 - Query process, informal
- The query process uses a primitive operation, triangle inclusion,
- which can be computed in O(1) with 3 Left tests.
- The query begins by determining if the query point q is
- within the enclosing triangle.
- If not, the unbounded face is the answer to the query.
- If it is, the current node is set to the root node of T.
- Then q is tested for inclusion in the triangle for each of the
- descendants of the current node; it will be in exactly one.
- The search advances along the arc to that node,
- which becomes the current node, and the process repeats.

### p. 128 - Query starts here
- This slide is mainly visual. Use the figure crop in this file and make sure you can explain what the diagram is showing.

### p. 129 - Query process
- Define Γ(v) to be a list of all descendants of node v of T,
- and TRIANGLE(v) to the triangle represented by node v.

```text
procedure PointLocation(T,q)
begin
(q ∉TRIANGLE(root(T)))
“q in unbounded face”
v = root(T)
while (Γ(v) ≠ ∅)
for each u ∈Γ(v)
(q ∈TRIANGLE(u))
```

### p. 130 - Query time
- The choice of the triangulation vertices to be removed
- in constructing Si from Si-1 determines the performance
- (query time and storage) of the method.
- Define Ni as the number of vertices in triangulation Si.
- Suppose it was possible to choose vertices to be removed
- such that these properties hold:
- (1) Ni = αiNi-1, with αi ≤α < 1 for i = 2, ..., h(N).
- αi < 1 ⇒Ni < Ni-1,
- i.e., each successive triangulation Si is smaller than Si-1.
- All are smaller than their predecessor by at least α.

### p. 131 - Storage
- Properties (1) and (2) imply O(N) storage required for T.
- Here’s why:
- Storage for T includes storage for nodes and for pointers.
- How may nodes? One per triangle in S1, S2, ..., Sh(N).
- How many triangles?
- Si contains Fi < 2Ni triangles,
- by Euler’s formula, p. 19, f ≤2v - 4.
- Total triangles for the sequence of triangulations is
- ≤ 2N1 + 2αN1 + 2α2N1 + ... + 2αi-1Ni + ... + 2αh(N)-1N1
- Sh(N)

### p. 132 - Justifying the properties, part 1
- Having shown that properties (1) and (2)
- lead to a query time ∈O(log N) and storage ∈O(N),
- the question remains:
- how can the vertices to be removed when constructing the sequence
- of triangulations be selected to satisfy the properties?
- The selection criteria to be used is:
- “Remove a set of nonadjacent vertices of degree less than K.”
- Integer K will be given a value momentarily.
- The order of selection at each stage is not important. Procedure:
- (1) Arbitrarily select one vertex with degree less than K to remove.

### p. 133 - Justifying the properties, part 2
- To show property (1) we use properties of planar graphs.
- Euler’s formula for a triangulation with a 3 edge boundary is
- e = 3v - 6
- where e is number of edges and v is number of vertices (v = N)
- Assume there exist internal vertices in the triangulation, i.e., N > 3.
- ⇒Each boundary vertex has degree ≥3.
- There are 3N - 6 edges and each edge contributes 2 to the sum
- of vertex degrees for the triangulation.
- ⇒Sum of vertex degrees=2*e < 6N.
- ⇒∃at least N/2 vertices of degree < 12.

### p. 134 - Analysis
- Query time: O(log N)
- Storage: O(N)
- Preprocessing: O(N log N) or O(N)?
- The steps in preprocessing consists of triangulation of the
- PSLG (takes O(NlogN) time [or O(N) time if one used
- Chazelle’s algorithm), finding maximal independent set
- (O(N) work), retriangulation (takes O(N) time since each
- new face created has less than 12 sides and retriangulation of
- the new polygon takes O(1) time and we repeat this for at
- most the size of the independent set < N. The creation of the

## What you must be able to say or do in an exam
- State the input, output, preprocessing, and query/update model precisely.
- Explain the invariant or ordering that makes the method work.
- Trace the method by hand on a small example.
- Give the exact time and space bounds.
- Mention one edge case, degeneracy, or limitation.

## Complexity and performance facts
The course presentation emphasizes search depth and search-graph size; use the slide statements, not vague guesses.

## Common mistakes and danger points
- “Move to the child containing q” is the conceptual step. In implementation the child set must be explicitly stored and searched.
- Remember the relationship between triangulation leaves and original subdivision faces.
- Textual Big-O phrasing: statements should be read as asymptotic membership (e.g., belongs to `O(log N)`), not mathematical equality; do not turn bounds into false exact equalities.

## Exam-style drills and answer skeletons
### Core exam drill
**Question.** State the problem solved by triangle refinement: hierarchy, query, storage, and analysis, describe preprocessing/query/update steps if any, and give the time and space bounds.

**How to answer.** An excellent answer names the input, the output, the invariant or ordering exploited by the method, and the exact asymptotic costs.

### Hand-trace drill
**Question.** Trace triangle refinement: hierarchy, query, storage, and analysis on a small example by hand and explain each comparison or structural change.

**How to answer.** On this course, being able to run the method on a picture matters more than writing vague slogans.

## Recap
### What you must know cold
- How to test which child triangle contains the query point.
- Why each level narrows the search region.
- Storage and search-graph size issues.
### Core test / key idea
- Start from a top-level triangle covering the subdivision.
- At each level, perform point-in-triangle tests on the few candidate children and move to the unique containing child.
- Stop at a leaf triangle and recover the face in the original PSLG.
### Complexity
- The course presentation emphasizes search depth and search-graph size; use the slide statements, not vague guesses.
### Common mistakes / danger points
- “Move to the child containing q” is the conceptual step. In implementation the child set must be explicitly stored and searched.
- Remember the relationship between triangulation leaves and original subdivision faces.
- Textual Big-O phrasing: statements should be read as asymptotic membership (e.g., belongs to `O(log N)`), not mathematical equality; do not turn bounds into false exact equalities.
## End-of-file summary
- How to test which child triangle contains the query point.
- Why each level narrows the search region.
- Storage and search-graph size issues.
- The course presentation emphasizes search depth and search-graph size; use the slide statements, not vague guesses.
- “Move to the child containing q” is the conceptual step. In implementation the child set must be explicitly stored and searched.
- Remember the relationship between triangulation leaves and original subdivision faces.

## Everything related to this topic
- **Previous file in reading order:** [Triangle refinement: setup and triangulation](../02_Geometric_Search/21_triangle-refinement-setup.md)
- **Next file in reading order:** [Range searching: problem statement and design space](../02_Geometric_Search/23_range-searching-intro.md)
- **Source slide range:** pp. 123-134 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.11 6.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead
