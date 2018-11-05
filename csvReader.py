import csv
import pprint

class DataReader:
    def __init__(self):
        self.csv_path = 'data/Salaries.csv'
        self.csv_file = open(self.csv_path, newline='')
        self.list = []


    def csv_to_list(self):
        self.csv_reader = csv.reader(self.csv_file, delimiter=',')
        for item in self.csv_reader: 
            temp = {
                    'id': item[0],
                    'employee_name': item[1],
                    'title': item[2],
                    'base_pay': item[3],
                    'ot_pay': item[4],
                    'other_pay': item[5],
                    'benifits': item[6],
                    'total_pay': item[7],
                    'tot_pay_ben': item[8],
                    'year': item[9],
                    'notes': item[10],
                    'agency': item[11],
                    'status': item[12]
                    }
            self.list.append(temp)


    def print_list(self):
        pprint.pprint(self.list)



dr = DataReader()
dr.csv_to_list()
dr.print_list()


