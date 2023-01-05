from src.xml_processor import XmlProcessor


def main():
    processor = XmlProcessor("../data/")
    filenames = processor.get_filenames()
    processor.process_xml_files(filenames)


if __name__ == "__main__":
    main()
