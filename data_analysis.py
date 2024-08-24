import csv

def read_csv(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def calculate_average(data, column):
    total = sum(float(row[column]) for row in data)
    return total / len(data)

if __name__ == "__main__":
    data = read_csv('sample_data.csv')
    average_age = calculate_average(data, 'Age')
    print(f"Average Age: {average_age}")