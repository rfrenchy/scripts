import vedo
import adaptors.vedo

# earth
def cube():
    points = adaptors.vedo.square()
    square = vedo.Line(points, closed=True)

    # print(square_functions.unit_square_3d())

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

# cosmos
def dodecahedron():
    print("dodecahedron")

cube()