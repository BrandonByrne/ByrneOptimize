from tkinter import *
import tkinter.filedialog
import Optimizations as optimizations
from tkinter.filedialog import askopenfilename
import os

steamFolderPath = 'C:/'
filename = ''
windowOpen = False

root = Tk()

class GUI(Frame):
    def OpenWindow(self):
        global windowOpen
        windowOpen = True
        root.geometry("800x600")
        root.title("ByrneOptimize")
        label1 = Label(root, text="Easily Optimize Steam Games")
        label1.config(font=("Times New Roman,", 32))
        breakLabel = Label(root, text="")
        button1 = Button(root, text="Browse for Games", command=lambda: GUI().FileBrowser())
        button1.config(font=("Times New Roman,", 28))
        breakLabel.pack()
        label1.pack()
        button1.pack()
        root.mainloop()
    def Optimizer(self):
        pass
    def FileBrowser(self):
        global filename
        if windowOpen == True:
            filename = tkinter.filedialog.askopenfilename(initialdir = "{}".format(steamFolderPath))
            print(filename)
            if filename in optimizations.supportedGames:
                print('worked')
                optimizations.Optimizer()
            else:
                print('did not work')
        else:
            pass
