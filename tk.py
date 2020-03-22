#Simple python GUI with a button to close it
#First import tkinter
from tkinter import * 

#set Tk() as win so we could easly code
win = Tk()

#Give a title for the GUI.
win.title('Hasan pasha')

#Create a command .
def Close():
  #This means to close win window, you could also use exit() instead of destroy().
	win.destroy()

#Create a button to excute the command .
1stBut = Button(win,text="close",command=Close).pack()

#That means that the script will stay running forever, Unless you didn't stop it.
win.mainloop()
