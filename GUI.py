from tkinter import*
from tkinter import Button
import tkinter as tk
from matplotlib import image, table
import teenytiny

from matplotlib.pyplot import margins
root = Tk()
root.title('Tiny Scanner App')
# root.iconbitmap('')
root.geometry("1000x800")
# root.configure(background='black')


class Table:

    def __init__(self, frame):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(frame, width=20, fg='black',
                               font=('Arial', 15, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

    def refresh_table(self, frame):
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(frame, width=20, fg='black',
                               font=('Arial', 15, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data

lst = [('TokenName', 'TokenType')]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
# create root window
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
    for i in a:
        lst.append((i, 'test'))
    Table.__init__


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
t = Table(frame1)
canvas = Canvas(root, width=250, height=250)
canvas.grid(row=11, column=2, padx=10, pady=10)
my_image = PhotoImage(file='compilers.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
#printElapsedTime('displayed image')
root.mainloop()
