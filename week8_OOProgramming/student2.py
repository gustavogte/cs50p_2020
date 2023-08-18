class Student:
    def __init__(self, name, house):     # __init__ ==> initialize method => instance
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    # Getter (always one value)
    @property
    def house(self):
        return self._house

    # Setter (always need an other value)
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # constructor code or intance code


if __name__ == "__main__":
    main()
