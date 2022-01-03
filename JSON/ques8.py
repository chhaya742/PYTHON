import json
a=[['neelam','programer','24','2400'],['komal','trainer','24','20000'],['anuradha','HR','25','40000'],['Abhishek','manager','29','63000']]
list1=["Name","Desigination","Age","Salary"]
dic={}
for i in range(0,len(a)):
    for j in range(0,len(a)):
        dic.update({list1[j]:a[i][j]})
        dict2={}
for i in range(0,4):
    u=input("enter keys")
    dict2.update({u:dic})
print(dict2)
add=open("emp.json","w") 
s=json.dump(dict2,add,indent=4)
print(s)
# emp1={}
# for i in range(0,len(a)):
#     keys=input("enter keys")
#     emp1.update({keys:a[i]})
# emp2={}
# for i in range(0,len(b)):
#     keys=input("enter keys")
#     emp2.update({keys:b[i]})
# emp3={}
# for i in range(0,len(c)):
#     keys=input("enter keys")
#     emp3.update({keys:c[i]})
# emp4={}
# for i in range(0,len(d)):
#     keys=input("enter keys")
#     emp4.update({keys:d[i]})

# out_file = open("myfile.json", "w")
# json.dump(emp1, out_file, indent = 6)
# json.dump(emp2, out_file, indent = 6)
# out_file.close()




