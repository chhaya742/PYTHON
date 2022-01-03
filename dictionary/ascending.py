dic2={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in dic2:
    for j in dic2:
        if dic2[i]<dic2[j]:
            tem=dic2[i]
            dic2[i]=dic2[j]
            dic2[j]=tem
print(dic2)
