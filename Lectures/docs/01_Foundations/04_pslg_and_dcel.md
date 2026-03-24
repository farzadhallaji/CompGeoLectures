# Planar Straight Line Graphs and the DCEL

**Slides covered:** 45–51  

**Topic folder:** 01 Foundations

## Motivation

A PSLG is the standard way to represent planar subdivisions. The DCEL is the classic data structure used to store edges, faces, and adjacency so algorithms can move around the subdivision efficiently.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 45: Example subdivision

Labeled edges, vertices, and faces in a sample PSLG (see figure).

![Figure from slide 45](images/slide_045.png)

### Slide 46: Planar straight line graph (PSLG)

A **planar straight line graph** is a planar embedding of a planar graph \(G = (V,E)\) such that:

1. Each vertex \(v \in V\) is mapped to a **distinct** point in the plane.
2. Each edge \(e \in E\) is mapped to a **straight segment** between the images of its endpoints.
3. Segments intersect **only** at shared endpoints (no crossings in the interior).

Thus a PSLG maps a combinatorial object (planar graph) to a geometric one; **coordinates** enter at this step.

![Figure from slide 46](images/slide_046.png)

### Slide 47: DCEL edge record

The **doubly-connected edge list (DCEL)** represents a PSLG with **one record per directed edge** (often two per undirected edge, one for each direction).

Each **edge record** has six fields (naming follows the slides):

| Field | Role |
|-------|------|
| \(V_1\) | **Origin** of the directed edge |
| \(V_2\) | **Terminus** (destination) — fixes orientation \(V_1 \to V_2\) |
| \(F_1\) | Face **to the left** of the directed edge |
| \(F_2\) | Face **to the right** of the directed edge |
| \(P_1\) | Index of the next edge **counterclockwise** around \(V_1\) after this edge |
| \(P_2\) | Index of the next edge **counterclockwise** around \(V_2\) after this edge |

(Variants in textbooks use `next`, `prev`, `twin`; the slide uses \(P_1,P_2\) for predecessor/next navigation around vertices.)

![Figure from slide 47](images/slide_047.png)

### Slide 48: Numeric example

The slide gives a full table of DCEL records: for each edge index, values of \(V_1, V_2\), left/right faces, and predecessor/successor edge indices. **See the figure** for the geometry and the slide image for the complete row listing.

![Figure from slide 48](images/slide_048.png)

### Slide 49: Storage and auxiliary arrays

If the PSLG has \(N\) vertices, \(M\) edges, and \(F\) faces, **Euler’s formula** gives \(N - M + F = 2\).

The DCEL can be stored in six arrays of length \(M\), e.g. \(V_1[i], V_2[i], \text{LeftF}[i], \text{RightF}[i], \text{PredE}[i], \text{NextE}[i]\). Since \(M, F \in O(N)\) for planar graphs, total space is **\(O(N)\)**.

- **`HV[1:N]`** — For vertex \(v_i\), `HV[i]` points to **some** DCEL record where \(v_i\) appears as \(V_1\) or \(V_2\).
- **`HF[1:F]`** — For face \(f_i\), `HF[i]` points to **some** DCEL record where \(f_i\) is the left or right face.

Both `HV` and `HF` can be filled in **\(O(N)\)** time by scanning the DCEL arrays (must scan **both** \(V_1\) and \(V_2\), and both face columns — see slide 51).

**Operation:** **`EdgesIncident(v_j)`** — Walk the DCEL to report all edge indices incident to vertex \(v_j\), storing indices in an answer array \(A\).

### Slide 50: `EdgesIncident` pseudocode

```
/* Get first DCEL entry for v_j; a is an index. */
a0 ← a
A[1] ← a
i ← 2
if V1[a] = j then a ← PredE[a] else a ← NextE[a] endif
while a ≠ a0 do
  A[i] ← a
  if V1[a] = j then a ← PredE[a] else a ← NextE[a] endif
  i ← i + 1
endwhile
```

The walk cycles through incident edges using `PredE` / `NextE` depending on whether the current edge has \(v_j\) as origin or terminus (see diagram on slide).

![Figure from slide 50](images/slide_050.png)

### Slide 51: Text erratum and complexity

**Erratum (text p. 16):** Building `HV` and `HF` requires scanning **both** `V1` and `V2` (and both face columns), not `V1` alone — a vertex might appear only as a terminus.

**Time:** `EdgesIncident` is **\(O(\deg(v_j))\)** for the output size; in the worst case over vertices, **\(O(N)\)** in a planar graph.

**Planar facts:** (1) \(v - e + f = 2\); (2) \(e \le 3v - 6\); (3) \(f \le \frac{2}{3}e\); (4) \(f \le 2v - 4\). With \(v = N\), we have \(e \in O(N)\), so the DCEL has **\(O(N)\)** records and **\(O(N)\)** storage.

## Recap

- A **PSLG** embeds a planar graph with straight segments that meet only at endpoints.
- The **DCEL** stores **one directed edge record per edge** with \((V_1,V_2)\), left/right **faces** \((F_1,F_2)\), and **next** pointers around \(V_1\) and \(V_2\) (\(P_1,P_2\) / Pred–Next variants).
- **Euler** gives \(N - M + F = 2\); with \(M = O(N)\), the DCEL uses **\(O(N)\)** storage; **vertex** and **face** entry arrays (`HV`, `HF`) need scans of **both** \(V_1\) and \(V_2\) (and both face columns).
- **`EdgesIncident`** walks the cycle of edges around a vertex in time **proportional to the degree** reported ( \(O(N)\) worst case over the subdivision).
