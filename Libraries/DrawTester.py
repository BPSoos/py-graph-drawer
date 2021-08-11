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


def draw_line_with_bounding_rect(start_point, end_point):
    pygame.draw.line(screen, pygame.Color('black'), start_point, end_point, 2)
    #pygame.draw.rect(screen, pygame.Color('black'), DrawHelper.get_rect_around_segment(S, E, get_top_rect=True), 1)
    #centers, radius = DrawHelper.get_arc_circle_data(start_point, end_point)
    #pygame.draw.circle(screen,pygame.Color('black'), centers[0], radius, 1)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        S = (100, 200)
        E = (100, 400)
        screen.fill(background)
        draw_line_with_bounding_rect(S, E)
        angle = DrawHelper.get_start_angle_segment_of_rected_segment(S, E, get_top_rect=False)
        arc_rect = DrawHelper.get_rect_around_segment(S, E, get_top_rect=False)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle[0], angle[1], 1)
        angle = DrawHelper.get_start_angle_segment_of_rected_segment(S, E, get_top_rect=True)
        arc_rect = DrawHelper.get_rect_around_segment(S, E, get_top_rect=True)
        pygame.draw.arc(screen, pygame.Color('black'), arc_rect, angle[0], angle[1], 1)
        #pygame.draw.line(screen, pygame.Color('black'), end_line[0], end_line[1])
        pygame.display.flip()
