class Counter : # 생성자(객체를 만들면 한번 실행 됨.)
    def __init__(self, v=0) :
       self.count = v # 객체 생성
    def increment(self) :
        self.count += 1
        
c1 = Counter(); print(c1.count)
c2 = Counter(100); print(c2.count)