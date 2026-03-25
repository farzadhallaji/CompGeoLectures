# Chain method: analysis and wrap-up

## Scope
- **Slides:** pp. 116-117
- **Major topic folder:** geometric-search
- **Recording files touching this material:** CS 564 - 02.06 5.2.txt
- **Goal of this file:** You should be able to study this topic without reopening the slide deck.

## Big picture
This short range is where you convert the construction story into formal performance claims. The method is only exam-safe when you can say what preprocessing buys you and at what cost.

## What you must know cold
- What data is stored after preprocessing.
- How many binary-search steps happen during a query.
- Trade-off relative to simpler point-location methods like slabs.

## Core ideas and reasoning
- Query time comes from binary search over an ordered family of chains plus local search on a chain.
- Preprocessing and storage are more involved than brute force, but the pay-off is sublinear query time.

## Figures to actually look at
These are cropped from the main slide PDF. Do not skip them.

### Figure from slide p. 117
![Figure from slide p. 117](../images/geometric-search/20_chain-method-analysis_p117.png)

## Slide-by-slide digestion

### p. 116 - Chain method analysis
- Query: O(log2 N)
- Binary search O(log N) with each comparison taking O(log N)
- Preprocessing: O(N log N)
- Regularizing G, O(N log N)
- Constructing C from regular G, O(N)
- Space: O(N)
- See text pp. 54-55 for details of space analysis.

### p. 117 - Chain method overview, “finale and segue”
- PSLG G
- Monotone complete
- set of chains C for G
- Regular PSLG G
- Regularize PSLG G
- (Text pp. 52-54)
- Construct C for regular G
- (Text pp. 50-52)
- Queries
- Preprocessing

## What you must be able to say or do in an exam
- State the claim precisely before giving the argument.
- Identify the known lower bound / recurrence / invariant you are using.
- Keep the direction of the argument correct.
- End with the exact asymptotic conclusion.

## Complexity and performance facts
State the course version of preprocessing, storage, and query bounds exactly as given in the slides.

## Common mistakes and danger points
- Do not describe the query bound without also describing what was precomputed to achieve it.

## Exam-style drills and answer skeletons
Existing drill reminders from the earlier pack:
- Adapted from HW2-Q4: Modify graph-weight balancing so the second pass constructs a monotone complete set of chains.

### Proof drill
**Question.** Explain the main argument in chain method: analysis and wrap-up in a logically correct order.

**How to answer.** Do not jump from intuition to conclusion. State the reduction/invariant/recurrence first, then derive the claimed bound.

## Recap
### What you must know cold
- What data is stored after preprocessing.
- How many binary-search steps happen during a query.
- Trade-off relative to simpler point-location methods like slabs.
### Core test / key idea
- Query time comes from binary search over an ordered family of chains plus local search on a chain.
- Preprocessing and storage are more involved than brute force, but the pay-off is sublinear query time.
### Complexity
- State the course version of preprocessing, storage, and query bounds exactly as given in the slides.
### Common mistakes / danger points
- Do not describe the query bound without also describing what was precomputed to achieve it.
## End-of-file summary
- What data is stored after preprocessing.
- How many binary-search steps happen during a query.
- Trade-off relative to simpler point-location methods like slabs.
- State the course version of preprocessing, storage, and query bounds exactly as given in the slides.
- Do not describe the query bound without also describing what was precomputed to achieve it.

## Everything related to this topic
- **Previous file in reading order:** [Chain method: regularization of arbitrary PSLGs](../02_Geometric_Search/19_chain-method-regularization.md)
- **Next file in reading order:** [Triangle refinement: setup and triangulation](../02_Geometric_Search/21_triangle-refinement-setup.md)
- **Source slide range:** pp. 116-117 of `comp_geometry_slides_new.pdf`
- **Related recordings:** CS 564 - 02.06 5.2.txt
- **Related homework-derived exam prompts included here:** none directly mapped; generic exam drills added instead
