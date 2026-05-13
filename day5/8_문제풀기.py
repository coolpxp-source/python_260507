from tkinter import *

def login() :
    print("로그인 성공!")

window = Tk()
window.title("첫번째 프로그램!") #타이틀 설정
f = Frame(window)
window.geometry("300x300")
label = Label(f, text="아아디 : ").grid(row=0, column=0, padx=10)
Entry(f , fg="black", width=20).grid(row=0, column=1)
label = Label(f, text="비밀번호 : ").grid(row=1, column=0)
Entry(f , fg="black", width=20, show="*").grid(row=1, column=1)
Button(f, text="로그인", command=login , bg="yellow").grid(row=3, column=1, pady=10) # pady = 위 아래 간격을 10

# pady / padx로 여백을 줄 수 있다.

f.pack()
window.mainloop()
