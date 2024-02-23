import csv
import json

# Read and print values in the first column of the CSV file
csv_file_path = 'day-08/Submission/BEA-DAY8/example1.csv'
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Get the header row

    for line in csv_reader:
        name, age, gender = line
        print(name)

# Read and print the contents of the JSON file
json_file_path = 'day-08/Submission/BEA-DAY8/example2.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

    for item in data:
        name = item.get('name', '')
        gender = item.get('gender', '')
        print(f"Name: {name}, Gender: {gender.capitalize()}")