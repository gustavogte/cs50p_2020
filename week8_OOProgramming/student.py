class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print((student))
    print(type(student))

def get_student():
    student = Student()                 # create an object(or instance) student from the class Student
    student.name = input("Name: ")      # with objects are calles attributes or instance variables
    student.house = input("House: ")    # with objects are calles attributes or instance variables
    return student


if __name__ == "__main__":
    main()
