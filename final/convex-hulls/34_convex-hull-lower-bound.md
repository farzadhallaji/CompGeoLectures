# Lower bound for convex hull via reduction from sorting

## Scope
- **Slides:** pp. 196-201
- **Major topic folder:** convex-hulls
- **Recording files touching this material:** CS 564 - 02.20 9.1.txt, CS 564 - 02.20 9.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This is a favorite exam idea because it tests actual reduction logic rather than memory. The punchline is that convex hull construction cannot beat Ω(N log N) in the comparison model because sorting reduces to it.

## What you must know cold
- What a problem transformation/reduction is.
- How to map numbers x_i to points on a parabola so sorted order can be read from the hull.
- Why O(N) transformation cost plus a hypothetical faster hull algorithm would imply a faster sorting algorithm.

## Core ideas and reasoning
- Transform the sorting instance x_1, ..., x_N into points (x_i, x_i^2).
- All points lie on a convex parabola, so their hull order reveals the sorted order by x.
- Therefore sorting reduces to convex hull, and convex hull has Ω(N log N) lower bound.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 199
![Figure from slide p. 199](../images/convex-hulls/34_convex-hull-lower-bound_p199.png)

### Figure from slide p. 200
![Figure from slide p. 200](../images/convex-hulls/34_convex-hull-lower-bound_p200.png)

## Slide-by-slide digestion

### p. 196 - Preliminaries and definitions
- Transformation of problems
- We would like to establish lower bounds for performance
- measures (time and space) for problems (not algorithms!).
- One reason: to avoid a futile search for an algorithm faster than
- the theoretical lower bound for the problem.
- Generally, proving a lower (or upper) is difficult,
- because it is a proof about all algorithms to solve the problem.
- There is a technique to do so, useful in some cases:
- transformation of problems.
- Suppose there are two problems A and B, which are related

### p. 197 - Preliminaries and definitions
- Lower and upper bounds via transformation
- Under the assumption that the transformation preserves the
- order of the instance size, the transformation has two properties:
- Property 1 (Lower bound via transformation). If problem A is
- known to require at least T(N) time and A is τ(N)-transformable to B,
- then B requires at least T(N) - O(τ(N)) time.
- Otherwise, you could use the transformation to solve A too fast.
- Property 2 (Upper bound via transformation). If problem B can be
- solved in T(N) time and A is τ(N)-transformable to B,
- then A requires at most T(N) + O(τ(N)) time.

### p. 198 - Preliminaries and definitions
- A known problem
- Note that the technique assumes that there is a problem with a
- known lower bound (to use property 1).
- We have such a problem: SORTING requires Ω(N log N).
- Problem A
- Problem B
- τ(N)-transformable
- Upper bound O(f(N))
- Lower bound Ω(f(N))

### p. 199 - Preliminaries and definitions
- Lower bound for CONVEX HULL
- Can we get a lower bound for time for CONVEX HULL?
- Recall that that the constructed hull H(S) must be given in order.
- This suggest a connection to SORTING.
- Theorem. SORTING is linear-time transformable to CONVEX
- HULL; SORTING αO(N) CONVEX HULL.
- Therefore, CONVEX HULL requires at least Ω(N log N) time.
- Proof. We show the transformation. Suppose the instance of
- SORTING is the set of N real numbers {x1, x2, …, xN}.
- Transform that set to an instance of CONVEX HULL

### p. 200 - Preliminaries and definitions
- Lower bound for CONVEX HULL
- The convex hull of the converted instance will consist of a
- list of points, sorted by abscissa. At most one pass through the list
- will find the smallest and the answer to SORTING can be
- read off from there in one pass. O(N)

### p. 201 - Preliminaries and definitions
- Lower bound for CONVEX HULL
- Note that the O(N) transformation is dominated by the O(N log N)
- complexity of the problem.
- As a consequence of this transformation,
- we know that CONVEX HULL requires at least Ω(N log N) time.
- SORTING
- CONVEX HULL
- O(N)-transformable
- Upper bound O(N log N)
- Lower bound Ω(N log N)

## What you must be able to say or do in an exam
- State the claim precisely before giving the argument.
- Identify the known lower bound / recurrence / invariant you are using.
- Keep the direction of the argument correct.
- End with the exact asymptotic conclusion.

## Complexity and performance facts
Lower bound Ω(N log N) for planar convex hull in the standard model.

## Common mistakes and danger points
- Direction matters: reduce from a problem with known lower bound to the problem whose lower bound you want.
- Do not propose an algorithm for sorting and call that a lower-bound proof. Professors develop headaches from this.

## Professor emphasis from recordings
These points are distilled from the related recordings and focus on what the professor slowed down for, warned about, or connected to homework/exam reasoning.

- The professor emphasizes that lower bounds are proved by transforming a problem with a known lower bound into the target problem, not the other way around.
- The most common mistake here is reversing the roles of the source and target problems and accidentally 'proving' nonsense.
- He presents this reduction as a template you are supposed to reuse later, not as a one-off trick for convex hull only.

## Exam-style drills and answer skeletons
Existing drill reminders from the earlier pack:
- Write the full input transformation, output extraction, and complexity argument for sorting ≤ convex hull.
- Explain why a reduction must not cost more than the lower bound you are trying to transfer.

### Proof drill
**Question.** Explain the main argument in lower bound for convex hull via reduction from sorting in a logically correct order.

**How to answer.** Do not jump from intuition to conclusion. State the reduction/invariant/recurrence first, then derive the claimed bound.

## Recap
### What you must know cold
- What a problem transformation/reduction is.
- How to map numbers x_i to points on a parabola so sorted order can be read from the hull.
- Why O(N) transformation cost plus a hypothetical faster hull algorithm would imply a faster sorting algorithm.
### Core test / key idea
- Transform the sorting instance x_1, ..., x_N into points (x_i, x_i^2).
- All points lie on a convex parabola, so their hull order reveals the sorted order by x.
- Therefore sorting reduces to convex hull, and convex hull has Ω(N log N) lower bound.
### Complexity
- Lower bound Ω(N log N) for planar convex hull in the standard model.
### Common mistakes / danger points
- Direction matters: reduce from a problem with known lower bound to the problem whose lower bound you want.
- Do not propose an algorithm for sorting and call that a lower-bound proof. Professors develop headaches from this.
### Professor emphasis (from recordings)
- The professor emphasizes that lower bounds are proved by transforming a problem with a known lower bound into the target problem, not the other way around.
- The most common mistake here is reversing the roles of the source and target problems and accidentally 'proving' nonsense.
- He presents this reduction as a template you are supposed to reuse later, not as a one-off trick for convex hull only.
## End-of-file summary
- What a problem transformation/reduction is.
- How to map numbers x_i to points on a parabola so sorted order can be read from the hull.
- Why O(N) transformation cost plus a hypothetical faster hull algorithm would imply a faster sorting algorithm.
- Lower bound Ω(N log N) for planar convex hull in the standard model.
- Direction matters: reduce from a problem with known lower bound to the problem whose lower bound you want.
- Do not propose an algorithm for sorting and call that a lower-bound proof. Professors develop headaches from this.

## Everything related to this topic
- **Previous file in reading order:** [Equivalent formulations and problem statement](../convex-hulls/33_convex-hull-equivalent-formulations.md)
- **Next file in reading order:** [Extreme points algorithm](../convex-hulls/35_extreme-points-algorithm.md)
- **Source slide range:** pp. 196-201 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.20 9.1.txt, CS 564 - 02.20 9.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead