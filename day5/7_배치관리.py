from tkinter import *
window = Tk()
f = Frame(window)
window.geometry("300x300")
Button(f, text="버튼", bg="yellow").pack(side="left")
Button(f, text="버튼2", bg="red").pack(side="left")
Button(f, text="버튼3", bg="blue").pack(side="left")

label = Label(window, text="버튼 위에 배치!")
label.pack()
f.pack()
# f.place(x=30, y=50)
window.mainloop()
