import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open ("students.csv", "a") as file: # a => append mode not overwrite
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
