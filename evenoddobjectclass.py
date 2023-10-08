class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        if num%2 == 0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n=Number(23)
n=Number(24)
n=Number(43)
n=Number(60)
print(n.even)
print(n.odd)