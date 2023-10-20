import tkinter as tk
from spelling_test import spelling_test as sp


vocabulary = []
with open('example_vocabulary') as f:
    for line in f.readlines():
        vocabulary.append(line.split())


def start_spelltest():
    # without this interface the window is just opened without button action
    sp(var1,sWindow,vocabulary,bg_grey)


sWindow=tk.Tk()
bg_grey = sWindow.cget('bg')
sWindow.title("Hindi Spelling Trainer")

var1= tk.BooleanVar()
tk.Checkbutton(sWindow, text="randomize", variable=var1).grid(row=0,column=0)

a = tk.Button(text="Click This",command = start_spelltest) #command=spelling_test(var1,sWindow,vocabulary,bg_grey))
a.grid(row=0,column=1)

sWindow.mainloop() #for infinite loop of main window
