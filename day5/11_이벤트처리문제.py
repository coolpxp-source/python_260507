from tkinter import *
from tkinter import messagebox 
import random
count = 0
answer = random.randint(1,100) # 정답을1에서100 사이의난수로설정한다
def try_game() :
    global count
    user_input = int(num.get())
    if user_input == answer :
        messagebox.showinfo("성공",f"정답입니다! {count}번 만에 맞췄어요.")
    elif user_input < answer :
        count += 1
        label2['text'] = "더 큽니다."
        label2['fg'] = "red"
    elif user_input > answer :
        count += 1
        label2['text'] = "더 작습니다."
        label2['fg'] = "blue"
    else :
        messagebox.showinfo("숫자만 입력하세요.")
def delect() :
    num.delete(0, END) # 0~끝까지 삭제
        
window = Tk()
f = Frame(window)
window.title("up and down game") #타이틀 설정
window.geometry("500x300")

label = Label(f, text="숫자를 입력 : ").pack(side="left")
num = Entry(f)
num.pack(side="left")
Button(f, text="시도", command=try_game , fg="green").pack(side="left")
Button(f, text="초기화", command=delect , fg="red").pack(side="left")

label2 = Label(f, text="결과 대기 중")
label2.pack(side="left")
f.pack()
window.mainloop()
