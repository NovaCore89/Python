import sqlite3
import shutil
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

     
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(350, 200))
        self.master.title("Move TXT files")

        # File source button
        self.browseButton = Button(self.master,text="Select source folder",width=18,height=1,command = lambda: source_path(self))
        self.browseButton.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=S+W)

        # Text box 1
        self.entry1 = tk.Entry(self.master, text='')
        self.entry1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        # File destination button
        self.browseButton2 = Button(self.master,text="Select destination folder",width=18,height=1,command = lambda: dest_path(self))
        self.browseButton2.grid(row=1,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        # text box 2
        self.entry2 = tk.Entry(self.master, text='')
        self.entry2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        # Moves TXT files
        self.moveButton = Button(self.master,text="Move files...",width=12,height=2,command = lambda: move_txt(self))
        self.moveButton.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        # Non functioning close button
        self.closeButton = Button(self.master,text="Close Program",width=12,height=2)
        self.closeButton.grid(row=2,column=3,padx=(20,0),pady=(20,0),sticky=S+E)

# Function for establishing source path
def source_path(self):
    global sourcePath
    sourcePath = filedialog.askdirectory()
    print(sourcePath) # Prints absolute path to text box 1
    self.entry1.delete(0, END)
    self.entry1.insert(0, sourcePath)

# Function for establishing destination path   
def dest_path(self):
    global destPath
    destPath = filedialog.askdirectory()
    print(destPath) # Prints absolute path to text box 2
    self.entry2.delete(0, END)
    self.entry2.insert(0, destPath)

def move_txt(self):
    source = sourcePath
    dest = destPath
    for file in os.listdir(source):
        if file.endswith(".txt"):
            absPath = os.path.join(source, file)
            print(absPath) 
            modification_time = os.path.getmtime(absPath)
            local_time = time.ctime(modification_time)
            print("Last modification time(Local time):", local_time) # Makes time stamp local time format
            newDest = shutil.move(absPath, dest)
            print("New destination path: ", newDest)
            dbUpdate(file, absPath, local_time)

def dbUpdate(file, absPath, local_time):
    conn = sqlite3.connect('drill_123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID  INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_filePath TEXT, \
            col_time     TEXT  \
            )")
        conn.commit()
    conn.close()
    conn = sqlite3.connect('drill_123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_fileName, col_filePath, col_time) values (?,?,?)", (file, absPath, local_time))
        conn.commit()
    conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()