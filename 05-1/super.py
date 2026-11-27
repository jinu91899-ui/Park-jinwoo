class 버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다")
        print("버튼을 화면에 출력합니다.")
class 빨간버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 빨간색으로 칠합니다.")
class 파란버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 파란색으로 칠합니다.")
class 초록버튼(버튼):
    def __init__(self):
        super().__init__()
        print("버튼을 초록색으로 칠합니다.")
빨간버튼()
파란버튼()
초록버튼()


