import unittest
import os
from ..file_reader import read_file

class TestFileReader(unittest.TestCase):
    def test_correct_list_from_file(self):
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.split(current_dir)[0]
        file = os.path.join(current_dir, "testfile.txt")
        list = read_file(file)
        self.assertEqual(list, ["Ihan", "tavallinen", ",", "tekstitiedosto", "vain", "."])
