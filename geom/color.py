import vedo

primary = [
    {"name": "red", "rgb": (255, 0, 0), "hex":"#FF0000"},
    {"name": "green", "rgb": (0, 255, 0), "hex": "#00FF00"},
    {"name": "blue", "rgb": (0, 0, 255), "hex": "#0000FF"}, 
]

def colors():
    points = [
        vedo.Point((255, 255, 255), c="#FFFFFF"), # white
        vedo.Point((4, 55, 242), c="#0437F2"),    # ultramarine
        vedo.Point((64, 130, 109), c="#40826D"),  # viridian
        vedo.Point((138, 51, 36), c="#8A3324"),   # burnt umber
        vedo.Point((0, 0, 0), c="#000000")        # black
    ]

    pantone = [
        {"name": "cerulean", "rgb": (0, 123, 167), "hex": "#007ba7"}
    ]    

    cer_point = next((p for p in pantone if p["name"] == "cerulean"))

    # create points,

    # create lines
    cerulean_cluster = []
#    for c in primary:

    # cerulean_cluster = vedo.Line([p["rgb"] for p in cer_points])

#     primary_points = [(vedo.Point(p["rgb"], c=p["hex"])) for p in primary]



    # vedo.show(points)
    # vedo.show(primary_points, points, axes=1)
 
 #   vedo.show(cerulean_cluster, primary_points, axes=1)

colors()