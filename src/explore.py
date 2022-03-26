import json

with open('../../datathon 2/covid19_partition_1.2020-05-30_20.jsonl', 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    print(f"result: {result}")
    print(isinstance(result, dict))
    break

print()