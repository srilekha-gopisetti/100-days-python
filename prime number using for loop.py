      code 1
##n=int(input("enter any number:"))
##count==0
##for i in range(1,n+1):
##    if n%i==0:
##        count+=1
##if count==2:
##    print(n,"prime number")
##else:
##    print(n,"not a prime number")
      code 2
##n=int(input("enter n value"))
##count=0
##for i in range(2 ,n):#5%2,5%3,#5%4
##    if n%i==0:
##      count+=1
#if count>0:
#    print(n,"not prime number")
#else:
#    print(n,"prime number")
     code 3
n=int(input("enter a number"))
for i in range(2,n):
    if n%i==0:
        print(n,'not a primenumber')
        break
else:
    print(n,'primenumber')
