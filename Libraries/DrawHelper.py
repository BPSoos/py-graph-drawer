import sys


class CustomIterable(object):

    def __init__(self, to_iter=None):
        if isinstance(to_iter, (tuple, list, dict)):
            self._to_iter = to_iter
        else:
            raise TypeError(f'Input type of {type(to_iter)} is invalid for '
                            f"<property '{sys._getframe().f_code.co_name}'> of <class '{self.__class__.__name__}'>")

    def __str__(self):
        return str(self._to_iter)

    def __len__(self):
        return len(self._to_iter)

    def __iter__(self):
        self.n = 0
        return iter(self._to_iter)

    def __next__(self):
        if self.n < len(self):
            result = self._to_iter[self.n]
            self.n += 1
            return result


class Point(CustomIterable):

    def __init__(self, x, y):
        super(Point, self).__init__([x, y])

    @property
    def x(self):
        return self._to_iter[0]

    @x.setter
    def x(self, value):
        self._to_iter[0] = value

    @property
    def y(self):
        return self._to_iter[1]

    @y.setter
    def y(self, value):
        self._to_iter[1] = value


class Segment(CustomIterable):

    def __init__(self, start_point, end_point):
        super(Segment, self).__init__([start_point, end_point])

    @property
    def start(self):
        return self._to_iter[0]

    @start.setter
    def start(self, value):
        if isinstance(value, Point):
            self._to_iter[0] = value
        elif isinstance(value, (tuple, list)):
            self._to_iter[0] = [*value]
        else:
            raise TypeError(f'Input type of {type(value)} is invalid for '
                            f"<property '{sys._getframe(  ).f_code.co_name}'> of <class '{self.__class__.__name__}'>")

    @property
    def end(self):
        return self._to_iter[1]

    @end.setter
    def end(self, value):
        if isinstance(value, Point):
            self._to_iter[1] = value
        elif isinstance(value, (tuple, list)):
            self._to_iter[1] = [*value]
        else:
            raise TypeError(f'Input type of {type(value)} is invalid for '
                            f"<property '{sys._getframe(  ).f_code.co_name}'> of <class '{self.__class__.__name__}'>")


class DrawHelper(object):

    def __init__(self):
        pass

    @staticmethod
    def get_rect_around_segment(start_point, end_point, get_top_rect=True):
        centers, radius = DrawHelper.get_arc_circle_data(start_point, end_point)
        center = centers[1] if get_top_rect else centers[0]
        return center[0] - radius, center[1] - radius, 2 * radius, 2 * radius

    @staticmethod
    def get_start_angle_for_point(point, center):
        point = DrawHelper.get_vector_of_segment(center, point)[1]
        x = point[0]
        y = point[1]
        if x > 0 and y <= 0:
            return atan(abs(y / x))
        if x <= 0 and y <= 0:
            return pi - atan(abs(y / x))
        if x <= 0 and y > 0:
            return pi + atan(abs(y / x))
        if x > 0 and y > 0:
            return 2 * pi - atan(abs(y / x))

    @staticmethod
    def get_arc_data_of_segment(start_point, end_point, get_top=False):
        angles = DrawHelper.get_start_angle_segment_of_rected_segment(start_point, end_point, get_top_rect=get_top)
        arc_rect = DrawHelper.get_rect_around_segment(start_point, end_point, get_top_rect=get_top)
        return (*angles, arc_rect)

    @staticmethod
    def get_start_angle_segment_of_rected_segment(start_point, end_point, get_top_rect=True):
        centers, radius = DrawHelper.get_arc_circle_data(start_point, end_point)
        center = centers[1] if get_top_rect else centers[0]
        angle_1 = DrawHelper.get_start_angle_for_point(start_point, center)
        angle_2 = DrawHelper.get_start_angle_for_point(end_point, center)
        if start_point[1] < center[1] < end_point[1] and angle_2 > pi + angle_1:
            angle = (angle_2, angle_1)
        elif start_point[1] > center[1] > end_point[1] and angle_1 > pi + angle_2:
            angle = (angle_1, angle_2)
        else:
            angle = (angle_1, angle_2) if angle_1 < angle_2 else (angle_2, angle_1)
        return angle

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
