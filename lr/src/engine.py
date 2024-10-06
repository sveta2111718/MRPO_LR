MAX_ROUNDS = 3

def play_game(game, name):
    """
    Общий движок для всех игр.
    :param game: Модуль игры
    :param name: Имя игрока
    """
    print(game.GAME_DESCRIPTION)
    
    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.get_question_and_answer()

        print(f"Question: {question}")

        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
