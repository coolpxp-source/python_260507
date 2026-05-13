from tkinter import *
window = Tk()
window.geometry("300x300")
# bg = background color / fg = font color
Button(window, text="클릭!", bg="yellow", fg="blue", width=80, height=3).pack()
Entry(window, text="클릭!", bg="yellow", fg="blue", width=80).pack()
window.mainloop()

