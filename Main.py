import tkinter as tk
import random 
from us_grades import grade
from button_file import buttons

def spelling_test():
    global l1, l2, l3, l4, state, k, vocab, vocabulary, nright, nwrong, mWindow, var1
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
            tk.Button(mWindow,text=key,width=6,height=2,relief='raised',
               command=lambda x=key:select(x),bd=6).grid(row=i+4,column=j)

def select(value):
    # only way to carry variables over
    global state, k, vocab, vocabulary, nright, nwrong
    length=len(l2.get())
    if (value=='Erase'):
        l2.delete(length-1,length)
        length=length-1
    elif value=='Space':
        l2.insert(length,' ')
    elif value=='Enter':
        # two possible states:
        # State True: Vocabulary is tested, "Enter" checks wether true or false
        if state:
            if l2.get() == vocab[1]:
                nright+=1
                l3=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
                l3=tk.Label(mWindow,text='Correct',bg=bg_grey,fg='green', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
            else :
                nwrong+=1
                l3=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                l3=tk.Label(mWindow,text='Incorrect. Proper Solution: '+vocab[1],bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            state = False
        # State False: Vocabulary was tested, "Enter" prompts the next vocabulary item
        else:
            k+=1
            vocab = vocabulary[k]
            l1=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
            l1=tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
            l3=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
            l3=tk.Label(mWindow,text='??????????',bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
            l4=tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            l4=tk.Label(mWindow,text=f'right = {nright}, wrong = {nwrong}; '+grade(nright/(nright+nwrong)),bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            l2.delete(0,'end')
            state = True
    else:
        l2.insert(length,value)

sWindow=tk.Tk()
sWindow.title("Hindi Spelling Trainer")
var1= tk.BooleanVar()
tk.Checkbutton(sWindow, text="randomize", variable=var1).pack()
a = tk.Button(text="Click This", command=spelling_test)
a.pack()

bg_grey = sWindow.cget('bg')
vocabulary = []
with open('example_vocabulary') as f:
    for line in f.readlines():
        vocabulary.append(line.split())




sWindow.mainloop() #for infinite loop of main window
