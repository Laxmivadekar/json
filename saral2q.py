# Q.2 Python object ko json data main convert karne ka program likho?
# Example:
# Input :-
import json
d={ "name": "David",
     "class":"I",
     "age": 6  }
json_string=json.dumps(d)
print(json_string)

# Output:-
# {
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }
