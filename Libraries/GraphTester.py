from BasicGraphObjects import *

bg = BasicGraph()

for edge in bg.edges:
    print(edge.end, edge.start)
for vertice in bg.vertices:
    print(vertice.x, vertice.y)