def maximum(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1,"is greater")
        else:
            print(num2,"is greater")
    elif num2>num3:
        print(num2,"is greater")
    else:
        print(num3,"is greater")
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
maximum(num1,num2,num3)
