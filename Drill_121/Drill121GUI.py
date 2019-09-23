import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        # Generates basic tkinter GUI window
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(475, 150))
        self.master.title("Check Files") 
    
        # Generates buttons 
        # Button dimensions + Button grid co-ordinates
        self.btn_Browse1 = Button(self.master, text="Browse...", width=12, height=1,)
        self.btn_Browse1.grid(row =0, column=0,padx=(10,0), pady=(30,0), sticky=W)
        self.btn_Browse2 = Button(self.master, text="Browse...", width=12, height=1,)
        self.btn_Browse2.grid(row =1, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btn_Check = Button(self.master, text="Check for files...",width=12, height=2)
        self.btn_Check.grid(row =2, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btn_Check = Button(self.master, text="Check for files...",width=12, height=2)
        self.btn_Check.grid(row =2, column=0,padx=(10,0), pady=(10,0), sticky=W)
        self.btn_Close = Button(self.master, text="Close Program",width=12, height=2)
        self.btn_Close.grid(row =2, column=2, sticky=E)

        # Generates text input fields 
        # Input field dimensions + grid co-ordinates
        self.txt_Box1 = Entry(self.master, text="", font=12, width=30)
        self.txt_Box1.grid(row=0, column=1, columnspan=2,padx=(25,0), pady=(30,0))
        self.txt_Box2 = Entry(self.master, text="", font=12, width=30)
        self.txt_Box2.grid(row=1, column=1, columnspan=2,padx=(25,0), pady=(10,0))




if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
