# 1. 숫자를 3개 입력받아서 리스트에 저장한 후 평균을 출력하시오.
num_list = []
num_list.append(int(input("첫번째 숫자 : "))) # 리스트에 숫자 넣기 : append
num_list.append(int(input("두번째 숫자 : ")))
num_list.append(int(input("세번째 숫자 : ")))

# sum_ =num_list[0] + num_list[1] + num_list[2]
# avg = sum_ /len(num_list) # len : 길이

avg = sum(num_list) / len(num_list)
print(f"평균 : {avg}")

# 2. 과일 이름과 가격을 아래와 같이 딕셔너리로 저장한 후 
# 과일이름을 입력받아 해당 과일의 가격을 출력하시오.
# 단, 없는 과일을 입력하면 "판매하지 않는 상품입니다" 출력하시오.

fruit = {"사과": 1000, "바나나": 1500, "딸기": 2000}
name = input("과일 이름을 입력하세요 : ")
if name in fruit : # if in 문법! : list에 순차적으로 접근!
    print(f"fruit[name]원")
else : 
    print("판매하지 않는 상품입니다")

# 3. 학생 2명의 이름과 점수를 각각 입력받아 names 리스트와 scores 리스트에 순서대로 저장하고
# 저장된 리스트를 사용하여 grade라는 딕셔너리를 만드시오
# 조회하고 싶은 학생 이름을 입력받아, 
# 딕셔너리에 이름이 있으면 "OOO 학생의 점수는 XX점입니다."를 출력하고, 
# 없으면 "등록되지 않은 학생입니다."를 출력하시오.
names = []
scores = []

names.append(input("이름을 입력하세요 : "))
scores.append(int(input("점수를 입력하세요 : ")))

names.append(input("이름을 입력하세요 : "))
scores.append(int(input("점수를 입력하세요 : ")))

grade = {
    names[0] : scores[0],
    names[1] : scores[1]
}

name = input("검색할 학생 이름 : ")
if name in grade : 
    print(f"{name}학생의 점수는 {grade[name]}점입니다.")
else : 
    print("등록되지 않은 학생입니다.")