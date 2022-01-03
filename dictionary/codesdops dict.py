# dic1={}
# i=1
# while i<=3:
#     name=input("enter name")
#     marks=int(input("enter marks"))
#     dic1.update({name:marks})
#     i+=1
# print(dic1)
# for i in dic1:
#     for j in dic1:
#         if dic1[i]<dic1[j]:
#             tem=dic1[i]
#             dic1[i]=dic1[j]
#             dic1[j]=tem
# print(dic1)


# dic1={'right':'left','up':'down','come':'go'}
# dic2={}
# for i,j in dic1.items():
#     dic2.update({j:i})
# print(dic2)

# user=int(input("enter size of dictionary"))
# i=0
# dic3={}
# while i<user:
#     keys=input("enter keys")
#     value=input("enter value")
#     dic3.update({value:keys})
#     i+=1
# print(dic3)


# a="MISSISIPPI" 
# b=list(a)
# i=0
# c=[]
# while i<len(b):
#     if b[i] not in c:
#         c.append(b[i])
#     i+=1
# j=0
# dic2={}
# while j<len(c):
#     m=0
#     count=0
#     while m<len(b):
#         if c[j]==b[m]:
#             count+=1
#         # dic2[c[j]]=count
#         dic2.update({c[j]:count})
#         m+=1
    
#     j+=1
# print(dic2)
# for i in dic2:
#     for j in dic2:
#         if dic2[i]<dic2[j]:
#             tem=dic2[i]
#             dic2[i]=dic2[j]
#             dic2[j]=tem
# print(dic2)

a=["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
b="bug"
c={}
for i in a:
    count=0
    for j in i.split():
        if j==b:
            count+=1
    c[count]=i
d=[]
for s in sorted(c):
    d.append(c[s])
d.reverse()
print(d)




    
    


                