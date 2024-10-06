from lr.src.cli import greet
from lr.src.engine import play_game
from lr.src.games import nokGame, progressionGame

def main():
    name = greet()

    print("Let's start with the NOK game!")
    play_game(nokGame, name)

    print("Now, let's try the Progression game!")
    play_game(progressionGame, name)

if __name__ == "__main__":
    main()
