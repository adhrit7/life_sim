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
                print("You were too hesitant to even meet them outside of school... You feel dissapointed in yourself")
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

#day 1 of year 12, referring back to what the user chose on their bday
def choose_plan():
    print("\n---YEAR 12---")
    print("Summer is over, and you are a senior now. On the first morning, your teacher hands out the subject forms for your final year.")
    plan = player["plan"]

    # branch 1: going uni
    if plan == "university":
        print("\nYour teacher leans over your desk. 'You said university. Entry requirements this year will be tough, so choose carefully.'")
        while True:
            print("\nWhat do you want to focus on?")
            print("1. Sciences and maths")
            print("2. Humanities and arts")
            print("3. A balanced study load")
            if sports["name"] != "":
                print("4. Drop a subject to focus more on your" + sports["name"] + "training")
            choice = input("> ")
            if choice == "1":
                if player["grades"] < 60:
                    print("\nThe teacher warns you this might be a stretch with your current grades...")
                    if random.random() < 0.5:
                        print("You push through the hard work and it pays off!")
                        player["grades"] += 10
                        print("Grades + 12")
                        player["happiness"] -= 3
                        print("Happiness - 3")
                    else:
                        print("It is too much, and you fall behind before even the first week is over.")
                        player["grades"] += 3
                        print("Grades + 3")
                        player["happiness"] -= 7
                        print("Happiness - 7")
                else:
                    print("\nThe workload is quite heavy, but you seem to handle it well.")
                    player["grades"] += 12
                    print("Grades + 12")
                    player["happiness"] -= 5
                    print("Happiness - 5")
                player["focus"] = "heavy"
                return
            elif choice == "2":
                print("\nYou pick the subjects you actually enjoy. The first week feels lighter, and your teachers are impressed by your essays.")
                player["grades"] += 8
                print("Grades + 8")
                player["happiness"] += 5
                print("Happiness + 5")
                player["focus"] = "creative"
                return
            elif choice == "3":
                print("\nYou spread your effort across a bit of everything. Good work!")
                player["grades"] += 5
                print("Grades + 5")
                player["focus"] = "balanced"
                return
            elif choice == "4" and sports["name"] != "":
                print("\nYou drop a subject to keep your evenings free for the team. Your coach is thrilled, your teacher... less so")
                sports["skills"] += 5
                print(sports["name"]) + " skills + 5"
                player["grades"] -= 3
                print("Grades - 3")
                player["focus"] = "sport"
                return
            else:
                print("Invalid choice, try again")

    #branch 2: getting a job
    elif plan == "job":
        print("\nour teacher nods. 'You want to work after school. There are some practical routes this year, so let's find you one.'")
        while True:
            print("\nWhat do you want to focus on?")
            print("1. An work-experience placement")
            print("2. A skills course")
            print("3. A talk with a local apprentice")
            if sports["name"] != "":
                print("4. Drop a subject to protect your " + sports["name"] + " training")
            choice = input("> ")

            if choice == "1":
                print("\nYou spend your weekend at a local business. The hours are long, but you get paid.")
                player["money"] += 30
                print("Money + 30")
                player["grades"] -= 3
                print("Grades - 3")
                player["focus"] = "placement"
                return
            elif choice == "2":
                print("\nThe course is hands- on and you pick up real skills.")
                player["grades"] += 6
                print("Grades + 6")
                player["happiness"] += 3
                print("Happiness + 3")
                player["focus"] = "vocational"
                return
            elif choice == "3":
                print("\nThe apprentice shows you what the job is really like, and introduces you to a few useful people around town.")
                popular_friends["respect"] += 5
                print("Respect + 5")
                player["happiness"] += 5
                print("Happiness + 5")
                player["focus"] = "netowrking"
                return
            elif choice == "4" and sports["name"] != "":
                print("\nYou drop a subject to keep your evenings free for the team.")
                sports["skills"] += 5
                print(sports["name"] + " skills + 5")
                player["grades"] -= 5
                print("Grades - 5")
                player["focus"] = "sport"
                return
            else:
                print("Invalid choice, try again")

    #branch 3: unsure + invalid input
    else:
        print("\nYour teacher sighs... 'Not sure yet? You need to make a decision fast for your career'")
        while True:
            print("\nWhat do you do?")
            print("1. Try a bit of everything")
            print("2. Pick one path and try out your luck")
            print("3. Put the decision off for now")
            choice = input("> ")

            if choice == "1":
                print("\nYou try to focus equally on each subject. Nothing clicks yet, but nothing hurts either")
                player["grades"] += 3
                print("Grades + 3")
                player["happiness"] += 3
                print("Happiness + 3")
                player["focus"] = "explore"
                return
            elif choice == "2":
                print("\nYou commit to one path as a trial run. It gives you something to aim for.")
                player["grades"] += 5
                print("Grades + 5")
                player["focus"] = "trial"
                return
            elif choice == "3":
                print("\nYou tell yourself you will think about it later. It feels great to be stress free, for now...")
                player["happiness"] += 8
                print("Happiness + 8")
                player["grades"] -= 5
                print("Grades- 5")
                player["focus"] = "later"
                return
            else:
                print("Invalid choice, try again")


#group project 1, with bully from school_1 fight_1
def assignment_1():
    print("\nYou are given a science assignement in which you have to work as partners")
    print("Unfortunately for you, the teacher paired you up with the person who bullied you last year...")
    while True:
        print("\nIt is awkward to be working together on the same assignment after everything that happened earlier... What do you say to him after class?")
        print("1. You got anything to say?")
        print("2. Let's just finish it without talking about the past")
        choice = input("> ")
        if choice == "1":
            print("\nThey threaten you, but you decide to focus on your work")
            split_failed = False
            while True:
                print("What do you do?")
                print("\n1. Do all the work yourself and give both of you the credit")
                if not split_failed:
                    print("2. Try to split the work equally amongst yourselves")
                print("3. Finish all the work but lie to the teacher that they didn't help out")
                choice_1 = input("> ")
                if choice_1 == "1":
                    print("\nYou feel exhausted, angry that they did not help out. But atleast your teacher loved your assignment")
                    player["happiness"] -= 3
                    print("Happiness - 3")
                    player["health"] -= 3
                    print("Health - 3")
                    player["grades"] += 7
                    print("Grades + 7")
                    return
                elif choice_1 == "2" and not split_failed:
                    if random.random() < 0.6:
                        print("\nSurprisingly the two of you manage to finish the work. The teacher grades your work average")
                        player["grades"] += 3
                        print("Grades + 3")
                        return
                    else:
                        print("\nThe bully says they do not care about the assignment... Try another option")
                        split_failed = True
                        continue
                elif choice_1 == "3":
                    print("\nBold move, but they totally deserve it")
                    if random.random() <= 0.5:
                        print("The teacher gave the bully a 0 for not working, but gave you good marks! What a great moment of joy!")
                        player["happiness"] += 5
                        print("Happiness + 5")
                        player['grades'] += 5
                        print("Grades + 5")
                        return
                    else:
                        print("The teacher did not believe you and instead gave you a 0 for framing your partner")
                        player["grades"] -= 5
                        print("Grades - 5")
                        return
                else:
                    print("Invalid choice, try again")
        elif choice == "2":
            print("\nThe two of you finish the assignment early. The bully even apologises for what they did to you last year. You feel better about him")
            roll = random.random()
            if roll < 0.4:
                print("You end up getting the highest marks in the class. Things ease up between you")
                player["happiness"] += 4
                print("Happiness + 4")
                player["grades"] += 5
                print("Grades + 5")
                return
            elif roll() < 0.8:
                print("You are given average marks for the assignment. Nothing special but now you aren't afraid of your classmate")
                player["grades"] += 5
                print("Grades + 5")
                player["happiness"] += 3
                print("Happiness + 3")
                return
            else:
                print("The teacher fails you both for a poor assignment")
                player["grades"] -= 3
                print("Grades - 3")
                return
        else:
            print("Invalid choice, try again")

#sports training sesh 1. make it as good as possible as will be quite useful and repeated. 
#do make updates in future depending on future code
def training_1():
    promotion_skills = 25 #skill level needed for subs to become starters
    low_health = 50 #you go home below ts

    #if no team yet
    if sports["name"] not in ("Table tennis", "Football", "Cricket"):
        return

    #intro for sports
    if sports["name"] == "Table tennis":
        print("\nYour alarm goes off at 5 qm. Your bed is warm and comfy, but you have table tennis training.")
    elif sports["name"] == "Football":
        print("\nYour phone buzzes at 5:45 am. It's freezing outside, but the team meets at the school field in half an hour.")
    else:
        print("\nSchool is over and the cricket nets are waiting. The sun is low and your legs already feel heavy.")

    #decide whether go or skpi
    while True:
        print("\nWhat do you do?")
        print("1. Go to training")
        print("2. skip for today")
        choice = input("> ")
        if choice == "1":
            break
        elif choice == "2":
            print("\nYou turn off the alarm and go back to sleep. Nobody says anything, but the coach definetly notices.")
            sports["skills"] -= 10
            print(sports["name"] + " skills - 10")
            player["happiness"] += 3
            print("Happiness + 3")
            return
        else:
            print("Invalid choice, try again")


    #health train
    if player["health"] < low_health:
        print("\nYou turn up, but you look terrible. After one lap the coach pulls you aside and sends you home to rest.")
        player["happiness"] -= 3
        print("Happiness - 3")
        return

    sports["sessions"] += 1
    print("\nTraining session number " + str(sports["sessions"]) + " begins.")

    drill = random.randint(1,3)

    #table tennis
    if sports["name"] == "Table tennis":
        if drill == 1:
            print("\nThe coach sets up a machine which shoots at you from every angle")
            while True:
                print("\n1. Focus on your footwork")
                print("2. Focus on putting spin on every shot")
                choice = input("> ")
                if choice == "1":
                    print("\nYou do the basics. It's tiring, but you hardly miss a ball.")
                    sports["skills"] += 4
                    print("Table tennis skills + 4")
                    player["health"] -= 3
                    print("Health - 3")
                    break
                elif choice == "2":
                    if random.random() < min(0.9, 0.45 + sports["skills"]/200):
                        print("\nThe ball curves exactly where you wanted it to. The coach nods calmly.")
                        sports["skills"] += 7
                        print("Table tennis skills + 7")
                    else:
                        print("\nYou get so busy trying to look fancy that you lose your rhythm...")
                        sports["skills"] += 2
                        print("Table tennis skills + 2")
                        player["happiness"] -= 2
                        print("Happiness - 2")
                    break
                else:
                    print("Invalid choice, try again")

        elif drill == "2":
            print("\nToday is serve practice. The coach tells you to aim at a small cup")
            while True:
                print("\n1. Go for a short, tricky serve")
                print("2. Go for a fast, long serve")
                choice = input("> ")
                if choice == "1":
                    if random.random() < min(0.9, 0.5 + sports["skills"]/200):
                        print("\nThe ball barely clears the net and hits the cup. A couple of teammates clap.")
                        sports["skills"] += 6
                        print("Table tennis skills + 6")
                        popular_friends["respect"] += 3
                        print("Respect + 3")
                    else:
                        print("\nIt hits the net and rolls back at you...")
                        sports["skills"] += 2
                        print("Table tennis skills + 2")
                    break
                else:
                    print("Invalid choice, try again")

        else:
            print("\nThe coach pairs you up for a rally.")
            while True:
                print("\n1. Play it safe and keep the ball in play")
                print("2. Go for a smash whenever you can")
                choice = input("> ")
                if choice == "1":
                    print("\nYou both settle into a steady rhythm and hit clean shots")
                    sports["skills"] += 4
                    print("Table tennis skills + 4")
                    player["happiness"] += 2
                    print("Happiness + 2")
                    break
                elif choice == "2":
                    if random.random() < min(0.9, 0.4 + sports["skills"] / 200):
                        print("\nYou smash three in a row and the rally keeps going.")
                        sports["skills"] + 8
                        print("Table tennis skills + 8")
                        popular_friends["respect"] + 5
                        print("Respect + 5")
                    else:
                        print("\nYou go for a big shot on the sixth ball and it flies out of the table. Your partner sighs...")
                        sports["skills"] += 2
                        print("Table tennis skills + 2")
                        player["happiness"] -= 3
                        print("Happiness - 3")
                    break
                else:
                    print("Invalid choice, try again")

    #football
    elif sports["name"] == "Football":

        if drill == 1:
            print("\nThe coch sets up the sprint ladders and holds a stopwatch. He notes everyone's time on a whiteboard.")
            while True:
                print("\n1. Push hard to beat your best time")
                print("2. Calm yourself and save energy")
                choice = input("> ")
                if choice == "1":
                    if random.random() < min(0.9, 0.6 + sports["skills"] / 200):
                        print("\nYour lungs are burning, but you beat your old time by a small margin. The coach writes your name at the top.")
                        sports["skills"] += 6
                        print("Football skills + 6")
                        player["health"] -= 4
                        print("Health - 4")
                        popular_friends["respect"] += 3
                        print("Respect + 3")
                    else:
                        print("\nHalfway through the last sprint your calf cramps and you hop off the pitch.")
                        sports["skills"] += 2
                        print("Football skills + 2")
                        player["health"] -= 6
                        print("Health - 6")
                    break
                elif choice == "2":
                    print("\nYou finish in the middle. Nothing special, but you are still standing")
                    sports["skills"] += 3
                    print("Football skills + 3")
                    player["health"] -= 2
                    print("Health - 2")
                    break
                else:
                    print("Invalid choice, try again")

        elif drill == "2":
            print("\nThe teach forms a cricle for a rondo, and somehow you ed up in the middle chasing the ball.")
            while True:
                print("\n1. Chase the ball as hard as you can")
                print("2. Stay calm and try to read the passes")
                choice = input("> ")
                if choice == "1":
                    print("\nYou run in circles until your legs give up. You barely touch the ball, but nobody can say you didn't try.")
                    sports["skills"] += 4
                    print("Football skills + 4")
                    player["health"] -= 4
                    print("Health - 4")
                    break
                elif choice == "2":
                    if random.random() < min(0.9, 0.5 + sports["skills"] / 200):
                        print("\nYou spot the pass a second before it happens and snatch the ball!")
                        sports["skills"] += 7
                        print("Football skills + 7")
                        popular_friends["respect"] += 4
                        print("Respect + 4")
                    else:
                        print("\nYou guess wrong again and again. Two minutes later you are still stuck in the center and everyone is laughing at you.")
                        sports["skills"] += 2
                        print("Football skills + 2")
                        popular_friends["respect"] -= 2
                        print("Respect - 2")
                    break
                else:
                    print("Invalid choice, try again")

        else:
            print("\nThe coach makes a 7 a side game. Ten minutes in, the ball finally lands at your feet.")
            while True:
                print("\n1. Pass to the best player on your team")
                print("2. Take the shot yourself")
                choice = input("> ")
                if choice == "1":
                    print("\nYou slide the ball cleanly across and your teammate scores. He points at you as he celebrates")
                    popular_friends["resepct"] == 5
                    print("Respect + 5")
                    sports["skills"] += 3
                    print("Football skills + 3")
                    break
                elif choice == "2":
                    if random.random() < min(0.9, 0.4 + sports["skills"] / 200):
                        print("\nYou don't even think about it. The ball flies into the top corner and you just stand there stunned.")
                        sports["skills"] += 8
                        print("Football skills + 8")
                        player["happiness"] += 5
                        print("Happiness + 5")
                    else:
                        print("\nYou blast it way over the bar and it lands in the bushes behind the goal. A teammate has to go and find it.")
                        sports["skills"] == 2
                        print("Football skills + 2")
                        popular_friends["respect"] -= 3
                        print("Respect - 3")
                    break
                else:
                    print("Invalid choice, try again")

    #cricket
    else:
        if drill == "1":
            print("\nThe coach puts the quickest bowler in the team at one end of the nets. You are up first")
            while True:
                print("\n1. Play it safe and defend")
                print("2. Attack every ball")
                choice = input("> ")
                if choice == "1":
                    print("\nYou leave the wide ones and block the rest. The coach says 'Good patience'!")
                    sports["skills"] += 3
                    print("Cricket skills + 3")
                    break
                elif choice == "2":
                    if random.random() < min(0.9, 0.45 + sports["skills"] / 200):
                        print("\nYou step down the pitch and smack the ball against the back fence. The bowler glares at you.")
                        sports["skills"] += 5
                        print("Cricket skills + 5")
                        player["happiness"] += 4
                        print("Happiness + 4")
                    else:
                        print("\nYou swing hard and the stumps fly off the ground. It's going to be a long evening.")
                        sports["skills"] == 2
                        print("Cricket skills + 2")
                        player["happiness"] -= 3
                        print("Happiness - 3")
                    break
                else:
                    print("Invalid choice, try again")

        elif drill == "2":
            print("\nIt's catching practise. The sun is blinding you but the coach keeps hitting high balls into the sky constantly")
            while True:
                print("\n1. Call for it loudly and and go for every catch coming your way")
                print("2. Hang back and wait to see where it lands")
                choice = input("> ")
                if choice == "1":
                    if random.random() < min(0.9, 0.55 + sports["skills"] / 200):
                        print("\nYou move under the ball and catch it Your teammates cheer you!")
                        sports["skills"] += 5
                        print("Cricket skills + 5")
                        popular_friends["respect"] += 3
                        print("Respect + 3")
                    else:
                        print("\nYou call for it, then lose it in the sun... The whole team teases you for a week")
                        sports["skills"] += 2
                        print("Cricket skills + 2")
                        popular_friends["respect"] -= 3
                        print("Respect - 3")
                    break
                elif choice == "2":
                    print("\nYou pick up a couple of easy ones, thats nothing special")
                    sports["skills"] += 2
                    print("Cricket skills + 2")
                    break
                else:
                    print("Invalid choice, try again")

        else:
            print("\nThe coach marks a target on the pitch and tells everyone to bowl there.")
            while True:
                print("1. Run in amd bowl as fast as you can")
                print("2 Slow down and focus on accuracy")
                choice = input("> ")
                if choice == "1":
                    player['health'] -= 3
                    print("Health - 3")
                    if random.random() < min(0.9, 0.4 + sports["skills"] / 200):
                        print("\nThe ball rips through and  hits the target zone. The batsman ducks to avoid the ball hitting is head.")
                        sports["skills"] += 7
                        print("Skills + 7")
                    else:
                        print("\nYou bowl consecutive wides and no balls... He's not happy")
                        sports["skills"] == 2
                        print("Cricket skills + 2")
                    break
                elif choice == "2":
                    print("\nYou slow down and are mostly hitting the target.")
                    sports["skills"] += 5
                    print("Cricket skills + 5")
                    break
                else:
                    print("Invalid choice, try again")

    #sometimes crush["name"] can come to watch training
    if crush["affection"] >= 40 and random.random() < 0.2:
        print("\nOn your way out you spot " + crush["name"] + " by the fence. They came to watch for a bit and give you a wave.")
        crush["affection"] += 3
        print("Affecion + 3")


    #check whether you are promoted or demoted
    print("")
    if sports["position"] in ("reserve", "substitute") and sports["skills"] >= promotion_skills:
        print("The coach calls you over after training. He says 'You've just earned your spot in the starting lineup. Keep up the good work.'")
        sports["position"] = "starter"
        player["happiness"] += 8
        print("Happiness") + 8
        popular_friends["respect"] += 5
        print("Respect + 5")
    elif sports["position"] == "starter" and sports["skills"] < 35:
        print("The coach looks at you for a long second. He tells you that your spot isn't safe. You need to do better in training")
        player["happiness"] -= 3
        print("Happiness - 3")
    elif sports["skills"] >= 80:
        print("The coach nods at you and tells the others that you are on of the best on the team")
        player["happines"] += 5
        print("Happiness + 5")
    else:
        print("The coach tells you to keep training , you have potential")