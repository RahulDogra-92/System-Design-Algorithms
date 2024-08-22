# Description:
# Quadtrees and R-Trees are data structures for indexing multi-dimensional data, especially useful for spatial data.

# Use Case: Spatial databases
# Python Example (Using Rtree):

from rtree import index

# Create an R-tree index
p = index.Property()
idx = index.Index(properties=p)

# Insert some rectangles (xmin, ymin, xmax, ymax)
rectangles = [(0, 0, 1, 1), (1, 1, 2, 2), (2, 2, 3, 3)]
for i, rect in enumerate(rectangles):
    idx.insert(i, rect)

# Query for rectangles that intersect a given bounding box
query_rect = (1.5, 1.5, 2.5, 2.5)
matches = list(idx.intersection(query_rect))
print("Intersecting rectangles:", matches)
