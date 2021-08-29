import math
import os
from cairo import *

#from BasicGraphObjects import *


WIDTH, HEIGHT = 1280, 720
output = "/root/py-graph-drawer/runtemp/cairo_tester.png"
surface = ImageSurface(FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = Context(surface)

ctx.scale(WIDTH, HEIGHT)

pat = LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(0, 255/255, 255/255, 204/255, 1)

ctx.rectangle(0, 0, 1, 1)
ctx.set_source(pat)
ctx.fill()
ctx.set_source_rgb(0.1, 0.0, 0.0)
ctx.set_line_width(0.001)
screen = None

background = (255, 255, 204)
#bg = BasicGraph(edges=[Edge(4, 2)])
testing_points = {'start': [(200, 100), (100, 100), (100, 200), (100, 300),
                            (200, 300), (300, 300), (300, 200), (300, 100)],
                        'end': [(200, 200),(200, 200), (200, 200), (200, 200),
                                (200, 200), (200, 200), (200, 200), (200, 200)]}


def draw_basic_line(start_point, end_point):
    ctx.move_to(start_point[0]/WIDTH, start_point[1]/HEIGHT)
    ctx.line_to(end_point[0]/WIDTH, end_point[1]/HEIGHT)
    ctx.stroke()


def draw_bounding_rect_for_segment(start_point, end_point):
    pass
    #pygame.draw.rect(screen, line_color, DrawHelper.get_rect_around_segment(start_point, end_point, get_top_rect=True), 1)


def draw_test_flower():
    multiplier = 2
    for i in range(0, len(testing_points['start'])):
        start_point = tuple(cord * multiplier for cord in testing_points['start'][i])
        end_point = tuple(cord * multiplier for cord in testing_points['end'][i])
        draw_basic_line(start_point, end_point)
        #angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(start_point, end_point, False)
        #pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        #angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(start_point, end_point, True)
        #pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        #Vertice(*start_point).draw(screen)
        #Vertice(*end_point).draw(screen)


draw_test_flower()

if os.path.isfile(output):
    os.remove(output)
surface.write_to_png(output)
