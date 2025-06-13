import vedo
import adaptors.vedo
import numpy as np

# earth
def cube():
    # center of universe
    center = vedo.Point((0,0,0))

    # Create points
    pts1 = adaptors.vedo.square()
    pts2 = adaptors.vedo.square() @ adaptors.vedo.rotate(90,0,0)
    pts3 = adaptors.vedo.square() @ adaptors.vedo.rotate(0,-90,0)

    # First Face
    face1 = vedo.Line(pts1, closed=True)

    # Second Face
    pts1_translate = [(x,y,z-1) for x,y,z in pts1]
    face2 = vedo.Line(pts1_translate, closed=True)

    # Third Face
    face3 = vedo.Line(pts2, closed=True)

    # Fourth Face
    pts2_translate = [(x,y+1,z) for x,y,z in pts2]
    face4 = vedo.Line(pts2_translate, closed=True)
     
    # Fifth Face
    face5 = vedo.Line(pts3, closed=True)

    # Sixth Face
    pts3_translate = [(x+1,y,z) for x,y,z in pts3]
    face6 = vedo.Line(pts3_translate, closed=True)
     

    vedo.show(center,
        face1, face2,
        face3, face4,
        face5, face6
        # axes=1,
        ).close()

def spiral():
    print("spiral")

def wheel():
    print("wheel")

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