import unittest as ut
from xml_processor import *


class XmlProcessorTests(ut.TestCase):

    def test_get_filenames(self):
        processor = XmlProcessor("../data/")
        filenames = processor.get_filenames()
        self.assertTrue(len(filenames) > 0)


if __name__ == "__main__":
    ut.main()
