def primeTest(x):

    num = int(x)
    
    if num <= 1:
        return print("Please enter a number greater than or equal to 2.")
    
    for i in range(2,num):
        
        if num % i == 0:
            return print("Sorry, "+str(num)+" is not a prime.")
        
    return print("Yes! "+str(num)+ " is a prime!")



with open("prime100.txt", "r") as pfile:
    for line in pfile:
        primeTest(line)
pfile.close()

with open("comp100.txt", "r") as cfile:
    for line in cfile:
        primeTest(line)
cfile.close()
