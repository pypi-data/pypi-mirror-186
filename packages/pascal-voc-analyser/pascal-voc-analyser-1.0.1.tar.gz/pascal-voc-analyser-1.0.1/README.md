# Pascal VOC Analyser

Analyse your Pascal VOC XML annotation files with the help fo this package.



## Supported Features

- Get the count of annotations/objects/bounding boxes in the Pascal VOC XML file.

- Get the details of all the available classes in the XML annotation file.

- Get the coordinates of bounding boxes.

- Update the bounding boxes coordinates.

- Remove annotation classes from the VOC XML file.

- Save the modified annotation file.



## Usage

### Get Bounding Boxes Count

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)
xml_handler.get_bounding_boxes_count()

# Output
# 27
```



### Annotated Classes

Returns a dictionary containing annotated label name with it's count.

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)
xml_handler.get_annotation_classes_details()

# Output
# { "person": 10, "car": 12 }
```



### Bounding Box Coordinates

Get a 2D list of all the bounding box coordinates.

Each bounding box is represented as: `[xmin, ymin, xmax, ymax, label]`.

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)
xml_handler.get_all_bbox_coordinates_list()

# Output
# [
#    [1650, 418, 1668, 455, "person"],
#    ...
# ]
```



### Update Bunding Box Coordinates

To update the bouding box coordinates, pass a 2D list containing coordinates for new bounding boxes.

Each bounding box coordinate should look like: `[xmin, ymin, xmax, ymax, label]`.

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)
new_coordinates = [[647, 389, 664, 425, 'person_standing']]
xml_handler.update_all_bounding_box_coordinates(new_coordinates)
```



### Remove Annotation Classes

Sometime you may want to keep some classes and remove all others. Let's see how you can do this.

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)
remove_class_list = ["car", "bike"]
xml_handler.remove_class(remove_class_list)
```



### Save XML File

```python
xml_file_path = pathlib.Path("image1.xml")
xml_handler = XmlHandler(xml_file_path)

# Removing unnecesary classes
remove_class_list = ["car", "bike"]
xml_handler.remove_class(remove_class_list)

# Perform other operations if required
# ...

# Saving new file
output_file_path = "./output/image1_filtered_classes.xml"
xml_handler.save_xml_file(output_file_path)
```