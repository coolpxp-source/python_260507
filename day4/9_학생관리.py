# 외부 파일에 있는 class 가져다가 사용하기
from student import Student
# from student <- class가 있는 파일 이름. import Student <-가져올 class 이름

def student_add():
    # 학번, 이름, 학과를 입력 받아서
    # studen_dict에 저장
    # 저장 방법은 {"학번" : Student객체}
    stu_no = input("학번 : ")
    name = input("이름 : ")
    dept = input("학과 : ")
    s = Student(stu_no, name, dept)
    student_dict[stu_no] = s
    print(student_dict)

def student_grade_update():
    # 학번 입력 받아서 있으면 => 해당 학생 학번 수정
    # 없으면 '없는 학생 출력 후 메뉴로'
    stu_no = input("수정할 학생의 학번을 입력하세요 : ")
    
    if stu_no in student_dict: 
        print("수정할 정보를 입력하세요.")
        s = student_dict[stu_no] # 딕셔너리에서 해당 학번의 기존 Student 객체를 꺼내는 것
        grade = int(input("학년 입력 : "))
        s.set_stu_grade(grade)
    
        print(student_dict)
    else : 
        print("없는 학생입니다. 메뉴로 이동합니다.")
        
def student_search():
    #학번 입력 받아서 있으면 => 학번, 이름, 학과, 학년 출력
    # 없으면 '없는 학생 출력 후 메뉴로'
    # 필요에 따라 Student 클래스 수정해도 됨.
    stu_no = input("조회할 학생의 학번을 입력하세요 : ")
    
    if stu_no in student_dict:
        s = student_dict[stu_no]
        print(f"학번 : {s.get_stu_no()}")
        print(f"이름 : {s.get_stu_name()}")
        print(f"학과 : {s.get_stu_dept()}")
        print(f"학년 : {s.get_stu_grade()}")
    else : 
        print("없는 학생입니다. 메뉴로 이동합니다.")
        
student_dict = {}

while True : 
    menu = input("[ (1) 학생 추가 (2) 학년 수정 (3)학생 조회 (5) 종료 ] : ")
    if menu == "1" :
        student_add()
    elif menu == "2":
        student_grade_update()
    elif menu == "3":
        student_search()
    elif menu == "4":
        pass
    else :
        print("종료합니다.")
        break



# hong = Student("1234", "홍길동", "컴퓨터")
# print(hong.get_stu_grade())
# test=[]
# test.append(hong)
# print(test)
