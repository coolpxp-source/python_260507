# 1. Math class 완성하기
class Math :
    def __init__(self): #기본생성자
        print("Math 클래스 객체를 생성했습니다")
    def math_sum(self,*numbers, option=""):
        num_sum = 0
        odd_sum = 0
        even_sum = 0
        for n in numbers :
            if n % 2 == 0 :
               even_sum += n
            elif n % 2 == 1 :
                odd_sum += n
            num_sum += n # 전부다 더하는 거라 if문 사용하지 않음.
                
        if option == "even": # 반복문 바깥에서
            return even_sum
        elif option == "odd":
            return odd_sum
        else:
            return num_sum
    def math_max_min(self,*numbers, option="max") :
        if option == "min" :
            return min(numbers)
        else :
            return max(numbers)

m = Math() # 'Math 클래스 객체를 생성했습니다.' 출력
print(m.math_sum(1,5,2,9,3,2,6)) # 모든 숫자의 합 출력
print(m.math_sum(1,5,2,9,3,2,6,8,7, option="odd")) # 홀수의 합 출력
print(m.math_sum(1,5,2,9,3,8, option="even")) # 짝수의 합 출력

print(m.math_max_min(1,5,2,9,3,2,6)) # 가장 큰 숫자 출력
print(m.math_max_min(1,5,2,9,3,2,6, option="min")) # 가장 작은 숫자 출력

# 2.Student class 완성하기

class Student :
    def __init__(self, stu_no, stu_name, age, addr) : 
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__age = age
        self.__addr =addr
        
    def __eq__(self, other) :
        return self.__stu_no == other.get_stu_no()
    
    def get_stu_no(self):
        return self.__stu_no
    def get_stu_name(self):
        return self.__stu_name
    def get_age(self):
        return self.__age
    def get_addr(self):
        return self.__addr
            

s1 = Student("1234", "홍길동", 30, "인천") # 학번, 이름, 나이, 주소
s2 = Student("2341", "김철수", 25, "서울") 
s3 = Student("1234", "박영희", 28, "제주도")

print(f"{s1.get_stu_name()}의 학번은 {s1.get_stu_no()} 입니다.") # '홍길동의 학번은 1234 입니다' 출력
print(s1 == s2) # False
print(s1 == s3) # True (각 객체의 학번이 같으면 True가 나오도록)