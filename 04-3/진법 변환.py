a=[
    i
    for i in range(1,100+1)
    if f"{i:b}".count("0")==1
]
for i in a:
    print(f"{i}:{i:b}")
print(f"합계:{sum(a)}")