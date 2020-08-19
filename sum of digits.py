        code 1
def sum_digits(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n//=10
    return sum
n=int(input("enter a number:"))
print(sum_digits(n))

         code 2

n=input("enter n value:")
sum=0
for i in n:
    sum+=int(i)
print(sum)    



    
    
