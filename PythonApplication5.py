from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
t=0
def vajutamine(event):
    if a.get() == "" or b.get() == '' or c.get() == '':
        messagebox.showinfo('Ошибка!','ЗАПОЛНИ ВСЕ ПОЛЯ!')    
    else:
        av = int(a.get())
        bv = int(b.get())
        cv = int(c.get())
        D = (bv)**2 - 4 * av * cv
        if D < 0:
            solution.config(text="Уравнение не имеет корней")
        elif D == 0:
            x = -1 * bv/(2 * av)
            solution.config(text="D="+str(D)+", "+'X='+str(round(x,2)))
        else:
            x1 = (-1 * bv - D ** 0.5)/(2 * av)
            x2 = (-1 * bv + D ** 0.5)/(2 * av)
            solution.config(text="D="+str(D)+", "+'X1='+str(round(x1,2))+", "+'X2='+str(round(x2,2)))
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
        t=0
def graafik():
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
def lahenda():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return flag,D,t

aken=Tk()
aken.title("Квадратные уравнения")
aken.geometry('620x200')

a = StringVar()
a.set('')
b = StringVar()
b.set('')
c = StringVar()
c.set('')

nadpis = Label(aken,text="Решение квадратного уравнения",font=("Arial Bold",20),fg="green")
nadpis.pack(side=TOP)

ka=Entry(aken,width=2,font=("Arial Bold",30),textvariable = a)
kb=Entry(aken,width=2,font=("Arial Bold",30),textvariable = b)
kc=Entry(aken,width=2,font=("Arial Bold",30),textvariable = c)
ka.place(x=0,y=50)
kb.place(x=125,y=50)
kc.place(x=215,y=50)

x2l = Label(aken,text="x**2+",font=("Arial Bold",20),fg="green")
xl = Label(aken,text="x+",font=("Arial Bold",20),fg="green")
Ol = Label(aken,text="=0",font=("Arial Bold",20),fg="green")
x2l.place(x=50,y=50)
xl.place(x=175,y=50)
Ol.place(x=275,y=50)

nupp=Button(aken,text="Решить",height=1,width=7,bg="green",fg="blue", font="Arial 20") #.pack(side=TOP) command=vajutamine()
nupp.place(x=325,y=50)
nupp.bind('<Button-1>',vajutamine)
btn_g=Button(aken,text="График", font="Calibri 26",bg="green",command=graafik)
btn_g.pack(side=LEFT)

solution = Label(aken,width=25,text="Решение",font=("Arial Bold",20),fg="green",bg="yellow")
solution.place(x=30,y=120)


aken.mainloop() 
