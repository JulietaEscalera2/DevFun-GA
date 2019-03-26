import unittest

from src.com.jalasoft.SearchFile.utilities.validator import Validator

class ValidatorTest(unittest.TestCase):
    def test_pathData(self):
        list = 'C:\\Users\\hp\\Documents\\cartas'
        # path_correct = Validator(list)
        expected = list('C:\\Users\\hp\\Documents\\cartas')
        actual = list('C:\\Users\\hp\\Documents\\cartas')
        self.assertEqual(expected, actual)

    # def test_pathName(self):
    #     name = 'python-fundamentals'
    #     name_correct = Validator(list_SearchFile)
    #     expected = name_correct.read_list('python-fundamentals')
    #     actual = name_correct.read_list('python-fundamentals')
    #     self.assertEqual(expected, actual)
    #
    # def test_sizeName(self):
    #     size = 50
    #     size_correct = Validator(list_SearchFile)
    #     expected = size_correct.read_list(50)
    #     actual = size_correct.read_list(50)
    #     self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
