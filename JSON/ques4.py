import json
sam={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(json.dumps(sam,indent=6,sort_keys=True))

# dumps=json.dumps(sam,indent=4)
# print(type(dumps))

# loads=json.loads(dumps)
# print(type(loads))

# with open("data.json","w") as file:
#     json.dump(sam, file ,indent=4)


# with open("data.json","r") as file:
#     load=json.load(file)
#     print(type(load))