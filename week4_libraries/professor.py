import random
# Promt user for a Level [1, 2, 3]


def main():
    level = get_level()
    score = 10
    for i in range(10):
        x, y = get_numbers(level)
        result = round(x, y)
        if result is False:
            score -= 1
    print(f"Score = {score}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            pass


# Random generate 10 math problems like x + y =

def generate_integer(level):
    if level == 1:
        x = int(random.randint(0, 9))
    elif level == 2:
        x = int(random.randint(10, 99))
    else:
        x = int(random.randint(100, 999))
    return x

def get_numbers(level):
    x = generate_integer(level)
    y = generate_integer(level)
    return x, y

def round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


if __name__ == "__main__":
    main()
