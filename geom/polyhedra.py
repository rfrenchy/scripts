import vedo
import adaptors.vedo as av
import numpy as np
import math

import circle_functions as cf

### platonic solids

## constants


def vedo_plot(*p, axes=0):
    vedo.show(p, axes)

def circle():
    TOTAL_POINTS = 100

    segments = (np.pi*2)/ TOTAL_POINTS

    x = [np.cos(i*segments) for i in range(TOTAL_POINTS)]
    y = [np.sin(i*segments) for i in range(TOTAL_POINTS)]
    z = np.zeros(TOTAL_POINTS)

    p = [(x[i], y[i], z[i]) for i in range(TOTAL_POINTS)]

    vedo.show(vedo.Line(p, closed=True)).close()

def spiral(increase_arc = False):
    TOTAL_POINTS = 100   # total points
    R = 0.1              # radius
    osc = 5                # oscillations

    S = 0.1 # how many segments in an oscilation
    L = []
    start = 0           # start point of oscilation
    stop = TOTAL_POINTS # end point of oscilation

    r = R
    for _ in range(osc):
        X = []
        Y = []
        Z = []

        for i in range(start, stop):
            X.append((r*i) * np.cos(i*S))
            Y.append((r*i) * np.sin(i*S))
            Z.append(0)

            # incress growth arc
            if increase_arc:
                r = r + R
                

        # add to list of lines to show
        L.append(vedo.Line([(X[i], Y[i], Z[i]) for i in range(TOTAL_POINTS)]))

        # reset start and stop range for next oscillation (-1 to start from end of last oscillation)
        start = stop - 1                 
        stop  = stop + TOTAL_POINTS - 1  
        
    vedo.show(L).close()

#    vedo.show(vedo.Line(p)).close()

# earth
def cube():
    # center of universe
    center = vedo.Point((0,0,0))

    # Create points
    pts1 = av.square()
    pts2 = av.square() @ av.rotate(90,0,0)
    pts3 = av.square() @ av.rotate(0,-90,0)

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

def wheel():
    print("wheel")

# fire
def tetrahedron():
    unkn = 30 # right triangle angle

    pts1 = av.equilateral_triangle()
    pts1r = pts1 @ av.rotate(unkn,0,0)
    face1 = vedo.Line(pts1r, closed=True)

    pts2 = av.equilateral_triangle()
    pts2r = pts2 @ av.rotate(-unkn,-90,0)
    face2 = vedo.Line(pts2r, closed=True)

    pts3 = av.equilateral_triangle()
    pts3r = pts3 @ av.rotate(-unkn,0,0)
    pts3r_translate = [(x,y,z-1) for x,y,z in pts3r]
    face3 = vedo.Line(pts3r_translate, closed=True)

    pts4 = av.equilateral_triangle()
    pts4r = pts4 @ av.rotate(unkn,-90,0)
    pts4r_translate = [(x+1,y,z) for x,y,z in pts4r]
    face4 = vedo.Line(pts4r_translate, closed=True)

    return pts1r,pts2r,pts3r_translate,pts4r_translate


# air
def octahedron():
    # top faces
    P = tetrahedron()
    faces_top = [vedo.Line(p, closed=True) for p in P]

    # bottom faces
    M = np.array([])
    for p in P:
        M = np.append(M, vedo.Line([(x,y*-1,z) for x,y,z in p], 
                                   closed=True))
    
    # the four individuals faces on the bottom half of octahedron
    fb1, fb2, fb3, fb4 = M.ravel()

    # show octahedron on screen
    vedo.show(faces_top, fb1, fb2, fb3, fb4).close()


# water
def icosahedron():
    print("icosahedron")

# cosmos
def dodecahedron():
    print("dodecahedron")

# cube()
# octahedron()
spiral(increase_arc=True)
# circle()