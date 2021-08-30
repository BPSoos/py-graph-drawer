import math
import random

from DrawHelper import *
PI = math.pi
class AbstractGraphObject(object):

    def __init__(self, context=None):
        self.context = context
        self.background_color = (255, 255, 204)
        self.color = (0, 0, 0)
        self.width = 1

class Vertice(Point, AbstractGraphObject):

    def __init__(self, x, y, context=None):
        super(Vertice, self).__init__(x, y)
        AbstractGraphObject.__init__(self, context)
        self.radius = 0.15

    def draw(self):
        self.context.arc(self.x, self.y, self.radius, 0, 2*PI)
        self.context.fill()
        self.context.stroke()


class Edge(Segment, AbstractGraphObject):

    def __init__(self, start_vertice, end_vertice, weight=None, context=None):
        super(Edge, self).__init__(start_vertice, end_vertice)
        AbstractGraphObject.__init__(self, context)
        self.edge_amount = 0

    def draw(self):
        self.context.move_to(self.start.x, self.start.y)
        self.context.line_to(self.end.x, self.end.y)
        self.context.stroke()


class BasicGraph(object):

    DEFAULT_VERTICES = [Vertice(100, 200), Vertice(100, 100),
                        Vertice(200, 100), Vertice(200, 200)]
    DEFAULT_EDGES = [(1, 2), (2, 1),
                     (1, 4), (4, 4)]

    def __init__(self, vertices=None, edges=None):
        self._vertices = vertices if vertices else self.DEFAULT_VERTICES
        self._edges = []
        vertice_list = edges if edges else self.DEFAULT_EDGES
        for vertices in vertice_list:
            self._edges.append(Edge(self.vertices[vertices[0]], self.vertices[vertices[1]]))
            
    def set_vertice_radius(self, value):
        for vertice in self.vertices:
            vertice.radius = value

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

    def set_context(self, context):
        for edge in self.edges:
            edge.context = context
        for vertice in self.vertices:
            vertice.context = context

    def init_adjacency(self, adj):
        self.vertices = []
        self.edges = []
        for i in range(0, len(adj)):
            self.vertices.append(Vertice(0, 0))
        for i, vertice_edges in enumerate(adj):
            for edge in vertice_edges:
                self.edges.append(Edge(self.vertices[i], self.vertices[edge[0]]))

    def create_layout_circle(self):
        radius = 0.4
        surf = self.vertices[0].context.get_target()
        pix_height = surf.get_height()
        pix_width = surf.get_width()
        ctm_x = self.vertices[0].context.get_matrix()[0]
        ctm_y = self.vertices[0].context.get_matrix()[3]
        multiplier_x = pix_width/ctm_x
        multiplier_y = pix_height/ctm_y
        multiplier_main = multiplier_x if multiplier_y > multiplier_x else multiplier_y
        print(multiplier_main, pix_width/ctm_x, pix_height/ctm_y)
        self.set_vertice_radius(0.3*multiplier_main*(1/len(self.vertices)))
        self.vertices[0].context.set_line_width(0.02*multiplier_main*(1/len(self.vertices)))
        center_x = 0.5 * multiplier_x
        center_y = 0.5 * multiplier_y

        for i, vertice in enumerate(self.vertices):
            gam = i * 2 * math.pi / len(self.vertices)
            alf = math.pi - math.pi / 2 - (math.pi - gam) / 2
            c = radius * 2 * math.sin(gam / 2)
            dx = c * math.sin(alf) * multiplier_main
            dy = c * math.cos(alf) * multiplier_main
            x = center_x + radius * multiplier_main if dx >= 0 else center_x - radius * multiplier_main
            y = center_y
            vertice.x = (x - dx)
            vertice.y = (y - dy)

    def create_layout_random(self):
        surf = self.vertices[0].context.get_target()
        pix_height = surf.get_height()
        pix_width = surf.get_width()
        ctm_x = self.vertices[0].context.get_matrix()[0]
        ctm_y = self.vertices[0].context.get_matrix()[3]
        multiplier_x = pix_width/ctm_x
        multiplier_y = pix_height/ctm_y
        multiplier_main = multiplier_x if multiplier_y > multiplier_x else multiplier_y
        print(multiplier_main, pix_width/ctm_x, pix_height/ctm_y)
        self.set_vertice_radius(2*multiplier_main*(1/len(self.vertices)))
        self.vertices[0].context.set_line_width(0.09*multiplier_main*(1/len(self.vertices)))

        for i, vertice in enumerate(self.vertices):
            vertice.x = random.randint(0, pix_width) / ctm_x
            vertice.y = random.randint(0, pix_height) / ctm_y

