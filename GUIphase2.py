from cProfile import label
import parse2_copy as parseTree
from tkinter import*
import tkinter as tk
from tkinter import Button 
from PIL import Image,ImageTk
from numpy import size
import teenytiny as teeny
root=Tk()
root.title('Compiler Phase 2')
root.geometry("1000x800")
frame =LabelFrame(root)
frame.grid(row=4,column=2,padx=100,pady=10)
#frame1=LabelFrame(root)
#frame1.grid(row=5,column=2)

l1=Label(frame,text="Welcome to phase 2",font=('Arial',24),padx=100,pady=10).grid(row=2,column=5,padx=100,pady=10)
l2=Label(frame,text="Enter your input here ",font=('Arial',20),fg='red',padx=100,pady=10).grid(row=3,column=5,padx=100,pady=10)
e= Entry(frame,width=50,fg='blue',font=('Arial',20))
e.grid(row=4,column=5,padx=100,pady=10)
def open_first_follow():
    new=Toplevel()
    new.title('parsing table steps')
    new.geometry("1000x1000")
    img2=ImageTk.PhotoImage(Image.open("first&follow.png"))
    panel=Label(new,image=img2)
    panel.photo=img2
    panel.grid(row=2,column=2)
def open_parse_table():
    newlevel=Toplevel()
    newlevel.title('parsing table')
    newlevel.geometry("1200x1200")
    img3=ImageTk.PhotoImage(Image.open("parseTable.png"))
    panel1=Label(newlevel,image=img3)
    panel1.photo=img3
    panel1.grid(row=2,column=2)
def ttttt():
    check=teeny.analizer(e.get(),'scan')
    if check !='Invalid' :   
        parseTree.parserTree(e.get())
    else:
        pass
my_button2 =Button(frame,text="show your parsing table steps",font=('Arial',20),bg='#20B2AA',fg='black',padx=100,pady=10,command=open_first_follow).grid(row=6,column=5,padx=100,pady=10)
my_button3 =Button(frame,text="show your parsing table",bg='#20B2AA',font=('Arial',20),fg='black',padx=100,pady=10,command=open_parse_table).grid(row=7,column=5,padx=100,pady=10)
my_button1 =Button(frame,text="show your parse tree",bg='#20B2AA',font=('Arial',20),fg='black',padx=100,pady=10,command=ttttt).grid(row=8,column=5,padx=100,pady=10)
my_button4 =Button(frame,text="show your Syntax Tree",bg='#20B2AA',font=('Arial',20),fg='black',padx=100,pady=10).grid(row=9,column=5,padx=100,pady=10)
img4=ImageTk.PhotoImage(Image.open("compilers.jpeg"))
panel2=Label(frame,image=img4)
panel2.photo=img4
panel2.grid(row=10,column=5)
def click():
    mylabel=Label(frame,e.get())
    mylabel.grid(row=5,column=5)

       
root.mainloop()
