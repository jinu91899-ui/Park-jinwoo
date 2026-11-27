class 원:
    def __init__(self, 반지름):
        if 반지름 < 0:
            raise ValueError("반지름은 0 이상이어야 합니다.")    
        self.__반지름 = 반지름
        self.__파이 = 3.14
    def get_반지름(self):
        return self.__반지름
    def set_반지름(self,value):
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = value
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름

    def 넓이(self):
        return self.__파이 * (self.__반지름 ** 2)


circle = 원(10)
circle.set_반지름(20)
print(circle.get_반지름())
print(circle.둘레())
print(circle.넓이())