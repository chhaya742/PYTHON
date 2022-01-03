a="MISSISSIPPI" 
b=list(a)
i=0
c=[]
while i<len(b):
    if b[i] not in c:
        c.append(b[i])
    i+=1
j=0
dic2={}
while j<len(c):
    m=0
    count=0
    while m<len(b):
        if c[j]==b[m]:
            count+=1
        # dic2[c[j]]=count
        dic2.update({c[j]:count})
        m+=1
    
    j+=1
print(dic2)





    
    