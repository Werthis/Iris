import unittest
from iris import ReadFile

SOURCE_FILE = 'Iris_part.csv'

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.program = ReadFile(SOURCE_FILE)
        self.program.open_data_file()
        self.program.read_data_file()
        self.program.iterate()
        self.program.close_file()

    # def test_file_type(self):
    #     self.assertIs(self.program.open_data_file is "<_io.TextIOWrapper name='Iris_part.csv' mode='r' encoding='UTF-8'>")

    def test_reading_lines(self):
        self.assertEqual(self.program.str_list_of_lines[1], ['1', '5.1', '3.5', '1.4', '0.2', 'Iris-setosa'])
        self.assertEqual(self.program.str_list_of_lines[2], ['2', '4.9', '3.0', '1.4', '0.2', 'Iris-setosa'])
        self.assertEqual(self.program.str_list_of_lines[25], ['60', '5.2', '2.7', '3.9', '1.4', 'Iris-versicolor'])

        # SyntaxError('invalid syntax', ('<string>', 1, 1, ))

if __name__ == "__main__":
    unittest.main()
