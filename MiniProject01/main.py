# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Person import Person
from Student import Student
from GraduateStudent import GraduateStudent


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    person1 = Person("John", "Doe", 30, "123 Main St")
    print(person1.get_details())

    person2 = Person("Jane", "Smith", 25, "456 Elm St")
    print(person2.get_details())

    Student = Student(person2, "123456", "Computer Science")
    print(Student.get_details())

    GraduateStudent = GraduateStudent(Student, "Master's", "Dr. Smith")
    print(GraduateStudent.get_details())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
