from tkinter import *
import os

get_dir = os.path.dirname(__file__)


class Tela():
    def __init__(self):
        self.root = Tk()
        self.make_img()
        self.root.mainloop()

    def make_img(self):
        self.img_sfs = PhotoImage(file=f'{get_dir}\images\sfs.png')
        Label(self.root, image=self.img_sfs).place(relx=0)
    

Tela()


# from tkinter import *
# import os

# get_dir = os.path.dirname(__file__)


# root = Tk()

# img_sfs = PhotoImage(file=f'{get_dir}\images\sfs.png')
# Label(root, image=img_sfs).place(relx=0)

# mainloop()

