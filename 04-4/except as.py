try:
    리스트[0]
except ValueError:
    print("값을 다시 제대로 입력해주세요.")
except ConnectionError:
    print("인터넷 연결에 문제가 있습니다.")
except Exception as e:
    i = input("오류 내용을 전송하시겠습니까? [Y/N]")
    if i in ["Y", "y"]:
        메일보내기(type(e), str(e))