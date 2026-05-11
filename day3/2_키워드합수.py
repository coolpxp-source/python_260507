## 파이썬의 함수는 자바의 오버로딩을 대체하는 방법으로
## 키워드 기반 파라미터를 사용한다.

def java_sum1(x,y):
    print(f"합:{x+y}")
    
def java_sum2(x,y,z):
    print(f"합:{x+y+z}")
    
def keyword_sum(x=0, y=0, z=0) :
    print(f"합 : {x+y+z}")
    
keyword_sum()
keyword_sum(1) # 1
keyword_sum(1,2) # 1+2
keyword_sum(1,2,3) # 1+2+3
keyword_sum(1,z=100) # 1+0+100
keyword_sum(y=1,z=100) # 0+1+100 

# 일반 인자값은 무조건 키워드 인자 앞에 존재.
# keyword_sum(y=1,y=100, 30) 