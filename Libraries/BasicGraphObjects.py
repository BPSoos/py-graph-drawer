import math

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
        self.radius = 15

    def draw(self):
        self.context.arc(self.x, self.y, self.radius, 0, 2*PI)
        self.context.fill()
        self.context.stroke()


class Edge(Segment, AbstractGraphObject):

    def __init__(self, start_vertice, end_vertice, context=None):
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
    

