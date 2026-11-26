def isfloat(입력):
    try:
        float(입력)
        return True
    except:
        return False


입력리스트 = ["52", "273", "32.1", "103", "숫자로변환할수없는문자열"]
출력리스트 = []

for 요소 in 입력리스트:
    if isfloat(요소):
        출력리스트.append(float(요소))

print(출력리스트)