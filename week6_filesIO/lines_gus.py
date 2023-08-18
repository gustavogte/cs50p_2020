import sys

# print(sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Two few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Two many command-line arguments")
elif len(sys.argv) == 2:
    try:
        if sys.argv[1].split(".")[1] != "py":
            sys.exit("Not a Python file")
    except:
        sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        i = 0
        for line in file:
            if line.lstrip().startswith("#") == False and len(line) > 1 :
                i += 1
        #    print(len(line), line, end="")
        #print()
        print(i)

except FileNotFoundError:
    sys.exit("File does not exist")
