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
def sports_1():
    print("\nJust before the new school year begins, you decide to try out for your school's sports team")
    tried = [] #sports list if you fail
    while True:
        if len(tried) == 3:
            print("\nUnfortunately you were not selected for any team. There may be more opportunities in the future")
            print("Focus on improving your health for that")
            return
        print("\nWhich sport do you select?")
        if "table tennis" not in tried:
            print("1. Table tennis")
        if "football" not in tried:
            print("2. Football")
        if "cricket" not in tried:
            print("3. Cricket")
        print("4. Don't try out for any team")
        choice = input("> ")
        #table tennis
        if choice == "1" and "table tennis" not in tried:
            print("\nYou turn up on time for the tryouts. It seems like it won't be easy to get in the team as there are over 50 other people there")
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
                else:
                    print("Invalid choice, try again")
                    continue
                print("The coach makes all the players do fitness exercises. It's either a pass or fail")
                if player["health"] == 100:
                    print("You finish them easily and are now part of the Table Tennis team!")
                    sports["name"] = "Table Tennis"
                    sports["skills"] += 10
                    print("Table Tennis skills + 10")
                    player["happiness"] += 7
                    print("Happiness + 7")
                    sports["position"] = "starter"
                    return
                elif player["health"] >= 70:
                    print("You managed to finish the exercises, struggling a bit. But you are still selected!")
                    sports["name"] = "Table Tennis"
                    sports["skills"] += 8
                    print("Table Tennis skills + 8")
                    player["happiness"] += 7
                    print("Happiness + 7")
                    sports["position"] = "starter"
                    return
                elif player["health"] > 50:
                    print("You barely managed to finish the exercises. For now you are just a reserve player...")
                    sports["name"] = "Table Tennis"
                    sports["skills"] += 5
                    print("Table Tennis skills + 5")
                    player["happiness"] += 3
                    print("Happiness + 3")
                    sports["position"] = "reserve"
                    return
                else:
                    print("You could not complete the exercises and unfortunately weren't selected for Table Tennis, however you can attempt a tryout for other sports!")
                    tried.append("table tennis")
                    break
        #football, more demanding
        elif choice == "2" and "football" not in tried:
            print("\nYou turn up at the pitch at 6 am in the morning. You're tired, so you have to do your best!")
            print("You tryout as a striker. The game starts...")
            print("You have the ball, what do you do?")
            while True:
                print("\n1. Shoot from outside the box")
                print("2. Dribble through the defence")
                choice_2 = input("> ")
                if choice_2 == "1":
                    if random.random() < 0.7:
                        print("\nYour shot was saved, and your team won a corner, which resulted in a goal!")
                    else:
                        print("You scored a goal from 30 metres out! You and your team celebrate wildly!")
                        sports["skills"] += 10
                        print("Skills + 10")
                        player["happiness"] += 15
                        print("Happiness + 15")
                    break
                elif choice_2 == "2":
                    print("\nYou start dribbling like a pro, and are about to shoot until you get fouled from behind. Penalty awarded")
                    print("You decide to take the penalty... Where do you shoot?")
                    while True:
                        print("\n1. Calmly chip it in the middle")
                        print("2. Bang it into the top corner")
                        choice_3 = input("> ")
                        if choice_3 == "1":
                            if random.random() < 0.4:
                                print("\nYou missed trying to look cool, you lost all your aura and the game...")
                                popular_friends["respect"] -= 10
                                print("Respect - 10")
                                player["happiness"] -= 10
                                print("Happiness - 10")
                            else:
                                print("\nYou just coldly celebrate as you just won the game for your team...")
                                popular_friends["respect"] += 10
                                print("Respect + 10")
                                player["happiness"] += 10
                                print("Happiness + 10")
                            break
                        elif choice_3 == "2":
                            if random.random() < 0.2:
                                print("\nYou hit the crossbar, but your team lost the game")
                                player["happiness"] -= 5
                                print("Happiness - 5")
                                popular_friends["respect"] -= 5
                                print("Respect - 5")
                            else:
                                print("\nYou scored a beautiful penalty to win the game in the last minutes!")
                                player["happiness"] += 10
                                print("Happiness + 10")
                                popular_friends["respect"] += 5
                                print("Respect + 5")
                            break
                        else:
                            print("Invalid choice, try again")
                    break
                else:
                    print("Invalid choice, try again")
            print("The coach makes all the players do fitness exercises. It's either a pass or fail")
            if player["health"] == 100:
                print("You finish them easily and are now part of the Football team!")
                sports["name"] = "Football"
                sports["skills"] += 10
                print("Football skills + 10")
                player["happiness"] += 7
                print("Happiness + 7")
                sports["position"] = "starter"
                return
            elif player["health"] >= 80:
                print("You managed to finish the exercises, struggling a bit. But you are still selected!")
                sports["name"] = "Football"
                sports["skills"] += 8
                print("Football skills + 8")
                player["happiness"] += 7
                print("Happiness + 7")
                sports["position"] = "starter"
                return
            elif player["health"] > 65:
                print("You barely made it through. You will need to work harder. But you are selected as a substitute")
                sports["name"] = "Football"
                sports["skills"] += 5
                print("Football skills + 5")
                player["happiness"] += 3
                print("Happiness + 3")
                sports["position"] = "substitute"
                return
            else:
                print("You could not complete the exercises and unfortunately weren't selected for Football, however you can attempt a tryout for other sports!")
                tried.append("football")
                continue
        #cricket, middle of the 2
        elif choice == "3" and "cricket" not in tried:
            print("\nYou step foot onto the pitch with a bat in hand. The coach tells you to show him what you've got as a batter.")
            print("The first ball is bowled. It's fast and heading straight at you!")
            while True:
                print("\n1. Play a defensive shot")
                print("2. Go for a big hit")
                choice_4 = input("> ")
                if choice_4 == "1":
                    print("\nYou block it safely. The coach nods... a steady start.")
                    sports["skills"] += 3
                    print("Cricket skills + 3")
                    break
                elif choice_4 == "2":
                    if random.random() < 0.5:
                        print("\nYou smash it over the boundary for six! The few spectators cheer.")
                        sports["skills"] += 8
                        print("Cricket skills + 8")
                        player["happiness"] += 10
                        print("Happiness + 10")
                    else:
                        print("\nYou swing and miss completely. The stumps go flying...")
                        player["happiness"] -= 5
                        print("Happiness - 5")
                    break
                else:
                    print("Invalid choice, try again")
            print("\nNext, the coach sends you to field. A high ball goes up, straight towards you...")
            while True:
                print("\n1. Go for the catch")
                print("2. Let your teammate take it")
                choice_5 = input("> ")
                if choice_5 == "1":
                    if random.random() < 0.6:
                        print("\nYou hold on to a brilliant catch! Your teammates cheer you.")
                        popular_friends["respect"] += 5
                        print("Respect + 5")
                        sports["skills"] += 5
                        print("Cricket skills + 5")
                    else:
                        print("\nThe ball slips through your fingers and rolls away. A few people groan.")
                        popular_friends["respect"] -= 5
                        print("Respect - 5")
                    break
                elif choice_5 == "2":
                    print("\nYour teammate takes the catch safely. You didn't do much to stand out.")
                    break
                else:
                    print("Invalid choice, try again")
            print("\nThe coach makes all the players do fitness exercises. It's either a pass or fail")
            if player["health"] >= 90:
                print("You finish them easily and are now part of the Cricket team!")
                sports["name"] = "Cricket"
                sports["skills"] += 10
                print("Cricket skills + 10")
                player["happiness"] += 7
                print("Happiness + 7")
                sports["position"] = "starter"
                return
            elif player["health"] >= 75:
                print("You finish the exercises, struggling a bit, but you are still selected!")
                sports["name"] = "Cricket"
                sports["skills"] += 8
                print("Cricket skills + 8")
                player["happiness"] += 7
                print("Happiness + 7")
                sports["position"] = "starter"
                return
            elif player["health"] > 60:
                print("You barely make it through. For now you are just a reserve player...")
                sports["name"] = "Cricket"
                sports["skills"] += 5
                print("Cricket skills + 5")
                player["happiness"] += 3
                print("Happiness + 3")
                sports["position"] = "reserve"
                return
            else:
                print("You could not complete the exercises and weren't selected for Cricket, but you can try out for another sport!")
                tried.append("cricket")
                continue
        elif choice == "4":
            print("\nYou decide sports aren't for you right now. Maybe next year.")
            return
        else:
            print("Invalid choice, try again")

#random event (again)!!!
def random_event_2():
    if random.random() < 0.5:
        print("\nYou are shopping with your parents one day before school reopens. Suddenly you see " + crush["name"] + "across the isles, but they haven't seen you yet.")
        while True:
            print("\n1. Go up to them and say hi")
            print("2. Act like you did not see them")
            choice = input("> ")
            if choice == "1":
                print("\n" + crush["name"] + " waves at you with a big smile. The two of you meet each other's parents")
                print("All of you go for a lunch together. You and " + crush["name"] + " chat together!")
                player["happiness"] += 5
                print("Happiness + 5")
                crush["affection"] += 3
                print("Affection + 3")
                return
            elif choice == "2":
                print("\nYou were too hesitant to even meet them outside of school... You feel dissapointed in yourself")
                player["happiness"] -= 5
                print("Happiness - 5")
                return
            else:
                print("Invalid choice, try again")
                continue
    else:
        print("\nYou played video games for 15 hours straight. Your head and eyes begin to hurt...")
        print("What do you do?")
        while True:
            print("\n1. Keep playing as it's last day before school")
            print("2. Go to sleep")
            choice_1 = input("> ")
            if choice_1 == "1":
                print("\nYour eyes start to burn and you feel a lot of pain")
                player["health"] -= 5
                print("Health - 5")
                player["happiness"] -= 5
                print("Happiness - 5")
                return
            elif choice_1 == "2":
                print("\nYou finally take some rest. You really enjoyed the game nicely!")
                player["happiness"] += 10
                print("Happiness + 10")
                return
            else:
                print("Invalid choice, try again")
                continue