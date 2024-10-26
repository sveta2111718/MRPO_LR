import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,'lr', 'src'))

from cli import greet
from engine import play_game
from games import nokGame, progressionGame

def main():
    name = greet()
    while True:
        game_choice = int(input("Choose the game:\n1)NOK game\n2)Progression game\n"))
        
        if game_choice == 1:
            print("Let's start with the NOK game!")
            play_game(nokGame, name)
        elif game_choice == 2:
            print("Now, let's try the Progression game!")
            play_game(progressionGame, name)

if __name__ == "__main__":
    main()
