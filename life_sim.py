from data import player, crush, popular_friends, sports
import random
import school_1
import school_2
from helpers import show_stats, check_stats



def intro():
    print('''Welcome, this is a simple life simulator game where you will be choosing your own destiny. To play, you simply enter
the number of the choice you see in front of you. For example, if you are presented with choice 1. or choice 2.,
to choose you will simply enter a "1" or a "2" and then press "ENTER".''')
    print("")
    player["name"] = input("What is your name? ")
    print("Hey", player["name"] + ", you are a 16 year old who is just starting year 11 at a new high school you transferred to.")


intro()

# every scene in the order it should happen
scenes = [
    school_1.day_1_morning,
    school_1.day_1_lunch,
    school_1.day_2_morning,
    school_1.fight_1,
    school_1.party_1,
    school_1.exam_1,
    school_1.exam_2,
    school_1.report_card,
    school_1.job_1,
    school_1.money_spend_1,
    school_1.crush_1,
    school_1.random_event_1,
    school_1.prom_1,
    school_1.prom_2,
    school_1.exam_3,
    school_1.report_card,
    school_2.reset_stats,
    school_2.birthday_1,
    school_2.sports_1,
    school_2.random_event_2,
    school_2.choose_plan,
    school_2.assignment_1,
    school_2.training_1,
    school_2.pop_quiz_1,
    school_2.elections_1,
]

for scene in scenes:
    scene()
    print("\n")
    show_stats()
    if check_stats():
        break
print("\n\nThe end for now. Thank you for playing!")