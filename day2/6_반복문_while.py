# num_list = [1,3,5,2,4]
# for i in num_list : 
#     print(i, end=" ")

range(5)
# [0,1,2,3,4]
range(1,5)
# [1,2,3,4]
range(1,10,2) # 1부터 시작해서 10까지 + 2개씩 건너뛰어서 출력.
# [1,3,5,7,9]

for i in range(1,5) : 
    print(i, end=" ")
print()

for a in range(1,6) : 
    print('*' *a) # a에 *을 넣고 다음 반복부터 *(a)에 *를 붙여서 *가 하나씩 증가