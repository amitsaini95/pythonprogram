def add(x):
    x+=2
    return x
mynumlist=[3,12,5,63,66,78]
mylist=list(map(add,mynumlist))
print(mylist)