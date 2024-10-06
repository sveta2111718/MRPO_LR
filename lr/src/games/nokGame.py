import random
import math

GAME_DESCRIPTION = "Find the smallest common multiple of given numbers."

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)

def get_question_and_answer():
    numbers = [random.randint(1, 100) for _ in range(3)]

    correct_answer = lcm_of_three(*numbers)

    question = f"{numbers[0]} {numbers[1]} {numbers[2]}"
    
    return question, correct_answer
