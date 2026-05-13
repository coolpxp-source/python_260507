from tkinter import *
from tkinter import messagebox 

# 아이디 test / 비밀번호 1234 입력하면 '로그인 성공'
# 아니면 '로그인 실패' 출력
def login() :
    if id.get() == "test" and pwd.get() == "1234" :
        messagebox.showinfo("알림","로그인 성공")
    else :
        id.delete(0, END) # 0~끝까지 삭제
        pwd.delete(0,END)
        messagebox.showinfo("경고","로그인 실패")

window = Tk()
window.title("첫번째 프로그램!") #타이틀 설정
f = Frame(window)
window.geometry("300x300")
label = Label(f, text="아아디 : ").grid(row=0, column=0, padx=10)
id = Entry(f)
id.grid(row=0, column=1)
label = Label(f, text="비밀번호 : ").grid(row=1, column=0)
pwd = Entry(f, show="*")
pwd.grid(row=1, column=1)
Button(f, text="로그인", command=login , bg="yellow").grid(row=3, column=1, pady=10) # pady = 위 아래 간격을 10

# pady / padx로 여백을 줄 수 있다.

f.pack()
window.mainloop()
