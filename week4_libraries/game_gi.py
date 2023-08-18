# Get Level
import random

while True:
    try:
        level = input("Level: ")
        if level > 0:
            break
    except:
        pass

# Set random number

random_number = random.randint(1, level)

# Get Guess and check
while True:
    try:
        guess = input("Guess: ")
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
         pass
