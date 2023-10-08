number=int(input("Enter the prime or non prime number"))
if number>1:
    for i in range(2,number):
        if number%i == 0:
            print("not prime")
            break
    else:
        print("prime")