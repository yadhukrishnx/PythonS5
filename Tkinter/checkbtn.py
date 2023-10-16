from tkinter import Tk,Checkbutton,Label
top=Tk()
label=Label(top,text="Select Skills")
checkbutton=Checkbutton(top,text="Python")
checkbutton2=Checkbutton(top,text="Tkinter")
checkbutton.pack()
checkbutton2.pack()
label.pack()
top.mainloop()