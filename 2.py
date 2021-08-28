i=1
sum=0
while i<=2:
    user1=input("enter numerical in words(one/two):")
    b=user1.split()
    j=0
    s=""
    while j<len(b):
        if b[j]=="one":
            s=s+str(1)
        elif b[j]=="tw0":
            s=s+str(2)
        elif b[j]=="three":
            s=s+str(3)
        elif b[j]=="four":
            s=s+str(4)
        elif b[j]=="five":
            s=s+str(5)
        elif b[j]=="six":
            s=s+str(6)
        elif b[j]=="seven":
            s=s+str(7)
        elif b[j]=="eight":
            s=s+str(8)
        elif b[j]=="nine":
            s=s+str(9)
        elif b[j]=="zero":
            s=s+str(0)
        j=j+1
    sum=sum+int(s)
    i=i+1
print(sum)

    

