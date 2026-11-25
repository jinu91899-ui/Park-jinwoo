a=[1,2,3,[4,5],6,7,8,[9,10]]
b=[]
for c in a:
    if type(c)==list:
        for d in c:
            b.append(d)
    else:
        b.append(c)
print(f"{a}를 평탄화하면")
print(f"{b}입니다.")
