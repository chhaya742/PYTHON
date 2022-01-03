u=int(input("enter size of dictionary"))
i=1
dic2={}
while i<u:
    dic2.update({i:(i**2)})
    i+=1
print(dic2)
