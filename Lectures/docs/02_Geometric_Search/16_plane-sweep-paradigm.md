# Plane sweep as a recurring paradigm

## Scope
- **Slides:** pp. 86-90
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 02.04 4.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
Plane sweep is not one algorithm. It is a habit of mind: move an imaginary line, process events in order, and maintain exactly the active structure you need.

## What you must know cold
- Sweep line or sweep plane idea.
- Event queue and status structure.
- Why geometry often becomes easier when you impose a global order.

## Core ideas and reasoning
- Sort critical events such as vertex coordinates, segment endpoints, or intersections.
- Maintain a balanced structure for currently active objects intersecting the sweep line.
- Update only when the combinatorial situation changes.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 86
![Figure from slide p. 86](../images/geometric-search/16_plane-sweep-paradigm_p86.png)

### Figure from slide p. 88
![Figure from slide p. 88](../images/geometric-search/16_plane-sweep-paradigm_p88.png)

## Slide-by-slide digestion

### p. 86 - Plane sweep algorithmic technique
- Plane sweep is an algorithmic technique, or pattern,
- that is used frequently in computational geometry.
- The essential idea is that a geometric object, or collection of
- objects, in the plane is processed with an algorithm that
- is suggested by the idea of a vertical (or horizontal) line
- passing over the object(s).
- Processing occurs at discrete abscissa (or ordinates) as the line
- passes over key points in the object(s).
- Those points are called events.
- We will see how to apply this technique to perform preprocessing

### p. 87 - Plane sweep data structures
- Plane sweep algorithms often use two data structures:
- 1. Event-point schedule
- Sequence of positions to be assumed by the sweep-line.
- 2. Sweep-line status
- Description of the intersection of the sweep-line with
- the geometric object(s) being swept at the current event.
- Sweep line status
- For the slab method preprocessing, the sweep-line status is a
- left-to-right sequence of edges of G that intersect the
- sweep-line.

### p. 88 - Event processing
- At each event, i.e., vertex v ∈V,
- 1. the edges terminating at v are deleted from the sweep-line status
- 2. the edges originating at v are added to the sweep-line status
- 3. the sweep-line status data structure is reported,
- and used to construct a slab.
- The sweep-line status can be maintained in a height balanced
- binary tree (e.g., a AVL tree) that provides INSERT
- and DELETE operations in O(log N).

### p. 89 - Preprocessing algorithm
- Data structures
- VERTEX
- Array storing vertices of G,
- ordered by increasing y-coordinates
- B[i]
- Set of edges incident on VERTEX[i] from below,
- ordered counterclockwise
- A[i]
- Set of edges incident on VERTEX[i] from above,
- ordered clockwise

### p. 90 - Preprocessing analysis
- Preprocessing time: O(N2); O(N) slabs, each requiring O(N)
- time to construct a slab.
- There will be at most O(N) insertions and deletions to L,
- each requiring O(log N) time, so without the slab construction
- the time required is in O(N log N).
- Comments
- The slab method’s O(log N) query time is optimal.
- Preprocessing time reduced from O(N2 log N) to O(N2) through
- use of the plane-sweep technique.
- Still, O(N2) is unacceptable for some applications.

## What you must be able to say or do in an exam
- State the input, output, preprocessing, and query/update model precisely.
- Explain the invariant or ordering that makes the method work.
- Trace the method by hand on a small example.
- Give the exact time and space bounds.
- Mention one edge case, degeneracy, or limitation.

## Complexity and performance facts
Usually O((number of events) log N) plus output size, depending on the problem.

## Common mistakes and danger points
- Do not store everything in the status, only active objects.
- Correct event ordering and tie handling are part of the algorithm, not implementation trivia.

## Exam-style drills and answer skeletons
### Definition drill
**Question.** Give the precise definitions and the most important consequences from plane sweep as a recurring paradigm.

**How to answer.** A strong answer distinguishes similar objects and uses the course terminology exactly.

## Recap
### What you must know cold
- Sweep line or sweep plane idea.
- Event queue and status structure.
- Why geometry often becomes easier when you impose a global order.
### Core test / key idea
- Sort critical events such as vertex coordinates, segment endpoints, or intersections.
- Maintain a balanced structure for currently active objects intersecting the sweep line.
- Update only when the combinatorial situation changes.
### Complexity
- Usually O((number of events) log N) plus output size, depending on the problem.
### Common mistakes / danger points
- Do not store everything in the status, only active objects.
- Correct event ordering and tie handling are part of the algorithm, not implementation trivia.
## End-of-file summary
- Sweep line or sweep plane idea.
- Event queue and status structure.
- Why geometry often becomes easier when you impose a global order.
- Usually O((number of events) log N) plus output size, depending on the problem.
- Do not store everything in the status, only active objects.
- Correct event ordering and tie handling are part of the algorithm, not implementation trivia.

## Everything related to this topic
- **Previous file in reading order:** [Point location by slab decomposition](../02_Geometric_Search/15_point-location-slab-method.md)
- **Next file in reading order:** [Chain method: basics, definitions, and query idea](../02_Geometric_Search/17_chain-method-basics-and-query.md)
- **Source slide range:** pp. 86-90 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.04 4.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead
