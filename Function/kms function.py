def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("median")
        else:
            Print("far")
user=int(input("enter number"))
distance(user) 