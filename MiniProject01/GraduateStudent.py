from Student import Student

class GraduateStudent(Student):
    def __init__(self, student, degreeProgram, advisor):
        super().__init__(
            student,
            student.major,
            student.student_id)
        self.degreeProgram = degreeProgram
        self.advisor = advisor

    def get_details(self, include_degreeProgram_and_advisor: bool = True):
        previous = super().get_details()
        if include_degreeProgram_and_advisor:
            return f'{previous}, degree program:{self.degreeProgram}, advisor:{self.advisor}'
        return previous

    def set_degreeProgram(self, degreeProgram):
        self.degreeProgram = degreeProgram

    def set_advisor(self, advisor):
        self.advisor = advisor

    def get_degreeProgram(self):
        return self.degreeProgram

    def get_advisor(self):
        return self.advisor