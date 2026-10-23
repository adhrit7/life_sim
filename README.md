# Life Simulator

A text-based life simulator written in Python. You play as a 14-year-old starting high school, and every choice you make changes your stats, your friendships, and what happens next. Make friends, sit alone, or stand up to the school bully. Early choices come back to affect later scenes.

## How to play

Type the number of the choice you want and press ENTER. If you type something that isn't a valid choice, the game asks you again.

```
It is the first day of school and you enter your classroom. What do you do?
1. Sit next to the popular kid
2. Sit next to a girl you find attractive
> 2
She becomes your first friend!
```

## Download (Mac only)

Download `life_sim_mac.zip` from the [Releases page](https://github.com/adhrit7/life_sim/releases), unzip it, then open Terminal in that folder and run:

```
chmod +x life_sim
./life_sim
```

If macOS blocks it, go to System Settings, then Privacy & Security, and click "Open Anyway".

## Run with Python (any system)

You need Python 3 installed. Download or clone this repo, open a terminal in the project folder, and run:

```
python3 life_sim.py
```

On Windows, use `python life_sim.py` instead.

## What's in the game

- **Stats:** money, health, happiness, grades, and age, shown after each scene
- **Friendships that remember you:** whether you met the popular kids or the girl on day 1 changes what you can do at lunch on day 2
- **Branching choices:** some scenes, like the bully fight, have choices inside choices (fight back, then choose how, then explain yourself to the principal)
- **Consequences:** choices change your money, health, happiness, and how much the popular group respects you
- **Input checking:** typing nonsense never crashes the game

## Scenes so far

1. First day of school: who do you sit next to?
2. Lunch: where do you sit? (depends on who you met)
3. The school bully: pay up, walk away, or fight back

## Project structure

| File | What it does |
|------|--------------|
| `life_sim.py` | The main file. Run this one |
| `data.py` | The shared data: player stats and the characters |
| `school_1.py` | The high school scenes, each one its own function |

Each scene is its own function, so new scenes are easy to add and fix without touching the rest of the game.

## Planned

- More high school scenes
- Random events
- Save and load
- University and adult life
- Multiple endings
- A UI

## Screenshot

<img width="864" height="815" alt="image" src="https://github.com/user-attachments/assets/dd5eb082-c198-4d1c-9db8-03cacf957168" />


## Credits

Written by Adhrit Sharma.
