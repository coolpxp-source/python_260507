num = 10

def test() :
    global num #전역 변수를 변경하기 위해서 선언
    num += 5
    print(num)