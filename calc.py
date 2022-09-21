import tkinter
from tkinter import *

root = Tk()
root.title("simple calculator")
root.geometry("450x410+100+200")
root.resizable(False,False)
root.configure(bg="#513C2D")
resultSpace = Label(root,width=37,height=2,text="",font=("arial",20))
resultSpace.pack()

equation = ""
def clear():
	global equation
	equation = ""
	resultSpace.config(text=equation)
	
def show(value):
	global equation
	equation+=value
	resultSpace.config(text=equation)
	
def calculate():
	global equation
	result = ""
	if equation != "":
		try:
			result = eval(equation)
		except:
			result = "error"
			equation = ""
	resultSpace.config(text=result)

Button(root,width=6,height=2,text="C",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=3,y=60)
Button(root,width=6,height=2,text="/",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=115,y=60)
Button(root,width=6,height=2,text="%",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=227,y=60)
Button(root,width=6,height=2,text="*",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=339,y=60)

Button(root,width=6,height=2,text="7",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=3,y=130)
Button(root,width=6,height=2,text="8",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=115,y=130)
Button(root,width=6,height=2,text="9",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=227,y=130)
Button(root,width=6,height=2,text="-",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=339,y=130)


Button(root,width=6,height=2,text="4",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=3,y=200)
Button(root,width=6,height=2,text="5",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=115,y=200)
Button(root,width=6,height=2,text="6",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=227,y=200)
Button(root,width=6,height=2,text="+",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=339,y=200)

Button(root,width=6,height=2,text="1",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=3,y=270)
Button(root,width=6,height=2,text="2",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=115,y=270)
Button(root,width=6,height=2,text="3",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=227,y=270)
Button(root,width=6,height=5,text="=",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=339,y=270)

Button(root,width=15,height=2,text="0",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=3,y=340)
Button(root,width=6,height=2,text=".",font=("arial",20,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=227,y=340)
root.mainloop()
