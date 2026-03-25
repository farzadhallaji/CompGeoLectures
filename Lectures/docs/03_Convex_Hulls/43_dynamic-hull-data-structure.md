# Dynamic/on-line convex hull insertion: data structure, search, update, and analysis

## Scope
- **Slides:** pp. 254-263
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.27 11.2.txt, CS 564 - 03.04 12.1.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This section is about making dynamic hull updates fast by storing the hull in a searchable, concatenable structure rather than a raw cyclic list.

## What you must know cold
- Operations needed: search, split, splice/concatenate.
- Balanced-tree or concatenable-queue representation of hull vertices.
- Locate support vertices, remove visible chain, insert new point, restore cyclic order.

## Core ideas and reasoning
- The hull is maintained in cyclic order in a structure supporting logarithmic search and logarithmic local surgery.
- Update = find support vertices + split at supports + discard visible chain + insert the new point + concatenate the remaining pieces.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 257
![Figure from slide p. 257](../images/convex-hulls/43_dynamic-hull-data-structure_p257.png)

### Figure from slide p. 258
![Figure from slide p. 258](../images/convex-hulls/43_dynamic-hull-data-structure_p258.png)

## Slide-by-slide digestion

### p. 254 - Dynamic hull (insertion)
- Data structure for Ci-1
- The data structure for Ci-1 must support certain operations:
- 1. SEARCH an ordered string of items (the vertices of the hull)
- to locate the supporting lines from pi.
- 2. SPLIT a string of items into two substrings.
- 3. CONCATENATE (or SPLICE) two strings of items.
- 4. INSERT one item (e.g., the current pi) in its ordered location.
- The concatenable queue data structure supports these operations,
- all in O(log N) time, where N is the number of items stored.
- (For more information, see [Aho,1974] or [Reingold,1977].)

### p. 255 - Dynamic hull (insertion)
- Search tree for Ci-1
- A concatenable queue is a height balanced search tree, call it T.
- It stores the vertices of Ci-1 in (counterclockwise) order.
- In T, the cycle of vertices of Ci-1 appears as a chain, in order.
- The first and last items are considered to be adjacent.
- Vertex M is the vertex of the root of T.
- Vertex m is the vertex of the leftmost (first) node of T.
- Angle α is angle mpiM; α may be convex (≤π) or reflex (> π).
- Each node of T corresponds
- to a vertex of Ci-1.

### p. 256 - Dynamic hull (insertion)
- Search combinations
- If we examine the classifications of m, M, and α,
- there are 18 possible combinations.
- Vertex m is concave, supporting, or reflex.
- Vertex M is concave, supporting, or reflex.
- Angle α is convex or reflex.
- convex
- concave
- supporting
- The action to take to find l and r depends on the combination.

### p. 257 - Dynamic hull (insertion)
- Search cases
- The 18 possible combinations reduce to 8 cases
- where distinct actions are required.
- Combinations
- convex
- concave
- nonconcave
- nonreflex
- Figure 3.16, text p. 122, illustrates the cases.
- In Figure 3.16:

### p. 258 - Dynamic hull (insertion)
- T-R(M)
- T-L(M)

### p. 259 - Dynamic hull (insertion)
- Finding l and r, 1
- A distinct action is required to locate l and r in each of the 8 cases.
- Consider cases 2, 4, 6, and 8.
- Vertices l and r are known to exist, because pi cannot be internal.
- (Point pi can be internal only if m and M are both concave.)
- In these cases, l and r are in separate subtrees of the root of T
- (one of the subtrees is extended to include the root in each case).
- Thus l and r can be found by analogous searches of the two subtrees.
- For example, l is found by the following function:

```text
procedure LEFTSEARCH(T)
```

### p. 260 - Dynamic hull (insertion)
- Finding l and r, 2
- A distinct action is required to locate l and r in each of the 8 cases.
- Consider cases 1, 3, 5, and 7.
- Vertices l and r may not exist,
- because pi could be internal in cases 1 and 7.
- In these cases, if they exist l and r are in the same subtree
- of the root of T (the circled subtree in Figure 3.16).
- Case
- Subtree
- The search calls itself recursively on that subtree until one of cases

### p. 261 - Dynamic hull (insertion)
- Finding l and r, 3
- In general, finding l and r for pi involves tracing a single path in T
- from the root to the node where l and r must be in separate subtrees,
- and then following two paths to find l and r from there.
- T contains O(N) nodes (actually it has < i when pi is added, i ≤N).
- Since T is balanced and therefore has O(log N) levels,
- and O(1) time is expended at each node on the two paths,
- the entire search requires O(log N) time.

### p. 262 - Dynamic hull (insertion)
- Inserting pi into the hull
- If pi is external to Ci-1, it must be added,
- and possibly some other vertices removed, to produce Ci.
- Put another way, the (possibly empty) chain of vertices between
- l and r must be replaced with pi.
- Vertex l may either precede or follow vertex r in the vertex
- order of Ci-1. The “splicing in” step requires a different set of
- operations for each case.
- Vertex sequence
- Split

### p. 263 - Dynamic hull (insertion)
- Analysis
- Each insertion requires O(log N) time:
- 1. O(log N) to find l and r
- 2. O(log N) to splice in pi
- For N insertions, the overall time is O(N log N).
- The storage required is O(N) for T.

## What you must be able to say or do in an exam
- State the input, output, preprocessing, and query/update model precisely.
- Explain the invariant or ordering that makes the method work.
- Trace the method by hand on a small example.
- Give the exact time and space bounds.
- Mention one edge case, degeneracy, or limitation.

## Complexity and performance facts
O(log N) per insertion in the course presentation; O(N log N) total for N insertions.

## Common mistakes and danger points
- The data structure is there to make the visible-chain replacement fast; explain that connection explicitly.

## Professor emphasis from recordings
These points are distilled from the related recordings and focus on what the professor slowed down for, warned about, or connected to homework/exam reasoning.

- The recording explicitly mentions that the many local cases can be reduced to a smaller set once equivalent support/reflex situations are merged.
- This topic is procedural: if you cannot say how the search walks the structure and how the hull list is updated, you do not really know it.

## Exam-style drills and answer skeletons
### Core exam drill
**Question.** State the problem solved by dynamic/on-line convex hull insertion: data structure, search, update, and analysis, describe preprocessing/query/update steps if any, and give the time and space bounds.

**How to answer.** An excellent answer names the input, the output, the invariant or ordering exploited by the method, and the exact asymptotic costs.

### Hand-trace drill
**Question.** Trace dynamic/on-line convex hull insertion: data structure, search, update, and analysis on a small example by hand and explain each comparison or structural change.

**How to answer.** On this course, being able to run the method on a picture matters more than writing vague slogans.

## Recap
### What you must know cold
- Operations needed: search, split, splice/concatenate.
- Balanced-tree or concatenable-queue representation of hull vertices.
- Locate support vertices, remove visible chain, insert new point, restore cyclic order.
### Core test / key idea
- The hull is maintained in cyclic order in a structure supporting logarithmic search and logarithmic local surgery.
- Update = find support vertices + split at supports + discard visible chain + insert the new point + concatenate the remaining pieces.
### Complexity
- O(log N) per insertion in the course presentation; O(N log N) total for N insertions.
### Common mistakes / danger points
- The data structure is there to make the visible-chain replacement fast; explain that connection explicitly.
### Professor emphasis (from recordings)
- The recording explicitly mentions that the many local cases can be reduced to a smaller set once equivalent support/reflex situations are merged.
- This topic is procedural: if you cannot say how the search walks the structure and how the hull list is updated, you do not really know it.
## End-of-file summary
- Operations needed: search, split, splice/concatenate.
- Balanced-tree or concatenable-queue representation of hull vertices.
- Locate support vertices, remove visible chain, insert new point, restore cyclic order.
- O(log N) per insertion in the course presentation; O(N log N) total for N insertions.
- The data structure is there to make the visible-chain replacement fast; explain that connection explicitly.
- The recording explicitly mentions that the many local cases can be reduced to a smaller set once equivalent support/reflex situations are merged.

## Everything related to this topic
- **Previous file in reading order:** [Dynamic/on-line convex hull insertion: problem setting and core idea](../03_Convex_Hulls/42_dynamic-hull-core-idea.md)
- **Next file in reading order:** [Gift wrapping in higher dimensions: background and setup](../03_Convex_Hulls/44_higher-dimensional-hull-background.md)
- **Source slide range:** pp. 254-263 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.27 11.2.txt, CS 564 - 03.04 12.1.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead
