list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]  
dic={}
i=0
j=0
while i<len(list1):
    dic.update({list1[i]:list2[j]})
    j+=1
    i+=1
print(str(dic))
