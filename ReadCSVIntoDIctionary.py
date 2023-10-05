import csv

def read_CSV_into_dictionary(csv_file_path):
    CSV_dictionary = {}
    try:
        with open(csv_file_path, mode='r') as file:
           
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                
                title = row['TITLE']
                actl = int(row['ACTL'])
                max_value = int(row['MAX'])
    
                CSV_dictionary[title] = {
                    'ACTL': actl,
                    'MAX': max_value
                    }
    finally:
        file.close()
    return CSV_dictionary

csv_file_path = "C:/Users/donny/Downloads/CSV+example.csv" #This file path was to test locally will need to be changed for future uses
print(read_CSV_into_dictionary(csv_file_path))
