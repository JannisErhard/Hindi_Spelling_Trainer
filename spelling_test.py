import random 
import tkinter as tk
from us_grades import grade
from button_file import buttons
from key_functions import select

global state, k, vocab, nright, nwrong, l1, l2, l3, l4, mWindow

def press(key):
    # the global statement is the onlyy way for the function in command in button to learn about variables 
    global state, k, vocab, nright, nwrong, l1, l2, l3, l4, mWindow
    state, nright, nwrong,  vocab, k= select(key,state, k, vocab, gocabulary, nright, nwrong, l1, l2, l3, l4, mWindow, go_bg_grey)

def spelling_test(var1,sWindow,vocabulary,bg_grey):
    global state, k, vocab, nright, nwrong, l1, l2, l3, l4, mWindow, gocabulary, go_bg_grey
    gocabulary = vocabulary
    go_bg_grey = bg_grey
    print(var1.get())
    if var1.get():
        random.shuffle(vocabulary)
    sWindow.destroy()
    mWindow=tk.Tk() 
    mWindow.title("Hindi Spelling Trainer")
    state = True 
    k=0
    nright, nwrong = 0 , 0 
    vocab = vocabulary[k]
    l1=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
    l1=tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
    l2=tk.Entry(mWindow,bg='black',fg='white',relief='raised', font=('Times', 24))
    l2.grid(row=1,column=0,columnspan=13,pady=10)
    l3=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
    l3=tk.Label(mWindow,text='??????????',bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
    l4=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
    l4=tk.Label(mWindow,text=f'right = {nright}, wrong = {nwrong}; '+grade(1.0),bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
    for i,row in enumerate(buttons):
        for j,key in enumerate(row):
            tk.Button(mWindow,text=key,width=6,height=2,relief='raised',command=lambda x=key:press(x),bd=6).grid(row=i+4,column=j)
