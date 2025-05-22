import csv
import json

csv_file = 'profiles1.csv'
json_file = 'profiles.json'

data = []
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)
