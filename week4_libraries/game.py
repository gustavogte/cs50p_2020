import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1 and str(level).isnumeric() and level <= 100:
            break
    except ValueError:
        pass

number = random.randint(1, level)
# print(number)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too Small!")
        elif guess > number:
            print("Too Large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
