# Image Segmentation Network Library

This project is being made with the objective of detecting 
and measuring distances between points in an image and 
the points should be marked using 
***[VGG Image annotator](https://www.robots.ox.ac.uk/~vgg/software/via/via.html)***.

## How to use it

In order to use this package you can install it as a pip package using

    pip install -i https://test.pypi.org/simple/ networkLibrary==1.0

or clone it and use it as part of your project using

    git clone <link_of_repository>

## How to prepare the data

In order for the package functions to work, it is advised that one uses the
[VGG Image annotator](https://www.robots.ox.ac.uk/~vgg/software/via/via.html). With this the user should be aware of the order they mark the 
points in each image so that all points marked follow the same sequence and represent
the same thing across all images used.

For now, the package library can only work using the generated **JSON** from [VGG Image annotator](https://www.robots.ox.ac.uk/~vgg/software/via/via.html), further changes will include CSV compatibility.

In the sample images, each image has 3 points marked:

![Annotated Image](samples/examples/example.png)

In all sample images the order in which the points appear is **not inconsequential**. In the example 
images point number 1 is always representative of one of the front horse legs
(depending on which is on the ground), point number 2 is always representative of the 
horse's shoulders, and point number 3 is always representative of the horse's behind.

## The Functions

There are five available functions in this library:

1. extractImages
2. read_json
3. find_floor
4. draw_floor
5. measure_length

### 1. extractImages

| Parameter | Description                                                             | Type   |
|-----------|-------------------------------------------------------------------------|--------|
| pathIn    | The filepath of the video file                                          | String |
| pathOut   | The filepath where the taken frames will be saved                       | String |
| verbose   | verbose = 0 for no extra information, verbose = 1 for extra information | Number |

### 2. read_json

| Parameter | Description                   | Type   |
|-----------|-------------------------------|--------|
| path      | The filepath to the JSON file | String |
| verbose   | verbose = 0 for no extra information, verbose = 1 for extra information | Number |

> returns a dictionary in the format 
> key = <name_of_image_file>, value = <list_of_pixel_coordinates>

### 3. find_floor


| Parameter | Description                             | Type                 |
|-----------|-----------------------------------------|----------------------|
| dict      | The dictionary with each images' points | <String, Number[][]> |

> The dict variable has compatibility with the format returned from function
> read_json described above.

> returns a dictionary in the format
> key = <name_of_image_file>, value = <y_coordinate_of_floor>


### 4. draw_floor


| Parameter       | Description                                         | Type             |
|-----------------|-----------------------------------------------------|------------------|
| dict            | The dictionary with each images' y floor coordinate | <String, Number> |
| img_path        | The filepath to the images' folder                  | String           |
| floor_thickness | Value of how thick the floor line should be         | Number           |
| floor_color     | Value of the RGB colour of the floor line           | Number[]         |

> returns an image object with floor line drawn in

### 5. measure_length


| Parameter         | Description                                                                                                 | Type                 |
|-------------------|-------------------------------------------------------------------------------------------------------------|----------------------|
| dict              | The dictionary with each images' points                                                                     | <String, Number[][]> |
| points_to_measure | An array denoting which distances are to be measured                                                        | Number[][]           |
| pixel_irl         | Value of a pixel in a real life unit (cm, mm, etc)                                                          | Number               |
| verbose           | verbose = 0 for no extra information, verbose = 1 for extra information, verbose = 2 for exception warnings | Number               |
| mode              | "avg" to calculate the average of all measurements                                                          | String               |

> returns a dictionary in the format
> key = <name_of_image_file>, value = <measurements_between_coordinates>,
> when mode is specified as "avg" the function also returns the average of
> all specified measurements in points_to_measure, otherwise it returns None

### Usage Cases and Code Examples

Assuming a project directory the same as 

```
project
│   README.md
│   LICENSE 
│
└───dataset
│   │   via_project_[..]_json.json
└───video
    │   video.mp4
└───main.py
```

And data prepared as instructed in chapter **How to prepare the data**.

#### Extract frames from the video

    video_path = <video_filepath>
    dataset_path = <output_folder>
    extractImages (video_path, dataset_path)

This will yield the following structure.

```
project
│   README.md
│   LICENSE 
│
└───dataset
│   │   frame_0.png
│   │   frame_1.png
│   │   ...
│   │   via_project_[..]_json.json
└───video
    │   video.mp4
└───main.py
```

#### Read VGG Image Annotator JSON

Using the JSON downloaded from VGG Image Annotator, which
should have the following format:

    "frame1.jpg433017": {
        "filename": "frame1.jpg",
        "size": 433017,
        "regions": [
          {
            "shape_attributes": {
              "name": "point",
              "cx": 1709,
              "cy": 601
            },
            "region_attributes": {}
          },
          {
            "shape_attributes": {
              "name": "point",
              "cx": 1718,
              "cy": 252
            },
            "region_attributes": {}
          }
        ],
        "file_attributes": {}
      }, ....

By using the function **read_json** we can go from this format to a simpler 
dictionary format of the following shape

    "frame1.jpg":[[1709,601], [1718,252]]
    "frame2.jpg":[[<x>, <y>], [<x>, <y>], [<x>, <y>]
    ...

The amount of coordinates in each key is dependent on how many points are marked
in the image. The order of the different pixel coordinates is equal to the
order in which they were marked in VGG Image Annotator.

We can make this transformation using:

    path = <json_path>
    dict_json = read_json (path)

#### Find Floor Coordinates

The floor y coordinates, are defined by which coordinate is higher in the y_value for each 
image in the dictionary. In order to use this function, we can reuse the dictionary
returned from the previous function (read_json).

    dict_json = read_json(<json_path>)
    dict_floors = find_floor(dict_json)

The output will have the following shape:

    "frame1.jpg":601
    "frame2.jpg":<y_max>
    ...

#### Draw Floor

If we want to visualize the different floors for each image we can call the
draw_floor function, it shows each images' floor with a drawn in line of 
variable thickness and color.

For this, we can use the dictionary returned from the previous function: **find_floor**.

    dict_json = read_json(<json_path>)
    dict_floors = find_floor(dict_json)
    draw_floor(dict_floors, <img_folder_path>, floor_thickness=9, floor_color=(0, 255, 0))

#### Measure Length

Looking at this image of a horse, we might want to measure the distance between
point 1 and point 2, and point 2 and point 3. For this we can use the function
measure_length.

Firstly, we need to determine which distances the function should measure providing
the function with a list (this is the input parameter points_to_measure). To
specify this we declare the following variable

    points_to_measure = [[0,1], [1,2]]

![Annotated Image](samples/examples/example.png)

By using the dictionary from dict_json we have all the pieces to get the different
measurements.

    dict_json = json_read(<json_path>)
    dict_dist, avg = measure_lenght(dict_json, points_to_measure, mode:'avg')

The parameter *mode* is optional, but it will only return a second parameter
if it is defined as 'avg', otherwise it will return None.

the dictionary dict_dist will have the following shape

    "frame1.jpg":[<distance1>]
    "frame2.jpg":[<distance1>, <distance2>]
    ...

The amount of distances calculated is dependent on the amount of initial 
points marked, for images with one point obstructed or missing, the amount of 
distances calculated varies, this is valid for images with no points marked.
For these situations, the user can choose to see the exception warning if
it decides to use verbose=2.

The average is calculated across columns and according to the amount of 
distances measured for that particular calculation. But it will have the same
amount of values as the amount of distances specified in *points_to_measure*

In this case the avg value would have the shape

    [<distance1>, <distance2>]

