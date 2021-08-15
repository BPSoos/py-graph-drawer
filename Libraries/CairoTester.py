import math
import os
from cairo import *

WIDTH, HEIGHT = 256, 256
output = "/root/py-graph-drawer/runtemp/cairo_tester.png"
surface = ImageSurface(FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = Context(surface)

ctx.scale(WIDTH, HEIGHT)

pat = LinearGradient(0.0, 0.0, 0.0, 1.0)
#pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)
#pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)

ctx.rectangle(0, 0, 1, 1)
ctx.set_source(pat)
ctx.fill()

ctx.translate(0.1, 0.1)

ctx.move_to(0, 0)

ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
ctx.line_to(0.5, 0.1)

ctx.curve_to(0.7, 0.5, 0.7, 0.7, 0.2, 0.8)
ctx. close_path()

ctx. close_path()

ctx.set_source_rgb(0.0, 0.0, 0.0)
ctx.set_line_width(0.02)
ctx.stroke()

if os.path.isfile(output):
    os.remove(output)
surface.write_to_png(output)
