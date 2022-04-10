
import os
from tkinter import *
from PIL import ImageTk, Image
import cv2
from datetime import time
from cvvideo import VideoCapture

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
            sign_label.image = current_img #handle python garbage collector


    """
    video stream 
    """
    def update_screen():
        success, new_frame = vc.get_frame()
        if success:
            new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2RGB)
            tk_img = ImageTk.PhotoImage(Image.fromarray(new_frame).resize((700, 600), Image.Resampling.LANCZOS))
            screen_label.configure(image=tk_img)
            screen_label.image = tk_img
        root.after(15, update_screen)

    """
    snapshot function
    """
    def snapshot():
        success, frame = vc.get_frame()
        if success:
            cv2.imwrite("photo" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))



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


    #creating a button to take the snapshot of the live feed

    snap_button = Button(l_frame, text='snap', bg="black", fg="white",height=5, command=snapshot)
    picture_button = Button(r_frame, text="Next Sign",
                         bg="gray", fg="white", height=7,
                         command=next_img)





    #create Label to represent where the "sign to sign" will go

    img = ImageTk.PhotoImage(Image.open('Images/dog.jpeg').resize((200, 270), Image.Resampling.LANCZOS))
    sign_label = Label(r_frame, image=img)


    #pack everything, i.e. display it in the window according to layout rules (fill, expand, etc)

    screen_label.pack(fill=BOTH, expand=True)
    sign_label.pack(fill=BOTH, expand=True)
    snap_button.pack(fill=X)
    picture_button.pack(fill=X)

    vc = VideoCapture()

    update_screen()

    root.mainloop()


main()
