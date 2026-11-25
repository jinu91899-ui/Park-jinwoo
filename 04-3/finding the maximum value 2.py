a=[]
for c in range(1,99+1):
    b=100-c
    a.append([c,b,c*b])
최대리스트=a[0]
현재최댓값=최대리스트[2]
for c in a:
    if 현재최댓값<c[2]:
        최대리스트=c
        현재최댓값=최대리스트[2]
print(최대리스트)