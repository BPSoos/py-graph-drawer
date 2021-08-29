import os
from cairo import *

from BasicGraphObjects import *

PIXEL_SCALE = 100
WIDTH, HEIGHT = 12.80, 7.20
output = "/root/py-graph-drawer/runtemp/cairo_tester.png"
surface = ImageSurface(FORMAT_ARGB32, int(WIDTH*PIXEL_SCALE), int(HEIGHT*PIXEL_SCALE))
ctx = Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

pat = LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(0, 255/255, 255/255, 204/255, 1)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source(pat)
ctx.fill()
ctx.set_source_rgb(0.1, 0.0, 0.0)
ctx.set_line_width(0.01)

testing_points = {'start': [(200, 100), (100, 100), (100, 200), (100, 300),
                            (200, 300), (300, 300), (300, 200), (300, 100)],
                        'end': [(200, 200),(200, 200), (200, 200), (200, 200),
                                (200, 200), (200, 200), (200, 200), (200, 200)]}

testing_adj = [[(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)],
               [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)],
               [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)], [(0, 1),(1, 1), (2, 1),(3, 1), (4, 1),(5, 1), (6, 1),(7, 1), (8, 1)]]
for pdict in testing_points.keys():
    for i, point in enumerate(testing_points[pdict]):
        testing_points[pdict][i] = Vertice(point[0]/PIXEL_SCALE, point[1]/PIXEL_SCALE, ctx)
        testing_points[pdict][i].radius /= PIXEL_SCALE
print(testing_points)
bg = BasicGraph(vertices=[*testing_points['start'],*testing_points['end']])
bg.set_context(ctx)
for edge in bg.edges:
    edge.draw()
for vertice in bg.vertices:
    vertice.draw()

if os.path.isfile(output):
    os.remove(output)
surface.write_to_png(output)
