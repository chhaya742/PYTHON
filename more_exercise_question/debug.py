list1=[[1,2,3],[5,8,9],[4,3,77,521,31,311]]
i= 0
while i< len(list1):
    j=0
    while j<len(list1[i]):
        print (list1[i][j])
        j+=1
    i+=1
    print ('-----') 


string_name = ["Rishabh Verma","amisha","neha"]
print(len(string_name[2]))
print (len(string_name)) 
print("R" in string_name)


def numbers_less_than_twenty(list):
    counter = 0
    while counter < len(list):
        item = list[counter]
        if item > 20:
            list.remove(item)
        else:
            counter += 1
    return list
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)
print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 




