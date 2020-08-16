import math
n=int(input("enter a number:"))
i=2
while i<=abs(int(math.sqrt(n))):
    if(n%i==0):
        print(n,"is not a prime number")
        break
    i+=1
else:
    print(n,"is a prime number")
  


