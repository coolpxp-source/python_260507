import random
while True :
    q = int(input("풀고 싶은 문제 수를 입력하세요. (2~5개) : "))
    if 1 < q < 6 :
        correct = 0
        wrong = 0
        for q_ in range(1,q+1): 
            x = random.randint(2,9) # 2단 ~ 9단
            y = random.randint(1,9) # 1 ~ 9 곱하기
            print(f"[{q_}번 문제]")
            print(f"{x} * {y} = ?")
            a = int(input("정답 입력 : "))
            
            if a != x*y : 
                print(f"틀렸습니다. 정답은 {x*y}입니다.")
                wrong +=1
            else :
                print("정답입니다!")
                correct +=1
        print("-" * 30)
        print(f"결과 발표: 맞춘 개수: {correct}, 틀린 개수: {wrong}")
        print("-" * 30)
        
        retry = input("다시 하시겠습니까? (y/n): ").lower()
        if retry != 'y':
            print("종료합니다.")
            break
    else :
        print("2~5사이의 숫자만 입력 가능합니다.")
        
       