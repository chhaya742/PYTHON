def driver(speed):
    if speed<=70:
        print("ok")
    elif speed>70:
        a=speed-70
        b=a%5
        print(a//5,"point")
        if a>12:
            print("lisence suspended ")
i=int(input("enter speed"))
driver(i)
