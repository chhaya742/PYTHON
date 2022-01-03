def factorial(num):
    num2=num
    print("fabonicy series")
    a=0
    b=1
    c=0
    while num2>=c:
        print(c)
        a=b
        b=c
        c=a+b
        num2-=1
    print()
    i=1
    sum=1
    dictt={}
    n=1
    while i<=num:
        print(num)
        dictt.update({n:num})
        f=0
        j=1
        a=num
        while j<=num:
            if num%j==0:
                f+=1    
            j+=1
        if f==2:
            print("prime")
        else:  
            print("not")
        sum*=num
        n+=1
        num-=1
    print("sum of factor",sum)
    print(dictt) 
    


factorial(5)

