# install inflect module
import inflect

#  prompt the user for names until ctr-d
names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break


# print Adieu, adieu plus the names separated by  ',' and the last with 'and'
# n - 1 => ','  one 'and'
p = inflect.engine()
names = p.join(names)
print(f"Adieu, adieu, to {names}")
