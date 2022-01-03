def perfect(number):
    a=number
    i=1
    sum=0
    while i<number:
        if number%i==0:
            sum=sum+i
        i+=1
    if a==sum:
        return number,'is perfect number'
    else:
        return "not perfect number"
n=int(input("enter number"))
print(perfect(n))
