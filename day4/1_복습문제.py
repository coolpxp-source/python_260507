print("===1번 문제===")
# 1.
def text_join(*args, sep=" ") : # 여러개를 한번에 받기 위해서 *붙이기
    print(sep.join(args)) # join 안에 리스트나 튜플을 넣으면 문자열을 연결해준다.

text_join("apple", "banana", "kiwi", "orange", sep="-")  
# apple-banana-kiwi-orange 출력
text_join("Python", "Java", "C++")  
# Python Java C++ 출력

print("===2번 문제===")
2.
# sort()는 원본에 영향을 준다.
# sorted()는 원본은 그대로 두고 새로운 리스트를 만들어서 반환(return)
num_list = [3, 1, 7, 2, 9]
def list_tool(numbers, mode=""): #None도 가능
    # *numbers로 받으면 ([3, 1, 7, 2, 9],) 처럼 튜플 안에 리스트가 들어가요.
    # 그래서 실제 리스트를 꺼내려면 numbers[0]을 사용합니다.
    if mode == "reverse":
        # 내림차순 , 역순일 때는 [::-1]
        return sorted(num_list, reverse=True)
    elif mode == "sum":
        return sum(num_list)
    else : 
        return sorted(num_list)
        
print(list_tool([3, 1, 7, 2, 9]))
# [1, 2, 3, 7, 9] 출력
print(list_tool([3, 1, 7, 2, 9], mode="reverse"))
# [9, 7, 2, 1, 3] 출력
print(list_tool([3, 1, 7, 2, 9], mode="sum"))
# 22 출력
print(num_list) # sorted로 해서 원본에 영향 없다.


print("===3번 문제===")
# 3. ★
def dict_pick(data, option="max"):
    if option == "min" : 
        target_key= min(data, key=data.get)
    else : 
        target_key= max(data, key=data.get)
    return {target_key: data[target_key]}
    

print(dict_pick({"apple": 3, "banana": 5, "kiwi": 2}))
# {'banana': 5} 출력
print(dict_pick({"apple": 3, "banana": 5, "kiwi": 2}, option="min"))
# {'kiwi': 2} 출력

print("===4번 문제===")
# # 4.
def inventory(school, item, count ):
    # school이라는 딕셔너리 그룹을 선언해서 item을 넣어서 count
    if item in school : 
        school[item] += count
    else : 
        school[item] = count
    print(school) #딕셔너리 출력

items = {"pen": 10, "note": 5}
inventory(items, "pen", 3)  
# {'pen': 13, 'note': 5} 출력
inventory(items, "note", -2)  
# {'pen': 10, 'note': 3} 출력
inventory(items, "colored pencil", 5)  
# {'pen': 10, 'note': 3, 'colored pencil' : 5} 출력
print("=====")

