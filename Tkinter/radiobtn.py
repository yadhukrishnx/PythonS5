from tkinter import Tk,Button
def click():
    print("Button Clicked . But WHy ! ")
top=Tk()
button=Button(top,text="Click me",command=click)
button.pack()
top.mainloop()