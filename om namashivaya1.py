# Q.1 Json data ko python object main convert karne ka program likho?.
# Example:
# Input :-
import json
d='''{"Name":"Laxmi", 
     "Class":"python", 
     "Age":22}'''
python_string=json.loads(d)
print(python_string)

# Output :-
#     {'Name': 'Ram', 
#     'Class': 'IV', 
#     'Age': 9}
