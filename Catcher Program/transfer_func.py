#       Version         Python 3.6
#
#       Author          Mathew Perrow
#
#       Description:    Catcher Program for Transferring
#                       files over USB connection
#
import transfer_main
import transfer_gui
import shutil
import os
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
                                                                                #Begins scan and catches user imput error
def begin_transfer(self):
    try:
       get_file(self) 
    except OSError:
        e = sys.exc_info()
        tk.messagebox.showerror('Invalid entry',str(e))
        


def get_file(self):
    file_list = {1:"vid1.mp4",2:"vid2.mp4",3:"vid3.mp4", 4:"vid4.mp4"}     #Need to replace file names in file_list 
    curDir = os.getcwd()
    file = self.v.get()
    os.startfile('USBApplication4.exe %s'%(file_list[file]))                #Need command line protocal here
        
    
       



def ask_quit(self):
    
    answer = tk.messagebox.askquestion("Exit program", "Okay to exit application?")
    if answer == 'yes':
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass
