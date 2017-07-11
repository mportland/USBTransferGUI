#       Author: Mathew Perrow
#
#       Version:Python 3.6
#
#       Description: Pitcher Program for Transferring
#                    files over USB connection
#
#

from tkinter import *
import tkinter as tk

import pitcher_main
import pitcher_func

def load_gui(self):



     

    #Label for user instructions    
    self.info_label = tk.Label(self.master, text="USB File Selector").grid(row=0, column=1, sticky= W)
    self.name_label = tk.Label(self.master, text="Choose File To Transfer").grid(row=1, column=0, sticky=N)

    self.txt_filename = tk.Entry(self.master,text='')
    self.txt_filename.grid(row=2,column=0,rowspan=1,columnspan=2,padx=(27,20),pady=(0,0),sticky=N+E+W)
    self.btn_selectfile1 = tk.Button(self.master,width=10,height=1,text='Select File',command=lambda: pitcher_func.ask_destination(self))
    self.btn_selectfile1.grid(row=3,column=0,padx=(27,0),pady=(10,10),sticky=N+W)

    # Create button to begin file creation
    self.btn_scncpy = tk.Button(self.master, width=12, height=2, text='Begin Transfer',
                                command=lambda: pitcher_func.begin_transfer(self))
    self.btn_scncpy.grid(row=8, column=0, padx=(15, 0), pady=(30, 10), sticky=W)
    self.btn_reset = tk.Button(self.master, width=12, height=2, text='Reset',
                               command=lambda: pitcher_func.reset(self))
    self.btn_reset.grid(row=8, column=1, columnspan=1, padx=(15,0),pady=(30,10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close',
                               command=lambda: pitcher_func.ask_quit(self))
    self.btn_close.grid(row=8, column=2, columnspan=1, padx=(15, 0), pady=(30, 10), sticky=W)


if __name__ == "__main__":
    pass
