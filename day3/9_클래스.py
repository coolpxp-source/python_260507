class Counter : # 생성자(객체를 만들면 한번 실행 됨.)
    def __init__(self) :
       self.count = 0 # 객체 생성
    def increment(self) :
        self.count += 1
c = Counter() # new 키워드 없이 그냥 선언

print(c.count)
c.increment()
print(c.count)