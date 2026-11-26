
def create_student(이름, 국어, 영어, 수학, 과학):
    return {"이름": 이름, "국어": 국어, "영어": 영어, "수학": 수학, "과학": 과학}


def sum_student(학생):
    return 학생["국어"] + 학생["영어"] + 학생["수학"] + 학생["과학"]


def average_student(학생):
    return sum_student(학생) / 4


학생들 = [
    create_student("인성", 87, 88, 98, 95),
    create_student("구름", 92, 98, 97, 98),
    create_student("별이", 76, 96, 95, 90)
]

print("이름", "총점", "평균", sep="\t")
for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"], 총점, 평균, sep="\t")