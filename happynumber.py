n=int(input("enter n value:"))
def num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**2
        n=n//10
    return(s)
def happy(n):
    while n>10:
        k=num(n)
        if k==1 or k==7:
            return('yes')
        else:
            n=k
    else:
        if n==1 or n==7:
            return('yes')
        else:
            return('no')
print(happy(n))
