class CmLength:
    def __init__(self, cm):
        if cm < 0:
            raise ValueError("길이는 0 이상으로 지정해야 합니다.")
        self.length = cm

    def get(self):
        return self.length

    def __add__(self, 다른대상):
        if not isinstance(다른대상, CmLength):
            raise TypeError("길이 단위를 통일해주세요!")
        return CmLength(self.get() + 다른대상.get())

result = CmLength(3) + CmLength(10)
print(result.length)