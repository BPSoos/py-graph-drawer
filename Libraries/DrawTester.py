import sys
import pygame
from sympy import *

from BasicGraphObjects import *

pygame.init()
pygame.font.init()
my_font = pygame.font.Font(None, 30)
pygame.display.set_caption('Your Graph')

size = width, height = 1000, 1000
speed = [2, 2]
background = (255, 255, 204)

bg = BasicGraph(edges=[Edge(4, 2)])


def get_arc_circle_data(start_point, end_point):
    Xa = start_point[0]
    Xb = end_point[0]
    Ya = start_point[1]
    Yb = end_point[1]
    radius = sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)
    #print(radius)
    half_point = (int((start_point[0] + end_point[0])/2),
                  int((start_point[1] + end_point[1])/2))
    #print(half_point)

    center_x, center_y = symbols(' center_x center_y ')

    if Ya != Yb:
        halving_line_eq = Eq(center_y, (-(Xa - Xb) /
                                        (Ya - Yb)) * center_x +
                             ((Xa ** 2 - Xb ** 2 + Ya ** 2 - Yb ** 2) /
                              (2 * (Ya - Yb))))
    else:
        halving_line_eq = Eq(center_x, 0.5*(Xa+Xb))

    distance_eq = Eq(radius, (sqrt((center_x - Xa) ** 2 + (center_y - Ya) ** 2)))

    eq_solutions = solve((halving_line_eq, distance_eq), (center_x, center_y))
    return [eq_solutions, radius]

def get_vector_of_segment(start_point, end_point):
    return [(0, 0), (end_point[0] - start_point[0], end_point[1] - start_point[1])]

def get_lenght_of_segment(start_point, end_point):
    return sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)

def get_rad_from_x_of_segment(start_point, end_point):
    vector = get_vector_of_segment(start_point, end_point)
    a = vector[1][0]
    b = get_lenght_of_segment(vector[0], vector[1])
    c = get_lenght_of_segment(vector[1], (a, 0))
    print(f'rad {(a ** 2 + b ** 2 - c ** 2)/(2*a*b)}')
    return acos((a ** 2 + b ** 2 - c ** 2)/(2*a*b))

def get_rad_of_triangle(A, B, C):
    a = get_lenght_of_segment(C, B)
    b = get_lenght_of_segment(A, C)
    c = get_lenght_of_segment(A, B)
    return acos((a ** 2 + b ** 2 - c ** 2)/(2*a*b))


def get_arc_circle_rect(center, radius):
    return center[0] - radius, center[1] - radius, 2 * radius, 2 * radius


def draw_arc_for_line(screen, center, radius, start_point, end_point):
    arc_rect = get_arc_circle_rect(center, radius)
    arc_angle = get_rad_of_triangle(start_point, end_point, center)
    end_angle = get_rad_from_x_of_segment(end_point, center)
    start_angle = end_angle + arc_angle
    pygame.draw.rect(screen, pygame.Color('black'), arc_rect, 1)
    modifier = 1.75
    pygame.draw.arc(screen, pygame.Color('black'), arc_rect, end_angle -pi*modifier, start_angle -pi*modifier )


screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        S = (200, 200)
        E = (300, 250)
        a = math.sqrt(math.pow(E[0] - S[0], 2) + math.pow(E[1] - S[1], 2))
        F = (int((S[0] + E[0])/2), int((S[1] + E[1])/2))
        screen.fill(background)
        O, a = get_arc_circle_data(S, E)
        draw_arc_for_line(screen, O[0], a, S, E)
        rect1 = (O[0][0]-a, O[0][1]-a, 2*a, 2*a)
        rect2 = (O[1][0]-a, O[1][1]-a, 2*a, 2*a)
        pygame.draw.line(screen, pygame.Color('black'), S, E, 2)
        #pygame.draw.line(screen, pygame.Color('black'), S, O[0])
        #pygame.draw.line(screen, pygame.Color('black'), E, O[0])
        #pygame.draw.line(screen, pygame.Color('black'), S, O[1])
        #pygame.draw.line(screen, pygame.Color('black'), E, O[1])
        #pygame.draw.rect(screen, pygame.Color('black'), rect1, 1)
        #pygame.draw.rect(screen, pygame.Color('black'), rect2, 1)
        alph = get_rad_of_triangle(S, E, O[1])
        r1 = get_rad_from_x_of_segment(E, O[1])
        r2 = r1 - alph
        #pygame.draw.arc(screen, pygame.Color('black'), rect1, r2, r1)
        #pygame.draw.arc(screen, pygame.Color('black'), rect2, r2, r1)
        #for edge in bg.edges:
        #    edge.draw(screen, bg)
        #for i,vertice in enumerate(bg.vertices):
        #    vertice.draw(screen)
        #    text0 = my_font.render(str(i+1), True, pygame.Color('black'))
        #    screen.blit(text0, (vertice.x - vertice.radius/2, vertice.y- vertice.radius/2))
        pygame.display.flip()
