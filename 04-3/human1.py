import random
한글=list("가나다라마바사아자차카타파하")
파일 = open("human2.py", "w", encoding="utf-8")
파일.write("이름,몸무게,키\n")
for i in range(1000):
    이름=random.choice(한글)+random.choice(한글)
    몸무게 = random.randrange(40, 120)
    키=random.randrange(140,200)
    파일.write(f"{이름},{몸무게},{키}\n")
파일.close()

