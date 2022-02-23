import sys
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import json

import cv2
# from google.colab.patches import cv2_imshow
def cv2_imshow(img):
    img = np.concatenate((img[:,:,2:3], img[:,:,1:2], img[:,:,0:1]), axis=2)
    plt.imshow(img)
    plt.show()

# !pip3 install rich
from rich.progress import Progress

from utils import get_abs_path
from a_star import find_path


def load_images(path):
    images_path = path + 'maps/'
    json_path = path + 'planned_maps/'
    data = {}
    images = []
    files = []

    for (dirpath, dirnames, filenames) in os.walk(json_path):
            files.extend(filenames)
            break

    for (dirpath, dirnames, filenames) in os.walk(images_path):
            images.extend(filenames)
            break

    for file in files:
        file = file[0:-5] + '.png'
        if file in images:
            images.remove(file)

    images = sorted(images)

    with Progress() as progress:
        task = progress.add_task('[yellow]Loading images...', total=len(images))

        for i in range(len(images)):
            img_path = images_path + images[i]
            img = cv2.imread(img_path)
            data[images[i]] = img
            progress.update(task, advance=1)

    return data


def get_points(image):
    image = np.copy(image)
    points = []
    width = image.shape[0]
    height = image.shape[1]

    for y in range(height):
            for x in range(width):
                value = image[y, x, 1]
                if value == 255:
                    x_p = x + 2
                    y_p = y + 2
                    points.append(x_p)
                    points.append(y_p)
                    for i in range(y, y+5):
                        for j in range(x, x+5):
                            image[i, j, 1] = 0

    return points


def get_coordinates(images):

    rows = []
    with Progress() as progress:
        task = progress.add_task('[yellow]Loading coordinates...', total=len(images))

        for key in images:
            points = get_points(images[key])
            rows.append(points)
            progress.update(task, advance=1)

    return rows


def load_data(path):

    images = load_images(path)
    coordinates = get_coordinates(images)
    return images, coordinates


def mark_path_points(oryg_map, oryg_path):
    map = np.copy(oryg_map)
    path = oryg_path.copy()
    start_point = path[0]
    goal_point = path[-1]
    path = path[1:-1]

    # y, x
    directions_dict = {
        (-1,-1): 'NW',
        (-1, 0): 'N',
        (-1, 1): 'NE',
        ( 0, 1): 'E',
        ( 1, 1): 'SE',
        ( 1, 0): 'S',
        ( 1,-1): 'SW',
        ( 0,-1): 'W'
    }

    mark_points = []
    last_x = start_point[0]
    last_y = start_point[1]
    last_dir = None

    for curr_x, curr_y in path:
        x_change = curr_x - last_x
        y_change = curr_y - last_y
        dir = directions_dict[(y_change, x_change)]

        if dir is not last_dir:
            mark_points.append( (last_x, last_y) )

        last_x = curr_x
        last_y = curr_y
        last_dir = dir

    mark_points.append(goal_point)

    for x, y in mark_points:
        map[y, x, 1] = 0
        map[y, x, 2] = 255
    return map, mark_points


def generate_point_paths(dataset, coordinates, results_path):
    size = len(dataset)
    maps = []
    paths = {}

    with Progress() as progress:
        task = progress.add_task('[yellow]Loading images...', total=size)

        i = 0
        for key in dataset:
            map = dataset[key]
            coor = coordinates[i]
            map, path = find_path(map, coor)
            map, points = mark_path_points(map, path)
            maps.append(map)
            paths[key] = points
            print(key)

            with open(results_path + 'planned_maps/' + key[0:-4] + '.json', 'w') as f:
                json.dump(paths, f)

            #cv2_imshow(map)

            progress.update(task, advance=1)
            i += 1

    return maps, paths


if __name__ == "__main__":

    project_path = get_abs_path(0)

    dataset_path = project_path + '/data/train/'
    results_filename = 'paths.json'

    dataset, coordinates = load_data(dataset_path)

    maps, paths = generate_point_paths(dataset, coordinates, dataset_path)

