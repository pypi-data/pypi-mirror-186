import json
import math
import cv2 as cv

from image_network_library import visualization
from image_network_library import networks
def extract_images(pathIn, pathOut, verbose=0):
    '''
    Extracts and saves video frames every 1/4 of a second
    :param pathIn: Path of the video to read frames from
    :param pathOut: Path of the output folder where the resulting frames will be saved
    :param verbose: Verbose is 0 by default, which gives no information
    Verbose is 1 for adittional information while function is running
    :return: none
    '''
    count = 0
    vidcap = cv.VideoCapture(pathIn)
    success, image = vidcap.read()
    while success:
        vidcap.set(cv.CAP_PROP_POS_MSEC, (count * 250))  # added this line
        success, image = vidcap.read()
        if verbose == 1:
            print('Read a new frame: ', success)
        if success:
            cv.imwrite(pathOut + "/frame%d.jpg" % count, image)  # save frame as JPEG file
        count = count + 1


def read_json(path, verbose=0):
    '''
    Reads and converts the VGG Image Annotator json to a dictionary
    :param path: Path of the json file
    :param verbose: Verbose is 0 by default, gives no extra information
    Verbose is 1 to give the dictionary entries
    :return: Dictionary structure <Name of File, Coordinates>
    '''
    f = open(path)
    data = json.load(f)
    dict = {}

    for frame in data:
        points = []
        for shap_att in data[frame]['regions']:
            points.append([shap_att['shape_attributes']['cx'], shap_att['shape_attributes']['cy']])
        dict[data[frame]['filename']] = points
        if verbose == 1:
            print("name:" + data[frame]['filename'] + " points: " + str(points))
    f.close()
    return dict


def find_floor(dict):
    '''
    Finds the lower coordinate point in an image using the dictionary structure from read_json function

    :param dict: Dictionary structure <Name of File, Coordinates>
    :return: Dictionary structure <Name of File, Floor Coordinates>
    '''
    ymax = 0
    for name in dict.keys():
        value = dict.get(name)
        for coord in value:
            if ymax < coord[1]:
                ymax = coord[1]
        dict[name] = ymax
    return dict


# todo review this function
def draw_floor(dict, img_path, floor_thickness=9, floor_color=(0, 255, 0)):
    '''
    Visualise the different floor coordinates pointed by find_floor
    :param dict: Dictionary structure <Name of File, Floor Coordinates>
    :param img_path: Folder of the images in the dictionary structure
    :param floor_thickness: Pixel thickness for visualizing floor
    :param floor_color: Color of the floor line
    :return: Image with floor line
    '''
    for name in dict.keys():
        path = img_path + name
        img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        h, w = img.shape
        init_coord = [0, dict.get(name)]
        end_coord = [w, dict.get(name)]
        cv.line(img, init_coord, end_coord, floor_color, floor_thickness)
        return img


def measure_length(dict, points_to_measure, pixel_irl=None, verbose=0, mode='None'):
    '''
    Measures the lenght between coordinates according to the points_to_measure list
    If you want to measure the distances between point 1 and point 2, and point 3 and point 4
    the points to measure array should have this value [[0,1],[2,3]]
    :param dict: Dictionary structure <Name of File, Coordinates>
    :param points_to_measure: List of pairs to measure inbetween
    :param pixel_irl: The real life measurement of a pixel
    :param verbose: verbose = 0 for zero informational strings during the function's execution
    verbose = 1 for informational output with the final dictionary elements
    verbose = 2 only for when exceptions occur
    :param mode: How to calculate the final distances across all data points,
    mode='avg' for calculating the average across each distance calculated
    :return: Dictionary structure <Name of File, Distances> and Average value - average value is none when mode is not set or 'None'
    '''
    dist_dict = {}
    for name in dict.keys():
        value = dict.get(name)
        dist = []
        for p in points_to_measure:
            if value:
                try:
                    d = math.dist(value[p[0]], value[p[1]])
                    if pixel_irl:
                        d = d * pixel_irl
                    dist.append(d)
                    dist_dict[name] = dist
                except:
                    if verbose == 2:
                        print("Exception Occured")

    {k: v for k, v in dist_dict.items() if v}
    if verbose == 1:
        for name in dist_dict.keys():
            print("Key: " + name + " Value: " + str(dist_dict.get(name)))

    if mode == 'avg':
        avg = [0] * len(points_to_measure)

        for value in dist_dict.values():
            for i in range(len(value)):
                avg[i] = avg[i] + value[i]

        div = [0] * len(points_to_measure)
        for values in dist_dict.values():
            l = len(values)
            for i in range(l):
                div[i] = div[i] + 1

        for i in range(len(avg)):
            if div[i] != 0:
                avg[i] = avg[i] / div[i]

        if verbose == 1:
            print("Averages: " + str(avg))
        return dist_dict, avg
    return dist_dict, None


# todo make dict into tensors
def make_tensors(dict):
    '''
    Transforms the dictionary into input tensors
    :param dict: dictionary of shape <name_of_file, xy_coordinates>
    :return: a dictionary of the same shape but all xy_coordinates list have the same size and shape, any empty spaces
    are filled with [-1, -1]
    '''

    values = list(dict.values())
    longest = 0
    for value in values:
        longest = max(longest, len(value))

    for key in dict.keys():
        if len(dict[key]) != 3:
            dict[key].append([-1, -1])


