#, k, vocab, vocabulary, nright, nwrong, l1, l2, l3, l4, mWindow 
import tkinter as tk
from us_grades import grade
def restart_window():
    rWindow = tk.Tk()
    rWindow.title("End")
    line_1 = tk.Label(rWindow,text='You have finished your set, restart set?',fg='black', font=('Times', 24))
    line_1.grid(row=0,column=0,columnspan=2,sticky="NEWS")
    restart = tk.Button(text="Yes")
    end  = tk.Button(text="No")
    end.grid(row=1,column=0,sticky="NEWS")
    restart.grid(row=1,column=1,sticky="NEWS")


def select(value,state, k, vocab, vocabulary, nright, nwrong,  l2, mWindow, bg_grey):
    # only way to carry variables over
    length=len(l2.get())
    if (value=='Erase'):
        l2.delete(length-1,length)
        length=length-1
    elif value=='Space':
        l2.insert(length,' ')
    elif value=='Enter':
        # Enter Button, has two possible functions, depending on current "state" of the Program:
        # State True: Vocabulary is tested, "Enter" checks wether answer is correct or incorrect
        if state:
            if l2.get() == vocab[1]:
                nright+=1
                tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
                tk.Label(mWindow,text='Correct',bg=bg_grey,fg='green', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
            else :
                nwrong+=1
                tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                tk.Label(mWindow,text='Incorrect. Proper Solution: '+vocab[1],bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
            state = False
        # State False: Vocabulary was tested, "Enter" prompts the next vocabulary item
        else:
            k+=1
            if k == len(vocabulary):
                mWindow.destroy()
                restart_window()
            else:
                vocab = vocabulary[k]
                tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13,sticky="NEWS")
                tk.Label(mWindow,text=f"Translate \"{vocab[0]}\"",bg=bg_grey,fg='green', font=('Times', 24)).grid(row=0,column=0,columnspan=13,sticky="NEWS")
                tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
                tk.Label(mWindow,text='??????????',bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
                tk.Label(mWindow,text=' '*80,bg=bg_grey,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                tk.Label(mWindow,text=f'right = {nright}, wrong = {nwrong}; '+grade(nright/(nright+nwrong)),bg=bg_grey,fg='black', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                l2.delete(0,'end')
                state = True
    else:
        l2.insert(length,value)
    return state, nright, nwrong, vocab, k


