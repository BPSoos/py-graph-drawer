import sys
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

testing_points = {'start': [(200, 100), (100, 100), (100, 200), (100, 300), (200, 300), (300, 300), (300, 200), (300, 100)],
                        'end': [(200, 200),(200, 200), (200, 200), (200, 200), (200, 200), (200, 200), (200, 200), (200, 200)]}


def draw_line_with_bounding_rect(start_point, end_point):
    pygame.draw.line(screen, pygame.Color('black'), start_point, end_point, 2)
    #pygame.draw.rect(screen, pygame.Color('black'), DrawHelper.get_rect_around_segment(S, E, get_top_rect=True), 1)
    #centers, radius = DrawHelper.get_arc_circle_data(start_point, end_point)
    #pygame.draw.circle(screen,pygame.Color('black'), centers[0], radius, 1)


def draw_test_flower(screen):
    multiplier = 2
    for i in range(0, len(testing_points['start'])):
        S = tuple(cord * multiplier for cord in testing_points['start'][i])
        E = tuple(cord * multiplier for cord in testing_points['end'][i])
        draw_line_with_bounding_rect(S, E)
        angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(S, E, False)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        angle_1, angle_2, arc_rect = DrawHelper.get_arc_data_of_segment(S, E, True)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle_1, angle_2, 1)
        # pygame.draw.line(screen, pygame.Color('black'), end_line[0], end_line[1])
        Vertice(*S).draw(screen)
        Vertice(*E).draw(screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(background)
        draw_test_flower(screen)
        pygame.display.flip()
