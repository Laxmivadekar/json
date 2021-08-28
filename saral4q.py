# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
# Example:
# Input :-
import json
a={'4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
d={}
for i in sorted(a.keys()):
    d[i]=a[i]
json_string=json.dumps(d)
print(json_string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

# Output:- JSON data:
#    {"1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7}
