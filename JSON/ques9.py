import json
dic1={
    "shopp":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } }
num=input("enter item")
quan=int(input("enter quantity"))
for i in dic1:
    for j in dic1[i]:
        if num==j:
            print(j)
            print(dic1[i][j])
            print(dic1[i][j]*quan)
dic1[i].pop(num)
item=input("enter item")
price=int(input("enter price"))
dic1[i][item]=price
with open("shop.json","w") as f:
    print(json.dump(dic1,f,indent=5))

    


