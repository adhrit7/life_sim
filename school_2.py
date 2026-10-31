from data import player, crush, popular_friends
import random
import school_1
from school_1 import can_afford



#reset stats, wooo :D
def reset_stats():
    player["class"] = "12"
    player["suspension"] = False
    player["cheated"] = False
    player["grounded"] = False

#first birthday!!! yayyy xD
def birthday_1():
    player["age"] += 1
    print("---YOUR BIRTHDAY---")
    print("It is now your birthday, and you're finally 17!'")
    stage = 1
    while stage <= 4:
        #stage 1: how to celebrate
        if stage == 1:
            print("\nHow do you want to celebrate?")
            print("1. Throw a big party (35 coins)")
            print("2. Have a quiet dinner with your family")
            print("3. Go out with a few close friends")
            choice = input("> ")
            if choice == "1":
                if can_afford(35):
                    player["money"] -= 40
                    print("money - 40")
                    print("\nYou invite half the grade. The house is packed and the music is loud.")
                    if popular_friends["respect"] >= 20:
                        print("The popular kids show up and bring a cake. Everyone sings!")
                        popular_friends["respect"] += 10
                        print("Respect + 10")
                        player["happiness"] += 15
                        print("Happiness + 15")
                    else:
                        print("Only a few people show up, and most of the snacks go to waste")
                        player["happiness"] -= 5
                    stage = 2
            elif choice == "2":
                print("\nYour family cooks your favourite meal. It's calm and warm, and your parents tell you how proud they are.")
                player["happiness"] += 10
                print("Happiness + 10")
                stage = 2
            elif choice == "3":
                print("\nYou and a few friends head out for the evening")
                if crush["affection"] >= 30:
                    print(crush["name"] + " turns up too, with a small gift for you!")
                    crush["affection"] += 10
                    print("Affection + 10")
                    player["happiness"] += 10
                    print("Happiness + 10")
                else:
                    print("It's a fun night, even if it's a small group.")
                    player["happiness"] += 8
                    print("Happiness + 8")
                stage = 2
            else:
                print("Invalid choice, try again")
        #st