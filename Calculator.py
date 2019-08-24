import tkinter
from tkinter import *
from tkinter import messagebox

val=""
A=0
operator=""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
def btn_plus_isclicked():
    global A
    global val
    global operator
    A=int(val)
    operator="+"
    val=val+"+"
    data.set(val)

def btn_minus_isclicked():
    global A
    global val
    global operator
    A=int(val)
    operator="-"
    val=val+"-"
    data.set(val)

def btn_mul_isclicked():
    global A
    global val
    global operator
    A=int(val)
    operator="*"
    val=val+"*"
    data.set(val)

def btn_div_isclicked():
    global A
    global val
    global operator

    A=int(val)
    operator="/"
    val=val+"/"
    data.set(val)

def C_isclicked():
    global A
    global val
    global operator
    val=""
    A=0
    operator=""
    data.set(val)

def result():
    global A
    global val
    global operator
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val=str(C)
    elif operator=="-":
        x=int((val2.split("-")[1]))
        C=A-x
        data.set(C)
        val=str(C)
    elif operator=="*":
        x=int((val2.split("*")[1]))
        C=A*x
        data.set(C)
        val=str(C)

    elif operator == "/":

        x = int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("ERROR","Division by 0 not supported")
            A=""
            val=""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)
            val = str(C)


win=Tk()
win.geometry("250x400+300+300")#coordinate
win.resizable(0,0)#cant change size
win.title("CALCULATOR")#title
data=StringVar()
lbl=Label(
    win,
    text="label1",
    textvariable=data,
    font=("Verdana",20),
    anchor=SE,
    bg="#ffffff",
    fg="#000000",
)
lbl.pack(expand=True,fill="both")
#deviding window in frames:
btnrow1=Frame(win,bg="#000000")
btnrow1.pack(expand=True,fill="both",)


btnrow2=Frame(win)
btnrow2.pack(expand=True,fill="both",)


btnrow3=Frame(win)
btnrow3.pack(expand=True,fill="both",)


btnrow4=Frame(win)
btnrow4.pack(expand=True,fill="both",)
#creating button
btn1=Button(
    btnrow1,
    text="1",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2=Button(
    btnrow1,
    text="2",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(
    btnrow1,
    text="3",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT,expand=True,fill="both")

btn4=Button(
    btnrow1,
    text="+",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_plus_isclicked,
)
btn4.pack(side=LEFT,expand=True,fill="both")


btn5=Button(
    btnrow2,
    text="4",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6=Button(
    btnrow2,
    text="5",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn6.pack(side=LEFT,expand=True,fill="both")
btn7=Button(
    btnrow2,
    text="6",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8=Button(
    btnrow2,
    text="-",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_minus_isclicked,
)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9=Button(
    btnrow3,
    text="7",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,
)
btn9.pack(side=LEFT,expand=True,fill="both")

btn10=Button(
    btnrow3,
    text="8",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,
)
btn10.pack(side=LEFT,expand=True,fill="both")
btn11=Button(
    btnrow3,
    text="9",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn11.pack(side=LEFT,expand=True,fill="both")

btn12=Button(
    btnrow3,
    text="*",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_mul_isclicked,
)
btn12.pack(side=LEFT,expand=True,fill="both")


btn13=Button(
    btnrow4,
    text="C",
    font=("Verdana",22),
    bg="orange",
    relief=GROOVE,
    border=0,
    command=C_isclicked,

)
btn13.pack(side=LEFT,expand=True,fill="both")

btn14=Button(
    btnrow4,
    text="0",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked,
)
btn14.pack(side=LEFT,expand=True,fill="both")
btn15=Button(
    btnrow4,
    text="=",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=result,
)
btn15.pack(side=LEFT,expand=True,fill="both")

btn16=Button(
    btnrow4,
    text="/",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_div_isclicked,
)
btn16.pack(side=LEFT,expand=True,fill="both")







win.mainloop()    
       
