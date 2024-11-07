from tkinter import *
import tkinter.font as tkFont
root=Tk()
root.title("Calculator")
root.configure(background='black')
root.geometry("312x338")
root.resizable(False,False)

#button click
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#button clear
def btn_clear():
    expression = ""
    input_text.set("")

#button equal
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""

expression=""

input_text=StringVar()

input_frame=Frame(root,width=312,height=50)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,textvariable=input_text,bd=5,justify=RIGHT,font=("arial",18,"bold"),bg="lightgray")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns__frame=Frame(root,width=312,height=272.5,bg="black")
btns__frame.pack()

#first row
clear= Button(btns__frame,font=tkFont.Font(size=20),text="C",cursor="hand2",width=14,height=1,command=lambda:btn_clear(),bg="black",fg="orange").grid(row=0,column=0,columnspan=3)
divide=Button(btns__frame,font=tkFont.Font(size=20),text="/",width=4,height=1,command=lambda:btn_click("/"),bg="black",fg="orange").grid(row=0,column=3)

#second row
seven=Button(btns__frame,font=tkFont.Font(size=20),text="7",width=4,height=1,command=lambda:btn_click("7"),bg="black",fg="orange").grid(row=1,column=0)
eight=Button(btns__frame,font=tkFont.Font(size=20),text="8",width=4,height=1,command=lambda:btn_click("8"),bg="black",fg="orange").grid(row=1,column=1)
nine=Button(btns__frame,font=tkFont.Font(size=20),text="9",width=4,height=1,command=lambda:btn_click("9"),bg="black",fg="orange").grid(row=1,column=2)
minus=Button(btns__frame,font=tkFont.Font(size=20),text="-",width=4,height=1,command=lambda:btn_click("-"),bg="black",fg="orange").grid(row=1,column=3)

#Third row
four=Button(btns__frame,font=tkFont.Font(size=20),text="4",width=4,height=1,command=lambda:btn_click("4"),bg="black",fg="orange").grid(row=2,column=0)
five=Button(btns__frame,font=tkFont.Font(size=20),text="5",width=4,height=1,command=lambda:btn_click("5"),bg="black",fg="orange").grid(row=2,column=1)
six=Button(btns__frame,font=tkFont.Font(size=20),text="6",width=4,height=1,command=lambda:btn_click("6"),bg="black",fg="orange").grid(row=2,column=2)
plus=Button(btns__frame,font=tkFont.Font(size=20),text="+",width=4,height=1,command=lambda:btn_click("+"),bg="black",fg="orange").grid(row=2,column=3)

#Fourth row
one=Button(btns__frame,font=tkFont.Font(size=20),text="1",width=4,height=1,command=lambda:btn_click("1"),bg="black",fg="orange").grid(row=3,column=0)
two=Button(btns__frame,font=tkFont.Font(size=20),text="2",width=4,height=1,command=lambda:btn_click("2"),bg="black",fg="orange").grid(row=3,column=1)
three=Button(btns__frame,font=tkFont.Font(size=20),text="3",width=4,height=1,command=lambda:btn_click("3"),bg="black",fg="orange").grid(row=3,column=2)
multiply=Button(btns__frame,font=tkFont.Font(size=20),text="*",width=4,height=1,command=lambda:btn_click("*"),bg="black",fg="orange").grid(row=3,column=3)

#fifth row
zero=Button(btns__frame,font=tkFont.Font(size=20),text="0",padx=1,width=10,height=1,command=lambda:btn_click("0"),bg="black",fg="orange").grid(row=4,column=0,columnspan=2)
point=Button(btns__frame,font=tkFont.Font(size=20),text=".",width=4,height=1,command=lambda:btn_click("."),bg="black",fg="orange").grid(row=4,column=2)
equal=Button(btns__frame,font=tkFont.Font(size=20),text="=",width=4,height=1,command=lambda:btn_equal(),bg="black",fg="orange").grid(row=4,column=3)

mainloop()