from data import player, crush, popular_friends
import random
import school_2

#first day of school
def day_1_morning():
    while True:
        print("\nIt is the first day of school and you enter your classroom. What do you do?")
        print("1. Sit next to the popular kids")
        print("2. Sit next to a person you find attractive")
        choice = input("> ")

        if choice == "1":
            print("\nYou've got new friends!")
            player["happiness"] += 10
            print("Happiness + 10")
            popular_friends["met"] = True
            popular_friends["respect"] += 5
            print("Respect + 5") 
            return
        elif choice == "2":
            crush["name"] = input("\nYou sit beside them, and introduce yourself to them. They tell you that their name is - ")
            print(crush["name"] + " becomes your first friend!")
            player["happiness"] += 5
            print("Happiness + 5")
            crush["met"] = True
            crush["affection"] += 5
            print(" Affection + 5")
            return
        else:
            print("\nInvalid choice, try again")

#lunch at day 1
def day_1_lunch():
    while True:
        if crush["met"] == True:
            print("\nIt's lunchtime. Where do you sit?")
            print("1. With the popular kids")
            print("2. With " + crush["name"] + " from class")
            print("3. Alone")
            choice = input("> ")
        else:
            print("\nIt's lunchtime. Where do you sit?")
            print("1. With the popular kids")
            print("2. With the person you found attractive from class")
            print("3. Alone")
            choice = input("> ")

        if choice == "1":
            if popular_friends["met"] == False:
                print("\nThey tell you to go away. Try somewhere else")
            else:
                print("They crack jokes and you laugh along.")
                player["happiness"] += 5
                popular_friends["respect"] += 5
                print("Happiness + 5")
                print("Respect + 5")
                return
        elif choice == "2":
            if crush["met"] == False:
                print("\nYou don't really know them. It would be awkward. Try somewhere else.")
            else:
                print("You talk the whole lunch.")
                player["happiness"] += 5
                crush["affection"] += 5
                print("Happiness + 5")
                print("affection + 5")
                return
        elif choice == "3":
            print("\nQuiet lunch. Kind of lonely.")
            player["happiness"] -= 5
            print("Happiness - 5")
            return
        else:
            print("Invalid choice, try again")
#settling in well, become associates with everyone
def day_2_morning():
    print("\nIt has now been a couple weeks since you started at this school and you have gotten to know everyone in your class by now. \nYou reach school in the morning and step into the hallway.")
    if crush["met"] == False:
        crush["name"] = input("\nWhat was the name of the person you found attractive on day 1 again? - ")
        crush["met"] = True
    popular_friends["met"] = True

    while True:
        print("\nYou see the popular kids and " + crush["name"] + " from earlier. Who do you choose to talk to?")
        print("1. The popular kids")
        print("2. " + crush["name"])
        choice = input("> ")

        if choice == "1":
            print("\nYou greet the popular kids and walk to class together")
            popular_friends["respect"] += 2
            print("Respect + 2")
            return
        elif choice == "2":
            print("\n" + crush["name"] + " spots you amongst the crowd and waves at you! You walk to class together")
            crush["affection"] += 2
            print("Affection + 2")
            return
        else:
            print("Invalid choice, try again")

#first fight cuh
def fight_1():
    print("\nYou are talking to a friend until a school bully randomly corners you up against a wall :( He is much taller than you...")
    while True:
        print("He is demanding you to empty your wallet. What do you do?")
        print("\n1. Peacefully hand over the money and be suppressed")
        print("2. You try to walk away, but he will take your money anyways")
        print("3. You pick a fight with him (be careful, you are relatively new to the school)")
        choice = input("> ")

        if choice == "1":
            print("You got robbed of your money entirely and did nothing to stop it")
            player["money"] = 0
            print("Money = 0")
            player["happiness"] -= 15
            print("Happiness - 15")
            return
        elif choice == "2":
            print("\nOuch, he just slammed you against the lockers and took all your money anyways. That hurt quite a bit :( ")
            player["money"] = 0
            print("Money = 0")
            player["health"] -= 10
            print("Health - 10")
            player["happiness"] -= 10
            print("Happiness - 10")
            return
        elif choice == "3":
            print("\nBold move...")

            while True:
                print("1. Kick him in the shin")
                print("2. Punch him in the face")
                choice_1 = input("> ")

                if choice_1 == "1":
                    print("\nHe fell down, and you kicked him hard in the chest. The fight ended then and there!")
                    print("You won the fight, gained a lot of reputation amongst others but the teachers are sending you to the principal's office")
                    popular_friends["respect"] += 40
                    print("Respect + 40")
                    player["happiness"] += 10
                    print("Happiness + 10")
                    print("\nYou nervously enter the principal's office, he asks you what happened. What do you say?")

                    while True:
                        print("\n1. The bully started taking all my money so I stood up for myself")
                        print("2. I was teaching the bully a lesson to not mess with me ever again")
                        print("3. There was no teacher in sight, he was going to hit me anyways so I hit first")
                        choice_2 = input("> ")

                        if choice_2 == "1":
                            print("\nThe principal understands the situation, but he says you should not hit anybody at all. He lets you off with a warning and suspends the bully")
                            print("You are glad that you weren't punished")
                            player["happiness"] += 5
                            print("Happiness + 5")
                            break
                        elif choice_2 == "2":
                            print("\nThe principal hands you a note of suspension, your parents tell you that they are very disappointed and ground you")
                            player["suspension"] = True
                            player["grounded"] = True
                            player["happiness"] -= 10
                            print("Happiness - 10")
                            break
                        elif choice_2 == "3":
                            print("\nThe teacher makes you attend detention for a week straight as a 'lighter' punishment. Atleast you study hard there")
                            player["grades"] += 10
                            print("Grades + 10")
                            player["happiness"] -= 5
                            print("Happiness - 5")
                            break
                        else:
                            print("Invalid choice, try again")

                    return

                elif choice_1 == "2":
                    print("\nHe stops your punch midway, slams you onto the floor and takes all of your money. Ouch!")
                    player["health"] -= 30
                    print("Health - 30")
                    player["money"] = 0
                    print("Money = 0")
                    popular_friends["respect"] -= 10
                    print("Respect - 10")
                    return
                else:
                    print("Invalid choice, try again")
        else:
            print("Invalid choice, try again")

#first party ehheehehehehe
def party_1():
    if player["suspension"] == True:
        while True:
            print("\nYou are at home, disappointed about what happened. Your parents grounded you but there is a halloween party happening this night.")
            print("1. Sneak out at night to go")
            print("2. Stay at home")
            choice = input("Enter your choice - ")     
            if choice == "2":
                print("\nBoring but atleast you aren't risking any more trouble. You decide to study the whole night and prepare for an upcoming exam.")
                player["grades"] += 10
                print("Grades + 10")
                player["happiness"] -= 5
                print("Happiness -  5")
                player["grounded"] = False
                player["suspension"] = False 
                return         
            elif choice == "1":
                print("\nThe party starts at 10pm, when do you sneak out?")
                print("1. Right after dinner")
                print("2. Once everyone is asleep, by 11pm")
                choice_1 = input("> ")           
                if choice_1 == "1":
                    print("\nAs soon as you were about to sneak out, your parents came into your room.")
                    print("They ground you for another week and take away all electronics :(")
                    player["suspension"] = False 
                    player["happiness"] -= 7
                    print("Happiness - 7")
                    return       
                elif choice_1 == "2":
                    player["grounded"] = False
                    print("\nYou make it out without being noticed. Now you must find a quick way there as you are already late. What do you do?")
                    print("1. Take the bus there")
                    print("2. Ask a friend for a lift")
                    choice_2 = input("> ")
                    if choice_2 == "1":
                        print("\nTook you a while but you finally reached. You had loads of fun and somehow your parents never found out!")
                        player["happiness"] += 15
                        print("Happiness + 15")
                        player["suspension"] = False 
                        return
                    elif choice_2 == "2":
                        print("\nYou reached much faster and had a lot of fun! Lucky for you your parents never found out!")
                        player["happiness"] += 20
                        print("Happiness + 20")
                        player["suspension"] = False 
                        return
                    else:
                        print("Invalid choice. Try again.")
                else:
                    print("Invalid choice. Try again.")
            else:
                print("Invalid choice, try again.")
    else:
        print("\nYou were invited to a halloween party, and surprisingly your parents. allowed you to go.")
        while True:
            print("1. Go in a cheap costume")
            print("2. Buy a new outfit")
            choice_3 = input("> ")
            if choice_3 == "1":
                print("\nYou buy a basic halloween outfit, compared to other's costumes, you feel very underdressed")
                player["happiness"] -= 5
                print("Happiness - 5")
                break
            elif choice_3 == "2":
                print("\nTurns out everybody complimented your outfit the moment you entered the party!")
                player["happiness"] += 5
                print("Happiness + 5")
                break
            else:
                print("Invalid choice, try again")
        while True:
            print("\n1.You are enjoying yourself, but realise that you haven't started preparing for an upcoming exam-")
            print("1. Leave early to go study for it")
            print("2. Come home late and enjoy more!")
            choice_4 = input("> ")
            if choice_4 == "1":
                print("\nYou focus on your studies, but feel like you missed out on some more fun")
                player["grades"] += 5
                print("Grades + 5")
                player["happiness"] -= 3
                print("Happiness - 3")
                return
            elif choice_4 == "2":
                print("\nYou enjoy the party for longer, but miss out on your studies")
                player["happiness"] += 3
                print("Happiness + 3")
                player["grades"] -= 5 
                print("Grades - 5")
                return
            else:
                print("Invalid choice, try again")


#first scene for an upcoming exam
def exam_1():
    print("\nYou return to school after a great party on the weekend. What do you do?")
    while True:
        print("1. Study hard after school")
        print("2. Play football with friends")
        choice = input("> ")

        if choice == "1":
            print("\nGood work, you are taking your studies seriously!")
            player["grades"] += 7
            print("Grades + 7")
            player["happiness"] -= 3
            print("Happiness - 3")
            return
        elif choice == "2":
            print("\nYou definitely don't put as much effort into your exams as you did for football, but at least you had fun!")
            player["happiness"] += 7
            print("Happiness + 7")
            player["grades"] -= 3
            print("Grades - 3")
            return
        else:
            print("Invalid choice, try again")

#scenario inside the exam hall
def exam_2():
    print("\nYou are in the exam hall, you feel like you barely studied. The person next to you is writing fast...")
    while True:
        print("1. Copy their answers")
        print("2. Try your best on your own")
        choice = input("> ")
        if choice == "1":
            player["cheated"] = True
            if random.random()<0.4:
                print("\nThe teacher spotted you. You got a zero and a note back home...")
                player["grades"] -= 20
                print("Grades - 20")
                player["happiness"] -= 10
                print("Happiness - 10")
            else:
                print("\nYou got away with it. Decent score but you feel guilty...")
                player["grades"] += 15
                print("Grades + 15")
                player["happiness"] -= 5
                print("Happiness - 5")
            return
        elif choice == "2":
            print("\nAlthough you struggled, you did it honestly")
            player["grades"] += 10
            print("Grades + 10")
            return
        else:
            print("Invalid choice, try again")

#results day!!
def report_card():
    print("\n ---REPORT CARD---")
    print("You nervously peep into your report card, and you read-")
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
    print('\n"Your grade is:' + letter + '"')
    if player["cheated"]:
        print("You still feel guilty that you should've studied on your own")
    #player["cheated"] = False
    player["suspension"] = False
    player["grounded"] = False #resetting some stats

#part-time job hunt 1
def job_1():
    while True:
        print("\nIt is now holiday season and you want to earn money from a part time job. \nYou read a leaflet offering some part-time jobs. It reads-")
        print("1. Deliver the newspaper")
        print("2. Tutor a young kid")
        print("3. Cleaning cars")

    
        choice = input("> ")
        if choice == "1":
            print("\nThe job itself is boring as there is limited interaction, but you stay healthy as you deliver them by cycling!")
            player["happiness"] -= 10
            print("Happiness - 10")
            player["money"] += 40
            print("Money + 40")
            player["health"] += 15
            print("Health + 15")
            return
        elif choice == "2":
            print("\nThe job is demanding, but you earn a lot of money and the kid is nice")
            player["happiness"] -= 5
            print("Happiness - 5")
            player["money"] += 80
            print("Money + 80")
            player["grades"] += 10
            print("Grades + 10")
            return
        elif choice == "3":
            print("\nThe job is relaxing, you earn a decent wage, however you drop a heavy bottle of soap on your foot while on the job")
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
#function is major as it is useful everywhere, within school_!.py and future files as well
#plan is to upgrade the function capabilities
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
        choice = input("> ")
        if choice == "1":
            if can_afford(30):
                player["money"] -= 30
                print("\nYou finally get to hang out with your friends, but you haven't told them you are afraid of heights...")
                print("\nAll of you begin queing up for the tallest ride in your state, but you feel like you will pass out if you ride it...\nYour friends are watching, what do you do?")
                while True:
                    print("1. Exit the queue")
                    print("2. Continue and face your fears")
                    choice_2 = input("> ")
                    if choice_2 == "1":
                        print("\nYou step out of the line and tell them you'll wait. They tease you a little, but it's soon forgotten")
                        player["happiness"] -= 5
                        print("Happiness - 5")
                        popular_friends["respect"] -= 5
                        print("Respect - 5")
                        return
                    elif choice_2 == "2":
                        print("\nYou close your eyes and get on the ride...")
                        if random.random() < 0.3:
                            print("You scream the whole ride and feel sick. Some parts of the ride were fun though")
                            player["health"] -= 10
                            print("Health - 10")
                            player["happiness"] += 5
                            print("Happiness + 5")
                            return
                        else:
                            print("\nIt was scary, but really fun at the same time! You and your friends loved the experience!")
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
                print("\nYou and " + crush["name"] + " get to the cinema. Which genre of movie do you want to watch?")
                while True:
                    print("1. A horror movie")
                    print("2. A comedy movie")
                    print("3. A romantic movie")
                    choice_3 = input("> ")
                    if choice_3 == "1":
                        print("\n" + crush["name"] + " grips your arm through the scary parts. You pretend as if you aren't scared too")
                        crush["affection"] += 10
                        print("Affection + 10")
                        player["happiness"] += 10
                        print("Happiness + 10")
                        return
                    elif choice_3 == "2":
                        print("\nThe two of you laugh so hard the people around shush at you")
                        crush["affection"] += 5
                        print("Affection + 5")
                        player["happiness"] += 15
                        print("Happiness + 15")
                        return
                    elif choice_3 == "3":
                        print("\nIt is a bit awkward to sit through it together, however " + crush["name"] + " smiles at you afterwards.")
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
                print("\nMoney - 25")
                print("You love the game, how do you choose to play it?")
                while True:
                    print("\n1. Play all night")
                    print("2. Only after you study for the day")
                    choice_4 = input("> ")
                    if choice_4 == "1":
                        print("\nYou finish half the game by sunrise. Your eyes hurt and you forgot to complete your homework")
                        player["happiness"] += 20
                        print("Happiness + 20")
                        player["health"] -= 5
                        print("Health - 5")
                        player["grades"] -= 10
                        print("Grades - 10")
                        return
                    elif choice_4 == "2":
                        print("\nYou enjoy it without letting your studies slip.")
                        player["happiness"] += 10
                        print("Happiness + 10")
                        player["grades"] += 10
                        print("Grades + 10")
                        return
                    else:
                        print("Invalid choice, try again")
        elif choice == "4":
            print("\nYou stay at home, study, exercise and save money. You feel responsible.")
            player["happiness"] += 5
            print("Happiness + 5")
            player["grades"] += 5
            print("Grades + 5")
            player["health"] += 5
            print("Health + 5")
            return
        else:
            print("Invalid choice, try again")

#trying to boost crush affection before prom
def crush_1():
    print("\nYou and " + crush["name"] + " were chatting as school was about to reopen. " + crush["name"] + " tells you that they broke their laptop screen and it will not turn on at all")
    print("They were unable to submit an assignment which is due by the end of first week of school. You offer a few solutions-")
    laptop_available = True
    laptop_repairable = True
    while True:
        if laptop_available:
            print("\n1. You lend " + crush["name"] + " your old laptop so they can submit their assignment")
        if laptop_repairable:
            print("2. You offer to fix it using your known knowledge of technology")
        print("3. Pay an amount of money for the repairs")
        print('4. Say "that is sad, tough luck" and nothing else')
        choice = input("> ")
        if choice == "1" and laptop_available:
            if random.random() < 0.35:
                print("\nOops! Turns out the laptop malfunctioned and won't turn on :( ")
                print(crush["name"] + " still appreciates your help!")
                crush["affection"] += 2
                print("Affection + 2")
                print("You need to choose another option!")
                laptop_available = False
                continue
            else:
                print("\n" + crush["name"] + " is really grateful for your help! They use your laptop and submit their assignment")
                crush["affection"] += 12
                print("Affection + 12")
                return
        elif choice == "2" and laptop_repairable:
            print("\n" + crush["name"] + " is thankful as they could not find a cheap repair nearby")
            if random.random() < 0.3:
                print("\nYou opened up the laptop, but its seems the issue is too complex for you to fix by yourself")
                print(crush["name"] + " still appreciates that you tried")
                crush["affection"] += 5
                print("Affection + 5")
                print("You need to choose another option!")
                laptop_repairable = False
                continue
            else:
                print("\nYou fix the issue with their laptop, turns out it was simple.")
                print(crush["name"] + " is immensely grateful as they were stressing out about the submission. They are very happy and so are you")
                player["happiness"] += 7
                print("Happiness + 7")
                crush["affection"] += 15
                print("Affection + 15")
                return
        elif choice == "3":
            print("\nYour current account balance is " + str(player["money"]))
            text = input("Enter an amount you would like to contribute to fixing their laptop - ")
            if not text.isdigit() or int(text) <= 0:
                print("Enter a whole number (integer) above 0.")
                continue
            cost = int(text)
            if not can_afford(cost):
                continue
            player["money"] -= cost
            print("Money - " + str(cost))
            if cost >= 80:
                print("\n" + crush["name"] + " is extremely thankful for such a large help, they say that they will never forget this favour")
                crush["affection"] += 20
                print("Affection + 20")
                player["happiness"] -= 15
                print("That was a lot of money you just spent, Happiness - 15")
                return
            elif cost >= 60:
                print("\n" + crush["name"] + " appreciates your help a lot and thanks you!")
                crush["affection"] += 16
                print("Affection + 16")
                player["happiness"] -= 10
                print("That was a hefty payment, Happiness - 10")
                return
            elif cost >= 40:
                print("\n" + crush["name"] + " thanks you a lot for your help!")
                crush["affection"] += 12
                print("Affection + 12")
                player["happiness"] -= 5
                print("That was expensive, happiness - 5")
                return
            elif cost >= 20:
                print("\n" + crush["name"] + " appreciates you contributing!")
                crush["affection"] += 10
                print("Affection + 10")
                return
            else:
                print("\n" + crush["name"] + " says thank you")
                crush["affection"] += 5
                print("Affection + 5")
                return
        elif choice == "4":
            print("\n" + crush["name"] + " says nothing... maybe you were too mean")
            crush["affection"] -= 5
            print("Affection - 5")
            return
        else:
            print("Invalid choice, try again")

#larp function
def random_event_1():
    i = random.random()
    j = random.random()
    print("\nYou are in school, you aren't feeling too well...")
    while True:
        if i < 0.3:
            print("You have caught a cold :( ")
            player["health"] -= 7
            print("Health - 7")
            player["grades"] -= 5
            print("You missed classes due to the cold, Grades - 5")
            return
        elif i < 0.65 :
            while True:
                if player["cheated"] == True:
                    print("\nA student sitting beside you asks for help on a test, its the same person you had cheaten off of earlier...")
                    print("\nWhat do you do?")
                    print("1. Give him the answers")
                    print("2. Ignore him and continue writing")
                    choice = input("> ")
                    if choice == "1":
                        if j < 0.3:
                            print("\nThe teacher has caught the two of you cheating, you are suspended and given 0 for the test")
                            player["suspension"] = True
                            player["grades"] -= 15
                            print("Grades - 15")
                            return
                        elif j <1.0:
                            print("\nYou don't feel as guilty as before because you repayed the favour, even if he may not know it")
                            player["happiness"] + 5
                            print("Happiness + 5")
                            return
                        else:
                            print("Invalid choice, try again")
                    elif choice == "2":
                        print("\nYou feel guilty for not helping him out")
                        player["happiness"] -= 10
                        print("Happiness - 10")
                        return
                    else:
                        print("Invalid choice, try again")
                elif player["cheated"] == False:
                    print("\nYou found 10 coins on the floor, sweet!")
                    player["money"] += 10
                    print("Money + 10")
                    return
        elif i < 1.0:
            print("\nA teacher praises your work in front of the class. This gives you motivation to study more!")
            player["grades"] += 5
            print("Grades + 5")
            player["happiness"] += 5
            print("Happiness + 5")
            return
        else:
            print("Invalid choice, try again")


#prom 1 part
PROM_AFFECTION_NEEDED = 25

def prom_1():
    asked_crush = False
    print("\nYou are walking through the school and see a flyer, it reads...")
    print("\n\n---PROM NIGHT---")
    print("Come with a partner or friends!")
    print("\nYou want to go to the dance with " + crush["name"] + " but you aren't sure if they would say yes...")

    while True:
        print("\nWhat do you do?")
        if not asked_crush:
            print("1. Ask " + crush["name"] + " out to prom")
        print("2. Go with your friends")
        choice = input("> ")

        if choice == "1" and not asked_crush:
            if crush["affection"] >= PROM_AFFECTION_NEEDED:
                while True:
                    print("\nWhen do you ask them out?")
                    print("1. After class in person")
                    print("2. Text them about it")
                    choice_1 = input("> ")

                    if choice_1 == "1":
                        print("\n" + crush["name"] + " smiles and says yes. They say that they were going to ask you out first. The two of you hug!")
                        crush["affection"] += 15
                        print("Affection + 15")
                        player["happiness"] += 10
                        print("Happiness + 10")
                        player["prom_with"] = "crush"
                        return
                    elif choice_1 == "2":
                        print("\n" + crush["name"] + " leaves you on delivered. For a whole day...")
                        print("You think to yourself, what went wrong...")
                        print("You decide to ask them out in person, when you have class together")
                        print("\n" + crush["name"] + " says yes, but they seem upset...")
                        print("They tell you that you should've asked them out in person and not online! You apologise")
                        player["happiness"] -= 5
                        print("Happiness - 5")
                        crush["affection"] -= 3
                        print("Affection - 3")
                        player["prom_with"] = "crush"
                        return
                    else:
                        print("Invalid choice, try again")
            else:
                print("\n" + crush["name"] + " gives you an awkward smile and says sorry, they already have other plans.")
                print("You can tell it's just an excuse, and you walk away feeling a bit stupid...")
                player["happiness"] -= 10
                print("Happiness - 10")
                asked_crush = True    # option 1 disappears from the menu now

        elif choice == "2":
            print("\nYou feel a bit bummed out that you didn't get to go to prom with " + crush["name"] + ". But at least you can go with your friends!")
            player["happiness"] += 5
            print("Happiness + 5")
            popular_friends["respect"] += 10
            print("Respect + 10")
            player["prom_with"] = "friends"
            return

        else:
            print("Invalid choice, try again")

def prom_2():
    print("\n---PROM NIGHT---")
    with_crush = player["prom_with"] == "crush"
    if with_crush:
        print("You walk into the hall with " + crush["name"] + ". The lights are dim and everyone is dressed up.")
    else:
        print("You walk into the hall with your friends. The lights are dim and the hall is full")
    while True:
        print("\nThe music starts. What do you do?")
        print("1. Dance with everyone")
        print("2. Hang out at the snack table")
        if with_crush:
            print("3. Ask " + crush["name"] + " for a slow dance")
        choice = input("> ")
        if choice == "1":
            print("\nYou join the crowd and dance badly, but nobody cares. Everyone is laughing and enjoying themselves.")
            player["happiness"] += 10
            print("Happiness + 10")
            popular_friends["respect"] += 5
            print("Respect + 5")
            break
        elif choice == "2":
            print("\nYou grab a snack and watch the dance floor. It's a bit quiet, but you overhear some funny gossip.")
            player["happiness"] += 3
            print("Happiness + 3")
            break
        elif choice == "3" and with_crush:
            print("\n" + crush["name"] + " takes your hand and the two of you sway under the lights.")
            crush["affection"] += 10
            player["happiness"] += 10
            print("Happiness + 10")
            break
        else:
            print("Invalid choice, try again")

    print("\nSuddenly the music cuts out and the whole hall goes silent...")
    while True:
        print("1. Start singing to fill the silence")
        print("2. Wait it out with everyone else")
        choice = input("> ")
        if choice == "1":
            print("\nYou belt out a song. It's awful, but the whole hall joins in!")
            popular_friends["respect"] += 10
            print("Respect + 10")
            player["happiness"] += 5
            print("Happiness + 5")
            break
        elif choice == "2":
            print("\nThe music comes back after a minute and everyone cheers.")
            break
        else:
            print("Invalid choice, try again")
    print("\nThe dance ends, it was really fun!")
    if with_crush:
        print("\nYou tell " + crush["name"] + " that you really enjoyed the dance with them.")
        return
    else:
        print("\nYou tell you friends that the dance was really fun")
        return
    
#final exam year 9
def exam_3():
    player["suspension"] = False
    player["grounded"] = False
    player["cheated"] = False
    print("\nIt is now the end of the academic year. You are sitting your final exam before you graduate to the final year of high school!!!")
    while True:
        print("\nYou are stuck on a question, you are sure that everything else is completely correct on the exam. What do you do?")
        print("1. Guess the answer")
        print("2. Go to the washroom and use your phone")
        choice = input("> ")
        if choice == "1":
            if random.random() < 0.4:
                print("\nAfter the exam ends, you discuss the questions and turns out you got it correct. Well done!")
                player["happiness"] += 5
                print("Happiness + 5")
                player["grades"] += 15
                print("Grades + 15")
                return
            else:
                print("\nYou discuss the question after the exam ends, turns out you got it wrong :(")
                print("You still got good marks though!")
                player["grades"] += 10
                print("Grades + 10")
                return
        elif choice == "2":
            player["cheated"] = True
            print("\nYou sneak out your phone from your bag, now try not to get caught...")
            while True:
                print("\n1. Enter a stall and cheat there")
                print("2. Wait outside a stall and use your phone there")
                choice_1 = input("> ")
                if choice_1 == "1":
                    while True:
                        print("Someone has entered the bathroom, you don't know if it is a teacher or a student...")
                        print("\n1. Quickly check your answer and walk out of the stall")
                        print("2. Wait for them to leave")
                        choice_2 = input("> ")
                        if choice_2 == "1":
                            if random.random() < 0.3:
                                print("\nIt is just a student, you breathe a sigh of relief")
                                print("You got the answer correct, but deep down you know you didn't deserve the full marks")
                                player["grades"] += 15
                                print("Grades + 15")
                                return
                            else:
                                print("\nYou walk out, but it's a teacher. You try to wash your hands in a hurry, as soon as you are about to exit you hear 'wait!'")
                                print("You take a deep breath, turn around as calmly as you can and say - 'Can I help you?'")
                                if random.random() < 0.65:
                                    print("The teacher says they noticed a bright flash coming from your pocket. Eventually they find out about your phone and complain about you")
                                    print("\nYou aren't suspended, but you are given reduced marks for the exam")
                                    player["grades"] -= 10
                                    print("Grades - 10")
                                    return
                                else:
                                    print("Turns out they were just asking what exam you had today. Close call!")
                                    print("\nYou end up getting full on the test")
                                    player["grades"] += 15
                                    print("Grades + 15")
                                    return
                        elif choice_2 == "2":
                            if random.random() < 0.6:
                                print("\nTurns out you messed up half the answer as you were nervous in the washroom")
                                player["grades"] += 12
                                print("Grades + 12")
                                return
                            else:
                                print("\nYou get full marks, but you feel guilty...")
                                player["grades"] += 15
                                print("Grades + 15")
                                return
                        else:
                            print("Invalid choice, try again")
                elif choice_1 == "2":
                    if random.random() < 0.4:
                        print("\nYou got the answer completely correct!")
                        player["grades"] += 15
                        print("Grades + 15")
                        return
                    else:
                        print("\nYou only got half the answer right as you were too nervous about someone catching you")
                        player["grades"] += 10
                        print("Grades + 10")
                        return
                else:
                    print("Invalid choice, try again")
        else:
            print("Invalid choice, try again")
