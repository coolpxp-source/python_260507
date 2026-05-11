# 사용자로부터 입력받은 문자열(영어, 대소문자 구분 x)에서
# 사용된 문자의 개수 딕셔너리 형태로 저장(공백은 제외)
# good luck => {"g" :1, "o":2, "d" : 1 ....}

# txt = input("문자를 입력하세요 : ").lower()
# word_dic = {}
# # txt = ttzt
# for word in txt :
#     if word == " ":        # 공백 건너뜀
#         continue
#     elif word in word_dic :
#         word_dic[word] += 1
#     else :
#         word_dic[word] = 1
        
# print(word_dic)

txt = input("문자를 입력하세요 : ").replace(" ", "").lower()
word_dic = {}
for word in txt : 
    word_dic[word] = word_dic.get(word, 0)+1 # word가 없으면 0을 넣는?
    
print(word_dic)

# 가장 많이 등장하는 문자와 해당 문자의 개수 출력 / 가장 많은 개수가 중복일 때는 중복인 것도 출력..
max(word_dic)
key_ =max(word_dic,key=word_dic.get) # max에 get함수를 쓰면 value 중에서 가장 큰 키값을 호출해준다.??
if int(key_) >= 2 :
    print(f"{key_} : {word_dic[key_]}")