class Shape:
    def __init__(self):
        raise NotImplementedError("생성자를 구현해주세요.")
    def 넓이(self):
        raise NotImplementedError("넓이 함수를 구현해주세요. 넓이를 리턴하는 함수를 작성해주세요.")
    def 출력보조(self):
        raise NotImplementedError("출력 보조 함수를 구현해주세요. 출력 전 한마디를 입력해주세요.")
    def 출력(self):
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
        self.출력보조()
        print(f"넓이: {self.넓이()}")
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
class Circle(Shape):
    def __init__(self, 반지름):
        self.파이 = 3.14
        self.반지름 = 반지름
    def 출력보조(self):
        print(f"원의 반지름은 {self.반지름}")
    def 넓이(self):
        return (self.반지름 ** 2) * self.파이 
class Square(Shape):
    def __init__(self, 길이):
        self.길이 = 길이
    def 출력보조(self):
        print(f"정사각형 한 변의 길이는 {self.길이}")
    def 넓이(self):
        return (self.길이) ** 2
Square = Square(10)
Square.출력()
circle = Circle(10)
circle.출력()