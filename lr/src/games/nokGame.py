import random
import math

TASK = "Find the smallest common multiple of given numbers."

def nok2(a, b):
    return abs(a * b) // math.gcd(a, b)

def nok3(a, b, c):
    return nok2(nok2(a, b), c)

def game():
    numbers = [random.randint(1, 100) for i in range(3)]

    correct_answer = nok3(*numbers)

    question = f"{numbers[0]} {numbers[1]} {numbers[2]}"
    
    return question, correct_answer
