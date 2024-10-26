import random

TASK = "What number is missing in the progression?"

def geometric_progression():
    length = random.randint(5, 10)
    first_element = random.randint(1, 10)
    ratio = random.randint(2, 5)
    
    return [first_element * (ratio ** i) for i in range(length)]

def game():
    progression = geometric_progression()
    hidden_element_index = random.randint(0, len(progression) - 1)
    
    correct_answer = progression[hidden_element_index]

    progression[hidden_element_index] = ".."

    question = ' '.join(map(str, progression))
    
    return question, correct_answer
