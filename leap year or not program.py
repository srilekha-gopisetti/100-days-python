#year=int(input("enter a year"))
#if year%4==0:
#    if year%100!=0:
#        if year%400==0:
#            print("leap year")
#        else:
 #           print("not a leap year")
 #   else:
 #       print("leap")
#else:
#    print("not a leap year")
        
#def fun(year):
#   if year%4==0:
 #       if year%100!=0:
 #           if year%400==0:
#                print("leap year")
#            else:
 #               print("not a leap year")
#        else:
           # print("leap")
#    else:
  #      print("not a leap year")
#year=int(input("enter a year:"))
#fun(year)


def fun1(year):
    if year%4==0 and year%100!=0 and year%400==0:
        return("leap")
    else:
        return("not leap")
year=int(input("enter a year:"))
print(fun1(year))
      
