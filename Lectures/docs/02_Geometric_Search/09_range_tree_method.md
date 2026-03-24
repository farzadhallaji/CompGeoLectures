# Range Searching by the Range Tree Method

**Slides covered:** 174–180  

**Topic folder:** 02 Geometric Search

## Motivation

A range tree combines segment-tree style decomposition with ordered secondary structures. It is one of the standard clean solutions for orthogonal range searching.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 174: Definition

A **range tree** is a **segment tree** on **\(x\)** (semi-closed scopes \([i,j)\)) where each node’s allocation list \(A(v)\) is replaced by a **threaded binary search tree** on **\(y\)** holding exactly those points of \(S\) whose **\(x\)** lies in \(v\)’s scope interval, sorted by \(y\).

For \(S=\{p_1,\ldots,p_N\}\) sorted by \(x\), the primary tree is **\(T(1,N+1)\)** in half-open indexing (node \([i,j)\) **excludes** right endpoint \(p_j\) in the slide convention).

![Figure from slide 174](images/slide_174.png)

### Slide 175: `SearchRangeTree`

To query \(R = [\ell_x,r_x] \times [\ell_y,r_y]\), call `SearchRangeTree(lx, rx+1, ly, ry, root)` to match semi-closed \(x\)-intervals.

At node \(v\):

- If \([B(v),E(v))\) is **fully contained** in \([\ell_x,r_x)\), search \(v\)’s **allocation tree** for all points with \(y \in [\ell_y,r_y]\).  
- Else recurse to children whose \(x\)-intervals intersect \([\ell_x,r_x)\) (standard segment-tree descent with \(\lfloor(B+E)/2\rfloor\) splits).

The **`rx+1`** in the initial call aligns closed input \(r_x\) with half-open primary intervals.

### Slide 176: Analysis and bridging trick

- **Preprocessing:** **\(O(N\log N)\)**.  
- **Query:** **\(O((\log N)^2 + K)\)** — \(O(\log N)\) canonical nodes for the \(x\)-range, each with an \(O(\log N)\) \(y\)-search.  
- **Storage:** **\(O(N\log N)\)** (Preparata p. 86).

**Improvement:** **Bridged range tree** achieves **\(O(\log N + K)\)** query by replacing most allocation BSTs with **\(y\)-sorted lists** linked so one binary search at the root supplies start positions; other levels **scan** in \(O(K)\) along threads.

### Slides 177–179: Figures

![Figure from slide 177](images/slide_177.png)

### Slide 180: Topic summary table (partial on slide)

The slide begins a summary of polygon inclusion, point location, and range methods with preprocessing/query/storage columns (truncated in source export). Use the per-section notes in this site for full bounds.

## Recap

- **Range tree:** **segment tree on \(x\)** (half-open scopes \([i,j)\)) with each node’s **associated structure** = **BST (or sorted list) on \(y\)** for points whose \(x\) falls in that scope; primary tree is **\(T(1,N+1)\)** in the slide indexing.
- **Query:** decompose \([ \ell_x, r_x ]\) into **\(O(\log N)\)** canonical nodes; each does a **\(y\)-range search** — **\(O((\log N)^2 + K)\)** total.
- **Preprocess** **\(O(N\log N)\)**; **storage** **\(O(N\log N)\)**; **bridged** variant drops to **\(O(\log N + K)\)** query by threading \(y\)-lists and reusing one binary search.
