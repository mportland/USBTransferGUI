#       Version         Python 3.6
#
#       Author          Mathew Perrow
#
#       Description:    Pitcher Program for Transferring
#                       files over USB connection
#
import pitcher_main
import pitcher_gui
import shutil
import os,sys, subprocess
from tkinter import messagebox
from tkinter import *
import tkinter as tk

from tkinter import filedialog




def center_window(self, w, h): 
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
                                                                                #Begins transfer and catches user imput error
def begin_transfer(self):
    try:
       get_file(self) 
    except OSError:
        e = sys.exc_info()
        tk.messagebox.showerror('Invalid entry',str(e))

def get_file(self): 
    file = self.txt_filename.get()
    ext = self.txt_fileext.get()
    subprocess.run('USBApplication4.exe %s.%s'%(file, ext))
    print('USBApplication4.exe %s.%s'%(file, ext))
    
def reset(self):                                                                #Clears text boxes 
    self.txt_filename.delete(0,END)
    self.txt_fileext.delete(0,END)

    
def ask_quit(self):
    answer = tk.messagebox.askquestion("Exit program", "Okay to exit application?")
    if answer == 'yes':
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
