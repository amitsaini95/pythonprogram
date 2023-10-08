# num=int(input("Enter the right star row"))
# for i in range(1,num+1):
#     for k in range(num,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
num=int(input("Enter the right  number"))
for i in range(1,num+1):
    for k in range(num,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()