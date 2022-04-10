from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from tkinter.messagebox import _show
from datetime import datetime

# creating tkinter window
root = Tk()
#root.geometry('200x100 + 300 + 250')

button = Button(root, text='Geeks')
button.pack(side=TOP, pady=5)

def print_now():
    print(datetime.now())

# in after method 5000 milliseconds
# is passed i.e after 5 seconds
# a message will be prompted
print_now()
root.after(5000, print_now)

# Destroying root window after 6.7 seconds
root.after(6700, root.destroy)

mainloop()