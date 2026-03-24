# Extreme Points Algorithm

**Slides covered:** 202–205  

**Topic folder:** 03 Convex Hulls

## Motivation

The extreme points algorithm is the straightforward idea: a point is a hull vertex if it is not inside any triangle formed by the others. It is conceptually simple and computationally painful, which sounds exactly like the kind of algorithm humans invent first.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 202: Extreme points and hull outline

A point \(p\) of a convex set \(S\) is an **extreme point** if there do **not** exist \(a,b \in S\) with \(p\) strictly **between** \(a\) and \(b\) on segment \(\overline{ab}\).

Let \(E \subseteq S\) be the set of extreme points. Then \(E\) is the **smallest** subset with \(H(E) = H(S)\); equivalently \(E\) is the vertex set of \(H(S)\).

**Two-step hull algorithm:**

1. Find the extreme points \(E\).  
2. **Order** \(E\) cyclically around the hull to form a convex polygon.

![Figure from slide 202](images/slide_202.png)

### Slide 203: Characterization for the plane

**Theorem:** A point \(p \in S\) **fails** to be extreme iff \(p\) lies **inside** (or on) some **triangle** whose vertices are three points of \(S\), and \(p\) is **not** one of those three vertices.

![Figure from slide 203](images/slide_203.png)

### Slide 204: Naive extreme-point test

There are \(\binom{N}{3} = O(N^3)\) triangles determined by \(S\). **Point-in-triangle** tests are \(O(1)\) each.

To test one point \(p\): try all \(O(N^3)\) triangles; if \(p\) lies in none (as a non-vertex), then \(p \in E\).

Repeating for all \(p \in S\): **\(O(N^4)\)** time.

(Alternative \(O(N^3)\) approaches for related edge tests appear in O’Rourke, p. 67.)

![Figure from slide 204](images/slide_204.png)

### Slide 205: Ordering \(E\)

After finding \(E\) in \(O(N^4)\):

1. Pick an interior point \(c\) (e.g. **centroid** of \(S\)) — **\(O(N)\)**.  
2. For each \(p \in E\), compute polar angle from \(c\) to \(p\) — **\(O(|E|)\)**.  
3. **Sort** \(E\) by polar angle — **\(O(|E| \log |E|)\)**.

Overall: **\(O(N^4)\)** dominated by the extreme-point phase.

![Figure from slide 205](images/slide_205.png)

## Recap

- A point is **extreme** iff it is not strictly inside a segment between two other points of \(S\); the extreme set \(E\) is the vertex set of \(H(S)\).
- **Test:** \(p\) is non-extreme iff \(p\) lies in some **triangle** determined by three other points of \(S\) — **\(O(N^3)\)** triangles, **\(O(1)\)** test each → **\(O(N^4)\)** naively for all points.
- After finding \(E\), sort by **polar angle** about an interior point (e.g. centroid) in **\(O(|E|\log |E|)\)** to produce a polygon boundary; total remains **\(O(N^4)\)**.
