import random

import numpy                as np
import pandas               as pd
import matplotlib.pyplot    as plt
import triangle_functions   as triangle
import circle_functions     as circle
import square_functions     as square


### "The secret to fractals is its relationships to power laws"

## constants
CUBE_1  = 3**1      # 3
CUBE_2  = 3**2      # 9
CUBE_N1 = 3**-1     # 0.333
255
def gasket_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

def sierpinski_gasket_v2(n = 1, side_effects = gasket_side_effects):
    sgx, sgy = triangle.equilateral()

    def sgn(n, sgx, sgy):
        if n == 0:
            return (sgx, sgy)

        xrange = np.max(sgx) - np.min(sgx)
        yrange = np.max(sgy) - np.min(sgy)

        c1x = sgx + (xrange / 2)
        c2x = sgx - (xrange / 2) 
        c1y = sgy - yrange

        sgx = np.concatenate((sgx, c1x, c2x))
        sgy = np.concatenate((sgy, c1y, c1y))
        
        side_effects(n, sgx, sgy)

        return sgn(n - 1, sgx, sgy)
    
    return sgn(n, sgx, sgy)

def carpet_side_effects(n, x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'n': n, 'x': x, 'y': y}))

### DONE - Shrink
### TODO - Magnify
def sierpinski_carpet(n = 1, side_effects = carpet_side_effects):
    # generation
    x1, y1  = square.unit_square()      # init
    x2, y2  = x1*CUBE_N1, y1*CUBE_N1    # shrink
    TX      = np.max(x2) - np.min(x2)   # find translate
    x2, y2  = x2+TX, y2+TX              # apply translate

    # side effects e.g. print
    side_effects(n, x1, y1)
    side_effects(n, x2, y2)
    
    # define recursion
    def carpet_recurse(n, x2, y2, TX):
        # return from recursion
        if n <= 0: return

        # shrink
        x2, y2 = x2/CUBE_1, y2/CUBE_1

        # plot and recurse
        def do(x, y):
            side_effects(n, x, y)
            carpet_recurse(n -1, x, y, TX)
        
        # recurse for each carpet segment
        for i in range(CUBE_2):
            if i == 0: do(x2, y2)
            if i == 1: do(x2, y2+TX) 
            if i == 2: do(x2, y2+TX+TX)
            if i == 3: do(x2+TX, y2)
            # if i == 4: do nothing
            if i == 5: do(x2+TX, y2+TX+TX)
            if i == 6: do(x2+TX+TX, y2)
            if i == 7: do(x2+TX+TX, y2+TX)
            if i == 8: do(x2+TX+TX, y2+TX+TX)

    # recurse
    carpet_recurse(n-1, x2, y2, TX)

def fractal_side_effects(x, y): 
    plt.plot(x, y, 'b')
    print(pd.DataFrame({'x': x, 'y': y}))

def fractal_tree(n = 1, side_effects = fractal_side_effects):

    T = 10 # Amount of parts in a tree line
    random_rotation = lambda : circle.rot(random.uniform(0, np.pi*2)) 

    branch = np.linspace(0, 1, T)

    # scramble branch
    for i in range(len(branch)):
        rand = random.uniform(0,1)
        if rand > 0.666: branch[i] = branch[i]+1
        if rand < 0.333: branch[i] = branch[i]-1
        
    x = np.linspace(0, 1, T)

    fractal_side_effects(x, branch)

    def recurse(n, origin):
        if n == 0: return

        xlin    = np.linspace(0, 1, T)
        branch  = np.linspace(0, 1, T)
        ox, oy  = origin

        xlin    = xlin + ox
        branch  = branch + oy
        
        # scramble branch
        for i in range(len(branch)):
            rand = random.uniform(0,1)
            if rand > 0.666: branch[i] = branch[i]+1
            if rand < 0.333: branch[i] = branch[i]-1

        side_effects(xlin, branch)

        rp = random.randint(0,T-1)
        ox = xlin[rp]
        oy = branch[rp] 

        recurse(n-1, (ox, oy))
            
    rp = random.randint(0, T-1)
    ox = x[rp]
    oy = branch[rp] 

    # recurse for n
    recurse(n-1, (ox, oy))

def scatter(data):
    plt.grid()
    plt.axis("equal")
    plt.show()

def koch_snowflake():
    # create base triangle
    x, y = triangle.equilateral()

    plt.plot(x, y, 'b')

    def koch_recurse(kx, ky, n = 1):
        # create first fractal part
        tx1 = np.zeros(len(kx))    
        ty1 = np.zeros(len(ky))    

        # shrink triangle to half size
        for i in range(len(kx)):
            tx1[i] = kx[i] / 2
            ty1[i] = ky[i] / 2

        stx1 = [x - 0.1 for x in tx1] 
        sty1 = [y + 0.4 for y in ty1]

        points = (stx1, sty1)

        rtx1, rty1 = rotate_around_centroid_2d(points, 63.333)
        for i in range(len(rtx1)):
            rtx1[i] = rtx1[i] + -0.05

        plt.plot(rtx1, rty1, 'g')

        # create new triangle with bottom centered at this point

        tx2 = np.array(tx1)
        ty2 = np.array(ty1)
        tx2 = [(x + np.max(tx2)) for x in tx2]

        stx2 = [x + 0.05 for x in tx2]
        sty2 = [y + 0.4 for y in ty2] 
        # 0.4 = scaled triangle width - base triangle width

        points = (stx2, sty2)

        # rotate 45
        rtx2, rty2 = rotate_around_centroid_2d(points, -63.333)

        for i in range(len(rtx2)):
            rtx2[i] = rtx2[i] + 0.1

        plt.plot(rtx2, rty2, 'g')

        # point 3
        tx3 = np.zeros(len(kx))    
        ty3 = np.zeros(len(ky))    
        for i in range(len(kx)):
            tx3[i] = kx[i] * .5
            ty3[i] = ky[i] * .5
        
        tx3= [x + np.median(tx3) for x in tx3]
        # rotate 90

        points = (tx3, ty3)
        rtx3, rty3 = rotate_around_centroid_2d(points, 180)

        for i in range(len(rty3)):
            rty3[i] = rty3[i] - 0.33333


        plt.plot(rtx3, rty3, 'g')
        n = n -1
        if n > 0:
            #koch_recurse(rtx1, rty1, n)
            koch_recurse_2(rtx1, rty1)

    def koch_recurse_2(kx, ky): 
        print("koch recurse 2")
        # create first fractal part
        tx1 = np.zeros(len(kx))    
        ty1 = np.zeros(len(ky))    

        for i in range(0, len(kx)):
            tx1[i] = kx[i] / 2
            ty1[i] = ky[i] / 2


        for i in range(0, len(kx), 6):
            # translate        
            pts = (kx[i], kx[i+1])
            a = (np.max(pts) - np.min(pts)) / 6
            print(a)

            stx1 = [x + a for x in tx1] 
            sty1 = [y + .516 for y in ty1]

            #stx1 = tx1
            #sty1 = ty1

            # rotate
            points = (stx1, sty1)

            rtx1, rty1 = rotate_around_centroid_2d(points, -63)
            for i in range(len(rtx1)):
                kx
    #            rtx1[i] = rtx1[i] + -0.05

            plt.plot(rtx1, rty1, 'g')


    n = 2
    koch_recurse(x, y, n)

    plt.axis("equal")
    plt.savefig("test")

def show():
    plt.grid()
    plt.axis("equal")
    plt.show()

def rotate_around_centroid_2d(xy_tuple, angle_deg):
    x_array, y_array = xy_tuple
    x_array = np.array(x_array)
    y_array = np.array(y_array)

    # Stack into Nx2 array of (x, y) points
    pts = np.column_stack((x_array, y_array))

    # Compute centroid
    centroid = pts.mean(axis=0)

    # Translate to origin
    translated = pts - centroid

    # Rotation matrix
    theta = np.radians(angle_deg)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])

    # Apply rotation and translate back
    rotated = (R @ translated.T).T + centroid

    # Split back into x and y
    x_rotated, y_rotated = rotated[:, 0], rotated[:, 1]

    return x_rotated, y_rotated

koch_snowflake()

# scatter(fractal_tree(3))
# scatter(sierpinski_gasket_v2(3))
# scatter(sierpinski_carpet(3))
# show()
