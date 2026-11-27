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
    def __eq__(self, 다른대상):
        print("__eq__()함수 호출")
        return self.sum() == 다른대상.sum()
    def __gt__(self, 다른대상):
        if type(다른대상) == 학생:
            return self.sum() > 다른대상.sum()
        elif type(다른대상) == int:
             return self.sum() > 다른대상
        else:
            raise TypeError("같은 자료형을 비교해주세요")
    def __str__(self):
        return f"{self.이름}\t{self.sum()}\t{self.average()}"
class 학생리스트:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.students:
            student.print()
    def clone(self):
        output = 학생리스트()
        for student in self.students:
            output.add(student)
        return output
    def __add__(self, 다른대상):
        output = self.clone()
        output.add(다른대상)
        return output
    def __str__(self):
        output = "이름\t총점\t평균\n"
        for student in self.students:
            output += f"{str(student)}\n"
        return output
students = 학생리스트()
students += (학생("진우", 90, 90, 90, 90))
students += (학생("나경", 90, 90, 90, 80))
students.add(학생("지환", 90, 90, 90, 90))
a = 학생("진우", 90, 90, 90, 90)
b = 학생("나경", 90, 90, 90, 80)
print(a==a)
print(b==a)
print(a > b)
print(학생("진우", 90, 90, 90, 90))
print(students)