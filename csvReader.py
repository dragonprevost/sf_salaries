import csv


class DataReader:
    def __init__(self):
        self.csv_path = 'data/Salaries.csv'
        self.csv_file = open(self.csv_path, newline='')

    def csv_to_list(self):
        self.csv_reader = csv.reader(self.csv_file, delimiter=',')
        for item in self.csv_reader: 
            print(item)





dr = DataReader()
dr.csv_to_list()
