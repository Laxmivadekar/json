import json
i=0
d={}
while i<10:
    name=input('enter the name')
    value=int(input('enter the number'))
    d[name]=value
    i=i+1
print(d)
with open('dictionary to json.json','w') as f:
    json_string=json.dump(d,f,indent=4)
f.close()