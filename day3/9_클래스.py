class Counter : # 생성자(객체를 만들면 한번 실행 됨.)
    def __init__(self) :
       self.count = 0 # 객체 생성
    def increment(self) :
        self.count += 1
c = Counter()

print(c.count)
c.increment()
print(c.count)