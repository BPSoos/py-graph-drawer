import os
from cairo import *

from BasicGraphObjects import *

PIXEL_SCALE = 2000
WIDTH, HEIGHT = 10, 10
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
with open("/root/py-graph-drawer/runtemp/road-minnesota.mtx", 'r') as f:
    data = f.read().splitlines()
testing_adj = []
for i, line in enumerate(data):
    testing_adj.append([])
    for num in line.split(' '):
        testing_adj[i].append((int(num), 0))
print(testing_adj)

'''with open("/root/py-graph-drawer/runtemp/email-Eu-core-temporal-Dept3.txt", 'r') as f:
    data = f.read().splitlines()
testing_adj = []
for i in range(0,89):
    testing_adj.append([])
for i, line in enumerate(data):
    line_data = line.split(' ')
    testing_adj[int(line_data[0]) - 1].append((int(line_data[1]) - 1, int(line_data[2])))
print(testing_adj)'''

for pdict in testing_points.keys():
    for i, point in enumerate(testing_points[pdict]):
        testing_points[pdict][i] = Vertice(point[0]/PIXEL_SCALE, point[1]/PIXEL_SCALE, ctx)
        #testing_points[pdict][i].radius /= PIXEL_SCALE
print(testing_points)
bg = BasicGraph(vertices=[*testing_points['start'],*testing_points['end']])
bg.set_context(ctx)
bg.init_adjacency(testing_adj)
bg.set_context(ctx)
bg.create_layout_random()
for edge in bg.edges:
    edge.draw()
for vertice in bg.vertices:
    vertice.draw()

if os.path.isfile(output):
    os.remove(output)
surface.write_to_png(output)
