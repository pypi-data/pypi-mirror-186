import logging
import xmltodict
import dict2xml
import pathlib


class XmlHandler:
    """
    XML files handling class
    """
    def __init__(self, xml_file_path: pathlib.Path):
        """
        Constructor

        Parameters:
            xml_file_path (pathlib.Path) : Path to Pascal VOC annotation XML file

        Throws:
            Exception if file does not exist
        """
        logging.debug("XmlHandler: XmlHandler initiated")
        if not xml_file_path.exists():
            raise Exception(f"The file { xml_file_path } does not exist")

        self.xml_file_path = xml_file_path
        self.xml_data_dict = self._xml_to_dict(xml_file_path)
        self.bounding_boxes_count = self._get_bounding_boxes_count()


    def get_xml_file_name(self, include_extension: bool = True) -> str:
        """
        Get the xml file name

        Parameters:
            include_extension: Whether to include image extension in file name
                Default=True
                Eg. Image name = image1.xml
                    Include extension = True, returns image1.xml
                    Include extension = False, returns image1
        """
        if include_extension:
            return self.xml_file_path.name
        return self.xml_file_path.stem


    def get_xml_file_extension(self, include_dot: bool = False) -> str:
        """
        Get the XML file extension

        Parameters:
            include_dot: Whether to return "xml" or ".xml"
                Default=False

        Eg. "image1.xml" returns "xml", if include dot is True returns ".xml"
            "image1.new.xml" returns "xml", if include dot is True returns ".xml"
        """
        ext = ""
        if include_dot:
            ext = "."
        return ext + self.xml_file_path.name.rsplit(".", 1)[-1]


    def _get_bounding_boxes_count(self) -> int:
        """
        Returns the count of objects/labels present in XML file
        """
        if "object" in self.xml_data_dict["annotation"]:
            annotated_objects = self.xml_data_dict["annotation"]["object"]
            if isinstance(annotated_objects, dict):
                # Single object
                return 1
            # Multiple objects
            return len(annotated_objects)
        return 0


    def get_bounding_boxes_count(self) -> int:
        """
        Get the count of objects/labels present in XML file
        """
        return self.bounding_boxes_count


    def _xml_to_dict(self, xml_file_path: str) -> dict:
        """
        Private method to convert XML file into a python dictionary

        Parameters:
            xml_file_path (str): Complete path to XML file to be loaded
        """
        with open(xml_file_path, 'r', encoding="utf-8") as xml_file:
            xml_file_data = xml_file.read()

        return xmltodict.parse(xml_file_data)


    def get_all_bbox_coordinates_list(self) -> list[list]:
        """
        Get list of objects with their coordinates in form of a 2D list
        Coordinates are: [xmin, ymin, xmax, ymax, label]

        Eg. [
            [1650, 418, 1668, 455, "person"],
            ...
        ]

        Return 2D list of all bounding box coordinates,
        if no bounding box found, returns empty list []
        """
        logging.debug("XmlHandler: Creating bounding boxes coordinates list")
        bounding_box_coordinates_list = []

        if self.bounding_boxes_count > 0:
            bounding_boxes = self.xml_data_dict["annotation"]["object"]

        if self.bounding_boxes_count == 1:
            # Single object/labels/annotation bounding box found
            # Object is of type dictionary, because only single object is present
            bounding_box_coordinates_list.append(self._get_bbox_coordinate(bounding_boxes))
        elif self.bounding_boxes_count > 1:
            # Multiple objects/labels/annotation boudning boxes found
            # Object is of type list, because multiple objects are present
            for bounding_box in bounding_boxes:
                bounding_box_coordinates_list.append(self._get_bbox_coordinate(bounding_box))

        return bounding_box_coordinates_list


    def _get_bbox_coordinate(self, bbox_dict: dict) -> list:
        """
        Get list of label/object/boudning box coordinates
        Coordinates are: [xmin, ymin, xmax, ymax, label]

        Parameters:
            bbox_dict(dict): Boudning box data as dict type

        Return a list of bounding box coordinate
        """
        xmin = int(float(bbox_dict["bndbox"]["xmin"]))
        ymin = int(float(bbox_dict["bndbox"]["ymin"]))
        xmax = int(float(bbox_dict["bndbox"]["xmax"]))
        ymax = int(float(bbox_dict["bndbox"]["ymax"]))
        label = bbox_dict["name"]
        return [xmin, ymin, xmax, ymax, label]


    def update_all_bounding_box_coordinates(self, bounding_boxes_coordinates_list: list[list]) -> None:
        """
        Update the bounding box coordinates in the XML file

        Parameters:
            bounding_boxes_coordinates_list: A 2D list containing all bouding box coordinates
                Format- [xmin, ymin, xmax, ymax, label]
                Eg.- [
                    [1650, 418, 1668, 455, "person"],
                    ...
                ]
        """
        if self.bounding_boxes_count > 0:
            annotated_object = self.xml_data_dict["annotation"]["object"]

            if self.bounding_boxes_count == 1:
                self._update_bbox_coordinate(annotated_object, bounding_boxes_coordinates_list[0])
            elif self.bounding_boxes_count > 1:
                i = 0
                for bounding_box in annotated_object:
                    self._update_bbox_coordinate(bounding_box, bounding_boxes_coordinates_list[i])
                    i += 1


    def _update_bbox_coordinate(self, bbox_dict: dict, bbox_coordinate: list) -> None:
        """
        Update bounding box coordinates and name in object/label

        Parameters:
            bbox_dict: A dict containing boudning box details, this dict will be updated
                with new bounding box coordinates
            bbox_coordinates: New coordinates for the bounding box
                Coordinate list format: [xmin, ymin, xmax, ymax, name]
        """
        bbox_dict["bndbox"]["xmin"] = bbox_coordinate[0]
        bbox_dict["bndbox"]["ymin"] = bbox_coordinate[1]
        bbox_dict["bndbox"]["xmax"] = bbox_coordinate[2]
        bbox_dict["bndbox"]["ymax"] = bbox_coordinate[3]
        bbox_dict["name"] = bbox_coordinate[4]


    def get_annotation_classes_details(self) -> dict:
        """
        Returns a dict of all classes present in XML file with their details
        Eg: {
            "<class_name>": <number_of_occurences>
        }
        """
        objects_dict = {}

        if self.bounding_boxes_count > 0:
            annotated_objects = self.xml_data_dict["annotation"]["object"]

        if self.bounding_boxes_count == 1:
            # Single object present
            obj_name = annotated_objects["name"]
            if obj_name in objects_dict:
                objects_dict[obj_name] += 1
            else:
                objects_dict[obj_name] = 1
        elif self.bounding_boxes_count > 1:
            # Multiple objects present
            for obj in annotated_objects:
                obj_name = obj["name"]
                if obj_name in objects_dict:
                    objects_dict[obj_name] += 1
                else:
                    objects_dict[obj_name] = 1

        return objects_dict


    def remove_class(self, remove_class_list: list) -> None:
        """
        To remove object of specific classes from the annotation file

        Parameters:
            class_list (list): List of class labels to be removed from the annotation(.xml) file
        """
        if self.bounding_boxes_count > 0:
            # List of classes available in current annotation file
            available_class_list = list(self.get_annotation_classes_details())

            # Check for any removable class
            is_removable_class_present = False
            for class_name in available_class_list:
                if class_name in remove_class_list:
                    is_removable_class_present = True

            if is_removable_class_present:
                # Removing the required classes
                annotated_objects = self.xml_data_dict["annotation"]["object"]
                filtered_objects = []

                if self.bounding_boxes_count == 1 and (annotated_objects["name"] not in remove_class_list):
                    # There is only 1 annotation in the current file and need to be removed
                    filtered_objects.append(annotated_objects)
                elif self.bounding_boxes_count > 1:
                    # Multiple objects in file
                    for obj in annotated_objects:
                        obj_name = obj["name"]
                        if obj_name not in remove_class_list:
                            filtered_objects.append(obj)

                # Updating annotation file
                if len(filtered_objects) == 0:
                    # No object of interest present, remove object tag
                    self.xml_data_dict["annotation"].pop("object")
                if len(filtered_objects) == 1:
                    # Only single object of ineterest present, adding object as dict
                    self.xml_data_dict["annotation"]["object"] = filtered_objects[0]
                elif len(filtered_objects) > 1:
                    # Multiple objects of interest present, adding objects as a list
                    self.xml_data_dict["annotation"]["object"] = filtered_objects

        # Updating objects count after removing objects/annotations
        self.bounding_boxes_count = self._get_bounding_boxes_count()


    def save_xml_file(self, save_path: str) -> None:
        """
        Save the XML file

        Limitation:
            Not able to add attribubtes, so this will remove verified attribute

        Parameters:
            save_path (str): Complete path with extension of XML file
        """
        logging.debug("XmlHandler: Save annotation file %s", save_path)

        # Due to library limitation removing verified attribute from annotation tag
        # https://github.com/delfick/python-dict2xml#limitations
        if "@verified" in self.xml_data_dict["annotation"]:
            self.xml_data_dict["annotation"].pop("@verified")

        new_xml_data = dict2xml.dict2xml(self.xml_data_dict)
        xml_file = open(save_path, "w", encoding="utf-8")
        xml_file.write(new_xml_data)
        xml_file.close()
