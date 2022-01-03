def add_list(l1,l2):
    i=0
    new_list=[]
    sum=0
    while i<len(l1):
        sum=l1[i]+l2[i]
        new_list.append(sum)
        print(sum)
        i+=1   
    print(new_list)
add_list([2,3,4,5,6],[1,1,1,1,1])




