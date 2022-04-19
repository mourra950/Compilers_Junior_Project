from tkinter import*
from tkinter import Button
import tkinter as tk
from tkinter import ttk
from matplotlib import image, table
import teenytiny

from matplotlib.pyplot import margins
root = Tk()
root.title('Tiny Scanner App')
# root.iconbitmap('')
root.geometry("1000x800")
# root.configure(background='black')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')
        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.grid(row=0, column=0, sticky=tk.NSEW)
        # adding an item
        tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))

        return tree


# take the data
frame = LabelFrame(root)
frame.grid(row=4, column=2, padx=10, pady=10)
my_label1 = Label(frame, text="Welcome to our Tiny Scanner App",
                  font=('Arial', 24)).grid(row=2, column=5)
my_label2 = Label(frame, text="Case 1 : Arithmetic Expressions ", font=(
    'Chaucer', 15), fg='red', padx=10, pady=10).grid(row=3, column=5)
my_label3 = Label(frame, text="kindly enter your input code here ", font=(
    'Chaucer', 15), fg='blue', padx=10, pady=10).grid(row=4, column=5)


def click():
    mylabel = Label(root, text='token chosen :'+e.get())
    mylabel.grid(row=5, column=5)
    a = teenytiny.analizer(e.get())


e = Entry(frame, width=50, fg='red', font=('Chaucer', 20))
e.grid(row=5, column=5)
myBtn1 = Button(frame, text="Tap to scan code", padx=20,
                pady=20, bg='white', fg='black', command=click)
myBtn1.grid(row=7, column=5, padx=10, pady=10)
myBtn2 = Button(frame, text="Tap to Show DFA", padx=20,
                pady=20, bg='white', fg='black')
myBtn2.grid(row=8, column=5, padx=10, pady=10)
my_label3 = Label(frame, text="Regular Expression:((ID|(-)?Num)operator)*(ID|Num))",
                  font=('Chaucer', 15), fg='blue', padx=10, pady=10).grid(row=9, column=5)
my_label3 = Label(frame, text="Tokens Table ", font=(
    'Chaucer', 15), fg='black', padx=10, pady=10).grid(row=10, column=5)
frame1 = LabelFrame(root)
frame1.grid(row=4, column=3)

canvas = Canvas(root, width=250, height=250)
canvas.grid(row=11, column=2, padx=10, pady=10)
my_image = PhotoImage(file='compilers.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
#printElapsedTime('displayed image')
root.mainloop()
