num1 = int(input("첫번째 숫자 : "))
num2 = int(input("두번째 숫자 : "))

# :2d -> 출력할 때 끝자리를 맞춰줌(들여쓰기를 해준다?)
print(f"첫번째 숫자는 {num1:2d}")
print(f"두번째 숫자는 {num2:2d}")

# :02d -> 3 입력 시 '03'으로 출력됨.
print(f"첫번째 숫자는 {num1:02d}")
print(f"두번째 숫자는 {num2:02d}")

# 천의 자리수마다 , 추가.
price = 1000000000
print(f"{price:,d}원")