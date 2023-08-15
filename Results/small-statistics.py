import csv
from statistics import mean, mode

def clean_value(value):
    value = value.rstrip('%')  # Remove "%" suffix
    return value

def calculate_mean_and_mode(file_path, column_index):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)

        column_values = []
        for line in lines:
            try:
                float_value = float(clean_value(line[column_index]))
                column_values.append(float_value)
            except ValueError:
                line_name = line[column_index]

        mean_value = sum(column_values) / len(column_values) if column_values else 0.0
        mode_value = max(set(column_values), key=column_values.count) if column_values else None
        max_value = max(column_values)
        min_value = min(column_values)

        return mean_value, mode_value, line_name, max_value, min_value

# Example usage:
file_path = 'results.csv'
column_index = 5  # Index of the column you want to analyze

mean_val, mode_val, line_name, max_value, min_value= calculate_mean_and_mode(file_path, column_index)

print(line_name)
print(f'Max: {max_value}, Min: {min_value}')
print(f"Mean: {mean_val} %")
print(f"Mode: {mode_val} %")