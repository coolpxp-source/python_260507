from tkinter import * #필수
window = Tk() #필수
window.title("첫번째 프로그램!") #타이틀 설정
window.geometry("500x500") # 크기를 지정
label=Label(window,text="Hello Python" ) # 1번 인자 : 위치할 컨테이너 , 2번 인자 : 입력할 텍스트
label.pack()
#pack() label을 붙이는  함수


window.mainloop() #필수
# 위의 3줄은 필수!