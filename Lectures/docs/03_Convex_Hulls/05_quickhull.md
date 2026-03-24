# Quickhull

**Slides covered:** 225–234  

**Topic folder:** 03 Convex Hulls

## Motivation

Quickhull copies the divide-and-prune spirit of Quicksort. It splits the point set by a line through extreme points and recurses on the outside subsets.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 225: Quicksort analogy

Quicksort **partitions** an array so every element of the left part is \(\le\) every element of the right part, then recurses. Pointers move inward, swap on violation, place the pivot, and recurse. **Expected** time \(O(N\log N)\) with balanced splits; **worst case** \(O(N^2)\) if splits are skewed.

![Figure from slide 225](images/slide_225.png)

### Slide 226: Quickhull overview

Quickhull **recursively partitions** the point set \(S\) and assembles \(H(S)\) by **concatenating** hulls from subproblems (same high-level pattern as Quicksort).

### Slide 227: Initial partition

Let \(\ell, r \in S\) be points with **minimum** and **maximum** abscissa. Line \(L\) through \(\ell,r\) splits \(S\) into:

- \(S^{(1)}\): points **on or above** \(L\).  
- \(S^{(2)}\): points **on or below** \(L\).

\(\{S^{(1)}, S^{(2)}\}\) is not a strict partition (\(\ell,r\) lie in both); that is fine. Compute \(H(S^{(1)})\), \(H(S^{(2)})\), then concatenate to get \(H(S)\). By symmetry, describe the process for \(S^{(1)}\).

![Figure from slide 227](images/slide_227.png)

### Slide 228: Apex \(h\)

Choose \(h \in S^{(1)}\) so that:

1. Triangle \(\triangle h\ell r\) has **maximum area** among \(\{\triangle p\ell r : p \in S^{(1)}\}\).  
2. If several tie, choose the one maximizing angle \(\angle h\ell r\).

Then \(h \in H(S)\): the line \(L'\) through \(h\) parallel to \(L\) has no points of \(S^{(1)}\) above it; on \(L'\), \(h\) is leftmost among ties, so \(h\) is not a convex combination of two others in \(S\).

Finding \(h\) is **\(O(|S^{(1)}|)\)** by scanning.

![Figure from slide 228](images/slide_228.png)

### Slide 229: Subproblems

Directed lines \(L_1: \ell \to h\) and \(L_2: h \to r\). Classify each point of \(S^{(1)}\) (point–line tests). No point lies left of **both** \(L_1\) and \(L_2\). Points right of **both** lie inside \(\triangle h\ell r\) and are **discarded**.

- \(S^{(1,1)}\): points left of \(L_1\).  
- \(S^{(1,2)}\): points left of \(L_2\).

![Figure from slide 229](images/slide_229.png)

### Slide 230: Recursion

Recurse on \((S^{(1,1)}, \ell, h)\) and \((S^{(1,2)}, h, r)\). When a subproblem has no interior points, segment \(\overline{\ell r}\) is a hull **edge**.

![Figure from slide 230](images/slide_230.png)

### Slide 231: Primitives

1. Point–line classification.  
2. Triangle area (or equivalent orientation tests).  

Both **\(O(1)\)** per test.

### Slide 232: Avoiding duplicate \(\ell,r\) in both hulls

To keep \(\ell,r\) from appearing in both upper and lower hull merges, use \(\ell_0 = (x_0,y_0)\) = leftmost point of \(S\) and **synthetic** \(r_0 = (x_0, y_0 - \varepsilon)\) for tiny \(\varepsilon > 0\), then remove \(r_0\) from the final vertex list.

![Figure from slide 232](images/slide_232.png)

### Slide 233: Pseudocode

Assume \(|S| \ge 2\). **`FURTHEST(S, l, r)`** returns the apex \(h\) as above. List concatenation is `||`.

```
procedure QUICKHULL(S, l, r)
  if S = {l, r} then return (l, r)    /* edge lr */
  else
    h ← FURTHEST(S, l, r)
    S₁ ← { p ∈ S : p on or left of line lh }
    S₂ ← { p ∈ S : p on or left of line hr }
    return QUICKHULL(S₁, l, h) || (QUICKHULL(S₂, h, r) minus duplicate h)
  endif
end

/* Initial call */
l₀ ← point of S with smallest x
r₀ ← (x₀, y₀ − ε)
result ← QUICKHULL(S, l₀, r₀) with r₀ removed
```

### Slide 234: Analysis

- **Worst-case time:** **\(O(N^2)\)** — each level may take \(O(N)\) to partition, and recursion depth can be \(O(N)\) if splits are unbalanced.  
- **Expected time:** **\(O(N \log N)\)** under typical randomness assumptions (analogous to Quicksort).  
- **Storage:** can grow **\(O(N^2)\)** in the worst case (same imbalance issue).

Balanced splits would give \(O(N \log N)\) worst case, but Quickhull does not guarantee balance.

## Recap

- Keep the formal problem statement precise.
- Focus on the geometric invariant used by the method.
- Remember the key complexity bound and when it applies.
