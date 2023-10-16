from tkinter import Listbox,Tk 
top=Tk()
listbox=Listbox(top)
listbox.insert(1,"one")
listbox.insert(2,"Two")
listbox.insert(3,"Three")
listbox.place()
top.mainloop()