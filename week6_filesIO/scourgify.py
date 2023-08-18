import sys
import csv

def main():
    check_command_line_arg()
    #print(sys.argv[1])
    try:
        students_b = []
        students_a = []
        with open(sys.argv[1]) as file:
            # reader = csv.reader(file)
            # for name, house in reader:
            #     students_b.append({"name": name, "house": house})
            reader = csv.DictReader(file)
            for row in reader:
                students_b.append(row)
            for student in students_b:
                last, first = student["name"].split(",")
                first = first.lstrip()
                # print(f_name, l_name, student["house"])
                student = {"first": first, "last": last, "house":student["house"]}
                # students_a.append({f_name, l_name, student["house"]})
                students_a.append(student)

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first",
                            "last": "last", "house": "house"})
            for row in students_a:
                #writer.writerow({"first": f_name, "last": l_name, "house":student["house"]})
                writer.writerow(row)


        # print(students_b)
        # print(students_a)
        # print(type(students_a))
        # for student in students_a:
        #    print(student["f_name"], student["l_name"], student["house"])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")



def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
     #   sys.exit("Not valid CSV")


if __name__ == "__main__":
    main()
