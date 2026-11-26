def 함수(파일이름):
    try:
        파일 = open(파일이름, "r")
        내용 = 파일.read()
        try:
            숫자 = int(내용)
            return 숫자
        except:
            print("숫자로 변환할 수 없는 파일입니다.")
        finally:
            파일.close()
    except:
        print("존재하지 않는 파일입니다.")


파일이름 = input("파일 이름> ")
print(함수(파일이름))