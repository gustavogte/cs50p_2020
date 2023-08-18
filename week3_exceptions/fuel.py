# prompt user for a fraction formatted as "X/Y" where X and Y are integers
# output the % rounded to the nearst integer
# 1% or less => E, 99% or more ==> F

def main():
    tank = get_tank()
    if tank > 1:
        get_tank()
    elif tank <= .01:
        print("E")
    elif tank >= 0.99:
         print("F")
    else:
        print(f"{int(tank*100)}%")


def get_tank():
    while True:
        try:
            t = input("X/Y = ")
            t = t.split(sep="/")
            x = int(t[0])
            y = int(t[1])
            t = round( x / y, 2)
            if t > 1:
                True
            else:
                return t
        except (ValueError, ZeroDivisionError, IndexError):
            True

main()


