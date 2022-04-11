import os
from tkinter import *
from PIL import ImageTk, Image
import cv2
from datetime import time
from cvvideo import VideoCapture
from Layouts import SignmanLayout
import preprocessing
from pyexpat import model
import numpy as np
from keras.models import load_model
import predict
from model import model_gen

img_list = os.listdir("Images")
current_index = 0
displayed_img = img_list[0]

def generator(filename):
     # if model exists, load existing one else save model 
    try: 
        mod = load_model('image_model')
    except OSError:
        x_train, x_test, y_train, y_test = preprocessing.preprocessing()
        # create model 
        mod = model_gen()
        mod.fit(x_train, y_train, batch_size = 512, epochs = 50, verbose = 1, validation_data = (x_test, y_test))
        mod.save('image_model')
    
    prediction = predict.prediction(filename, mod)
    return prediction

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
            layout.img_label.configure(image=current_img)
            layout.img_label.image = current_img #handle python garbage collector



    #video stream

    def update_screen():
        success, new_frame = vc.get_frame()
        if success:
            new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2RGB)
            tk_img = ImageTk.PhotoImage(Image.fromarray(new_frame).resize((600, 400), Image.Resampling.LANCZOS))
            layout.camera_label.configure(image=tk_img)
            layout.camera_label.image = tk_img
        layout.root.after(15, update_screen)


    #snapshot function

    def snapshot():
        success, frame = vc.get_frame()
        if success:
            cv2.imwrite("photo" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            #add code for prediction() ----> outputs image file
            prediction = generator('photo.jpg')
            prediction = chr(prediction + 65) + '-Sign.jpg'
            prediction = displayed_img
            if prediction == displayed_img:
                tl = layout.top_label
                tl.configure(text="Great job!", bg="green", fg="white")
            else:
                tl = layout.top_label
                tl.configure(text="YOU SUCK", bg="red", fg="white")
            tl.after(1500, lambda: tl.configure(text="Sign the letter:", bg="gray", fg="white"))



    def prev_img():
        global current_index
        global displayed_img

        current_index -= 1

        if current_index < 0:
            current_index = len(img_list) - 1

        current_img = os.path.join("Images",img_list[current_index])
        display_img = current_img
        if current_img:
            current_img = Image.open(current_img)
            current_img = ImageTk.PhotoImage(current_img.resize((200, 270), Image.Resampling.LANCZOS))
            layout.img_label.configure(image=current_img)
            layout.img_label.image = current_img #handle python garbage collector





    #establish a window to use

    layout = SignmanLayout()

    snap_button = Button(layout.b_frame, bg="blue", fg="white", text="Take Snap", command=snapshot)
    snap_button.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=5, pady=3)

    back_button = Button(layout.b_frame, bg="black", fg="white", text="Previous Sign", command=prev_img)
    back_button.grid(row=0, column=2, sticky=NSEW, padx=5, pady=3)

    next_button = Button(layout.b_frame, bg="black", fg="white", text="Next Sign", command=next_img)
    next_button.grid(row=0, column=3, sticky=NSEW, padx=5, pady=3)

    vc = VideoCapture()
    update_screen()

    layout.root.mainloop()

main()