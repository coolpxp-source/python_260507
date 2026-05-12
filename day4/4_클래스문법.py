class Human : 
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def set_age(self, age) : 
        self.__age =age
    def get_age(self) :
        return self.__age
    def get_name(self) :
        return self.__name
    
hong = Human("홍길동", 30)
kim = Human("김철수", 25)
human = hong

hong.set_age(35)
print(kim.get_age()) # 25

human.set_age(32)
print(hong.get_age()) # 32
print(kim.get_age())

if hong is kim :
    print("hong이랑 kim이랑 같다") # 출력 x
if hong is Human : 
    print("hong이랑 human이랑 같다") # 출력 o
if Human is not kim : 
    print("human이랑 kim이랑 다르다") # 출력 o
    
def change_age(obj, age=1):
    print(obj.get_name(),f"님의 나이를 {age}살 증가 시켰습니다.")
    obj.set_age(obj.get_age()+age)

yu = Human("유재석", 30)
park = Human("박명수", 25)
person = yu

change_age(yu,3)
print(yu.get_age()) # 33
print(person.get_age())