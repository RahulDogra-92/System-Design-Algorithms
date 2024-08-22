# Description:
# Ray casting is a technique used in computer graphics to determine which objects a ray intersects with, often used in rendering 3D scenes.

# Use Case: Line of sight calculations
# Python Example:

import numpy as np

def ray_intersects_triangle(p0, p1, triangle):
    epsilon = 0.000001
    vertex0, vertex1, vertex2 = triangle
    edge1 = vertex1 - vertex0
    edge2 = vertex2 - vertex0
    h = np.cross(p1 - p0, edge2)
    a = np.dot(edge1, h)
    if -epsilon < a < epsilon:
        return False
    f = 1 / a
    s = p0 - vertex0
    u = f * np.dot(s, h)
    if not 0 <= u <= 1:
        return False
    q = np.cross(s, edge1)
    v = f * np.dot(p1 - p0, q)
    if v < 0 or u + v > 1:
        return False
    t = f * np.dot(edge2, q)
    if t > epsilon:
        return True
    return False

# Define a triangle and a ray
