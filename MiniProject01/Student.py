# This class is written by Jiaming Yu

from Person import Person

class Student(Person):
    def __init__(self, person, student_id, major):
        super().__init__(
            person.first_name,
            person.last_name,
            person.age,
            person.address)
        if (not isinstance(student_id, int)
                or not isinstance(major, str) or not major.strip()):
            raise ValueError('Student id and major cannot be empty or invalid values')
        self.student_id = student_id
        self.major = major

    def get_details(self, include_student_id_and_major: bool = True):
        previous = super().get_details()
        if include_student_id_and_major:
            return f'{previous}, student id:{self.student_id}, major:{self.major}'
        return previous

    def set_student_id(self, student_id):
        if not isinstance(student_id, int):
            raise ValueError('Student id cannot empty or invalid values')
        self.student_id = student_id

    def set_major(self, major):
        if not isinstance(major, str) or not major.strip():
            raise ValueError('Major cannot be empty or invalid values')
        self.major = major

    def get_student_id(self):
        return self.student_id

    def get_major(self):
        return self.major