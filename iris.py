from csv import reader
from sklearn.decomposition import PCA

SOURCE_FILE = 'Iris_part.csv'

class ReadFile():

    def __init__(self, source_file_path, number_of_rows: int=None):
        self.source_file_path = source_file_path
        self.number_of_rows = number_of_rows        
        self.str_list_of_lines = []

    def open_data_file(self):
        self.data_file = open(SOURCE_FILE, 'r')
        return self.data_file

    def read_data_file(self):
        self.data_file_read = reader(self.data_file)
        return self.data_file_read

    def iterate(self):
        for row in self.data_file_read:
            self.str_list_of_lines.append(row)
        # for i in self.

    def close_file(self):
        self.data_file.close()


if __name__ == "__main__":
    file = ReadFile(SOURCE_FILE)
    file.open_data_file()
    file.read_data_file()
    file.iterate()
    file.close_file()