from data import player, crush, popular_friends, sports
import random
from helpers import can_afford



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
    print("It is now your birthday, and you're finally 17!")
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
                    player["money"] -= 35
                    print("Money - 35")
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
                        print("Happiness - 5")
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
                    print("\nIt's a fun night, even if it's a small group.")
                    player["happiness"] += 8
                    print("Happiness + 8")
                stage = 2
            else:
                print("Invalid choice, try again")
        #stage 2: random surprise
        elif stage == 2:
            roll = random.random()
            if roll < 0.3:
                print("\nYour uncle sends you a card with some money inside!")
                player["money"] += 25
                print("Money + 25")
            elif roll < 0.6:
                print("\nYour phone is flooded with birthday wishes!")
                player["happiness"] += 5
                print("Happiness + 5")
            elif roll < 0.75:
                print("\nYou trip over your own shoelace in front of everyone and the whole room laughs, even you...")
                player["happiness"] -= 3
                print("Happiness - 3")
            else:
                print("\nThe rest of the day passes quietly")
            stage = 3
        #stage 3, the wish for bday
        elif stage == 3:
            print("\nBefore you blow out the candles, you get to make a wish. What do you wish for?")
            print("1. Better grades")
            print("2. More friends")
            print("3. More money")
            choice_1 = input("> ")
            if choice_1 == "1":
                player["grades"] += 5
                print("Grades + 5")
                stage = 4
            elif choice_1 == "2":
                popular_friends["respect"] += 5
                print("Respect + 5")
                stage = 4
            elif choice_1 == "3":
                player["money"] += 15
                print("Money + 15")
                stage = 4
            else:
                print("Invalid choice, try again")
        #stage 4, future talks with parents
        elif stage == 4:
            print("\nLater that night your parents sit next to you. They say 'You're almost done with school. What's the plan?'")
            print("1. University")
            print("2. Get a job straight away after graduating")
            print("3. I'm not sure yet")
            choice_2 = input("> ")
            if choice_2 == "1":
                player["plan"] = "university"
                if player["grades"] >= 60:
                    print("\nThey smile and tell you - 'With your grades, you'll do great.'")
                    player["happiness"]+= 5
                    print("Happiness + 5")
                    stage = 5
                else:
                    print("\nThey nod, but look a little worried. 'You'll need to work harder on your grades.' ")
                    player["happiness"] -= 3
                    print("Happiness - 3")
                    stage = 5
            elif choice_2 == "2":
                player["plan"] = "job"
                print("\nThey are surprised, but they reassure you that they will always support your choice. They even hand you some extra money to start")
                player["money"] += 30
                print("Money + 30")
                stage = 5
            elif choice_2 == "3":
                player["plan"] = "unsure"
                print("\nThey tell you that it's ok, but there is not much time left to decide")
                player["happiness"] -= 2
                print("Happiness - 2")
                stage = 5
            else:
                print("Invalid choice, try again")


#sports team
def sport_1():
    print("\nJust before the new school year begins, you decide to try out for your school's sports team")
    while True:
        print("Which sport do you select?")
        print("1. Table tennis")
        print("2. Football")
        print("3. Basketball")
        choice = input("> ")
        #table tennis
        if choice == "1":
            print("You turn up on time for the tryouts. It seems like it won't be easy to get in the team as there are over 50 other people there")
            print("You are put up in a game of doubles by the coach. Your teammate is making your team lose points, and you are barely even hitting the ball because of her")
            while True:
                print("\nWhat do you say to her?")
                print("1. Try to focus on accuracy more than power")
                print("2. Just lightly tap the ball onto their table, I'll manage the rest")
                choice_1 = input("> ")
                if choice_1 == "1":
                    print("\nSeems like they are finally connecting more shots, you lose but your coach still notices your leadership and game skills ")
                elif choice_1 == "2":
                    print("\nYour teammate gets angry at you for not helping them out, but you still play well.")
                print("The coach makes all the players do fitness exercises. It's either a pass or fail")
                if player["health"] == 100:
                    print("You finish them easily and are now part of the Table Tennis team!")
                    sports["name"] = "Table Tennis"
                    sports["skills"] += 10
                    print("Tabble Tennis skills + 10")
                    player["happiness"] += 7
                    print("happiness + 7")
                    return
                elif player["health"] >= 70:
                    print("You managed to finish the exercises, struggling a bit. But you are still selected!")
                    sports["name"] = "Table Tennis"
                    sports["skills"] += 8
                    print("Tabble Tennis skills + 8")
                    player["happiness"] += 7
                    print("happiness + 7")
                    return
                elif player["health"] < 70:
                    print("You could not complete the exercises and unfortunately weren't selected for Table Tennis, however you can attempt a tryout for other sports!")
                    break
        #football, more demanding
        # elif choice == "2":
        #     print("\nYou turn up at the pitch at 6 am in the morning. You're tired, so you have to do your best!")
        #     print("You tryout as a striker. The game starts...")
        #     print("You have the ball, what do you do?")
        #     print("\n1. Shoot from outside the box")
        #     print("2.")


        # elif choice == "3":

        # else:
        #     print("Invalid choice, try again")