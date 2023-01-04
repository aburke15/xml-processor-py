import multiprocessing
import xml.etree.ElementTree as Et
from os import listdir


def get_filenames() -> None:
    # if running this script via IDE
    # path = "../data/"
    path = "data/"
    filenames = []
    for f in listdir(path):
        if ".xml" in f:
            filenames.append(f"{path}{f}")

    if len(filenames) == 0:
        print("Drop xml files in the 'data' folder and try again")
        return

    process_multi_files(filenames)


def process_file(filename: str):
    tree = Et.parse(filename)
    root = tree.getroot()
    type_dict: dict[str, str] = {}

    for element in root:
        is_duplicate, type_name = is_duplicate_type(element, type_dict)
        if is_duplicate:
            print("Duplicate class:", type_name)
            continue

        nominal_prop, min_prop = handle_sub_element(element)
        if min_prop > nominal_prop:
            print("Min greater than nominal detected for class:", type_name)
            continue

    print("EOF:", filename)


def process_multi_files(filenames: [str]) -> None:
    try:
        with multiprocessing.Pool() as pool:
            pool.map(process_file, filenames)
    except Exception as e:
        print("Error:", e)


def is_duplicate_type(element, type_dict) -> (bool, str):
    type_attribute = element.attrib.values()
    type_name = type_attribute.mapping["name"]

    if type_name in type_dict:
        return True, type_name

    type_dict[type_name] = "name"
    return False, type_name


def handle_sub_element(element) -> (int, int):
    nominal_prop = -1
    min_prop = -1
    for sub_element in element:
        if sub_element.tag == "nominal":
            nominal_prop = int(sub_element.text)
        if sub_element.tag == "min":
            min_prop = int(sub_element.text)
        if nominal_prop > -1 and min_prop > -1:
            return nominal_prop, min_prop


def main() -> None:
    get_filenames()


if __name__ == "__main__":
    main()
