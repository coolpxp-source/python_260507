# start가 end 숫자가 더 크면 "끝 숫자는 시작 숫자보다 커야합니다." 출력 후
# 두 숫자를 다시 입력 받을 수 있도록
while True :
    start = int(input("시작 숫자 : "))
    end = int(input("끝 숫자 : "))
    if end < start :
        print("끝 숫자는 시작 숫자보다 커야합니다.")
        continue # 조건에 부합하지 않으면 아래 코드 실행하지 않음.
    sum = 0
    for a in range(start, end+1) : 
        sum +=a
    print(f"합: {sum}")
    break
