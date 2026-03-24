# Jarvis’ March

**Slides covered:** 220–224  

**Topic folder:** 03 Convex Hulls

## Motivation

Jarvis’ march, also called gift wrapping in 2D, walks from one hull vertex to the next by always choosing the most counterclockwise candidate. It is output-sensitive because its time depends on the number of hull vertices.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 220: Edges vs. Graham’s vertex view

Graham’s scan identifies **vertices** (with possible backtracking). Jarvis’ march finds **edges** of \(H(S)\).

**Theorem:** Segment \(\overline{pq}\) between two points of \(S\) is a **hull edge** iff **all** other points of \(S\) lie in the **closed halfplane** bounded by the line through \(p\) and \(q\) on one side of that line (collinearity allowed on the line).

![Figure from slide 220](images/slide_220.png)

### Slide 221: Naive \(O(N^3)\) edge finding

There are \(O(N^2)\) candidate lines from point pairs. For each, test the other \(N-2\) points with **point–line classification** — \(O(N)\) per line → **\(O(N^3)\)** to list all hull edges, then **\(O(N)\)** to order them around the hull.

**Improvement:** Once a hull edge \(pq\) is known, the next edge must **start** at \(q\). Reusing this cuts the worst-case work to **\(O(N^2)\)** (slide).

![Figure from slide 221](images/slide_221.png)

### Slide 222: Marching “up” the hull

Let \(p_1\) be the **rightmost lowest** point (minimum \(y\), then maximum \(x\)); \(p_1 \in H(S)\).

The next hull vertex \(p_2\) is the point of \(S\) with **smallest polar angle** \(\ge 0\) measured from the **positive \(x\)-axis** at \(p_1\). Similarly, \(p_3\) minimizes polar angle at \(p_2\), etc.

Each new vertex costs **\(O(N)\)** by scanning all of \(S\) (compare angles via **orientation** / cross products — no trig). This builds the hull from \(p_1\) “upward” along the boundary.

*(Slide notes a figure error in Preparata Fig. 3.9, p. 111.)*

![Figure from slide 222](images/slide_222.png)

### Slide 223: Marching “down”

On the other chain, measure polar angles relative to the **negative \(x\)-axis** (not the positive one) so comparisons stay consistent.

![Figure from slide 223](images/slide_223.png)

### Slide 224: Analysis

- **Worst-case time:** \(O(N^2)\) — at most \(N\) hull vertices, each step \(O(N)\).  
- **Storage:** \(O(N)\).

Let \(h = |H(S) \cap S|\) be the number of hull vertices. Actual work is **\(O(hN)\)** left/right tests. When \(h \ll N\), **\(O(hN)\)** beats Graham’s **\(O(N\log N)\)** when e.g. \(h < \log N\). If \(h = O(1)\), time is **linear** in \(N\).

**Intuition:** repeatedly “wrapping” with turning angles; generalizes to **gift wrapping** in \(d > 2\).

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
