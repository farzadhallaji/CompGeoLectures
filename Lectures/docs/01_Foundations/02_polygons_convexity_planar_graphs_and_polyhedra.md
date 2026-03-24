# Polygons, Convexity, Planar Graphs, and Polyhedra

**Slides covered:** 20–28  

**Topic folder:** 01 Foundations

## Motivation

This part defines polygons and their inside/outside, then connects geometry with graph structure. It also introduces convexity, planar graphs, Euler’s formula, and polyhedra.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 20: Polygon (O’Rourke, pp. 1–2)

A **polygon** is the region of the plane bounded by a finite set of segments forming a **simple closed curve** (we work in \(d = 2\)).

Let \(v_0, v_1, \ldots, v_{N-1}\) be \(N\) **vertices**. Let

\[
e_0 = v_0v_1,\; e_1 = v_1v_2,\; \ldots,\; e_{N-1} = v_{N-1}v_0
\]

be \(N\) **edges**. The edges bound a polygon iff consecutive edges meet only at their shared vertex:

\[
e_i \cap e_{i+1} = \{v_{i+1}\} \quad \text{for } i = 0,\ldots,N-1
\]

(indices mod \(N\)). Vertices are numbered **counterclockwise** by convention.

![Figure from slide 20](images/slide_020.png)

### Slide 21: Interior, exterior, boundary

**Jordan curve theorem:** every simple closed plane curve divides the plane into an **interior**, an **exterior**, and the **boundary** (the curve itself).

**Polygon** = interior \(\cup\) boundary (when we mean the filled region). When we care only about the boundary or only the interior, we say so explicitly (same convention for rectangles, etc.).

![Figure from slide 21](images/slide_021.png)

### Slide 22: Simple polygon

A polygon is **simple** iff **non-adjacent** edges do not intersect:

\[
e_i \cap e_j = \emptyset \quad \text{for all } 0 \le i,j \le N-1 \text{ with } j \neq i,\; j \neq i\pm 1 \pmod N.
\]

Non-simple vs. simple examples are illustrated on the slide.

![Figure from slide 22](images/slide_022.png)

### Slide 23: Convex polygon

A polygon is **convex** iff for any two points in the polygon (interior \(\cup\) boundary), the segment joining them lies entirely in the polygon.

![Figure from slide 23](images/slide_023.png)

### Slide 24: Convex set in \(d\) dimensions

Let \(p, q\) be two points in \(d\)-dimensional Euclidean space belonging to a set \(C\). Then \(C\) is **convex** iff for every such pair, all points on the segment between \(p\) and \(q\) belong to \(C\). Equivalently, for all \(p,q \in C\) and all \(\alpha\) with \(0 \le \alpha \le 1\),

\[
\alpha p + (1-\alpha) q \in C.
\]

When \(d = 2\) and \(C\) is a bounded polygonal region, this matches the definition of a convex polygon.

### Slide 25: Planar graphs and Euler’s formula

A graph \(G(V,E)\) is **planar** if it can be embedded in the plane without edge crossings. A straight-line embedding induces a **planar subdivision** (a **map**).

Let \(v = |V|\), \(e = |E|\), and \(f\) = number of **faces**. Then **Euler’s formula**:

\[
v - e + f = 2.
\]

**Idea:** a simple polygon has \(v = e\) and \(f = 2\) (interior and exterior face).

![Figure from slide 25](images/slide_025.png)

### Slide 26: Consequences of Euler’s formula

Adding a **chord** or a **chain** of new vertices preserves \(v - e + f = 2\) (as in the slide’s counting argument).

For any planar graph,

\[
e \le 3v - 6.
\]

Using Euler’s formula, one obtains bounds such as \(f \le \frac{2}{3}e\) and \(f \le 2v - 4\). If every vertex has degree at least 3 (e.g. polyhedral graphs), then \(3v \le 2e\), hence \(e \le 3f - 6\) and \(v \le 2f - 4\). These are all **linear** relations.

![Figure from slide 26](images/slide_026.png)

### Slide 27: Polyhedron (3D)

In 3D Euclidean space, a **polyhedron** is a finite set of planar polygons such that every edge belongs to **exactly two** facets and no proper subset of polygons has the same property (rules out “union of separate pieces”). The polygons are **facets**; edges and vertices are standard.

A polyhedron is **simple** if no two non-adjacent facets share a point. A simple polyhedron partitions \(\mathbb{R}^3\) into interior and exterior. It is **convex** if its interior is convex.

The surface is isomorphic to a planar subdivision on a sphere, so \((v,e,f)\) again satisfy **\(v - e + f = 2\)**.

### Slide 28: Convex vs. reflex vertices

A polygon vertex is **convex** if its interior angle is **\(\le \pi\)** (\(180^\circ\)); **reflex** if the interior angle is **\(> \pi\)**. In a convex polygon, every vertex is convex.

![Figure from slide 28](images/slide_028.png)

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
