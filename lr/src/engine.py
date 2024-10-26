
def play_game(game, name):

    print(game.TASK)
    
    for i in range(3):
        question, correct_answer = game.game()

        print(f"Question: {question}")

        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
