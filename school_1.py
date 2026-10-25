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
        print("2. With " + crush["name"] + " from class")
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
    print("It has now been a couple weeks since you started at this school and you have gotten to know everyone in your class by now. You reach school in the morning and step into the hallway.")
    if crush["met"] == False:
        crush["name"] = input("What was the name of the person you found attractive on day 1 again? - ")
        crush["met"] = True
    popular_friends["met"] = True

    while True:
        print("You see the popular kids and " + crush["name"] + " from earlier. Who do you choose to talk to?")
        print("1. The popular kids")
        print("2. " + crush["name"])
        choice = input("> ")

        if choice == "1":
            print("You greet the popular kids and walk to class together")
            popular_friends["respect"] += 2
            print("Respect + 2")
            return
        elif choice == "2":
            print(crush["name"] + " spots you amongst the crowd and waves at you! You walk to class together")
            crush["affection"] += 2
            print("Affection + 2")
            return
        else:
            print("Invalid choice, try again")


# def fight_1():
#     print("A school bully corners you up against a wall :( He is much taller than you...)")
#     print("He gives you 2 options-")
#     print("Either you give him all of your money right now and he lets you go or he beats you up and takes it anyways")
#     print("Or an option he didn't account for, you fight him")
#     choice = input("""1. Peacefully hand over the money and be supressed
#                       2. You try to walk away, but he will take your money anyways
#                       3. You pick a fight with him(be careful, you are relatively new to the school)""")
#     if choice == "1":
#         player["money"] -= 30
#         player["happiness"] -= 10
#         print("Bruh, you just got robbed and did nothing about it")
#         return
#     elif choice == "2":
#         print("Ouch, he just slammed you against the lockers and took all your money anyways")
#         player["money"] = 0
#         player["health"] -= 5
#         return
#     elif choice == "3":
#         print("Bold move...")
#         choice_1 = input("Kick him in the shin(1) OR Punch him in the face(2)")
#         if choice_1 == "1":
#             print("He fell down, and you continued to kick him until a teacher intervened")
#             print("You won the fight, gained some reputation amongst others but the teachers are sending you to the principal's office")
#             popular_friends["respect"] += 40
#             player["happiness"] += 10
#             print("")
#             print("You nervously enter the principal's office, he asks you what happened. What do you say?")
#             choice_2 = input("""1.The bully started taking all my money so I stood up for myself
#                                 2.I was teaching the bully a lesson to not mess with me ever again
#                                 3.There was no teacher in sight, he was going to hit me anyways so I hit first""")
#             if choice_2 == "1":
#                 print("The principal understands the situation, but he says you should not hit anybody at all. He lets you off with a warning and suspends the bully")
#             elif choice_2 == "2":
#                 print("The principal hands you a note of suspension , your parents tell you that they are very dissapointed")
#                 player["suspension"] = True
#                 player["happiness"] -= 10
#             elif choice_2 == "3":
#                 print("The principal says that he understands you were scared, but you cannot be certain if he was going to hit you. He lets you off with a warning if you apologise to the bully. You reluctantly agree")
#             else:
#                 print("Invalid choice, try again")
#             return
#         elif choice_1 == "2":
#             print("He stops your punch midway, slams you onto the floor and takes all of your money. Ouch!")
#             player["health"] -= 30
#             player["money"] = 0
#             popular_friends["respect"] -= 15
#             return
#         else:
#             print("Invalid choice, try again")

#first fight in school ,leads to possible suspension and groudnding
def fight_1():
    print("A school bully corners you up against a wall :( He is much taller than you...")
    print("He gives you 2 options-")
    print("Either you give him all of your money right now and he lets you go or he beats you up and takes it anyways")
    print("Or an option he didn't account for, you fight him")

    while True:
        print("1. Peacefully hand over the money and be suppressed")
        print("2. You try to walk away, but he will take your money anyways")
        print("3. You pick a fight with him (be careful, you are relatively new to the school)")
        choice = input("> ")

        if choice == "1":
            player["money"] -= 30
            player["happiness"] -= 10
            print("Bruh, you just got robbed and did nothing about it")
            return
        elif choice == "2":
            print("Ouch, he just slammed you against the lockers and took all your money anyways")
            player["money"] = 0
            player["health"] -= 5
            return
        elif choice == "3":
            print("Bold move...")

            while True:
                print("1. Kick him in the shin")
                print("2. Punch him in the face")
                choice_1 = input("> ")

                if choice_1 == "1":
                    print("He fell down, and you continued to kick him until a teacher intervened")
                    print("You won the fight, gained some reputation amongst others but the teachers are sending you to the principal's office")
                    popular_friends["respect"] += 40
                    player["happiness"] += 10
                    print("")
                    print("You nervously enter the principal's office, he asks you what happened. What do you say?")

                    while True:
                        print("1. The bully started taking all my money so I stood up for myself")
                        print("2. I was teaching the bully a lesson to not mess with me ever again")
                        print("3. There was no teacher in sight, he was going to hit me anyways so I hit first")
                        choice_2 = input("> ")

                        if choice_2 == "1":
                            print("The principal understands the situation, but he says you should not hit anybody at all. He lets you off with a warning and suspends the bully")
                            break
                        elif choice_2 == "2":
                            print("The principal hands you a note of suspension, your parents tell you that they are very disappointed and ground you")
                            player["suspension"] = True
                            player["grounded"] = True
                            player["happiness"] -= 10
                            break
                        elif choice_2 == "3":
                            print("The principal says that he understands you were scared, but you cannot be certain if he was going to hit you. He lets you off with a warning if you apologise to the bully. You reluctantly agree")
                            break
                        else:
                            print("Invalid choice, try again")

                    return

                elif choice_1 == "2":
                    print("He stops your punch midway, slams you onto the floor and takes all of your money. Ouch!")
                    player["health"] -= 30
                    player["money"] = 0
                    popular_friends["respect"] -= 15
                    return
                else:
                    print("Invalid choice, try again")
        else:
            print("Invalid choice, try again")
# def suspension_1():
#     while player["suspension"] == True:
#         print("You are at home, disappointed about what happened. Your parents grounded you but there is a halloween party happening this night")
#         print("1. Sneak out at night to go")
#         print("2. Stay at home")
#         choice = input("Enter your choice - ")
#         if choice == "2":
#             print("Boring but atleast you aren't risking any more trouble. You decide to study the whole night and prepare for an upcoming exam")
#             player["grades"] += 10
#             player["grounded"] = False
#             return
#         elif choice == "1":
#             print("The party starts at 10pm, when do you sneak out?")
#             print("1. Right after dinner" \
#             "2. Once everyone is asleep, by 11pm")
#             choice_1 = input(">")
#             if choice_1 == "1":
#                 print("As soon as you were about to sneak out, your parents came in." \
#                 "They ground you for another week and take away all electronics :( ")
#                 return
#             elif choice_1 == "2":
#                 player["grounded"] = False
#                 print("You make it out without being noticed. Now you must find a quick way there as you are already late. What do you do?")
#                 print("1. Take the bus there" \
#                 "2. Ask a friend for a lift")
#                 choice_2 = input(">")
#                 if choice_2 == "1":
#                     print("Took you a while but you finally reached. You had loads of fun and somehow your parents never found out!")
#                     player["happiness"] += 20
#                     return
#                 elif choice_2 == "2":
#                     print("You reached much faster and had a lot of fun! Lucky for you your parents never found out!")
#                     player["happiness"] += 30
#                     return
#                 else:
#                     print("Invalid choice, try again")
#             return
#         else:
#             print("Invalid choice, try again")
#     player["suspension"] = False

#if supended what would happen for a party
def suspension_1():
    while player["suspension"] == True:
        print("\nYou are at home, disappointed about what happened. Your parents grounded you but there is a halloween party happening this night.")
        print("1. Sneak out at night to go")
        print("2. Stay at home")
        choice = input("Enter your choice - ")     
        if choice == "2":
            print("\nBoring but atleast you aren't risking any more trouble. You decide to study the whole night and prepare for an upcoming exam.")
            player["grades"] += 10
            player["grounded"] = False
            player["suspension"] = False 
            return         
        elif choice == "1":
            print("\nThe party starts at 10pm, when do you sneak out?")
            print("1. Right after dinner")
            print("2. Once everyone is asleep, by 11pm")
            choice_1 = input("> ")           
            if choice_1 == "1":
                print("\nAs soon as you were about to sneak out, your parents came in.")
                print("They ground you for another week and take away all electronics :(")
                player["suspension"] = False 
                return       
            elif choice_1 == "2":
                player["grounded"] = False
                print("\nYou make it out without being noticed. Now you must find a quick way there as you are already late. What do you do?")
                print("1. Take the bus there")
                print("2. Ask a friend for a lift")
                choice_2 = input("> ")
                if choice_2 == "1":
                    print("\nTook you a while but you finally reached. You had loads of fun and somehow your parents never found out!")
                    player["happiness"] += 20
                    player["suspension"] = False 
                    return
                elif choice_2 == "2":
                    print("\nYou reached much faster and had a lot of fun! Lucky for you your parents never found out!")
                    player["happiness"] += 30
                    player["suspension"] = False 
                    return
                else:
                    print("Invalid choice. Try again from the beginning of the evening.")
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid choice, try again.")

#first scene for an upcoming exam
def exam_1():
    print("You return to school after all that drama, but exams are right around the corner. What do you do?")
    while True:
        print("1. Study hard after school")
        print("2. Play football with friends")
        choice = input("> ")

        if choice == "1":
            print("Good work, you are taking your studies seriously!")
            player["grades"] += 15
            print("Grades + 15")
            return
        elif choice == "2":
            print("You definitely don't put as much effort into your exams as you did for football, but at least you had fun!")
            player["happiness"] += 15
            print("Happiness + 15")
            return
        else:
            print("Invalid choice, try again")

#scenario inside the exam hall
def exam_2():
    print("You are in the exam hall, you feel like you barely studied. The person next to you is writing fast...")
    while True:
        print("1. Copy their answers")
        print("2. Try your best on your own")
        choice = input(">")
        if choice == "1":
            player["cheated"] = True
            if random.random()<0.4:
                print("The teacher spotted you. You got a zero and a note back home...")
                player["grades"] -= 20
                print("Grades - 20")
                player["happiness"] -= 10
                print("Happiness - 10")
            else:
                print("You got away with it. Decent score but you feel guilty...")
                player["grades"] += 20
                print("Grades + 20")
                player["happiness"] -= 5
                print("Happiness - 5")
            return
        elif choice == "2":
            print("Although you sturggled, you did it honestly")
            player["grades"] += 10
            print("Grades + 10")
            return
        else:
            print("Invalid choice, try again")

#results day!!
def report_card():
    print("\n ---REPORT CARD---")
    grades = player["grades"]
    if grades >= 90:
        letter = "A+"
    elif grades >= 80:
        letter = "A"
    elif grades >= 70:
        letter = "B"
    elif grades >= 60:
        letter = "C"
    elif grades >= 50:
        letter = "D"
    elif grades >= 40:
        letter = "E"
    else:
        letter = "F"
    print("Your grade is:", letter)
    if player["cheated"]:
        print("You still feel guilty that you should've studied on your own")
    player["cheated"] = False
    player["suspension"] = False
    player["grounded"] = False #resetting some stats

#part-time job hunt 1
def job_1():
    print("\nIt is now holiday season and you want to earn money from a part time job. \nYou have 3 options-")
    print("1. Delivering the newspaper on your cycle")
    print("2. Tutoring a kid")
    print("3. Washing neighbours cars")

    while True:
        choice = input(">")
        if choice == "1":
            print("The job itself is boring as there is limited interaction, but you stay healthy by cycling!")
            player["happiness"] -= 5
            print("Happiness - 5")
            player["money"] += 40
            print("Money + 40")
            player["health"] += 20
            print("Health + 20")
            return
        elif choice == "2":
            print("The job is demanding, but you earn a lot of money and the kid is nice")
            player["happiness"] -= 5
            print("Happiness - 5")
            player["money"] += 80
            print("Money + 80")
            player["grades"] += 10
            print("Grades + 10")
            return
        elif choice == "3":
            print("The job is relaxing, you earn a decent wage, however you drop a heavy bottle on your foot")
            player["happiness"] += 20
            print("Happiness + 20")
            player["money"] += 45
            print("Money + 45")
            player["health"] -= 10
            print("Health - 10")
            return
        else:
            print("Invalid choice, try again")

#function to verify if they can afford something
def can_afford(cost):
    if player["money"] >= cost:
        return True
    print("Sorry, you can't afford that right now. Try something else.")
    return False

#money spending area
def money_spend_1():
    while True:
        print("\nYou decide to spend some of your hard earned money. Where would you spend it?")
        print("1.Go to an amusement park with your friends (30 coins)")
        print("2. Go to the movies with " + crush["name"] + " (20 coins)")
        print("3. Buy a new video game (25 coins)")
        print("4. Save your money and stay home")
        choice = input(">")
        if choice == "1":
            if can_afford(30):
                player["money"] -= 30
                print("You finally get to hang out with your friends, but you haven't told them you are afraid of heights...")
                print("All of you begin queing up for the tallest ride in your state, but you feel like you will pass out if you ride it...\nYour friends are watching, what do you do?")
                while True:
                    print("1. Exit the queue")
                    print("2. Continue and face your fears")
                    choice_2 = input(">")
                    if choice_2 == "1":
                        print("You step out of the line and tell them you'll wait. They tease you a little, but it's soon forgotten")
                        player["happiness"] -= 5
                        print("Happiness - 5")
                        popular_friends["respect"] -= 5
                        print("Respect - 5")
                        return
                    elif choice_2 == "2":
                        print("You close your eyes and get on the ride...")
                        if random.random() < 0.3:
                            print("You scream the whole ride and feel sick")
                            player["health"] -= 10
                            print("Health - 10")
                            player["happiness"] += 5
                            print("Happiness + 5")
                            return
                        else:
                            print("It was scary, but really fun! Your friends are cheering you as you climb off for doing the ride")
                            player["happiness"] += 15
                            print("Happiness + 15")
                            popular_friends["respect"] += 10
                            print("Respect + 10")
                            return
                    else:
                        print("Invalid choice, try again")
        elif choice == "2":
            if can_afford(20):
                player["money"] -= 20
                print("Money - 20")
                print("You and " + crush["name"] + " get to the cinema. Which genre of movie do you want to watch?")
                while True:
                    print("1. A horror movie")
                    print("2. A comedy movie")
                    print("3. A romantic movie")
                    choice_3 = input(">")
                    if choice_3 == "1":
                        print(crush["name"] + " grips your arm through the scary parts. You pretend as if you aren't scared too")
                        crush["affection"] += 10
                        print("Affection + 10")
                        player["happiness"] += 10
                        print("Happiness + 10")
                        return
                    elif choice_3 == "2":
                        print("The two of you laugh so hard the people around shush at you")
                        crush["affection"] += 5
                        print("Affection + 5")
                        player["happiness"] += 15
                        print("Happiness + 15")
                        return
                    elif choice_3 == "3":
                        print("It is a bit awkward to sit through it together, however " + crush["name"] + " smiles at you afterwards.")
                        crush["affection"] += 8
                        print("Affection + 8")
                        player["happiness"] += 5
                        print("Happiness + 5")
                        return
                    else:
                        print("Invalid choice, try again")
        elif choice == "3":
            if can_afford(25):
                player["money"] -= 25
                print("Money - 25")
                print("You love the game, how do you choose to play it?")
                while True:
                    print("1. Play all night")
                    print("2. Only after you study for the day")
                    choice_4 = input(">")
                    if choice_4 == "1":
                        print("You finish half the game by sunrise. Your eyes hurt and you forgot to complete your homework")
                        player["happiness"] += 20
                        print("Happiness + 20")
                        player["health"] -= 5
                        print("Health - 5")
                        player["grades"] -= 10
                        print("Grades - 10")
                        return
                    elif choice_4 == "2":
                        print("You enjoy it without letting your studies slip.")
                        player["happiness"] += 10
                        print("Happiness + 10")
                        player["grades"] += 10
                        print("Grades + 10")
                        return
                    else:
                        print("Invalid choice, try again")
        elif choice == "4":
            print("You stay at home, study and save money. You feel responsible")
            player["happiness"] += 5
            print("Happiness + 5")
            player["grades"] += 5
            print("Grades + 5")
            return
        else:
            print("Invalid choice, try again")
