import vedo
# import pyvista

import square_functions


# vedo

# earth
def cube():
    points = [(0,0,0),(1,0,0),(1,1,0),(0,1,0)]
    square = vedo.Line(square_functions.unit_square_3d(), closed=True)
    print(square_functions.unit_square_3d())
    # print(points)
    vedo.show(square, axes=1).close()

# fire
def tetrahedron():
    print("tetrahedron")

# air
def octahedron():
    print("octahedron")

# water
def icosahedron():
    print("icosahedron")

def dodecahedron():
    print("dodecahedron")

cube()