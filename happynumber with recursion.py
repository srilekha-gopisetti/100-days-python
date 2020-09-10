n=int(input("enter n value:"))
sum1=0
def happy(n):
    sum1=0
    if(n==1 or n==7):
        return("yes")
    elif(n<10):
        return("no")
    else:
        while(n>0):
            num=n%10
            sum1+=num**2
            n=n//10
        return(happy(sum1))
print(happy(n))
