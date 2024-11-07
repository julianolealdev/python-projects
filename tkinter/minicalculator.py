from tkinter import *

def soma():
    sum = nfirst.get() + nsecond.get()
    variable.set(sum)

def subtrair():
    sum = nfirst.get() - nsecond.get()
    variable.set(sum)

def multiplicar():
    sum = nfirst.get() * nsecond.get()
    variable.set(sum)

def divisao():
    sum = nfirst.get() / nsecond.get()
    variable.set(sum)

root=Tk()
root.title("Soma")
root.configure(background='lightgray')
root.geometry("500x500")
root.resizable(False,False)
variable = StringVar()
nfirst = DoubleVar()
nsecond = DoubleVar()

texto=Label(text="Mini calculator",fg="white",bg="blue",font=("Arial","24"),justify=CENTER,height=2)
texto.pack(fill="both",padx=10,pady=5)

label=Label(text="First number:  ",font=("Arial","12"),bg='lightgray')
label.pack(fill="none",padx=10,pady=5)

primnum= Entry(textvariable=nfirst, justify=CENTER)
primnum.pack(fill="none",padx=10,pady=5)

label2=Label(text="Second number: ",font=("Arial","12"),bg='lightgray')
label2.pack(fill="none",padx=10,pady=5)

segnum=Entry(textvariable=nsecond,justify=CENTER)
segnum.pack(fill="none",padx=10,pady=5)

oper1 = Button(text="Sum",fg="white",bg="blue", command=soma)
oper1.pack(fill="none",padx=2,pady=2)

oper2=Button(text="Subtract",fg="white",bg="blue",command=subtrair)
oper2.pack(fill="none",padx=10,pady=5)

oper3=Button(text="Multiply",fg="white",bg="blue",command=multiplicar)
oper3.pack(fill="none",padx=10,pady=5)

oper4=Button(text="Division",fg="white",bg="blue",command=divisao)
oper4.pack(fill="none",padx=10,pady=5)

resultado=Label(text="Result:", font=("Arial","12"),bg='lightgray')
resultado.place(relx=0.05,rely=0.75)

resultadof=Label(textvariable=variable,font=("Arial","12"),bg='lightgray')
resultadof.place(relx=0.45,rely=0.75)

mainloop()