def show_number(limit):
    x=0
    while x<limit:
        if x%2==0:
            print(x,"even")
        else:
            print(x,"odd")
        x+=1
call=show_number(100)
print(call)
show_number(45)

# by user
def isEven(num):
    if(num%2==0):
        print("Even Number")
    else:
        print("odd Number") 
num=int(input("enter number"))
isEven(num)