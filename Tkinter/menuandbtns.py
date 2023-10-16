from tkinter import Tk,Menu,Menubutton,Label 

top=Tk()

menubutton=Menubutton(top,text="file")
menubutton.menu=Menu(menubutton)
menubutton["menu"]=menubutton.menu
menubutton.menu.add_command(label="open")
menubutton.menu.add_command(label="save")
menubutton.grid()

top.mainloop()