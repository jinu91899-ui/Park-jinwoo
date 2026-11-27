class 학생:
    def __init__(self,이름,국어,영어,수학,과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학

    def sum(self):
        return self.국어 + self.영어 + self.수학 + self.과학

    def average(self):
        return self.sum() / 4

    def print(self):
        print(self.이름, self.sum(), self.average(), sep="\t")


class 학생리스트:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
            student.print()


students = 학생리스트()
students.add(학생("진우", 90, 90, 90, 90))
students.add(학생("나경", 90, 90, 90, 90))
students.add(학생("지환", 90, 90, 90, 90))

students.print()