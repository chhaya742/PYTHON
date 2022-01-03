my_dict = {
    'a':500, 
    'b':58, 
    'c':56,
    'd':40, 
    'g':200,
    'e':100, 
    'f':20,
    'h':300
    }
for i in my_dict:
    for j in my_dict:
        if my_dict[i]<my_dict[j]:
            my_dict[i]=my_dict[j]
print(my_dict[j])



    


