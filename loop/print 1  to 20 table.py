outer=1
a=0
while outer<=20:
    a=a+1
    inner=1
    sum=0
    while inner<=10:
        sum=sum+1
        product=outer*inner
        print(product)
        inner+=1
    outer+=1
    print()
print("count",a*sum)

