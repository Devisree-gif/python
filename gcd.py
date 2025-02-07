def gcd(a,b):
    list1=[]
    for i in range(1,a+1):
        if a%i==0:
            list1.append(i)
    list2=[]
    for j in range(1,b+1):
        if b%j==0:
            list2.append(j)
    cf=[]
    for x in list1:
        if x in list2:
            cf.append(x)
            return cf[-1]
a=10
b=20
print(gcd(a,b))
print()














          
