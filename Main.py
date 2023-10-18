import tkinter as tk
from button_file import buttons

mWindow=tk.Tk() #creating main window
mWindow.title("Hindi Spelling Trainer")
#mWindow.resizable(0,0) 

vocabulary = []
with open('example_vocabulary') as f:
    for line in f.readlines():
        vocabulary.append(line.split())

def select(value):
    global state, k, vocab, vocabulary 
    length=len(l2.get())
    if (value=='Erase'):
        l2.delete(length-1,length)
        length=length-1
    elif value=='Space':
        l2.insert(length,' ')
    elif value=='Enter':
        if state:
            if l2.get() == vocab[1]:
                l3=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                l3=tk.Label(mWindow,text='Correct',bg='lightgrey',fg='green', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            else :
                l3=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                l3=tk.Label(mWindow,text='Incorrect. Proper Solution: '+vocab[1],bg='lightgrey',fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            state = False
        else:
            k+=1
            vocab = vocabulary[k]
            l1=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
            l1=tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg='lightgrey',fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
            l3=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            l3=tk.Label(mWindow,text='??????????',bg='lightgrey',fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            l2.delete(0,'end')
            state = True
    else:
        l2.insert(length,value)

state = True 
k=0
vocab = vocabulary[k]
l1=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
l1=tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg='lightgrey',fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13)
l2=tk.Entry(mWindow,bg='black',fg='white',relief='raised', font=('Times', 24))
l2.grid(row=1,column=0,columnspan=13)
l3=tk.Label(mWindow,text=' '*80,bg='lightgrey',fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
l3=tk.Label(mWindow,text='??????????',bg='lightgrey',fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)





for i,row in enumerate(buttons):
    for j,key in enumerate(row):
        tk.Button(mWindow,text=key,width=6,height=2,relief='raised',
           command=lambda x=key:select(x),bd=6).grid(row=i+3,column=j)


mWindow.mainloop() #for infinite loop of main window
