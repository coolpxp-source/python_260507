# 입력한 숫자의 구구단을 출력
# ex) 3입력 시 3단 출력

# i = int(input("숫자를 입력하세요 : ")) #단수

# for a in range(1,10) : # a : 1~9
#     print(f"{i}단")
#     print(f"{i} * {a} = {i*a}")
    
    
# 2~9단까지 모두 출력
for num1 in range(2,10) : # 2~9
    print(f"---{num1}단---")
    for num2 in range(1,10) : # 1~9
        print(f"{num1} * {num2} = {num1*num2}")
    print("----------")
print("수고하셨습니다~")