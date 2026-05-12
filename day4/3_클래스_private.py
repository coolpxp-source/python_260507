# 학번, 이름, 학과, 학년
class Student :
    def __init__(self, stu_no, stu_name, stu_dept, stu_grade=1):
        self.__stu_no = stu_no
        self.__stu_name = stu_name
        self.__stu_dept = stu_dept
        self.__stu_grade = stu_grade
        self.set_stu_grade(stu_grade) # 유효성 검사해야함.
        
    def set_stu_grade(self, stu_grade): #메소드는 기본 생성자 __init__랑 같은 레벨에
        if 1 <= stu_grade <= 4 :
            self.__stu_grade = stu_grade
        else : 
            print("학년은 1~4학년 까지만 가능합니다.")
    def get_stu_grade(self) :
        return self.__stu_grade
            
hong = Student("1234", "홍길동","컴퓨터",5)
print(hong.get_stu_grade())
# hong.__stu_grade =2
# print(hong.__stu_grade)

hong.__stu_grade =2
print(hong.__dict__)
print(hong.__stu_grade)

#__stu_grade를 기준으로 get, set 메소드 만들기
#grade의 값은 1부터 4까지만 허용. 그외의 값은
#'1~4까지만 가능합니다.' 출력 후 저장은 x
#set_stu_grade, get_stu_grade 등 스네이크 표기법 사용하기.

