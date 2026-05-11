# 함수를 만드는 키워드 : def
# 함수 정의 1. 기본 함수
def default_func() :
    print("파라미터 없음, 리턴 없는 함수")

# 2. 파라미터가 있는 함수
def param_func(x):
    print(f"전달 받은 값 : {x}")

# 3. 리턴이 있는 함수
def return_func(x,y) :
    return x+y

# 4. 리턴이 여러 개인 함수
def return_func2(x,y):
    return x+1, y-1

# 함수 호출 할 때는 ()를 붙인다.
default_func()
param_func(10)
num = return_func(100,200) # 출력하기 위해서 다른 곳에 담기 or 바로 print문 사용 
print(f"리턴이 있는 함수 : {num}")

a,b = return_func2(10,10)
print(f"a : {a}, b : {b}")