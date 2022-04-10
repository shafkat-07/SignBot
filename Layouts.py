from tkinter import *

# creating tkinter window

class SignmanLayout:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(1000, 500)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=4)
        self.root.rowconfigure(4, weight=2)

        self.t_frame = Frame(self.root)
        self.t_frame.grid(row=0, column=0, sticky=NSEW)

        self.top_label = Label(self.t_frame, bg="gray", fg="white", text="Sign the letter:", font=("Arial", 20))
        self.top_label.pack(fill=BOTH, expand=1)

        self.m_frame = Frame(self.root)
        self.m_frame.grid(row=1, column=0, rowspan=3, sticky=NSEW)

        self.m_frame.columnconfigure(0, weight=2)
        self.m_frame.columnconfigure(2, weight=1)
        self.m_frame.rowconfigure(0, weight=1)

        self.camera_label = Label(self.m_frame, bg="black")
        self.camera_label.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        self.img_label = Label(self.m_frame)
        self.img_label.grid(row=0, column=2, sticky=NSEW)

        self.b_frame = Frame(self.root)
        self.b_frame.grid(row=4, column=0, rowspan=2, sticky=NSEW)

        self.b_frame.columnconfigure(0, weight=2)
        self.b_frame.columnconfigure(2, weight=1)
        self.b_frame.columnconfigure(3, weight=1)
        self.b_frame.rowconfigure(0, weight=1)

        """
        self.snap_button = Button(self.b_frame, text="Take Snap")
        self.snap_button.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=5, pady=3)

        self.back_button = Button(self.b_frame, bg="gray", fg="white", text="Previous Sign")
        self.back_button.grid(row=0, column=2, sticky=NSEW, padx=5, pady=3)

        self.next_button = Button(self.b_frame, bg="gray", fg="white", text="Next Sign")
        self.next_button.grid(row=0, column=3, sticky=NSEW, padx=5, pady=3)
        """
        #self.root.mainloop()

