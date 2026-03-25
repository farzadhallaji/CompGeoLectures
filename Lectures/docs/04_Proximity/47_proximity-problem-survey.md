# Proximity problem family: survey and relations

## Scope
- **Slides:** pp. 290-299
- **Major topic folder:** proximity
- **Recording files touching this material:** CS 564 - 03.06 13.2.txt, CS 564 - 03.11 14.1.txt, CS 564 - 03.13 15.1a.txt, CS 564 - 03.25 16.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This file is the conceptual map for the last midterm block. Closest pair, nearest neighbors, EMST, triangulations, Voronoi, and search variants are introduced as one family of related proximity questions.

## What you must know cold
- Closest pair, all nearest neighbors, nearest-neighbor relation, EMST, triangulation, k-nearest neighbors.
- Difference between one-shot proximity problems and search/data-structure versions.
- How these problems reduce to one another conceptually.

## Core ideas and reasoning
- The block’s main message is not just a list of problems; it is that many of them share lower bounds and structural reductions.
- Nearest-neighbor relation need not be symmetric.
- Voronoi and Delaunay later become universal structures for many proximity queries, although later pages are outside your midterm.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 294
![Figure from slide p. 294](../images/proximity/47_proximity-problem-survey_p294.png)

### Figure from slide p. 299
![Figure from slide p. 299](../images/proximity/47_proximity-problem-survey_p299.png)

## Slide-by-slide digestion

### p. 290 - Comments
- We consider in this topic a large class of related problems
- that deal with proximity of points in the plane.
- We will:
- 1. Define some proximity problems and see how they are related
- 2. Study a classic algorithm for one of the problems
- 3. Introduce triangulations
- 4. Examine a data structure that seems to represent nearly
- everything we might like to know about proximity
- in a set of points in the plane.
- Overview of the topic

### p. 291 - CLOSEST PAIR
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Determine the two points of S whose mutual
- distance is smallest.
- Distance is defined as the usual Euclidean distance:
- distance(pi,pj) = sqrt((xi - xj)2 + (yi - yj)2).
- This problem is described as “one of the fundamental questions
- of computational geometry” in Preparata.
- Brute force
- A brute force solution is to compute the distance for every pair
- of points, saving the smallest; this requires O(dN2) time.

### p. 292 - All nearest neighbors
- ALL NEAREST NEIGHBORS
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Determine the “nearest neighbor” (point of
- minimum distance) for each point in S.
- Proximity
- Proximity problems

### p. 293 - “Nearest neighbor” is a relation on a set S as follows:
- point b is a nearest neighbor of point a, denoted a →b, if
- distance(a,b) = min distance(a,c)
- c ∈S - a
- (a, b, c ∈S).
- The “nearest neighbor” relation is not symmetric,
- i.e., a →b does not imply b →a (though it could be true).
- Preparata, p. 186 says:
- “Note also that a point is not the nearest neighbor of a unique point
- (i.e., “→” is not a function).”
- Perhaps slightly clearer:

### p. 294 - Footnote 2 on Preparata, p. 186:
- “Although a point can be the nearest neighbor of every other point,
- a point can have at most six nearest neighbors in two dimensions…”
- I think that is backwards, and should be:
- “Although a point can have every other point as a nearest neighbor,
- a point can be the nearest neighbor of at most six other points
- in two dimensions…”
- Proximity
- Proximity problems
- Point c has every other point
- as its nearest neighbor.

### p. 295 - Euclidean minimum spanning tree
- EUCLIDEAN MINIMUM SPANNING TREE
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Construct a tree of minimum total length
- whose vertices are the points in S.
- A solution to this problem will be the N-1 pairs of points in S
- that comprise the edges of the tree.
- The (more general) Minimum Spanning Tree (MST) problem is
- usually formulated as a problem in graph theory:
- Given a graph G with N nodes and E weighted edges,
- find the subtree of G that includes every vertex

### p. 296 - Triangulation
- TRIANGULATION
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Join the points in S with nonintersecting straight
- line segments so that every region internal to the convex hull
- of S is a triangle.
- Proximity
- Proximity problems
- A triangulation for a set S is not necessarily unique.
- As a planar graph, a triangulation on N vertices has ≤3N - 6 edges.

### p. 297 - Single-shot vs. search
- The previous problems (CLOSEST PAIR, ALL NEAREST
- NEIGHBORS, EUCLIDEAN MINIMUM SPANNING TREE,
- and TRIANGULATION) have been single shot.
- We now define two search-type proximity problems.
- Because these are search problems, repetitive mode is assumed,
- and thus preprocessing is allowed.
- Nearest neighbor search
- NEAREST NEIGHBOR SEARCH
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Given a query point q, which point p ∈S is a

### p. 298 - k nearest neighbors
- k-NEAREST NEIGHBORS
- INSTANCE: Set S = {p1, p2, ..., pN} of N points in the plane.
- QUESTION: Given a query point q, determine the k points of
- S nearest to q.
- This problem is equivalent to the previous one for k = 1.
- The figure gives the solution for k = 3.
- Proximity
- Proximity problems

### p. 299 - Proximity
- Proximity problems
- Element uniqueness
- Preparata defines a computational prototype as an archetypal
- problem, one which can act as a fundamental representative
- for a class of problems.
- For example, SATISFIABILITY for NP-complete problems,
- or SORTING for many problems in computational geometry.
- Another such problem is ELEMENT UNIQUENESS.
- ELEMENT UNIQUENESS
- INSTANCE: Set S = {x1, x2, ..., xN} of N real numbers.

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
This range mostly sets up relationships and why O(N log N) keeps reappearing.

## Common mistakes and danger points
- Do not assume “A is nearest to B” implies “B is nearest to A”.
- Separate static problem statements from query-data-structure versions.

## Professor emphasis from recordings
These points are distilled from the related recordings and focus on what the professor slowed down for, warned about, or connected to homework/exam reasoning.

- The lecture treats the proximity chapter as a family of related problems rather than a single isolated algorithm, so you should know how closest pair, nearest neighbor, Voronoi, and MST-type questions sit in the same neighborhood.

## Exam-style drills and answer skeletons
Existing drill reminders from the earlier pack:
- Adapted from HW2-Q2: For points on one axis stored in a range tree, find the closest neighbor in O(log N), then augment the structure to answer in O(1).

### Definition drill
**Question.** Give the precise definitions and the most important consequences from proximity problem family: survey and relations.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Closest pair, all nearest neighbors, nearest-neighbor relation, EMST, triangulation, k-nearest neighbors.
- Difference between one-shot proximity problems and search/data-structure versions.
- How these problems reduce to one another conceptually.
### Core test / key idea
- The block’s main message is not just a list of problems; it is that many of them share lower bounds and structural reductions.
- Nearest-neighbor relation need not be symmetric.
- Voronoi and Delaunay later become universal structures for many proximity queries, although later pages are outside your midterm.
### Complexity
- This range mostly sets up relationships and why O(N log N) keeps reappearing.
### Common mistakes / danger points
- Do not assume “A is nearest to B” implies “B is nearest to A”.
- Separate static problem statements from query-data-structure versions.
### Professor emphasis (from recordings)
- The lecture treats the proximity chapter as a family of related problems rather than a single isolated algorithm, so you should know how closest pair, nearest neighbor, Voronoi, and MST-type questions sit in the same neighborhood.
## End-of-file summary
- Closest pair, all nearest neighbors, nearest-neighbor relation, EMST, triangulation, k-nearest neighbors.
- Difference between one-shot proximity problems and search/data-structure versions.
- How these problems reduce to one another conceptually.
- This range mostly sets up relationships and why O(N log N) keeps reappearing.
- Do not assume “A is nearest to B” implies “B is nearest to A”.
- Separate static problem statements from query-data-structure versions.

## Everything related to this topic
- **Previous file in reading order:** [Gift wrapping in higher dimensions: supporting hyperplanes, initialization, candidates, and analysis](../03_Convex_Hulls/46_higher-dimensional-hull-init-analysis.md)
- **Next file in reading order:** [Proximity lower bounds and transformations](../04_Proximity/48_proximity-lower-bounds.md)
- **Source slide range:** pp. 290-299 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 03.06 13.2.txt, CS 564 - 03.11 14.1.txt, CS 564 - 03.13 15.1a.txt, CS 564 - 03.25 16.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead