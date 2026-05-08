# friend = {}
# while True :
#     answer = int(input("(1)친구 등록 (2)검색 (3)종료 : "))
#     if answer == 1 :
#         name = input("name : ")
#         phone = input("phone : ")
#         friend[name]= phone
#         print("등록되었습니다!")
#     elif answer == 2 :
#         name = input("name : ")
#         if name in friend :
#             print(friend[name])
#         else : 
#             print("존재하지 않습니다..")
#         pass
#     elif answer == 3 :
#         print("종료합니다.")
#         break
# print(friend)


# 학생관리 프로그램
# 동명이인 없다고 가정하고 실습
# 이름, 학과, 주소, 전화번호 입력받아서 저장
# 메뉴는 등록, 수정, 삭제, 검색, 종료

# 등록할때는 이미 등록된 이름일 경우 '이미 등록된 학생입니다' 출력
# 수정은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학과, 주소, 전화번호 다시 입력받아서 저장
# 삭제는 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 해당 학생 데이터 삭제
# 검색은 이름으로 검색 후 없으면 '없는 학생' 출력
    # 있으면 학생의 이름, 학과, 주소, 번호 출력 
# 종료는 프로그램 종료

student = {}
while True :
    menu = int(input("(1)등록, (2)수정, (3)삭제, (4)검색, (5)종료 : "))
    if menu == 1 : 
        name = input("name : ")
        dept = input("dept : ")
        addr = input("addr : ")
        phone = input("phone :")
        student[name]={"dept" : dept, "addr" : addr, "phone" : phone}
        print("등록되었습니다!")
    elif menu == 2 :
        print("수정할 학생 이름을 입력하세요")
        name = input("name : ")
        if name in student :
            dept = input("dept : ")
            addr = input("addr : ")
            phone = input("phone :")
            student[name]={"dept" : dept, "addr" : addr, "phone" : phone}
        else :
            print("없는 학생입니다.")
            pass
    elif menu == 3 :
        print("삭제할 학생 이름을 입력하세요")
        name = input("name : ")
        if name in student :
            student.pop(name) # pop : 삭제, clear : 전체 삭제
            print("삭제 되었습니다.")
        else :
            print("없는 학생입니다.")
            pass
    elif menu == 4 :
        print("조회할 학생 이름을 입력하세요")
        name = input("name : ")
        if name in student :
           print(f"dept : {student[name]['dept']}, addr : {student[name]['addr']}, phone : {student[name]['phone']}")
        else :
            print("없는 학생입니다.")
            pass
    elif menu == 5 :
        print("종료합니다.")
        break
    else :
        print("지원하지 않는 기능입니다.")