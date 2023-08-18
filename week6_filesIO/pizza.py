import sys
import csv
from tabulate import tabulate


def main():
    check_command_line_arg()
    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            if sys.argv[1] == "regular.csv":
                pizza = "Regular Pizza"
            else:
                pizza = "Sicilian Pizza"
            for row in reader:
                menu.append({pizza: row[pizza], "Small": row["Small"], "Large": row["Large"]})
        print(tabulate(menu, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
