
import numpy                as np
import matplotlib.pyplot    as plt
import triangle_functions   as triangle


### "The secret to fractals is its relationships to power laws"

def koch_snowflake():
    # create base triangle
    x, y = triangle.equilateral()

    plt.plot(x, y, 'b')

    def koch_recurse(kx, ky, n = 1):
        print("do")

        # get first line of triangle
        x = kx[:2]
        y = ky[:2]

        # shrink to right width/height
        x = x / 2
        y = y / 2

        # move to center of original triangles line
        x = x + (np.max(x) - np.min(x)) / 2
        y = y + (np.max(y) - np.min(y)) / 2

        print(x)
        print(y)

        # find center of line and plot
        cx = np.median(x)
        cy = np.median(y)

        # find angle of original line
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        deg = np.degrees(np.arctan2(dy, dx))

        # grow outward from -2x original angle
        print(deg)

        # grow outward from median at angle
        print(cx)
        print(cy)

        plt.plot(cx, cy, 'ro')
        plt.plot(x, y, 'r')

        if n > 1:
            koch_recurse(x, y, n-1)

    n = 1
    koch_recurse(x, y, n)

    # plt.axis("equal")
    plt.savefig("test")

def show():
    plt.grid()
#    plt.axis("equal")
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
show()