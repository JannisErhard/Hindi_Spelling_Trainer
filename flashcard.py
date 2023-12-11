import tkinter as tk 
def flashcard(Frame, nright, nwrong, vocab, grade):
    tk.Label(Frame,text=' '*80,fg='green', font=('Times', 24), height=2).grid(row=0,sticky="NEWS")
    tk.Label(Frame,text=f"Translate \"{vocab[0]}\"",fg='green', font=('Times', 24), height=2).grid(row=0,sticky="NEWS")
    l2=tk.Entry(Frame,width=35,bg='black',fg='white',relief='raised',selectborderwidth=5, font=('Times', 24))
    l2.grid(row=1,sticky="ns")
    tk.Label(Frame,text=' '*80,fg='red', font=('Times', 24), height=2).grid(row=2)
    if nright+nwrong > 0:
        tk.Label(Frame,text=f'right = {nright}, wrong = {nwrong}; '+grade((nright)/(nright+nwrong)),fg='black', font=('Times', 24), height=2).grid(row=2)
    else:
        tk.Label(Frame,text=f'right = {nright}, wrong = {nwrong}',fg='black', font=('Times', 24), height=2).grid(row=2)
    return l2 
