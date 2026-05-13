from tkinter import *
window = Tk()
window.geometry("300x300")
# 4. pack
# Button(window, text="버튼", bg="yellow").pack(side="left")
# Button(window, text="버튼2", bg="red").pack(side="left")
# Button(window, text="버튼3", bg="blue").pack(side="left")

# 5. grid
# Button(window, text="버튼", bg="yellow").grid(row=0, column=0)
# Button(window, text="버튼2", bg="red").grid(row=0, column=1)
# Button(window, text="버튼3", bg="blue").grid(row=1, column=0)
# Button(window, text="버튼4", bg="orange").grid(row=1, column=1)

# 6. place
Button(window, text="버튼", bg="yellow").place(x=3, y=50)
Button(window, text="버튼2", bg="red").place(x=20, y=8)
Button(window, text="버튼3", bg="blue").place(x=5, y=10)
Button(window, text="버튼4", bg="orange").place(x=70, y=5)
window.mainloop()
