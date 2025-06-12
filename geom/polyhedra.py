import vedo
import adaptors.vedo
import numpy as np

# earth
def cube():
    # faces on first plane
    points = adaptors.vedo.triangle()
    triangle = vedo.Line(points, closed=True)

    p = [(points[0][0],points[0][1],points[0][2]+1),
         (points[1][0],points[1][1],points[1][2]+1),
         (points[2][0],points[2][1],points[2][2]+1)]
    sq = vedo.Line(p, closed=True)

    # faces on second plane
    points2 = adaptors.vedo.triangle() @ adaptors.vedo.rotate(90, 0, 0).T
    triangle2 = vedo.Line(points2, closed=True)
    p2 = [(points2[0][0],points2[0][1]+1,points2[0][2]),
         (points2[1][0],points2[1][1]+1,points2[1][2]),
         (points2[2][0],points2[2][1]+1,points2[2][2])]
    sq2 = vedo.Line(p2, closed=True)

    pz = [(points2[0][0],points2[0][1]-1,points2[0][2]),
         (points2[1][0],points2[1][1]-1,points2[1][2]),
         (points2[2][0],points2[2][1]-1,points2[2][2])]
    tri_z = vedo.Line(pz @ adaptors.vedo.rotate(90,90,90), closed=True)
    
    pointsr = adaptors.vedo.triangle() @ adaptors.vedo.rotate(-90,-90,-90).T
    tri_y = vedo.Line(pointsr, closed=True)

    # faces on third plane
    points3 = adaptors.vedo.triangle() @ adaptors.vedo.rotate(0, -90, 0).T
    triangle3 = vedo.Line(points3, closed=True)

    p3 = [(points3[0][0]+1,points3[0][1],points3[0][2]),
         (points3[1][0]+1,points3[1][1],points3[1][2]),
         (points3[2][0]+1,points3[2][1],points3[2][2])]
    sq3 = vedo.Line(p3, closed=True)
    

    vedo.show(triangle, sq, tri_y,
              triangle2, sq2,
              triangle3, 
              #sq3,

              axes=0).close()
    # vedo.show(triangle, triangle2, triangle3, axes=1).close()

# earth
def cube_v2():
    points = adaptors.vedo.triangle()
    tri_1 = vedo.Line(points, closed=True)
    # find triangles center
    # print(points)
    
    tri_1_cent = vedo.Point(adaptors.vedo.centroid(points))
    # rotate points about center(0,0)?

    vedo.show(tri_1, tri_1_cent).close()

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

cube_v2()