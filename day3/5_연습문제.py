human = {"홍길동" : 170, "김철수" : 185, "김영희" : 165}
#딕셔너리에서 가장 큰 키를 찾아라

print(max(human.values()))

# human["홍길동"]
# human.get("홍길동")
max(human)
name =max(human,key=human.get) # max에 get함수를 쓰면 value 중에서 가장 큰 키값을 호출해준다.??
print(name)

# def test(dict, dict_func) : 
#     print(dict_func("홍길동"))
# test(human,print())