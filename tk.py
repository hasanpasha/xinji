from tkinter import * 

win = Tk()

win.title('Hasan pasha')

def Close():
  win.destroy()


1stBut = Button(win,text="close",command=Close).pack()


win.mainloop()
