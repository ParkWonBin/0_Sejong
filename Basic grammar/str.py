from tkinter import *

window=Tk()

window.title("pyton project")
window.geometry("640x400+100+100")
window.resizable(False, False)

label1 =Label(window,text='123') 
label1.pack()


btnUP = Button(window, width=10, text="UP", overrelief="sol")
btnUP.pack()
btnDOWN = Button(window, width=10, text="DOWN", overrelief="sol")
btnDOWN.pack()
btn5 = Button(window, width=10, text="5", overrelief="sol")
btn5.pack()

window.mainloop()