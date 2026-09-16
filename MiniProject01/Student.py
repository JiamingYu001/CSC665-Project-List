from Person import Person

class Student(Person):
    def __init__(self, person, student_id, major):
        super().__init__(
            person.first_name,
            person.last_name,
            person.age,
            person.address)
        self.student_id = student_id
        self.major = major

    def get_details(self, include_student_id_and_major: bool = True):
        previous = super().get_details()
        if include_student_id_and_major:
            return f'{previous}, student id:{self.student_id}, major:{self.major}'
        return previous

    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_major(self, major):
        self.major = major

    def get_student_id(self):
        return self.student_id

    def get_major(self):
        return self.major