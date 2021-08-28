import json
d=[{'id':0,'name':'laxmi','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':1,'name':'rajasri','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':2,'name':'jyotsna','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':3,'name':'jyothi','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':4,'name':'mahanandha','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':5,'name':'sunil','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':6,'name':'sajith','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':7,'name':'sainath','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':8,'name':'srinivas','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'id':9,'name':'venkatesh','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'}]
with open('uber.json','w') as f:
    json_string=json.dump(d,f,indent=4)
f.close()
    # j=0
    # while j<len(a):
    #     d[i][j]=input('enter the id of the rider')
    #     d['current location']=input('enter the current location of the user')
    #     d['destination']=input('enter the current location of the user')
