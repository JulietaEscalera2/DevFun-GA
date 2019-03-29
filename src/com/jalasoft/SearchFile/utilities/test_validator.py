import unittest
from src.com.jalasoft.SearchFile.controller.objectParameters import ObjectParameters
from src.com.jalasoft.SearchFile.utilities.validator import Validator

class ValidatorTest(unittest.TestCase):
    #to validate the path
    def test_pathData(self):
        expected = self.ObjectParameters.searchParameters['path']

        actual = 'C:\\Users'

        self.assertEqual(expected, actual)

    # to validate the Filename
    def test_fileName(self):
        name = 'python-fundamentals'
        name_correct = ObjectParameters()
        expected = ObjectParameters.searchParameters['Filename']
        actual = name
        self.assertEqual(expected, actual)

    # to validate the size of file
    def test_size(self):
        size = 50
        size_correct = ObjectParameters()
        expected = self.ObjectParameters.searchParameters['Size']
        actual = size
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
