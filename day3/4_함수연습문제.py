# 1. 문자열 거꾸로 출력하기
# def reverse_func(*values) :
#     for v in values :
#         print(v[::-1], end=" ") # 슬라이스에서 ::-1을 하면 문자열을 거꾸로 출력한다.
    
# reverse_func("java", "python", "html", "css")

# 2.
def num_sum(*values, option="even"):
    sum_1 = 0 # odd, even을 구분해서 sum 변수를 두개 만드는 방법도 있다!
    for v in values :
        if option == "even" and (v % 2) == 0: # 나누기 연산자는 % , / 는 나머지
            sum_1 += v
        elif option == "odd" and (v % 2) != 0:
            sum_1 += v
        else : 
            print("옵션을 다시 확인하세요.")
    print(f"{'짝수' if option == 'even' else '홀수'}의 합 : {sum_1}") 
    

num_sum(1,2,3,4,5,7,1) #짝수의 합 출력
num_sum(1,2,3,4,5,7,1, option ="odd") #홀수의 합 출력

## odd, even을 구분해서 sum 변수를 두개 만드는 방법도 있다!
def num_sum(*values, option="even"):
    even_sum = 0 # odd, even을 구분해서 sum 변수를 두개 만드는 방법도 있다!
    odd_sum = 0
    for v in values :
        if v % 2 == 0: # 나누기 연산자는 % , / 는 나머지
            even_sum += v
        elif v % 2 != 0:
            odd_sum += v
        else : 
            print("옵션을 다시 확인하세요.")
    print(f"짝수의 합 : {even_sum}, 홀수의 합 : {odd_sum}") 
    

num_sum(1,2,3,4,5,7,1) #짝수의 합 출력
num_sum(1,2,3,4,5,7,1, option ="odd") #홀수의 합 출력