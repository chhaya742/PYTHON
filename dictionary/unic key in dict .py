sample_data=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
i=0
j=1
dic2=[]
print(len(sample_data))
for x in sample_data:
     # for y in sample_data:
     if x not in dic2:
          dic2.append(x)
print(dic2)
          
          


     
