import vedo
import vedo.mesh
import adaptors.vedo as av
import numpy as np
import math

import circle_functions as cf

### platonic solids

## constants


def vedo_plot(*p, axes=0):
    vedo.show(p, axes)

def circle(show=False):
    TOTAL_POINTS = 100

    segments = (np.pi*2)/ TOTAL_POINTS

    x = [np.cos(i*segments) for i in range(TOTAL_POINTS)]
    y = [np.sin(i*segments) for i in range(TOTAL_POINTS)]
    z = np.zeros(TOTAL_POINTS)

    p = [(x[i], y[i], z[i]) for i in range(TOTAL_POINTS)]

    C = vedo.Line(p, closed=True)

    if show:
        vedo.show(vedo.Line(p, closed=True)).close()
    
    return C

def nothing():
    return

def show(lines):
    vedo.show(lines).close()

def spiral(increase_arc = False,
           r_growth = 0.1,
           z_growth = 0, 
           osc = 5,
           side_effects = nothing):


    TOTAL_POINTS = 100   # total points             

    S = 0.1 # how many segments in an oscilation
    L = []
    start = 0           # start point of oscilation
    stop = TOTAL_POINTS # end point of oscilation

    r = r_growth
    z = z_growth
    for _ in range(osc):
        X = []
        Y = []
        Z = []

        for i in range(start, stop):
            # cacl x and y of spiral
            X.append((r*i) * np.cos(i*S))
            Y.append((r*i) * np.sin(i*S))

            # add z_growth if any
            z+=z_growth
            Z.append(z)

            # incress growth arc
            if increase_arc:
                r = r + r_growth
                

        # add to list of lines to show
        L.append(vedo.Line([(X[i], Y[i], Z[i]) for i in range(TOTAL_POINTS)]))

        # reset start and stop range for next oscillation (-1 to start from end of last oscillation)
        start = stop - 1                 
        stop  = stop + TOTAL_POINTS - 1  
        
    side_effects(L)

def coil(side_effects=show, z_growth=0.01, oscilations=10):
    TOTAL_POINTS = 1000           # total points             
    osc = (np.pi*2) * oscilations # 3 oscilations
    seg = osc / TOTAL_POINTS      # all the angles to plot points on    

    # radius
    r = 1

    # vedo lines
    L = []

    # point arrays
    X = []
    Y = []
    Z = []

    # z loop variable
    z = z_growth

    for i in range(TOTAL_POINTS):
        X.append(r * np.cos(seg*i))
        Y.append(r * np.sin(seg*i))

        Z.append(z)
        z += z_growth

    L.append(vedo.Line([(X[i], Y[i], Z[i]) for i in range(TOTAL_POINTS)]))

    side_effects(L)



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

def wheel(total_spokes=7):
    # work out angle of each spoke 

    theta = (np.pi*2) / total_spokes

    # array of vedo lines
    spokes = []

    # work out points of each spoke
    for i in range(total_spokes):
        # work out point on circle
        x = np.cos(theta*i)
        y = np.sin(theta*i)
        z = 0

        # add spoke
        spokes.append(vedo.Line([(0,0,0),(x, y, z)]))

    # show
    vedo.show(circle, spokes).close()


# plato: fire
def tetrahedron(show=False):
    unkn = 30 # right triangle angle

    faces = []

    pts1 = av.equilateral_triangle()
    pts1r = pts1 @ av.rotate(unkn,0,0)
    faces.append(vedo.Line(pts1r, closed=True))

    pts2 = av.equilateral_triangle()
    pts2r = pts2 @ av.rotate(-unkn,-90,0)
    faces.append(vedo.Line(pts2r, closed=True))

    pts3 = av.equilateral_triangle()
    pts3r = pts3 @ av.rotate(-unkn,0,0)
    pts3r_translate = [(x,y,z-1) for x,y,z in pts3r]
    faces.append(vedo.Line(pts3r_translate, closed=True))

    pts4 = av.equilateral_triangle()
    pts4r = pts4 @ av.rotate(unkn,-90,0)
    pts4r_translate = [(x+1,y,z) for x,y,z in pts4r]
    faces.append(vedo.Line(pts4r_translate, closed=True))

    if show:
        vedo.show(faces)

    return pts1r,pts2r,pts3r_translate,pts4r_translate


# plato: air
def octahedron():
    # top faces
    P = tetrahedron()
    top = [vedo.Line(p, closed=True) for p in P]

    # bottom faces
    bottom = []
    for p in P:
        # flip the y points 
        bottom.append(vedo.Line([(x,y*-1,z) for x,y,z in p], closed=True))
    
    # show 
    vedo.show(top, bottom).close()


# plato: water
def icosahedron():
    print("icosahedron")

# plato: cosmos
def dodecahedron():
    print("dodecahedron")

def sphere():
    radius = 1
    theta_steps = 40 # around z-axis
    phi_steps = 20 # around y-axis

    P = []

    for i in range(phi_steps+1):
        phi = np.pi*i / phi_steps
        for j in range(theta_steps+1):
            # draw a circle
            theta = (2*np.pi) * (j / theta_steps)

            x = radius * np.sin(phi) * np.cos(theta)
            y = radius * np.sin(phi) * np.sin(theta)
            z = radius * np.cos(phi)

            P.append((x,y,z))
        
    print(P)

    cloud = vedo.Points(P)

    faces = []
    for i in range(phi_steps):
        for j in range(theta_steps):
            p1 = i * (theta_steps + 1) + j
            p2 = p1 + 1
            p3 = p1 + (theta_steps + 1)
            p4 = p3 + 1

            # Two triangles per quad on sphere
            faces.append([p1, p2, p4])
            faces.append([p1, p4, p3])

    # create a mesh along the surface of the sphere

    mesh = vedo.Mesh([P, faces])

    vedo.show(mesh).close()

    print("sphere")

# 
# cube()
# tetrahedron(show=True)
# octahedron()
#wheel(total_spokes=14)

# spiral(increase_arc=True, side_effects=show)

# circle()

def main():
    #coil(side_effects=show)
    sphere()

main()