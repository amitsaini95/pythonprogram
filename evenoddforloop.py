num=int(input("Enter the start range value"))
num2=int(input("Enter the end range value"))
for i in range(num,num2+1):
    if i%2 ==0:
        print("even")
    else:
        print("odd")
