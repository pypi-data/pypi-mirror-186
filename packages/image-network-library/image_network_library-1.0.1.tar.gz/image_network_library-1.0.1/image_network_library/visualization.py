import cv2 as cv
from image_network_library import preprocessing
from image_network_library import networks

def show_shapes(dict, connections, path, color=(0, 255, 0), thickness=5):
    '''
    From the connections list of arrays it connects the different coordinates in the dataset dictionary
    Shows ALL images with the connections made, singularly. Press any key to go to the next entry in dict
    :param thickness: thickness of the lines
    :param color: color of the lines
    :param dict: dictionary with structure <name_of_file, array_of_coordinates>
    :param connections: list of arrays describing which xy points connect to each other by the order
    they are represented in the values list of dict
    :param path: the path to the folder where the images described in the keys of dict
    :return: none
    '''

    for key in dict.keys():
        full_path = path + key
        img = cv.imread(full_path)
        values = dict[key]
        print(values)
        for i in connections:
            try:
                img = cv.line(img, values[i[0] - 1], values[i[1] - 1], color, thickness)
            except:
                print("exception")
                continue
        cv.imshow("lines", img)
        cv.waitKey(0)


def show_shapes_random(dict, connections, path, color=(0, 255, 0), thickness=5, how_many=4):
    '''
    From the connections list of arrays it connects the different coordinates in the dataset dictionary
    Shows ALL images with the connections made. Press any key to go to the next entry in dict
    :param how_many: how many images to show simultaneously instead of showing all singularly
    :param thickness: thickness of the lines
    :param color: color of the lines
    :param dict: dictionary with structure <name_of_file, array_of_coordinates>
    :param connections: list of arrays describing which xy points connect to each other by the order
    they are represented in the values list of dict
    :param path: the path to the folder where the images described in the keys of dict
    :return: none
    '''
    for key in dict.keys():
        full_path = path + key
        img = cv.imread(full_path)
        values = dict[key]
        print(values)
        for i in connections:
            try:
                img = cv.line(img, values[i[0] - 1], values[i[1] - 1], color, thickness)
            except:
                continue
        cv.imshow("lines", img)
        cv.waitKey(0)



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
