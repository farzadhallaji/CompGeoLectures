# Search problem taxonomy and inclusion basics

## Scope
- **Slides:** pp. 66-69
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 01.30 3.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This is the map of geometric search. The midterm then spends many pages filling in specific algorithmic answers to these generic search questions.

## What you must know cold
- Difference between inclusion, point location, and range searching.
- Static data set plus many queries viewpoint.
- Why preprocessing is worth paying for in search problems.

## Core ideas and reasoning
- Polygon inclusion asks whether one query point lies inside a given polygon.
- Point location asks which face of a planar subdivision contains the query point.
- Range searching asks which points of a set lie inside a query range, often an axis-parallel rectangle.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 67
![Figure from slide p. 67](../images/geometric-search/10_search-taxonomy_p67.png)

### Figure from slide p. 69
![Figure from slide p. 69](../images/geometric-search/10_search-taxonomy_p69.png)

## Slide-by-slide digestion

### p. 66 - Definitions of geometric search
- In general terms a geometric query or search problem has
- this form:
- Given a set S of geometric objects and a distinct geometric object q
- which is the query object, the objective is to determine the subset
- of the objects in set S that are in some specified geometric
- relationship with the query object.
- Many variations are possible, depending on the specific problem.
- 1. S may have 1 or more elements.
- 2. The elements of S may be of the same type as q, or not.
- 3. The answer set may be constrained to have exactly one element,

### p. 67 - Polygon inclusion
- Given polygon P and query point q, both in the plane, is q within P?
- P may be of different types (simple, convex, or star-shaped),
- which will affect the method.
- Methods
- Left test (convex)
- Intersection counting (Simple)
- Wedges (Convex and star-shaped)

### p. 68 - Point location
- Given a partition of the geometric space into regions and a query
- point q, determine which region contains q.
- We will consider only d = 2, i.e., the plane.
- Methods
- Brute force
- Slab method
- Chain method
- Triangle refinement

### p. 69 - Range searching
- RANGE SEARCHING
- INSTANCE: Set S = {p1, p2, ..., pN}, pi = (xi, yi) of points in the
- plane, and rectangle R = [lx, rx] × [ly, ry] in the plane.
- QUESTION: Which points of S are within R?
- Methods
- Brute force
- Dominance
- Grid
- Quadtree
- k-D tree

## What you must be able to say or do in an exam
- Give the precise definitions.
- Distinguish similar notions cleanly.
- Use the right primitive test or formula on a concrete example.

## Complexity and performance facts
Always report preprocessing, storage, and query time separately.

## Common mistakes and danger points
- Do not mix a single-shot problem with a repeated-query data-structure problem.
- For range searching, remember the query region is x-range cross y-range.

## Exam-style drills and answer skeletons
### Definition drill
**Question.** Give the precise definitions and the most important consequences from search problem taxonomy and inclusion basics.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Difference between inclusion, point location, and range searching.
- Static data set plus many queries viewpoint.
- Why preprocessing is worth paying for in search problems.
### Core test / key idea
- Polygon inclusion asks whether one query point lies inside a given polygon.
- Point location asks which face of a planar subdivision contains the query point.
- Range searching asks which points of a set lie inside a query range, often an axis-parallel rectangle.
### Complexity
- Always report preprocessing, storage, and query time separately.
### Common mistakes / danger points
- Do not mix a single-shot problem with a repeated-query data-structure problem.
- For range searching, remember the query region is x-range cross y-range.
## End-of-file summary
- Difference between inclusion, point location, and range searching.
- Static data set plus many queries viewpoint.
- Why preprocessing is worth paying for in search problems.
- Always report preprocessing, storage, and query time separately.
- Do not mix a single-shot problem with a repeated-query data-structure problem.
- For range searching, remember the query region is x-range cross y-range.

## Everything related to this topic
- **Previous file in reading order:** [Primitive formulas and summary](../01_Foundations/09_primitive-formulas-summary.md)
- **Next file in reading order:** [Convex polygon inclusion by left test](../02_Geometric_Search/11_convex-inclusion-left-test.md)
- **Source slide range:** pp. 66-69 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 01.30 3.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead