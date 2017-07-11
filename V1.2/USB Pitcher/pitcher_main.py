#       Author: Mathew Perrow
#
#       Version:Python 3.5
#
#       Description: Catcher Program for Transferring
#                    files over USB connection
#
#       This is the file you want to run to begin program

from tkinter import *
import tkinter as tk
# Importing both gui and function scripts for parent window
import pitcher_gui
import pitcher_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(420, 220)
        self.master.maxsize(420, 220)
        # Defining the dimensions of parent window and making it static
        pitcher_func.center_window(self, 420, 220)
        self.master.title('File Pitcher - Write')
        self.master.configure(bg='#F0F0F0')
        self.master.protocol('WM_DELETE_WINDOW', lambda: pitcher_func.ask_quit(self))
        arg = self.master
        self.master.iconbitmap('favicon.ico')

        pitcher_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)  # Creating menubar bar for parent window
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=1, accelerator='Ctrl+Q',
                             command=lambda: pitcher_func.ask_quit(self))
        menubar.add_cascade(label='File', underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label='How to use USB Transfer Program')
        helpmenu.add_separator()
        helpmenu.add_command(label='About USB Transfer')
        menubar.add_cascade(label='Help', menu=helpmenu)
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
