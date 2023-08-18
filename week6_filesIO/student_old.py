# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# Equivalent to anonymous function:  lambda student: student["name"]

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is from {student['home']}")

#print(students) # dict inside of a list

