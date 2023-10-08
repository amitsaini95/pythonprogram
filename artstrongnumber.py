num=int(input("Enter the number "))
sum=0
temp=num
order=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**order
    temp//=10   
if sum == num:
    print("it is armstrong number")
else:
    print("it is not armstrong number")