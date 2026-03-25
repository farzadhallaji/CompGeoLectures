# Computational Geometry midterm pack - complete markdown version

This pack is meant to stand on its own. The markdown files now include slide digestion, embedded figure crops from the main PDF, professor emphasis pulled from recordings when the transcript made one clear, and homework-style exam prompts placed in the relevant topic files.

## Scope
- Main source: `comp_geometry_slides_new.pdf`
- Included pages: **9-321** only
- Supporting sources folded in: lecture recording transcripts and the assigned homeworks

## How to study
- Read files in numeric order.
- In each file, do not just skim the summary. Study the slide-by-slide notes, then the `What you must be able to say/do in an exam` section, then the exam drills at the end.
- For algorithm files, memorize: problem statement, data structure, algorithm steps, invariant/correctness idea, and time/space bounds.
- For proof/lower-bound files, memorize the exact direction of the reduction or counting argument. Humans love reversing reductions and then acting surprised on exam day.

## Reading order
1. [Coordinate systems and basic geometric entities](01_Foundations/01_coordinate-systems-and-basic-entities.md) - pp. 9-18
2. [Polygonal geometry, convexity, planarity, and polyhedra](01_Foundations/02_polygonal-geometry-planarity-and-polyhedra.md) - pp. 19-28
3. [Computational models and complexity language](01_Foundations/03_models-and-complexity-language.md) - pp. 29-37
4. [Segment trees as a warm-up search structure](01_Foundations/04_segment-trees.md) - pp. 38-44
5. [Planar straight-line graphs and face-edge structure](01_Foundations/05_pslg-basics.md) - pp. 45-46
6. [DCEL representation and auxiliary structures](01_Foundations/06_dcel.md) - pp. 47-51
7. [Vector algebra and trigonometric groundwork](01_Foundations/07_vectors-and-trig-groundwork.md) - pp. 52-57
8. [Orientation tests and signed-area interpretation](01_Foundations/08_orientation-and-signed-area.md) - pp. 58-62
9. [Primitive formulas and summary](01_Foundations/09_primitive-formulas-summary.md) - pp. 63-65
10. [Search problem taxonomy and inclusion basics](02_Geometric_Search/10_search-taxonomy.md) - pp. 66-69
11. [Convex polygon inclusion by left test](02_Geometric_Search/11_convex-inclusion-left-test.md) - pp. 70-71
12. [Simple polygon inclusion by intersection counting](02_Geometric_Search/12_simple-polygon-inclusion-ray-shooting.md) - pp. 72-74
13. [Convex polygon inclusion by wedges](02_Geometric_Search/13_convex-inclusion-by-wedges.md) - pp. 75-77
14. [Star-shaped polygon inclusion by wedges](02_Geometric_Search/14_star-shaped-inclusion-by-wedges.md) - pp. 78-79
15. [Point location by slab decomposition](02_Geometric_Search/15_point-location-slab-method.md) - pp. 80-85
16. [Plane sweep as a recurring paradigm](02_Geometric_Search/16_plane-sweep-paradigm.md) - pp. 86-90
17. [Chain method: basics, definitions, and query idea](02_Geometric_Search/17_chain-method-basics-and-query.md) - pp. 91-101
18. [Chain method: regular PSLGs and constructing the chain family](02_Geometric_Search/18_chain-method-constructing-chains.md) - pp. 102-109
19. [Chain method: regularization of arbitrary PSLGs](02_Geometric_Search/19_chain-method-regularization.md) - pp. 110-115
20. [Chain method: analysis and wrap-up](02_Geometric_Search/20_chain-method-analysis.md) - pp. 116-117
21. [Triangle refinement: setup and triangulation](02_Geometric_Search/21_triangle-refinement-setup.md) - pp. 118-122
22. [Triangle refinement: hierarchy, query, storage, and analysis](02_Geometric_Search/22_triangle-refinement-query-and-analysis.md) - pp. 123-134
23. [Range searching: problem statement and design space](02_Geometric_Search/23_range-searching-intro.md) - pp. 135-137
24. [Grid method](02_Geometric_Search/24_grid-method.md) - pp. 138-141
25. [Quadtree method](02_Geometric_Search/25_quadtree-method.md) - pp. 142-151
26. [k-d tree method](02_Geometric_Search/26_kd-tree-method.md) - pp. 152-160
27. [Direct access methods](02_Geometric_Search/27_direct-access-methods.md) - pp. 161-173
28. [Range trees](02_Geometric_Search/28_range-trees.md) - pp. 174-179
29. [Range searching summary](02_Geometric_Search/29_range-searching-summary.md) - pp. 180-180
30. [Convex hull motivation and why the topic matters](03_Convex_Hulls/30_convex-hull-motivation.md) - pp. 181-182
31. [Convex hull intuition and preliminaries](03_Convex_Hulls/31_convex-hull-intuition.md) - pp. 183-185
32. [Convex combinations and dimension-sensitive definitions](03_Convex_Hulls/32_convex-combinations-and-dimension.md) - pp. 186-189
33. [Equivalent formulations and problem statement](03_Convex_Hulls/33_convex-hull-equivalent-formulations.md) - pp. 190-195
34. [Lower bound for convex hull via reduction from sorting](03_Convex_Hulls/34_convex-hull-lower-bound.md) - pp. 196-201
35. [Extreme points algorithm](03_Convex_Hulls/35_extreme-points-algorithm.md) - pp. 202-205
36. [Graham’s scan: concept and preparation](03_Convex_Hulls/36_graham-scan-algorithm.md) - pp. 206-214
37. [Graham’s scan: analysis, upper-lower hull view, and summary](03_Convex_Hulls/37_graham-scan-analysis.md) - pp. 215-219
38. [Jarvis march (gift wrapping) in 2D](03_Convex_Hulls/38_jarvis-march.md) - pp. 220-224
39. [Quickhull](03_Convex_Hulls/39_quickhull.md) - pp. 225-234
40. [Divide-and-conquer convex hulls and hull union](03_Convex_Hulls/40_divide-and-conquer-hull.md) - pp. 235-241
41. [Supporting lines from hull union](03_Convex_Hulls/41_supporting-lines.md) - pp. 242-244
42. [Dynamic/on-line convex hull insertion: problem setting and core idea](03_Convex_Hulls/42_dynamic-hull-core-idea.md) - pp. 245-253
43. [Dynamic/on-line convex hull insertion: data structure, search, update, and analysis](03_Convex_Hulls/43_dynamic-hull-data-structure.md) - pp. 254-263
44. [Gift wrapping in higher dimensions: background and setup](03_Convex_Hulls/44_higher-dimensional-hull-background.md) - pp. 264-271
45. [Gift wrapping in higher dimensions: algorithm and adjacent facets](03_Convex_Hulls/45_higher-dimensional-hull-algorithm.md) - pp. 272-279
46. [Gift wrapping in higher dimensions: supporting hyperplanes, initialization, candidates, and analysis](03_Convex_Hulls/46_higher-dimensional-hull-init-analysis.md) - pp. 280-289
47. [Proximity problem family: survey and relations](04_Proximity/47_proximity-problem-survey.md) - pp. 290-299
48. [Proximity lower bounds and transformations](04_Proximity/48_proximity-lower-bounds.md) - pp. 300-307
49. [Closest pair: problem setup and 1D version](04_Proximity/49_closest-pair-setup-1d.md) - pp. 308-313
50. [Closest pair: 2D merge step](04_Proximity/50_closest-pair-2d-merge.md) - pp. 314-319
51. [Closest pair: analysis and higher dimensions](04_Proximity/51_closest-pair-analysis.md) - pp. 320-321

## Folder map
- `convex-hulls/`
- `geometric-objects-notation-and-asymptotic-preliminaries/`
- `geometric-search/`
- `proximity/`
- `pslgs-dcels-vectors-and-geometric-primitives/`
- `images/` for figure crops used inside the notes