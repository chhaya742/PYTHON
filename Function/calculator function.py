def operator(x,y,o):
    if o=="+":
        return x+y
    elif o=="-":
        return x-y
    elif o=="*":
        return x*y
    elif o=="/":
        return x/y
    elif o=="%":
        return x%y
x=int(input("enter number"))
y=int(input("enter number"))
o=input("enter symbol")
result=operator(x,y,o)
print(result)
