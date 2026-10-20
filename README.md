# Life Simulator

A text-based life simulator written in Python. You play as a teenager starting high school, and every choice you make changes your stats, your friendships, and what happens next. Will you make friends, bunk class, or get into a fight with the school bully? It's up to you.


## How to play

You play by typing the number of the choice you want and pressing ENTER.

```
It is the first day of school and you enter your classroom. What do you do?
1. Sit next to the popular kid
2. Sit next to a girl you find attractive
> 2
She becomes your first friend!
```

If you type something that isn't a valid choice, the game just asks you again.

## How to run it

You need Python 3 installed. Check with:

```
python3 --version
```

Then download or clone this repo, open a terminal in the project folder, and run:

```
python3 life_sim.py
```

On Windows, use `python life_sim.py` instead.

## Features

- Stats that change with your choices: money, health, happiness, and grades
- Branching scenes where early choices affect later ones (for example, who you befriended on day 1)
- Characters who remember how you treated them
- Scenes with multiple layers of choices, like the school bully fight and the principal's office
- Input checking, so typing nonsense doesn't crash the game

## Project structure

| File | What it does |
|------|--------------|
| `life_sim.py` | The main file. Run this one. Shows stats and runs the scenes in order |
| `data.py` | Stores the shared data: the player's stats and the characters |
| `school_1.py` | The high school scenes, each written as its own function |

Each scene is its own function, so scenes are easy to add, test, and fix without touching the rest of the game.

## Status

This is a work in progress. Planned next:

- More high school scenes
- Random events
- A save and load system
- University and adult life
- Multiple endings
- A UI

## Screenshots

<img width="862" height="797" alt="image" src="https://github.com/user-attachments/assets/f63137f1-3192-4fa8-9454-a7f226daeca4" />


## Credits

Written by Adhrit Sharma
