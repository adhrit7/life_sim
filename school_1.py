from data import player, crush, popular_friends
import random

#first day of school
def day_1_morning():
    while True:
        print("It is the first day of school and you enter your classroom. What do you do?")
        print("1. Sit next to the popular kids")
        print("2. Sit next to a person you find attractive")
        choice = input(">")

        if choice == "1":
            print("You've got new friends!")
            player["happiness"] += 10
            print("Happiness + 10")
            popular_friends["met"] = True
            popular_friends["respect"] += 5
            print("Respect + 5") 
            return
        elif choice == "2":
            crush["name"] = input("You sit beside them, and introduce yourself to them. They tell you that their name is - ")
            print(crush["name"] + " becomes your first friend!")
            player["happiness"] += 5
            print("Happiness + 5")
            crush["met"] = True
            crush["affection"] += 10
            print(" Affection + 10")
            return
        else:
            print("Invalid choice, try again")

#lunch at day 1
def day_1_lunch():
    while True:
        print("It's lunchtime. Where do you sit?")
        print("1. With the popular kids")
        print("2. With the attractive person from class")
        print("3. Alone")
        choice = input(">")

        if choice == "1":
            if popular_friends["met"] == False:
                print("They tell you to go away. Try somewhere else")
            else:
                print("They crack jokes and you laugh along.")
                player["happiness"] += 5
                popular_friends["respect"] += 5
                print("Happiness + 5")
                print("Respect + 5")
                return
        elif choice == "2":
            if crush["met"] == False:
                print("You don't really know them. It would be awkward. Try somewhere else.")
            else:
                print("You talk the whole lunch.")
                player["happiness"] += 5
                crush["affection"] += 5
                print("Happiness + 5")
                print("affection + 5")
                return
        elif choice == "3":
            print("Quiet lunch. Kind of lonely.")
            player["happiness"] -= 5
            print("Happiness - 5")
            return
        else:
            print("Invalid choice, try again")
#settling in well, become associates with everyone
def day_2_morning():
    print('''It has now been a couple weeks since you are at this school and
     you have basically gotten to know everyone in your class by now. You 
    reach school in the morning and step foot into the hallway.''')
    if crush["met"] == False:
        crush["name"] = input("What was the name of the person you found attractive on day 1 again? -")
        crush["met"] = True 
    popular_friends["met"] = True
    choice = input("You see the popular kids(1) and " + crush["name"] + "(2)" + " from earlier, who do you choose to talk to? -")
    if choice == "1":
        print("You greet the popular kids and walk to class together")
        popular_friends["respect"] += 2
        return
    elif choice == "2":
        print( crush["name"] + " spots you amongst the crowd and waves at you! You walk to class together")
        crush["affection"] += 2
        return
    else:
        print("Invalid choice, try again")
def fight_1():
    print("A school bully corners you up against a wall :( He is much taller than you...)")
    print("He gives you 2 options-")
    print("Either you give him all of your money right now and he lets you go or he beats you up and takes it anyways")
    print("Or an option he didn't account for, you fight him")
    choice = input("""1. Peacefully hand over the money
                      2. You try to walk away, but he will take your money anyways
                      3. You pick a fight with him(be careful, you are relatively new to the school)""")