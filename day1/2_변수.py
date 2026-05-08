age = 20;
name = "홍길동";
height = 170.5;
hobbyList = ['게임','운동','코딩']

print("이름 : " + name, end="\n"); #  end="\n" <-\n은 디폴트(줄바꿈)라서 생략 가능!, 프린터문 끝나고 이걸 실행하겠다.
# end의 디폴트는 \n(줄바꿈)
print("나이 : " , age);  #print("이름 : ", name); +대신 ,도 허용
# sep 구분자 -> 변수 사이사이를 구분한다.
print(name, age, height, sep=" / ");