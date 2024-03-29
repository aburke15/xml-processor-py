import multiprocessing as mp
import xml.etree.ElementTree as Et
from os import listdir


class XmlProcessor:
    XML_FILE = ".xml"

    def __init__(self, path: str):
        self.path = path

    def get_filenames(self) -> [str]:
        filenames = []
        for f in listdir(self.path):
            if self.XML_FILE in f:
                filenames.append(f"{self.path}{f}")

        return filenames

    def process_xml_files(self, filenames: [str]) -> None:
        try:
            if len(filenames) == 0:
                print("Drop .xml files in 'data' folder and try again.")
                return
            with mp.Pool(len(filenames)) as pool:
                pool.map(self.process_xml_file, filenames)
        except Exception as e:
            print("Error:", e)

    def process_xml_file(self, filename: str) -> None:
        if len(filename) == 0 or self.XML_FILE not in filename:
            print("Drop an .xml file in the data folder and try again.")
            return
        tree = Et.parse(filename)
        root = tree.getroot()

        self.__handle_xml_elements(root)

        print("EOF:", filename)

    def __handle_xml_elements(self, xml_root):
        class_dict: dict[str, str] = {}
        for element in xml_root:
            is_duplicate_class, class_name = self.__is_duplicate_class(element, class_dict)
            if is_duplicate_class:
                print("Duplicate class:", class_name)
                continue

            nominal_prop, min_prop = self.__handle_xml_sub_elements(element, class_name)
            if min_prop > nominal_prop:
                print("Min > nominal for class:", class_name)

    @staticmethod
    def __is_duplicate_class(element: Et.Element, class_dict: dict[str, str]) -> (bool, str):
        name_attribute = element.attrib.values()
        class_name = name_attribute.mapping["name"]

        if class_name in class_dict:
            return True, class_name

        class_dict[class_name] = "name"
        return False, class_name

    @staticmethod
    def __handle_xml_sub_elements(element: Et.Element, class_name: str) -> (int, int):
        nominal_prop = -1
        min_prop = -1
        for sub_element in element:
            if sub_element.tag == "nominal":
                nominal_prop = int(sub_element.text)
            if sub_element.tag == "min":
                min_prop = int(sub_element.text)
            if nominal_prop > -1 and min_prop > -1:
                return nominal_prop, min_prop
