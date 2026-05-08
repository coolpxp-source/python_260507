import random

# print(random.random())
print(random.randint(1,10)) # randint(a,b) ->a와 b 사이의 숫자가 나옴.

fruits = ["사과", "오렌지", "키위", "리치", "용과", "귤"]
print(random.choice(fruits)) # 1개를 랜덤하게 뽑아줌
print(random.sample(fruits,2)) # 2개를 랜덤하게 뽑아줌

print(f"셔플 전 => {fruits}")
random.shuffle(fruits) # 리스트 순서를 랜덤하게 섞음
print(f"셔플 후 => {fruits}")