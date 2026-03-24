# Vector Algebra and Trigonometry

**Slides covered:** 52–57  

**Topic folder:** 01 Foundations


## Fast take

- Treat vectors as translated segments: add, subtract, scale, and measure length.
- Vector subtraction is the clean way to move geometry to the origin.
- Direction is described by angle, but later algorithms usually avoid computing the angle explicitly.
- Sine and cosine facts are here mainly to support orientation-style reasoning.

## Recording notes

**Recording references:** `CS 564 - 01.30 3.1.txt`, `CS 564 - 01.30 3.2.txt`

- The lecture used vector subtraction as the bridge from geometry-on-the-plane to algebra-at-the-origin.
- Do not over-focus on slope. Vectors and coordinates survive vertical cases without the drama.
- Polar-angle language is helpful for explanation, but the instructor keeps replacing expensive angle computations with sign tests as soon as possible.
- This section is setup for determinants, left-turn tests, and hull sorting arguments later.


## Motivation

These slides build the algebra behind geometric tests. Vectors, scaling, subtraction, direction, sine, and cosine are the tools used later to tell where points and segments lie relative to each other.

## Lecture Roadmap

- Know the problem definition.
- Know the main geometric idea.
- Know the key data structure or primitive test.
- Know the preprocessing / query / storage or total running time.
- Know one small example by hand.

## Detailed lecture notes

### Slide 52: Points vs. vectors, addition

An ordered pair \((x,y)\) may denote a **point** in the plane or a **vector** from the origin.

**Vector addition.** For \(\mathbf{a} = (x_a, y_a)\) and \(\mathbf{b} = (x_b, y_b)\),

\[
\mathbf{a} + \mathbf{b} = (x_a + x_b,\; y_a + y_b).
\]

Geometrically, \(\mathbf{a}\) and \(\mathbf{b}\) span a parallelogram with vertices \(\mathbf{0}, \mathbf{a}, \mathbf{b}, \mathbf{a}+\mathbf{b}\).

![Figure from slide 52](images/slide_052.png)

### Slide 53: Scalar multiplication

For scalar \(t \in \mathbb{R}\) and \(\mathbf{b} = (x_b, y_b)\),

\[
t\mathbf{b} = (t x_b,\; t y_b).
\]

Length scales by \(|t|\); if \(t < 0\), direction reverses.

![Figure from slide 53](images/slide_053.png)

### Slide 54: Subtraction and length

**Subtraction:**

\[
\mathbf{b} - \mathbf{a} = \mathbf{b} + (-1)\mathbf{a} = (x_b - x_a,\; y_b - y_a).
\]

**Length** of \(\mathbf{a} = (x_a, y_a)\):

\[
\|\mathbf{a}\| = \sqrt{x_a^2 + y_a^2}.
\]

![Figure from slide 54](images/slide_054.png)

### Slide 55: Translation and canonical segments

Let \(\mathbf{a} = \overrightarrow{op}\) and \(\mathbf{b} = \overrightarrow{oq}\). Then \(\mathbf{b} - \mathbf{a}\) is the vector \(\overrightarrow{pq}\) placed at the origin. Segments with the same length and direction are **translates** of one another and correspond to the same vector from the origin.

![Figure from slide 55](images/slide_055.png)

### Slide 56: Polar angles

The **polar angle** \(\theta_{\mathbf{a}}\) of vector \(\mathbf{a}\) is the angle from the **positive \(x\)-axis** to \(\mathbf{a}\), measured **counterclockwise**, with \(\theta_{\mathbf{a}} \in [0^\circ, 360^\circ)\) (or use radians).

The **angle from \(\mathbf{a}\) to \(\mathbf{b}\)** , denoted \(\theta_{\mathbf{a}\mathbf{b}}\), is measured counterclockwise **starting along \(\mathbf{a}\)**.

![Figure from slide 56](images/slide_056.png)

### Slide 57: Sine and cosine on the unit circle

For angle \(\theta\) from the \(x\)-axis to point \((x,y)\) on the **unit circle** \(x^2 + y^2 = 1\):

\[
x = \cos\theta,\qquad y = \sin\theta.
\]

- If \(0^\circ < \theta < 180^\circ\), then \(y > 0\) and \(\sin\theta > 0\).  
- If \(180^\circ < \theta < 360^\circ\), then \(y < 0\) and \(\sin\theta < 0\).

![Figure from slide 57](images/slide_057.png)

## Recap

- Vectors support **addition** (parallelogram rule), **scalar multiplication** (length scales, sign flips direction), **subtraction** \(b-a\), and **Euclidean length** \(\sqrt{x^2+y^2}\).
- A segment \(\overrightarrow{pq}\) corresponds to the vector \(b-a\) when \(a,b\) are position vectors from the origin.
- **Polar angle** measures rotation from the \(x\)-axis CCW; the angle **from** \(\mathbf{a}\) **to** \(\mathbf{b}\) is measured starting along \(\mathbf{a}\).
- **\(\cos\theta\)** and **\(\sin\theta\)** come from the **unit circle**; sign of \(\sin\theta\) matches the sign of \(y\) for \(\theta\) in \((0^\circ,360^\circ)\).
