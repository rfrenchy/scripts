import numpy as np
import triangle_functions as tr

def triangle(scale = 1):
    return tr.unit_trianglev3()

def equilateral_triangle():
    return  [(1,0,0),(0.5,1,0),(0,0,0)]

def square():
    return [(1,0,0),(0,1,0),(0,0,0), (1,0,0),(0,1,0),(1,1,0)]

def centroid(points):
    x_avg = sum((p[0] for p in points)) / len(points)
    y_avg = sum((p[1] for p in points)) / len(points)
    z_avg = sum((p[2] for p in points)) / len(points)

    return x_avg, y_avg, z_avg

def rotate(cx = 0,cy = 0,cz = 0):
    rx, ry, rz = np.radians((cx, cy, cz))

    # x rotation matrix
    Rx = np.array([[1, 0, 0],
                  [0, np.cos(rx), -np.sin(rx)], 
                  [0, np.sin(rx), np.cos(rx)]])

    # y rotation matrix
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)], 
                  [0, 1, 0], 
                  [-np.sin(ry), 0, np.cos(ry)]])

    # z rotation matrix
    Rz = np.array([[np.cos(rz), -np.sin(rz), 0], 
                  [np.sin(rz), np.cos(rz), 0],
                  [0, 0, 1]])

    R = Rx @ Ry @ Rz
    
    return R
    