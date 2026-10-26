from data import player, crush, popular_friends
import random
import school_1


def show_stats():
    print("---Your stats---")
    print("money:", player["money"])
    print("health:", player["health"])
    print("happiness:", player["happiness"])
    print("grades:", player["grades"])
    print("age:", player["age"])


def check_stats():
    # keep stats in a sensible range
    for stat in ["health", "happiness", "grades"]:
        if player[stat] > 100:
            player[stat] = 100
        if player[stat] < 0:
            player[stat] = 0

    # warnings (the game continues)
    if player["health"] < 30:
        print("WARNING: your health is dangerously low!")
    if player["happiness"] < 20:
        print("You feel really down lately...")
    if player["grades"] < 30:
        print("Your teachers are worried about your grades.")

    # game over conditions (return True to stop the game)
    if player["health"] <= 0:
        print("Your health hit zero. Game over.")
        return True
    if player["happiness"] <= 0:
        print("You gave up on everything. Game over.")
        return True
    if player["grades"] <= 0:
        print("You got expelled. Game over.")
        return True

    return False


def intro():
    print('''Welcome, this is a simple life simulator game where you will be choosing your own destiny. To play, you simply enter
the number of the choice you see in front of you. For example, if you are presented with choice 1. or choice 2.,
to choose you will simply enter a "1" or a "2" and then press "ENTER".''')
    print("")
    player["name"] = input("What is your name? ")
    print("Hey", player["name"] + ", you are a 14 year old who is just starting high school")


intro()

# every scene in the order it should happen
scenes = [
    school_1.day_1_morning,
    school_1.day_1_lunch,
    school_1.day_2_morning,
    school_1.fight_1,
    school_1.suspension_1,
    school_1.exam_1,
    school_1.exam_2,
    school_1.report_card,
    school_1.job_1,
    school_1.money_spend_1,
    school_1.crush_1,
    school_1.random_event_1,
    school_1.prom_1,
    school_1.prom_2,
]

for scene in scenes:
    scene()
    print("\n")
    show_stats()
    if check_stats():
        break
print("The end for now. Thanks for playing!")
print(crush["affection"])