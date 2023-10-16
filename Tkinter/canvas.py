from tkinter import Canvas,Tk
top=Tk()
canvas=Canvas(top,width=300,height=200)
canvas.create_rectangle(50,50,150,150,fill="red")
canvas.pack()
top.mainloop()