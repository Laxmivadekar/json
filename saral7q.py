# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# Example:
import json
text='''Name Abhishek
     Designation CEO of navgurukul
     Gender male
     Age 29'''
with open('saral7.json','w') as f:
    json_string=json.dump(text,f,indent=4)
f.close()
# Output:-
# Json_file.json:-
# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }
