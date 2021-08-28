import json
with open('saral7.json','r') as f:
    json_string=json.load(f)
print(json_string)
f.close()