import json
dic='{"a":1,"a":2,"a":3,"a": 4,"b": 1, "b": 2}'
print(json.loads(dic))


n="Name Abhishek Designation CEO,of,navgurukul Gender male Age 29"
sp=n.split()
dic2={}
for x in range(0,len(sp),2):
    dic2.update({sp[x]:sp[x-7]})
dum=json.dumps(dic2)
print(dum)






    





