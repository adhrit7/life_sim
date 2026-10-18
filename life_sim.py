from data import player, crush, popular_friends
import random
import school_1
#all the libraries and list things

def show_stats():
    print("---Your stats---")
    print("money:", player["money"])
    print("health:", player["health"])
    print("happiness:", player["happiness"])
    print("grades:", player["grades"])
    print("age:", player["age"])

show_stats()



print('''Welcome, this is a simple life simulator game where you will be choosing your own destiny.To play, you simply enter
        the number of the choice you see in front of you. For example, if you are presented with choice 1. or choice 2. ,
        to choose you will simply enter a "1" or a "2" and then click "ENTER" ''')

def intro():
    player["name"]= input("What is your name? ")
    print("Hey", player["name"], " ,you are a 14 year old who is just starting high school")

intro()


school_1.day_1_morning()
school_1.day_1_lunch()
school_1.day_2_morning()
show_stats()