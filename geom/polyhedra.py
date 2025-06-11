import vedo
import adaptors.vedo
import numpy as np

# earth
def cube():
    points = adaptors.vedo.square()
    square = vedo.Line(points, closed=True)
    points2 = adaptors.vedo.square() @ adaptors.vedo.rotate(90, 0, 0).T
    square2 = vedo.Line(points2, closed=True)
    points3 = adaptors.vedo.square() @ adaptors.vedo.rotate(0, -90, 0).T
    square3 = vedo.Line(points3, closed=True)

    vedo.show(square, square2, square3, axes=1).close()

# fire
def tetrahedron():
    print("tetrahedron")

# air
def octahedron():
    print("octahedron")

# water
def icosahedron():
    print("icosahedron")

# cosmos
def dodecahedron():
    print("dodecahedron")

cube()