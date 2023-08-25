
import os
import json
import csv


script_directory = os.path.dirname(os.path.abspath(__file__))


data_file_path = os.path.join(script_directory, 'config')

# Path to the folder containing JSON files
json_folder = 'config'

# List to store combined JSON data
combined_data = []

# Iterate over all JSON files in the folder
for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        json_path = os.path.join(json_folder, filename)
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                combined_data.extend(data)

# List of required fields to include in the CSV output
required_fields = ['a', 'b', 'c','d']

# Extract all unique keys from the combined data
all_keys = set()
for item in combined_data:
    if isinstance(item, dict):
        all_keys.update(item.keys())

# Determine the fields to write to the CSV based on required_fields
fields_to_write = [field for field in all_keys if field in required_fields]

# Specify the CSV output file
csv_file = 'output5.csv'

# Write CSV data
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fields_to_write)
    csv_writer.writeheader()
    for item in combined_data:
        if isinstance(item, dict):
            filtered_item = {field: item[field] for field in fields_to_write if field in item}
            csv_writer.writerow(filtered_item)
print(f'JSON data from all files with required fields has been combined and saved to {csv_file}')
