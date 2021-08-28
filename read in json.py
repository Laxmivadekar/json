import json
with open('lucky.json','r') as f:
    json_string=json.load(f)
print(json_string)
f.close()