def count_pair(a):
    b=[]
    i=0
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i+=1
    print(b)
    j=0
    while j<len(b):
        n=0
        count=0
        while n<len(a):
            if b[j]==a[n]:
                count+=1            
            n+=1
        v=count//2
        print(b[j],"=",v)       
        j+=1
count_pair([3,6,7,4,5,8,3,7,7,2,5,7,3,2,1,1,7,6,8,8,8])

