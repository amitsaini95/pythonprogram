def positiveNum(x):
    if x>=0:
        return x
mylistnum=[10,-3,-364,30,33,5,-330,-42,-413]
list12=[]
list12=list(filter(positiveNum,mylistnum))
print(list12)