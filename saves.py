import json
import os
from data import player, crush, popular_friends, sports

#fixed place
SAVE_FILE = os.path.join(os.path.expanduser("~"), "life_sim_save.json")

def save_game(next_scene):
    data = {
        "player": player,
        "crush": crush,
        "popular_friends": popular_friends,
        "sports": sports,
        "next_scene": next_scene,
    }
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("(Game saved.)")
    except (OSError, TypeError) as error:
        print("(Could not save your game:" , error, ")")

def has_save():
    return os.path.exists(SAVE_FILE)

def load_game():
    try:
        with open(SAVE_FILE) as f:
            data = json.load(f)
        saved_player = data["player"]
        saved_crush = data["crush"]
        saved_friends = data["popular_friends"]
        saved_sports = data["sports"]
        next_scene = data["next_scene"]
    except (OSError, ValueError, KeyError):
        return None

    player.update(saved_player)
    crush.update(saved_crush)
    popular_friends.update(saved_friends)
    sports.update(saved_sports)
    return next_scene

def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)