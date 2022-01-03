user=int(input("enter number"))
user2=user
add=0
while 0<user:
    a=user%10
    add+=a
    user=user//10
if user2%add==0:
    print("harsad number")
else:
    print("not")






