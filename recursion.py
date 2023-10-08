def number(n):
    if n==0 or n==1:
        return 1
    else:
        return n*number(n-1)
Num=int(input("Enter the Number"))
num=number(Num)
print(num)
