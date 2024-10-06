import random

GAME_DESCRIPTION = "What number is missing in the progression?"

def generate_geometric_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    
    return [start * (ratio ** i) for i in range(length)]

def get_question_and_answer():
    progression = generate_geometric_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = ' '.join(map(str, progression))
    
    return question, correct_answer
