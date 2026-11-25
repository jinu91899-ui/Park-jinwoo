a=int(input())
for b in range(1,a+1):
    star=""
    for c in range(a-b):
            star+=" "
    for c in range(2*b-1):
        star+="*"
    print(star)