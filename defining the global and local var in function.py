#a=10
#print(a,'1')
#def ex():
#    a=10
#    a+=1
 #   print(a,'2')
#ex()
#print(a,'3')

a=10
print(a,'1')
def ex():
    global a
    a=10
    a+=1
    print(a,'2')
ex()
print(a,'3')
