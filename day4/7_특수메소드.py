class Point :
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __eq__(self, other): # 특수연산자
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return Point(self.x + other.x , self.y + other.y)
        # 새로운 point 객체를 생성
    
p1 =Point(2,3)
p2 =Point(2,3)
# p1 = p2 =>서로 다른 객체! false!!
print(p1 == p2) # ==를 사용하면 특수연산자 __eq__이 호출되어서 p1 = p2가 true로 나옴!

p3 = p1+p2
print(p3.x)