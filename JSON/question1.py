import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 
# my_file=open("qestion1.json","w")
# print(my_file)
# print(json.dumps(dict1,indent=5))
with open("question.json","w") as f:
    print(json.dump(dict1,f,indent=4))
