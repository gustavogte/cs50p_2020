# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


def get_house(student):
    return student["house"]


for student in sorted(students, key=get_name, reverse=False):
    print(f"{student['name']} is in {student['house']}")

print(students)  # dict inside of a list
