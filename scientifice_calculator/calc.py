from tkinter import *

import math
import tkinter.messagebox
root=Tk()
root.geometry("650x400+300+300")
root.title("Scientific calculator")
switch=None

def btn_1():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'1')

def btn_2():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'2')

def btn_3():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'3')

def btn_4():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'4')

def btn_5():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'5')

def btn_6():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'6')

def btn_7():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'7')

def btn_8():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'8')

def btn_9():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'9')

def btn_0():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'0')

def btn_p():
    pos=len(disp.get())
    disp.insert(pos,'+')

def btn_s():
    pos=len(disp.get())
    disp.insert(pos,'-')

def btn_ml():
    pos=len(disp.get())
    disp.insert(pos,'*')

def btn_di():
    pos=len(disp.get())
    disp.insert(pos,'/')


def sin():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def cos():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def tan():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def asin():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.asin(math.radians(ans))
        else:
            ans=math.asin(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def acos():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.acos(math.radians(ans))
        else:
            ans=math.acos(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def atan():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.atan(math.radians(ans))
        else:
            ans=math.atan(ans)
            disp.delete(0,END)
            disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def pow():
    pos=len(disp.get())
    disp.insert(pos,'**')

def dot():
    pos=len(disp.get())
    disp.insert(pos,'.')

def br():
    pos=len(disp.get())
    disp.insert(pos,')')

def bl():
    pos=len(disp.get())
    disp.insert(pos,'(')

def cl():
    disp.delete(0, END)
    disp.insert(0, '0')

    # pos=len(disp.get())
    # disp.insert(pos,"0")


def mo():
    pos=len(disp.get())
    disp.insert(pos,"%")

def eq():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def log():
    try:
        ans=float(disp.get())
        ans=math.log10(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def round():
    try:
        ans=float(disp.get())
        ans=round(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def sqrt():
    try:
        ans=float(disp.get())
        ans=math.sqrt(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def ln():
    try:
        ans=float(disp.get())
        ans=math.log(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def fact():
    try:
        ans=int(float(disp.get()))
        ans=math.factorial(ans)
        disp.delete(0,END)
        disp.insert(0,str(ans))
    except Exception:
        tkinter.messagebox.showerror("value error! check your operator and operator")

def btn_pi():
    if disp.get=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,str(math.pi))

def btn_ex():
    if disp.get=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,str(math.e))

def back():
    pos=len(disp.get())
    display=str(disp.get())
    if display== '':
        disp.insert(0,'0')
    elif display== ' ':
        disp.insert(0,'0')
    elif display=='0':
        pass
    else:
        disp.delete(0,END)
        disp.insert(0,display[0:pos-1])

def conv():
    global switch
    if switch is None:
        switch=True
        conv['text']="Deg"
    else:
        conv['text']="Rad"


disp=Entry(root,font="Verdana 20",fg="Black",bg="mistyrose",bd=4,justify=RIGHT)
disp.insert(0,'0')
disp.pack(expand=TRUE,fill=BOTH)



#Row  1
btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=TRUE,fill=BOTH)
pibtn=Button(btnrow1,text="╥",font="segoe 18",relief=GROOVE,bd=0,command=btn_pi,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
factbtn=Button(btnrow1,text="x!",font="segoe 18",relief=GROOVE,bd=0,command=fact,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
sinbtn=Button(btnrow1,text="sin",font="segoe 18",relief=GROOVE,bd=0,command=sin,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
cosbtn=Button(btnrow1,text="cos",font="segoe 18",relief=GROOVE,bd=0,command=cos,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
tanbtn=Button(btnrow1,text="tan",font="segoe 18",relief=GROOVE,bd=0,command=tan,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn1=Button(btnrow1,text="1",font="segoe 23",relief=GROOVE,bd=0,command=btn_1,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn2=Button(btnrow1,text="2",font="segoe 23",relief=GROOVE,bd=0,command=btn_2,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn3=Button(btnrow1,text="3",font="segoe 23",relief=GROOVE,bd=0,command=btn_3,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btnp=Button(btnrow1,text="+",font="segoe 23",relief=GROOVE,bd=0,command=btn_p,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

#Row 2
btnrow2=Frame(root)
btnrow2.pack(expand=TRUE,fill=BOTH)
e_btn=Button(btnrow2,text="e",font="segoe 18",relief=GROOVE,bd=0,command=btn_ex,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
sqr_btn=Button(btnrow2,text="√x",font="segoe 18",relief=GROOVE,bd=0,command=sqrt,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
sinh_btn=Button(btnrow2,text="sin-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=asin,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
cosh_btn=Button(btnrow2,text="cos-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=acos,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
tanh_btn=Button(btnrow2,text="tan-1",font="segoe 11 bold",relief=GROOVE,bd=0,command=atan,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn4=Button(btnrow2,text="4",font="segoe 23",relief=GROOVE,bd=0,command=btn_4,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn5=Button(btnrow2,text="5",font="segoe 23",relief=GROOVE,bd=0,command=btn_5,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn6=Button(btnrow2,text="6",font="segoe 23",relief=GROOVE,bd=0,command=btn_6,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btnm=Button(btnrow2,text="-",font="segoe 23",relief=GROOVE,bd=0,command=btn_s,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

#Row 3
btnrow3=Frame(root)
btnrow3.pack(expand=TRUE,fill=BOTH)
conv_btn=Button(btnrow3,text="Red",font="segoe 12 bold",relief=GROOVE,bd=0,command=conv,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
round_btn=Button(btnrow3,text="round",font="segoe 10 bold",relief=GROOVE,bd=0,command=round,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
ln_btn=Button(btnrow3,text="ln",font="segoe 18",relief=GROOVE,bd=0,command=ln,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
logarithm_btn=Button(btnrow3,text="log",font="segoe 17",relief=GROOVE,command=log,bd=0,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
pow_btn=Button(btnrow3,text="x^y",font="segoe 17",relief=GROOVE,bd=0,command=pow,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn7=Button(btnrow3,text="7",font="segoe 23",relief=GROOVE,bd=0,command=btn_7,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn8=Button(btnrow3,text="8",font="segoe 23",relief=GROOVE,bd=0,command=btn_8,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn9=Button(btnrow3,text="9",font="segoe 23",relief=GROOVE,bd=0,command=btn_9,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btnml=Button(btnrow3,text="*",font="segoe 23",relief=GROOVE,bd=0,command=btn_ml,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)

#Row 4
btnrow4=Frame(root)
btnrow4.pack(expand=TRUE,fill=BOTH)
mod_btn=Button(btnrow4,text="%",font="segoe 21",relief=GROOVE,bd=0,command=mo,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
bl_btn=Button(btnrow4,text="(",font="segoe 21",relief=GROOVE,bd=0,command=bl,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
br_btn=Button(btnrow4,text=")",font="segoe 21 ",relief=GROOVE,bd=0,command=br,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
dot_btn=Button(btnrow4,text="•",font="segoe 21",relief=GROOVE,bd=0,command=dot,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btnc=Button(btnrow4,text="C",font="segoe 23 ",relief=GROOVE,bd=0,command=cl,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
del_btn=Button(btnrow4,text="⌫",font="segoe 20",relief=GROOVE,bd=0,command=back,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn0=Button(btnrow4,text="0",font="segoe 23",relief=GROOVE,bd=0,command=btn_0,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btneq=Button(btnrow4,text="=",font="segoe 23",relief=GROOVE,bd=0,command=eq,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)
btnd=Button(btnrow4,text="/",font="segoe 23",relief=GROOVE,bd=0,command=btn_di,fg="white",bg="#333333").pack(side=LEFT,expand=TRUE,fill=BOTH)



root.mainloop()