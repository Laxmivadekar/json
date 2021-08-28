# Q8. You have the details of four employees List my:- 
# Now you have to create 4 dictionaries viz. emp1 emp2 emp3 and emp4. 
# The dictionary key of each employee should be name, designation, age and salary.
#  And all these are the keys of the dictionary, which I have given the list main value.
#  Do you have to file a json using isca? As given
import json
a=[['Laxmi','python learner',22,0],['swapna','programme designer',22,100000,],['Shailaja','Interior designer',22,200000,],['Savithri','software engineer',22,1000000,]]
b=['name','designation','Age','Salary']
d={}
f='employee'
i=0
c=1
while i<len(a):
    j=0
    k=0
    d1={}
    while j<len(b):
        d2=b[k]
        d1[d2]=a[i][j]
        k=k+1
        j=j+1
    c_e_c=f+str(c)#combine employee and count
    d[c_e_c]=d1
    i=i+1
    c=c+1
# print(d)
json_string=json.dumps(d,indent=4)
print(json_string)



# o/p: { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",{ 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }




#        "salary":"24000",
#          }
#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }
#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }



