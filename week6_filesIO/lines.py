import sys

def main():
    check_command_line_arg()
    try:
        file = open(sys.argv[1], "r")
        lines =  file.readlines()
        # print(lines)

    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        if check_line(line) == False:
            count += 1
    print(count)



def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


def check_command_line_arg():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")



if __name__ == "__main__":
    main()

