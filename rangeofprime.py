num1=int(input("enter the lower prime range number "))
num2=int(input("enter the lower prime range number "))
for num in range(num1,num2):
    for  i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num)