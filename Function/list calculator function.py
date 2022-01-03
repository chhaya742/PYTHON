def calculator(num1,num2,operator):   
    i=0
    list1=[]
    while i<len(num1):
        if operator=="+":
            b=num1[i]+num2[i]
            list1.append(b)
        elif operator=="-":
            b=num1[i]-num2[i]
            list1.append(b)
        elif operator=="%":
            b=num1[i]%num2[i]
            list1.append(b)
        elif operator=="/":
            b=num1[i]/num2[i]
            list1.append(b)
        elif operator=="%":
            b=num1[i]%num2[i]
            list1.append(b)
        i+=1
    return list1
size=int(input("enter size of list"))
list1=[]
list2=[]
for i in range(size):
    num1=int(input("enter first list element"))
    list1.append(num1)
    num2=int(input("enter second list"))
    list2.append(num2)
operator=input("entet symboll")
add=calculator(list1,list2,operator)
print(add)


