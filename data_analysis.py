import csv

def read_csv(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def calculate_average(data, column):
    valid_values = [float(row[column]) for row in data if row[column].strip().isdigit()]
    return sum(valid_values) / len(valid_values) if valid_values else 0

def find_min_max(data, column):
    values = [float(row[column]) for row in data if row[column].strip().isdigit()]
    return min(values), max(values) if values else (None, None)

if __name__ == "__main__":
    data = read_csv('sample_data.csv')

    column_name = input("Enter column name for analysis: Age/Score(case sesistive) ").strip()

    if column_name in data[0]:
        average = calculate_average(data, column_name)
        min_value, max_value = find_min_max(data, column_name)

        print(f"Average {column_name}: {average}")
        print(f"Min {column_name}: {min_value}")
        print(f"Max {column_name}: {max_value}")
    else:
        print(f"Column '{column_name}' not found!")
