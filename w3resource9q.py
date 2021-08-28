# Write a Python program to access only unique key value of a Python object.
import json
python_obj = '{"a":1, "a":2, "a":3, "a":4, "b":1, "b":2}'
print('original one:',python_obj)
json_obj = json.loads(python_obj)
print('ofter covertion python object To json: ',json_obj) 
print('_______________________________')
try:
    if '1' != 1:
        raise "someError"
    else:
        print("someError has not occured")
except:
    print ("someError has occured")