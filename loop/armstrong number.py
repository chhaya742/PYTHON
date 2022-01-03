num=int(input("enter number"))
num_1=num
index_1=0
count=0
while index_1<num:
    num=num//10
    count+=1
# print(count)
sum=0
num_2=num_1
while num_1>0:
    var=num_1%10
    sum=(var**count)+sum
    num_1=num_1//10
# print(sum)
if sum==num_2:
    print("yes")
else:
    print("no")