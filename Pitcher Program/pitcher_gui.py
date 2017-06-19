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

    #Radio buttons for file selection
    MODES = [
    ("Video One", "1"),
    ("Video Two", "2"),
    ("Video Three", "3"),
    ("Video Four", "4"),
    ]

    self.v = IntVar()
    self.v.set(1) # initialize
    x = 2
    for text, mode in MODES:
        b = tk.Radiobutton(self.master, text=text,
                        variable=self.v, value=mode )
        b.grid(row=x, column=0, sticky = W)
        x = x+1

    #Label for user instructions    
    self.info_label = tk.Label(self.master, text="Choose file to transfer").grid(row=0, column=0, sticky= W)
    # Create button to begin file creation
    self.btn_scncpy = tk.Button(self.master, width=12, height=2, text='Begin Transfer',
                                command=lambda: pitcher_func.begin_transfer(self))
    self.btn_scncpy.grid(row=8, column=0, padx=(25, 0), pady=(30, 10), sticky=W)

    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close',
                               command=lambda: pitcher_func.ask_quit(self))
    self.btn_close.grid(row=8, column=1, columnspan=1, padx=(15, 0), pady=(30, 10), sticky=E)


if __name__ == "__main__":
    pass
