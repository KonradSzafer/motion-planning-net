import numpy as np
from pathlib import Path


def get_abs_path(n_parent: int = 0):
    path = Path('../' * n_parent).resolve()
    return str(path)


def steer_to(img, p1, p2):

    def calculate_line(p1, p2):
        x0, y0 = p1
        x1, y1 = p2
        a = (y1 - y0) / (x1 - x0)
        b = y0 - a * x0

        x_range = abs(x0 - x1) - 1
        x_array = np.linspace(x0 + 1, x1, num=x_range, endpoint=False, dtype=int)

        points = []
        for x in x_array:
            y = a * x + b
            y = round(y)
            points.append([x, y])
        return points

    def check_oversection(img, points):
        for x, y in points:
            if img[x, y, 0] == 255:
                return False
        return True

    line = calculate_line(p1, p2)

    return check_oversection(img, line)


def lazy_states_contraction(path):

    can_connect = True
    while can_connect:
        for i in range(len(path) - 2):

            if steer_to(path[0 + i], path[2 + i]):
                path.pop(i + 1)
                can_connect = False

        can_connect = False if can_connect == True else True

    return path


def is_feasible(path):

    feasible = True
    for i in range(len(path) - 1):
        if not steer_to(path[0 + i], path[1 + i]):
            feasible = False

    return feasible