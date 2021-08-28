# 15
# 14 10
# 13 9 6
# 12 8 5 3
# 11 7 4 2 1
i=1
k=15
while i<=5:
    m=k
    j=1
    l=4
    while j<=i:
        print(m,end=' ')
        m=m-l
        l=l-1
        j=j+1
    print()
    i=i+1
    k=k-1