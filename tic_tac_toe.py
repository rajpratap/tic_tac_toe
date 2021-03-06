# DEVELOPED BY RAJ PRATAP SINGH

from tkinter import *
from random import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Tic Tac Toe")
root.geometry('350x420')
c=Canvas(root,bg="#797e83")
c.pack(fill=BOTH,expand=1)
lbl=Label(root,text="Choose your player",fg="Red",bg="#797e83",font="Times 16 bold")
lbl.place(x=90,y=2)
lbl1=Label(root,bg="#797e83")
selected=IntVar()
select=IntVar()
rad1=Radiobutton(root,text='O',value=0,variable=selected,bg="#797e83").place(x=100,y=30)
rad2=Radiobutton(root,text='X',value=1,variable=selected,bg="#797e83").place(x=200,y=30)
c.create_line(130,130,130,350,width=3)
c.create_line(210,130,210,350,width=3)
c.create_line(55,200,280,200,width=3)
c.create_line(55,270,280,270,width=3)
def clicked():
    global plr
    global opp
    temp=selected.get()
    if temp==0:
        plr='O'
        opp='X'
    elif temp==1:
        plr='X'
        opp='O'
    lbl1.configure(text="Chosen player is :"+plr)
    enable()
def enable():
    but1.configure(state=NORMAL)
    but2.configure(state=NORMAL)
    but3.configure(state=NORMAL)
    but4.configure(state=NORMAL)
    but5.configure(state=NORMAL)
    but6.configure(state=NORMAL)
    but7.configure(state=NORMAL)
    but8.configure(state=NORMAL)
    but9.configure(state=NORMAL)
r=list(range(0,9))
itr=1
def reset():
    global r
    global itr
    but1.configure(text="")
    but2.configure(text="")
    but3.configure(text="")
    but4.configure(text="")
    but5.configure(text="")
    but6.configure(text="")
    but7.configure(text="")
    but8.configure(text="")
    but9.configure(text="")
    r=list(range(0,9))
    itr=1
def btn(button,a):
    global r
    global itr
    r.remove(a)
    button.configure(text=plr)
    if itr!=5:
        itr+=1
        stm()
    if len(r)==0:
        check_for_win()
def stm():
    global r
    temp=choice(r)
    if temp==0:
        but1.configure(text=opp)
        r.remove(temp)
    elif temp==1:
        but2.configure(text=opp)
        r.remove(temp)
    elif temp==2:
        but3.configure(text=opp)
        r.remove(temp)
    elif temp==3:
        but4.configure(text=opp)
        r.remove(temp)
    elif temp==4:
        but5.configure(text=opp)
        r.remove(temp)
    elif temp==5:
        but6.configure(text=opp)
        r.remove(temp)
    elif temp==6:
        but7.configure(text=opp)
        r.remove(temp)
    elif temp==7:
        but8.configure(text=opp)
        r.remove(temp)
    elif temp==8:
        but9.configure(text=opp)
        r.remove(temp)
def check_for_win():
    if (but1['text']==plr and but2['text']==plr and but3['text']==plr) or \
       (but4['text']==plr and but5['text']==plr and but6['text']==plr) or \
       (but7['text']==plr and but8['text']==plr and but9['text']==plr) or \
       (but1['text']==plr and but4['text']==plr and but7['text']==plr) or \
       (but2['text']==plr and but5['text']==plr and but8['text']==plr) or \
       (but3['text']==plr and but6['text']==plr and but9['text']==plr) or \
       (but1['text']==plr and but5['text']==plr and but9['text']==plr) or \
       (but3['text']==plr and but5['text']==plr and but7['text']==plr):
        tmsg.showinfo("Tic Tac Toe","You won")
    elif (but1['text']==opp and but2['text']==opp and but3['text']==opp) or \
         (but4['text']==opp and but5['text']==opp and but6['text']==opp) or \
         (but7['text']==opp and but8['text']==opp and but9['text']==opp) or \
         (but1['text']==opp and but4['text']==opp and but7['text']==opp) or \
         (but2['text']==opp and but5['text']==opp and but8['text']==opp) or \
         (but3['text']==opp and but6['text']==opp and but9['text']==opp) or \
         (but1['text']==opp and but5['text']==opp and but9['text']==opp) or \
         (but3['text']==opp and but5['text']==opp and but7['text']==opp):
        tmsg.showwarning("Oops!","You lost")
    else:
        tmsg.showinfo("Tic Tac Toe","It's a Tie")
res=Button(root,text="[Reset]",padx=10,font="Times 16 bold",command=reset)
but=Button(root,text='Done',bd=5,padx=50,command=clicked)
but.place(x=100,y=80)
lbl1.place(x=110,y=55)
but1=Button(root,state=DISABLED,bd=0,height=1,width=3,bg="#797e83",font="Times 21 bold",command=lambda:btn(but1,0))
but2=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but2,1))
but3=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but3,2))
but4=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but4,3))
but5=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but5,4))
but6=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but6,5))
but7=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but7,6))
but8=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but8,7))
but9=Button(root,height=1,width=3,state=DISABLED,bd=0,bg="#797e83",font="Times 21 bold",command=lambda:btn(but9,8))
but1.place(x=70,y=140)
but2.place(x=140,y=140)
but3.place(x=220,y=140)
but4.place(x=70,y=210)
but5.place(x=140,y=210)
but6.place(x=220,y=210)
but7.place(x=70,y=280)
but8.place(x=140,y=280)
but9.place(x=220,y=280)
res.place(x=120,y=370)
root.mainloop()
