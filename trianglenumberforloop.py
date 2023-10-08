num=int(input("enter the triangle number"))
for i in range(1,num+1):
    for j in range(num,i,-1):
        print("",end=" ")
    for k in range(1,i+1):
        print(i,end=" ")
    print()