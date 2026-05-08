list = [1,5,9,6,7]
list.sort(reverse = False) # 오름차순, default가 false
list.sort(reverse = True) # 내림차순

print("꺼낸 값 => ", list.pop()) # 맨 뒤에 값 : 인자값을 안넣으면 맨 뒤의 값
print(list)
print("꺼낸 값 => ", list.pop(2)) # 2번째 인덱스 값
print(list)