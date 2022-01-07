import numpy as np
from numpy import inf
from queue import PriorityQueue

def calculate_cost(point1, point2):
    cost = np.sqrt( (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 )
    return np.round(cost, 2)

def find_neighbours(map, point, free_space, occupied_space, layer=0):
    size_x, size_y = map.shape[0], map.shape[1]
    occ_map = map[:, :, layer]

    nieghbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(point[0] + i < 1 or point[0] + i > size_y - 1 or point[1] + j < 0 or point[1] + j > size_x - 1 or (i == 0 and j == 0)):
                # print(point[0] + i, [point[1] + j], " - ", occ_map[14 + i][72 + j])
                if occ_map[point[1] + j][point[0] + i] != 255:
                    neighbour_x = point[0] + i
                    neighbour_y = point[1] + j
                    cost = calculate_cost(point, (neighbour_x, neighbour_y))
                    nieghbours.append( (cost, (neighbour_x, neighbour_y)) )

    return nieghbours

def find_path(oryg_map, oryg_coordinates):
    map = np.copy(oryg_map)
    coordinates = oryg_coordinates.copy()

    free_space = (0, 0, 0)
    occupied_space = (255, 0, 0)

    width, height, layers = map.shape
    pixel_count = width * height

    index = 0
    start_point = ( int(coordinates[0]), int(coordinates[1]) )
    goal_point  = ( int(coordinates[2]), int(coordinates[3]) )
    # print('start point: ', start_point, ' goal point: ', goal_point)

    cost_map = np.array( [[inf for x in range(width)] for y in range(height)] )
    cost_map[start_point[0]][start_point[1]] = 0

    visited = set()

    parent_list = []
    for x in range(width):
        for y in range(height):
            parent_list.append( (x,y) )

    parent = {n: None for n in parent_list}

    q = PriorityQueue()
    q.put( (0, start_point) )

    while not q.empty():
        _, curr_node = q.get(q)
        if curr_node in visited:
            continue

        visited.add(curr_node)
        if curr_node == goal_point:
            break

        for distance, curr_neighbour in find_neighbours(map, curr_node, free_space, occupied_space):
            if curr_neighbour in visited:
                continue

            curr_node_x, curr_node_y = curr_node
            curr_neighbour_x, curr_neighbour_y = curr_neighbour

            old_cost = cost_map[curr_neighbour_x][curr_neighbour_y]
            new_cost = cost_map[curr_node_x][curr_node_y] + distance

            if parent[curr_node] != None:
                first_coords = np.subtract(parent[curr_node], curr_node)
                second_coords = np.subtract(curr_node, curr_neighbour)

                if not(first_coords[0] == second_coords[0] and first_coords[1] == second_coords[1]) :
                    new_cost += 1

            if new_cost < old_cost:
                cost_map[curr_neighbour_x][curr_neighbour_y] = new_cost
                parent[curr_neighbour] = curr_node
                priority = new_cost + calculate_cost(goal_point, curr_neighbour)
                q.put( (priority, curr_neighbour) )

    path = []
    curr_node = goal_point
    while curr_node is not None:
        path.append(curr_node)
        curr_node = parent[curr_node]
    path.reverse()

    for x, y in path:
        map[y, x, 1] = 255
        # cv2_imshow(map)

    return map, path
