from xml_processor import XmlProcessor


def main():
    # if running via IDE
    # path = "../data/"
    path = "data/"
    processor = XmlProcessor(path)
    filenames = processor.get_filenames()
    processor.process_xml_file("data/test_data_type_duplicate.xml")


if __name__ == "__main__":
    main()
