import numpy as np
import vedo
import colour

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
 
def color_science_hello_world():
    # perceptual color space
    colour.plotting.colour_style()
    colour.plotting.plot_visible_spectrum()

def color_palette():
    base_rgb = (1, 1, 0)  # normalized RGB (0-1)

    # Convert to Lab (perceptual color space)
    lab = colour.XYZ_to_Lab(colour.sRGB_to_XYZ(base_rgb))

    # Generate palette by varying the Lightness (L*)
    palette_lab = [(l, lab[1], lab[2]) for l in np.linspace(20, 90, 6)]

    # Convert back to sRGB
    palette_rgb = [colour.XYZ_to_sRGB(colour.Lab_to_XYZ(c)) for c in palette_lab]

    # Clip values to valid range [0, 1] and convert to 8-bit RGB
    palette_rgb_8bit = [tuple(int(max(0, min(1, c)) * 255) for c in rgb) for rgb in palette_rgb]

    swatches = []
    for i, rgb in enumerate(palette_rgb_8bit):
        # Covert RGB to hex format for vedo
        hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)

        r = vedo.Rectangle(
                p1=(i*1.1,0), 
                p2=((i*1.1)+1, 1),
                c=hex_color)
        
        swatches.append(r)

    print(palette_rgb_8bit)
    vedo.show(swatches, "color palette", size=(800,200), bg="white")
    

color_palette()

# colors()