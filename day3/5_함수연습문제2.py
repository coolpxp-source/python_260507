import random

#3.
# 내가 푼거 .. 
def num_pick(*values):
    max = values[0]
    min = values[0]
    for v in values : 
        if v > max :
            max = v # max에 v를 넣음
        elif v < min :
            min = v
    print(f"가장 큰 값 : {max}, 가장 작은 값 : {min}")

## ------------------------------------------------------
# 이미 만들어져 있는 함수로 출력하기(더 간단.)
def num_pick(*values, option="max"):
    if option == "max" : #최대 최소를 옵션으로 줘서 구분...
        print(max(values))
    elif option == "min" :
        print(min(values))
    else : 
        print("옵션을 다시 확인하세요.")


num_pick(3,7,1,9,4,2,10,19) # 가장 큰 수 출력
num_pick(3,7,1,9,4,2,10,19) # 가장 작은 수 출력


# 4.
def dedupe(*numbers) :
    return list(set(numbers))

num_list= dedupe(1,3,5,2,4,1,2,3) # 중복 제거된 결과(리스트)를 리턴
print(num_list) # [1,3,5,2,4]
print("=====")
# 5.
def union_list(list1, list2, *list3) :
    result = set(list1) | set(list2) | set(list3)
    return list(result)

list1 = [1,4,2,9,10,3]
list2 = [3,5,9,2,8]
print("5번문제")
result = union_list(list1, list2, 3,5,20,9,15,7)
# 결과로 list1, list2. 숫자들(3,5,20,9,15,7)의 중복 없는 결과 리스트 리턴 
print(result)
print("=====")

# 6. 랜덤 숫자 출력
def ran_list(count, start=1, end=50) :
    result = []
    while len(result) < count :
        ran = random.randint(start, end)
        if ran not in result : # result에 없을 때 넣기.
            result.append(ran) # 리스트에 넣기
    return result

print("6번문제")
# 10부터 45까지의 숫자 중 랜덤으로 6개의 숫자를 중복 없이 리스트로 리턴
result1 = ran_list(6, start=10, end=45)
result1.sort()
print(result1)

# 1부터 100까지의 숫자 중 랜덤으로 5개의 숫자를 중복 없이 리스트로 리턴
result2 =ran_list(5, end=100)
result2.sort()
print(result2)

# 1부터 50까지의 숫자 중 랜덤으로 10개의 숫자를 중복 없이 리스트로 리턴
result3 = ran_list(10)
result3.sort()
print(result3)
print("=====")

# 7.
print("7번 문제")
def str_num_sum(number) :
    sum = 0
    for a in str(number) :
        print(a, end = " ") # 없어도 됨, 그냥 예쁘게 하려고 넣었음.
        sum += int(a)
    return sum
    


print(f"(합은 : {str_num_sum(1352)})") # 각 숫자를 한자리씩 구분한 후 더하기
                  # 11
print(f"(합은 : {str_num_sum(209479)})") # 31
print("=====")
