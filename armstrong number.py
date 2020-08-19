def is_armstrong(n):
    arm=0
    n1=n
    while n>0:
        rem=n%10
        arm+=rem*rem*rem
        n//=10
    if n1==arm:
        return("armstrong")
    else:
        return("not armstrong")
n=int(input("enter n value:"))
print(is_armstrong(n))

