def show_number(limit):
    x=0
    sum=0
    while x<limit:
        if x%3==0 and x%5==0:
            sum=sum+x
        x+=1
    print(sum)
show_number(100)

