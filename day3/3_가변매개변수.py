def sum(*num) : # *를 붙이면 여러개의 인자를 한번에 받아서 튜플의 형태로 만들어줌.
    sum = 0 # 빈 변수 선언
    for a in num : # 숫차적으로 접근해서 더하기 (반복문 사용)
        sum += a
    print(sum)

# sum(1,2,3,4,5)
# sum(1,2,3,4,5,6,7,8,9,10)
# num_list = [1,2,3,4,5,6,7,8,9,10]

## 리스트로 반복문
# for a in range(len(num_list)) :
#     sum += num_list[a]

## 튜플로 반복문
# for a in num_list :
#     sum += a

    