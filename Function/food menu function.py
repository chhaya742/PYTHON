def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"
    print ("Kya main print ho payungi? :-(")
day=input("Enter day")
mon_menu = menu(day)
print (mon_menu)
