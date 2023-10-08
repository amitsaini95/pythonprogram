num=int(input('Enter the pattern star'))
for i in range(0,num+1):
    for j in range(num,i,-1):
        print("*",end="")
    print()