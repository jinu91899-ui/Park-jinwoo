class 학생:
    def __init__(self, 이름, 국어, 영어, 수학, 과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학

    def sum(self):
        return self.국어 + self.영어 + self.수학 + self.과학

    def average(self):
        return self.sum() / 4


학생들 = [
    학생("진우",90,90,90,90),
    학생("나경",80,80,80,80),
    학생("지환",70,70,70,70)
]

print("이름", "총점", "평균", sep="\t")
for 학생 in 학생들:
    총점 = 학생.sum()
    평균 = 학생.average()
    print(학생.이름, 총점, 평균, sep="\t")