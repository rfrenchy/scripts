import vedo
from colour.plotting import *

primary = [
    {"name": "red", "rgb": (255, 0, 0), "hex":"#FF0000"},
    {"name": "green", "rgb": (0, 255, 0), "hex": "#00FF00"},
    {"name": "blue", "rgb": (0, 0, 255), "hex": "#0000FF"}, 
]

secondary = [
    {"name": "yellow", "rgb": (255,255,0), "hex": "#FFFF00"},
    {"name": "orange", "rgb": (255,165,0), "hex": "#FFA500"},
    {"name": "indigo", "rgb": (75, 0, 130), "hex": "#4B0082"},
    {"name": "violet", "rgb": (143, 0, 255), "hex": "#8F00FF"}
]

points = [
    vedo.Point((255, 255, 255), c="#FFFFFF"), # white
    vedo.Point((4, 55, 242), c="#0437F2"),    # ultramarine
    vedo.Point((64, 130, 109), c="#40826D"),  # viridian
    vedo.Point((138, 51, 36), c="#8A3324"),   # burnt umber
    vedo.Point((0, 0, 0), c="#000000")        # black
]

def colors():

    pantone = [
        {"name": "cerulean", "rgb": (0, 123, 167), "hex": "#007ba7"}
    ]    

    cer_point = next((p for p in pantone if p["name"] == "cerulean"))


    primary_points = [(vedo.Point(p["rgb"], c=p["hex"])) for p in primary]
    secondary_points = [(vedo.Point(p["rgb"], c=p["hex"])) for p in secondary]

    vedo.show(primary_points, 
              secondary_points, 
              axes=1)
 
def color_science():
    colour_style()
    plot_visible_spectrum()

color_science()

# colors()