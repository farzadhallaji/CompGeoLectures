# Lectures index


## Fast take

- These notes cover **slides 9–289** of `comp_geometry_slides.pdf`.
- Each lecture file now starts with a **Fast take** and **Recording notes** section for quicker review.
- Use the files in order: **Foundations → Geometric Search → Convex Hulls**.
- The detailed slide-by-slide notes remain below the short summaries in each file.

## Recording notes

- The refined version is meant to be skim-friendly first and detailed second.
- Recording-based notes were merged into the lecture files so the pages read more like real lecture notes and less like a cleaned OCR dump.
- If you are studying for homework or exams, start with the Fast take, then jump to the detailed section only where you still have gaps.
- Because apparently humans enjoy revisiting the same course topic from three different angles before it sticks.

These notes cover slides 9–289 of `comp_geometry_slides.pdf`, stopping before the proximity topic starts at slide 290.

The structure is topic folder → one markdown file per major subtopic or algorithm. Formulas use LaTeX rendered with MathJax (inline `\( ... \)`, display `\[ ... \]`).

## How to use these notes

- Start with **Fast take** if you want the shortest useful version.
- Read **Recording notes** for lecturer emphasis, pitfalls, and what matters in practice.
- Use the detailed section when you need formulas, proofs, pseudocode, or slide-level detail.
- The files are ordered to match the course flow from basics to search to convex hulls.

## 01 Foundations

- [Coordinate Systems and Basic Geometric Objects](01_Foundations/01_coordinate_systems_and_basic_objects.md)
- [Polygons, Convexity, Planar Graphs, and Polyhedra](01_Foundations/02_polygons_convexity_planar_graphs_and_polyhedra.md)
- [Complexity Basics and Segment Trees](01_Foundations/03_complexity_basics_and_segment_trees.md)
- [Planar Straight Line Graphs and the DCEL](01_Foundations/04_pslg_and_dcel.md)
- [Vector Algebra and Trigonometry](01_Foundations/05_vector_algebra_and_trigonometry.md)
- [Orientation, Determinants, Area, and Point-Line Classification](01_Foundations/06_orientation_determinants_area_and_point_line_classification.md)

## 02 Geometric Search

- [Geometric Search Overview and Polygon Inclusion](02_Geometric_Search/01_overview_and_polygon_inclusion.md)
- [Point Location: Brute Force, Slab Method, and Plane Sweep](02_Geometric_Search/02_point_location_bruteforce_slab_and_plane_sweep.md)
- [Point Location by the Chain Method](02_Geometric_Search/03_point_location_chain_method.md)
- [Point Location by the Triangle Refinement Method](02_Geometric_Search/04_point_location_triangle_refinement_method.md)
- [Range Searching Overview and the Grid Method](02_Geometric_Search/05_range_searching_overview_and_grid_method.md)
- [Range Searching by the Quadtree Method](02_Geometric_Search/06_range_searching_quadtree_method.md)
- [Range Searching by the k-D Tree Method](02_Geometric_Search/07_range_searching_kd_tree_method.md)
- [Range Searching by Direct Access Methods](02_Geometric_Search/08_range_searching_direct_access_methods.md)
- [Range Searching by the Range Tree Method](02_Geometric_Search/09_range_tree_method.md)

## 03 Convex Hulls

- [Convex Hull Overview, Definitions, and Lower Bounds](03_Convex_Hulls/01_overview_definitions_and_lower_bounds.md)
- [Extreme Points Algorithm](03_Convex_Hulls/02_extreme_points_algorithm.md)
- [Graham’s Scan](03_Convex_Hulls/03_grahams_scan.md)
- [Jarvis’ March](03_Convex_Hulls/04_jarvis_march.md)
- [Quickhull](03_Convex_Hulls/05_quickhull.md)
- [Divide-and-Conquer Convex Hull](03_Convex_Hulls/06_divide_and_conquer.md)
- [Dynamic Hull Maintenance Under Insertion](03_Convex_Hulls/07_dynamic_hull_insertion.md)
- [Gift Wrapping in Higher Dimensions](03_Convex_Hulls/08_gift_wrapping_in_higher_dimensions.md)
