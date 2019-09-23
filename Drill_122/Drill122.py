import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

     
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(350, 150))
        self.master.title("Check files")

        # Browse button with get_path enabled from the askdirectory() function
        self.browseButton = Button(self.master,text="Browse...",width=12,height=1,command = lambda: ask_directory(self))
        self.browseButton.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=S+W)

        # Text box 
        self.entry1 = tk.Entry(self.master, text='')
        self.entry1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        self.ckeckButton = Button(self.master,text="Check for files...",width=12,height=2)
        self.ckeckButton.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=S+W)
        
        self.closeButton = Button(self.master,text="Close Program",width=12,height=2)
        self.closeButton.grid(row=2,column=3,padx=(20,0),pady=(20,0),sticky=S+E)

# Allows user to select file path on their system 
def ask_directory(self):
    global sourcePath
    sourcePath = filedialog.askdirectory()
    print(sourcePath) # prints absolute path to the text box
    self.entry1.delete(0, END)
    self.entry1.insert(0, sourcePath)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()