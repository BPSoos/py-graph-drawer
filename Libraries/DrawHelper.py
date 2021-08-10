import pygame
from sympy import *

class PygamePoint(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    @property
    def coordinates(self):
        return self.x, self.y


class DrawHelper(object):

    def __init__(self):
        pass

    @staticmethod
    def get_arc_circle_data(start_point, end_point):
        """
        calculates the center and radius of the two possible bounding circles for a given segment
        :param start_point: segment start
        :param end_point: segment end
        :return: type of list and int: the two center coordinates for the bounding circles and a radius
        """
        Xa = start_point[0]
        Xb = end_point[0]
        Ya = start_point[1]
        Yb = end_point[1]
        radius = sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)
        half_point = (int((start_point[0] + end_point[0]) / 2),
                      int((start_point[1] + end_point[1]) / 2))
        center_x, center_y = symbols(' center_x center_y ')
        if Ya != Yb:
            halving_line_eq = Eq(center_y, (-(Xa - Xb) /
                                            (Ya - Yb)) * center_x +
                                 ((Xa ** 2 - Xb ** 2 + Ya ** 2 - Yb ** 2) /
                                  (2 * (Ya - Yb))))
        else:
            halving_line_eq = Eq(center_x, 0.5 * (Xa + Xb))
        distance_eq = Eq(radius, (sqrt((center_x - Xa) ** 2 + (center_y - Ya) ** 2)))
        eq_solutions = solve((halving_line_eq, distance_eq), (center_x, center_y))
        return [eq_solutions, radius]

    @staticmethod
    def get_vector_of_segment(start_point, end_point):
        return [(0, 0), (end_point[0] - start_point[0], end_point[1] - start_point[1])]

    @staticmethod
    def get_lenght_of_segment(start_point, end_point):
        return sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)

    @staticmethod
    def get_rad_from_x_of_segment(start_point, end_point):
        vector = DrawHelper.get_vector_of_segment(start_point, end_point)
        a = vector[1][0]
        b = DrawHelper.get_lenght_of_segment(vector[0], vector[1])
        c = DrawHelper.get_lenght_of_segment(vector[1], (a, 0))
        #print(f'rad {(a ** 2 + b ** 2 - c ** 2) / (2 * a * b)}')
        return acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    @staticmethod
    def get_rad_of_triangle(point_a, point_b, point_c):
        side_a = DrawHelper.get_lenght_of_segment(point_c, point_b)
        side_b = DrawHelper.get_lenght_of_segment(point_a, point_c)
        side_c = DrawHelper.get_lenght_of_segment(point_a, point_b)
        return acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b))

    @staticmethod
    def get_arc_circle_rect(center, radius):
        return center[0] - radius, center[1] - radius, 2 * radius, 2 * radius

