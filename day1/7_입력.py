subject = input("좋아하는 프로그래밍 언어를 입력해주세요 : ");
print(subject, "을(를) 좋아합니다!");

# input은 값을 문자열(string)로 인식한다!
a = input("첫번째 숫자 : "); # 10
b = input("두번째 숫자 : "); # 20
print(a+b); # 1020으로 문자를 이어붙인 결과가 나온다.

# int로 계산하기 위해서는 숫자로 전환해야한다.
a = int(input("첫번째 숫자 : "));
b = int(input("두번째 숫자 : "));
print(a+b);