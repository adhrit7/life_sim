from data import player, crush, popular_friends
import random


#function to verify if they can afford something
#function is major as it is useful everywhere, within school_!.py and future files as well
#plan is to upgrade the function capabilities
def can_afford(cost):
    if player["money"] >= cost:
        return True
    print("You can't afford that right now. Try something else.")
    return False


#show stats after every function
def show_stats():
    print("---Your stats---")
    print("money:", player["money"])
    print("health:", player["health"])
    print("happiness:", player["happiness"])
    print("grades:", player["grades"])
    print("age:", player["age"])

#check stats always
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
    if player["grades"] < 50:
        print("Your teachers are worried about your grades.")

    # game over conditions (return True to stop the game)
    if player["health"] <= 0:
        print("Your health hit zero. Game over.")
        return True
    if player["happiness"] <= 0:
        print("You gave up on everything. Game over.")
        return True
    if player["grades"] <= 30:
        print("You got expelled. Game over.")
        return True

    return False