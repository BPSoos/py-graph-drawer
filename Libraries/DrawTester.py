import sys
import pygame

from BasicGraphObjects import *

pygame.init()
pygame.display.set_caption('Your Graph')

size = width, height = 320, 240
speed = [2, 2]
background = (255, 255, 204)

bg = BasicGraph(edges=[Edge(1, 2), Edge(2, 1),
                       Edge(1, 4), Edge(4, 4),
                       Edge(2, 4), Edge(1, 3),
                       Edge(4, 3)])

screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill(background)
        for edge in bg.edges:
            edge.draw(screen, bg)
        for vertice in bg.vertices:
            vertice.draw(screen)
        pygame.display.flip()
