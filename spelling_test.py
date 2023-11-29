import random 
import tkinter as tk
import customtkinter as Ctk
from us_grades import grade
from button_file import buttons
from key_functions import select

global state, k,  nright, nwrong
state = True
k, nright, nwrong = 0, 0, 0



def press(key):
    # the global statement is the onlyy way for the function in command in button to learn about variables 
    global state, k, nright, nwrong
    global l2, mWindow, gocabulary, vocab, go_bg_grey
    state, nright, nwrong,  vocab, k= select(key,state, k, vocab, gocabulary, nright, nwrong, l2, mWindow, go_bg_grey)

def spelling_test(var1,sWindow,vocabulary,bg_grey):
    global l2, mWindow, gocabulary, vocab, go_bg_grey
    gocabulary = vocabulary
    go_bg_grey = bg_grey
    if var1.get():
        random.shuffle(vocabulary)
    sWindow.destroy()
    mWindow=tk.Tk() 
    mWindow.title("Hindi Spelling Trainer")
    vocab = vocabulary[k]
    tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='green', font=('Times', 24), height=2).grid(row=0,column=0,columnspan=13,sticky="NEWS")
    tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg=bg_grey,fg='green', font=('Times', 24), height=2).grid(row=0,column=0,columnspan=13,sticky="NEWS")
    l2=tk.Entry(mWindow,width=35,bg='black',fg='white',relief='raised',selectborderwidth=5, font=('Times', 24))
    l2.grid(row=1,column=0,columnspan=13,sticky="ns")
    tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
    tk.Label(mWindow,text='??????????',bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
    tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
    tk.Label(mWindow,text=f'right = {nright}, wrong = {nwrong}; '+grade(1.0),bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
    for i,row in enumerate(buttons):
        for j,key in enumerate(row):
            tk.Button(mWindow,text=key,font=('Times', 24),width=6,height=2,relief='raised',command=lambda x=key:press(x),bd=6).grid(row=i+4,column=j)
    mWindow.grid_rowconfigure(0,weight=1)
    mWindow.grid_rowconfigure(1,weight=1)
    mWindow.grid_rowconfigure(2,weight=1)

