import json

# given a list of json files
file_names = ['file1.json', 'file2.json', 'file3.json']

# the dict for json files
merged_data = {}

# loop
for file_name in file_names:
    with open(file_name) as f:
        data = json.load(f)
        merged_data.update(data)

# merge
with open('merged_data.json', 'w') as f:
    json.dump(merged_data, f, indent=4)