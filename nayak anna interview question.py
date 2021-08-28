import json
a=[]
b='username'
c='passwor'
while True:
    d={}
    user=input('enter the user name')
    password=input('enter the password')
    d[b]=user
    d[c]=password
    a.append(d)
    print(a)
    with open('list.json','w') as f:
        json_string=json.dump(a,f,indent=4)
    f.close()
