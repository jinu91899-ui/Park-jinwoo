class Student:
    def __init__(self,수학):
        self.수학 = 수학
class StudentList:
    def __init__(self):
        self.__리스트 = []

    def append(self, 요소):
        if type(요소) != Student:
            raise TypeError("Student를 전달해주세요.")
        self.__리스트.append(요소)

    def sum(self):
        output = 0
        for 학생 in self.__리스트:
            output += 학생.수학
        return output

    def average(self):
        return self.sum() / len(self.__리스트)


학생목록 = StudentList()
학생목록.append(Student(100))
학생목록.append(Student(80))
학생목록.append(Student(70))
print(학생목록.sum())
print(학생목록.average())