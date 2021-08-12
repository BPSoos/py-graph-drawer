import pygame
import math

from DrawHelper import *
PI = math.pi
class AbstractGraphObject(object):

    def __init__(self):
        self.background_color = (255, 255, 204)
        self.color = pygame.Color('black')
        self.width = 1

class Vertice(Point, AbstractGraphObject):

    def __init__(self, x, y):
        super(Vertice, self).__init__(x, y)
        AbstractGraphObject.__init__(self)
        self.radius = 15

    def draw(self, screen):
        pygame.draw.circle(screen, self.background_color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)


class Edge(Segment, AbstractGraphObject):

    def __init__(self, start_vertice, end_vertice):
        super(Edge, self).__init__(start_vertice, end_vertice)
        AbstractGraphObject.__init__(self)

    def draw(self, screen, graph, current_edges=0):
        start_location = Point(graph.vertices[self.start-1].x, graph.vertices[self.start-1].y)
        end_location = Point(graph.vertices[self.end-1].x, graph.vertices[self.end-1].y)
        if start_location.x == end_location.x:
            height = graph.vertices[0].radius * current_edges + 1
            width = (end_location.y - start_location.y)
        elif start_location.y == end_location.y:
            height = (end_location.x - start_location.x)
            width = graph.vertices[0].radius * current_edges + 1
        else:
            height = (end_location.x - start_location.x)
            width = (end_location.y - start_location.y)
        #curve_rect = pygame.Rect(start_location.x, start_location.y, height, width)
        curve_rect = pygame.Rect(start_location.x, start_location.y, 2*(end_location.x-start_location.x),
                                 2*(end_location.y-start_location.y))

        #pygame.draw.rect(screen, self.color, curve_rect, 1)
        pygame.draw.arc(screen, self.color, curve_rect, PI/2, PI, 1)



class BasicGraph(object):

    DEFAULT_VERTICES = [Vertice(100, 200), Vertice(100, 100),
                        Vertice(200, 100), Vertice(200, 200)]
    DEFAULT_EDGES = [Edge(1, 2), Edge(2, 1),
                     Edge(1, 4), Edge(4, 4)]

    def __init__(self, vertices=None, edges=None):
        self._vertices = vertices if vertices else self.DEFAULT_VERTICES
        self._edges = edges if edges else self.DEFAULT_EDGES

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        self._vertices = value

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value):
        self._edges = value

