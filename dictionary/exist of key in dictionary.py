dic1={
    2:45,
    1:30,
    3:56,
    6:78,
    8:34
    } 
key = int(input("Enter"))
for key in dic1:
    if key in dic1:
        print("exists")
        break
    else:
        print("not exists")


