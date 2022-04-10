
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


img_list = os.listdir("Images")
current_index = 0

def main():


    #defining function to rotate images when button is pressed
    def next_img():
        global current_index
        current_index += 1

        if current_index == len(img_list):
            current_index = 0

        current_img = os.path.join("Images", img_list[current_index])

        if current_img:
            current_img = Image.open(current_img)
            current_img = ImageTk.PhotoImage(current_img.resize((200, 270), Image.Resampling.LANCZOS))
            sign_label.configure(image=current_img)
            sign_label.image = current_img


    #establish a window to use, set its minimum size to 1000x500

    root = Tk()
    root.minsize(1000, 500)


    #adding two frames to split the screen in half, set each to be the size of their half

    l_frame = Frame(root)
    l_frame.pack(expand=True, side=LEFT, fill=BOTH)

    r_frame = Frame(root)
    r_frame.pack(expand=True, side=RIGHT, fill=BOTH)


    #create a Label to represent where the live feed will be

    screen_label = Label(l_frame, text="Screen", bg="green", fg="white", padx=300)


    #creating a button to take the snapshot of the live feed (THOUGHTS?)

    snap_button = Button(r_frame, text="Snapshot Button",
                         bg="gray", fg="white", height=7,
                         command=next_img)


    #create Label to represent where the "sign to sign" will go

    #img = img.resize((100, 100), Image.LANCZOS)
    img = ImageTk.PhotoImage(Image.open('Images/dog.jpeg').resize((200, 270), Image.Resampling.LANCZOS))
    sign_label = Label(r_frame, image=img)


    #pack everything, i.e. display it in the window according to layout rules (fill, expand, etc)

    screen_label.pack(fill=BOTH, expand=True)
    sign_label.pack(fill=BOTH, expand=True)
    snap_button.pack(fill=X)

    root.mainloop()

main()