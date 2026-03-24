# Gift Wrapping in Higher Dimensions

**Slides covered:** 264–289  

**Topic folder:** 03 Convex Hulls


## Fast take

- Generalize gift wrapping from edges in 2D to **facets** in higher dimensions.
- The algorithm grows the hull by discovering adjacent facets across shared subfacets.
- In 3D, think in terms of facets, edges as subfacets, and supporting planes.
- The method is output-sensitive in spirit, but dimensional growth makes it expensive fast.

## Recording notes

**Recording references:** `CS 564 - 03.06 13.1.txt`, `CS 564 - 03.06 13.2.txt`

- The lecture stayed close to the 3D picture even though the definitions are d-dimensional. That is the only way this remains human-readable.
- You need the terminology clean: **facet**, **subfacet**, **supporting hyperplane**, **simplex**, and adjacency between facets.
- The algorithm is elegant, but higher dimensions punish runtime brutally. That is why it shows up as a project-worthy method.
- This is the natural generalization of wrapping, except the geometry gets meaner every time the dimension increases.


## Motivation

For \(d > 2\), the convex hull is no longer just a cycle of vertices. The algorithm wraps facets instead of edges, so the ideas from 2D survive but the bookkeeping becomes much nastier.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 264: Convex hull in \(E^d\)

**CONVEX HULL, \(d>2\)**  
**INSTANCE:** \(S = \{p_1,\ldots,p_N\} \subset E^d\), with \(p_i = (x_1,\ldots,x_d)\).  
**QUESTION:** Construct \(H(S)\).

For \(d=2\) the output was an **ordered vertex cycle**. For \(d>2\) we need a **boundary representation** (facets and adjacency).

### Slide 265: Polyhedron in \(E^3\)

Finite set of planar polygons: each edge belongs to **exactly two** facets; no proper sub-collection duplicates that property. **Facets** = polygons; **simple** polyhedron: no two non-adjacent facets share a point; interior/exterior partition \(\mathbb{R}^3\). **Convex** if interior is convex. Often “polyhedron” means boundary \(\cup\) interior.

### Slide 266: Polytopes

A **closed half-space** is one side of a hyperplane. A **polyhedral set** = intersection of finitely many closed half-spaces (hence **convex**). Bounded \(d\)-dimensional polyhedral sets are **polytopes** (“\(d\)-polytope”, “convex \(d\)-polytope” are synonymous).

**Theorem:** \(H(S)\) for finite \(S \subset E^d\) is a convex \(d\)-polytope; conversely every polytope is \(H(S)\) for some finite \(S\). For \(d=3\), \(H(S)\) is a convex polyhedron.

### Slide 267: Affine hull

Affine combination: \(p = \sum_{j=1}^k \alpha_j p_j\) with \(\sum_j \alpha_j = 1\). For \(k=2\): line; \(k=3\): plane; generally a flat of dimension \(\le k-1\). **Affine hull** \(\operatorname{aff}(L)\) = smallest affine set containing \(L\). Points are **affinely independent** if no proper subset generates the same affine hull.

### Slide 268: Faces of a polytope

| Dimension | Name (general \(d\)-polytope) |
|-----------|------------------------------|
| \(d\) | \(d\)-face = polytope itself |
| \(d-1\) | **facet** |
| \(d-2\) | **subfacet** (ridge) |
| \(1\) | **edge** |
| \(0\) | **vertex** |

For a **3-polytope:** facets are 2D polygons, subfacets are edges.

### Slide 269: Simplex

A **\(d\)-simplex** is the convex hull of **\(d+1\)** affinely independent points. Each subset of vertices spans a face. Examples: segment, triangle, tetrahedron for \(d=1,2,3\).

![Figure from slide 269](images/slide_269.png)

### Slide 270: Simplicial polytope

A \(d\)-polytope is **simplicial** if every **facet** is a \((d-1)\)-simplex. In 3D: every facet is a **triangle**; if a facet has \(>3\) coplanar vertices, the hull is **not** simplicial.

![Figure from slide 270](images/slide_270.png)

### Slide 271: Beneath / beyond

Facet \(F\) has supporting hyperplane \(\operatorname{aff}(F)\). Point \(p\) is **beneath** \(F\) if \(p\) lies in the **open** half-space on the same side as the polytope’s interior; **beyond** if in the other open half-space.

*(Text §3.4 erratum: “the P” should be “p”.)*

![Figure from slide 271](images/slide_271.png)

### Slide 272: History and idea

**Gift wrapping:** Chand–Kapur (1970); analyzed Bhattacharya (1982); 2D specialization = **Jarvis** (1973).

Given one **facet** (\((d-1)\)-face) of \(H(S)\), **rotate** a \((d-1)\)-dimensional affine hull around a **subfacet** to find the **adjacent** facet. Repeat until all facets are known. \(d=3\): wrap a 2D “sheet” around the hull; \(d=2\): wrap a line (Jarvis).

### Slide 273: Simplicial assumption; adjacency

Assume \(H(S)\) is **simplicial**: each facet is a \((d-1)\)-simplex on exactly \(d\) vertices. No extra points of \(S\) coplanar with those \(d\) vertices on the facet.

**Theorem (simplicial):** Each **subfacet** (ridge) lies in **exactly two** facets. Facets \(F_1,F_2\) are **adjacent on** subfacet \(e\) iff \(e\) is determined by the **\(d-1\) vertices common** to the vertex sets of \(F_1\) and \(F_2\).

For \(d=3\): an **edge** is shared by **two** triangular facets; adjacent facets share **two** vertices.

### Slide 274: Adjacent facet in general

Known facet \(F_1\) of \(H(S)\) with subfacets. To advance across subfacet \(e\) to adjacent facet \(F'\): among points \(p' \in S\) not vertices of \(F\), choose \(p'\) so **all** of \(S\) lies **beneath** \(\operatorname{aff}(e \cup \{p'\})\) — i.e. the hyperplane through \(e\) and \(p'\) makes the **largest** feasible “hinge angle” with \(\operatorname{aff}(F)\).

![Figure from slide 274](images/slide_274.png)

### Slide 275: Example \(d=3\)

Among planes through fixed edge \(e\) and each candidate point, pick the one forming the largest **convex** angle \(<\pi\) with \(\operatorname{aff}(F)\).

![Figure from slide 275](images/slide_275.png)

### Slides 276–277: Cotangent comparison

Per advance: **\(O(d^3 + Nd)\)** — **\(O(d^3)\)** once for a helper vector; **\(O(Nd)\)** to evaluate/compare candidates.

Let \(\mathbf{n}\) be a **unit normal** to \(F\) pointing into the half-space **beneath** \(\operatorname{aff}(F)\). Let \(\mathbf{a}\) be a unit vector orthogonal to edge \(e\) and to \(\mathbf{n}\), oriented consistently (slide: like \(\mathbf{n} \times \overrightarrow{p_2p_1}\)). For candidate \(p_k\), set \(\mathbf{v}_k = \overrightarrow{p_2 p_k}\).

Compare angles via **cotangents**. With dot products as on the slide,

\[
\rho_k = -\frac{\mathbf{v}_k \cdot \mathbf{a}}{\mathbf{v}_k \cdot \mathbf{n}};
\]

choose \(p_i\) that **maximizes** \(\rho_k\) among feasible \(p_k\) (details in text; avoid degenerate \(\mathbf{v}_k \cdot \mathbf{n} = 0\)).

![Figure from slide 277](images/slide_277.png)

### Slide 278: Algorithm outline

Start from an **initial facet**; for each subfacet, generate the **neighbor** facet; maintain a **pool** of subfacets that are **candidates** (shared by **exactly one** constructed facet so far).

### Slide 279: Pseudocode sketch

- Queue \(Q\) of facets to process; file \(\mathcal{I}\) of candidate subfacets.  
- Find initial facet \(F\); enqueue \(F\); insert all subfacets of \(F\) into \(\mathcal{I}\).  
- While \(Q \neq \emptyset\): dequeue \(F\); for each subfacet \(e\) of \(F\) that is still a candidate, **wrap** to neighbor facet \(F'\); update \(\mathcal{I}\) and enqueue \(F'\).

Still needed: (2) find initial facet; (7) list subfacets of \(F\); (8) test candidate membership.

### Slide 280: Supporting hyperplanes

Supporting **line** in 2D / **plane** in 3D: hyperplane touching the polytope with the body on one side. Intersection dimension with the polytope can be vertex, edge, or facet depending on \(d\).

![Figure from slide 280](images/slide_280.png)

### Slides 281–284: Initial facet

Build supporting hyperplanes \(\pi_1,\ldots,\pi_d\) where \(\pi_i\) shares **\(i\)** vertices with \(H(S)\). \(\pi_0\) is informal “no contact”; \(\pi_d = \operatorname{aff}(F)\) for a true facet.

For \(d=3\): \(\pi_1\) touches at a vertex; \(\pi_2\) rotates to contain an edge; \(\pi_3\) contains a facet.

Start from \(p_1'\) with **minimum** \(x_1\)-coordinate (a hull vertex). Take \(\pi_1\) orthogonal to \((1,0,\ldots,0)\) through \(p_1'\). Iteration \(j\): given \(\pi_{j-1}\) through \(p_1',\ldots,p_{j-1}'\), choose \(p_j'\) so \(\pi_j\) makes **largest angle** with \(\pi_{j-1}\). Each iteration **\(O(Nd) + O(d^2)\)**; **\(d\)** iterations → **\(O(Nd^2 + d^3) = O(Nd^2)\)** for step 2.

![Figure from slide 283](images/slide_283.png)

![Figure from slide 284](images/slide_284.png)

### Slide 285: Generate subfacets (step 7)

Simplicial facet has **\(d\)** vertices; each \((d-1)\)-subset is a **subfacet**. Enumerate in **\(O(d^2)\)**. Store facet as length-\(d\) index vector; subfacet as length-\((d-1)\) vector (vertices in an array).

### Slides 286–287: Candidate test (step 8)

A subfacet is a **candidate** iff it appears in **only one** constructed facet so far (the other adjacent facet is unknown). Maintain \(\mathcal{I}\) in a **balanced BST** keyed by lexicographic \((d-1)\)-tuple of vertex indices: insert if new, delete if seen twice. Each op **\(O((d-1)\log M)\)** for \(M\) subfacets stored.

![Figure from slide 286](images/slide_286.png)

### Slides 288–289: Complexity summary

Let \(\phi_{d-1}\) = number of facets, \(\phi_{d-2}\) = number of subfacets of \(H(S)\).

- Initialization (steps 1–4): **\(O(Nd^2)\)**.  
- Per-facet queue I/O: **\(O(d\,\phi_{d-1})\)**.  
- Subfacet generation: **\(O((d-1)\,\phi_{d-2})\)** (each ridge twice).  
- Subfacet tree ops: **\(O((d-1)\log\phi_{d-2} \cdot \phi_{d-2})\)**.  
- Gift-wrapping steps: **\(O((d^3 + Nd)\,\phi_{d-1})\)**.

Using \(\phi_{d-1}, \phi_{d-2} = O(N^{\lfloor d/2\rfloor})\) (upper bound theorem style):

\[
T(d,N) = O\bigl(N^{\lfloor d/2\rfloor + 1} + N^{\lfloor d/2\rfloor}\log N\bigr).
\]

Here \(d\) appears in the **exponent** of \(N\) even when treated as a constant in asymptotic notation.

## Recap

- In \(d>2\), \(H(S)\) is a **convex polytope**; boundary faces range from **vertices** to **facets** (\((d-1)\)-faces); **simplicial** hulls have every facet a \((d-1)\)-simplex.
- **Gift wrapping:** from a known **facet**, pivot around a **ridge** (subfacet) to the adjacent facet by choosing the supporting hyperplane through that ridge and the “best” point (e.g. **cotangent** comparison in 3D).
- **Initialization** builds a supporting facet by a sequence of **\(d\)** hyperplane refinements in **\(O(N d^2)\)**-style cost.
- **Complexity (slides):** worst-case time **\(T(d,N) = O(N^{\lfloor d/2\rfloor+1} + N^{\lfloor d/2\rfloor}\log N)\)** using bounds on numbers of faces/subfacets.
