def eligible_for_vote(age):
    if age>=18:
        return   "you are eligible"
    else:
        return "you are not eligible"
user_input=int(input("enter age"))
b=eligible_for_vote(user_input)
print(b)