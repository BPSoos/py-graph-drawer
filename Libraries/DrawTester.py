import pygame

from DrawHelper import *
from BasicGraphObjects import *

pygame.init()
pygame.font.init()
my_font = pygame.font.Font(None, 30)
pygame.display.set_caption('Your Graph')

size = width, height = 1000, 900
speed = [2, 2]
background = (255, 255, 204)
bg = BasicGraph(edges=[Edge(4, 2)])
screen = pygame.display.set_mode(size)
line_color = pygame.Color('black')
testing_points = {'start': [(200, 100), (100, 100), (100, 200), (100, 300),
                            (200, 300), (300, 300), (300, 200), (300, 100)],
                        'end': [(200, 200),(200, 200), (200, 200), (200, 200),
                                (200, 200), (200, 200), (200, 200), (200, 200)]}


def draw_basic_line(start_point, end_point):
    pygame.draw.line(screen, line_color, start_point, end_point, 2)


def draw_bounding_rect_for_segment(start_point, end_point):
    pygame.draw.rect(screen, line_color, DrawHelper.get_rect_around_segment(start_point, end_point, get_top_rect=True), 1)


def draw_test_flower():
    multiplier = 2
    for i in range(0, len(testing_points['start'])):
        start_point = tuple(cord * multiplier for cord in testing_points['start'][i])
        end_point = tuple(cord * multiplier for cord in testing_points['end'][i])
        draw_basic_line(start_point, end_point)
        angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(start_point, end_point, False)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(start_point, end_point, True)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        Vertice(*start_point).draw(screen)
        Vertice(*end_point).draw(screen)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(background)
        draw_test_flower()
        pygame.display.flip()
