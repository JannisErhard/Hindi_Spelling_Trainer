import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pickle
from spelling_test import spelling_test as sp

def print_decisions():
    for decision in vocabulary_choices.keys():
        print(decision, ":" , vocabulary_choices[decision].get())

def start_spelltest():
    vocabulary = []
    for decision in vocabulary_choices.keys():
        if vocabulary_choices[decision].get():
            for item in unserialized_data[decision][0:]:
                vocabulary.append([item[1], item[0]])
    sp(var1,sWindow,vocabulary,bg_grey)


sWindow = tk.Tk()
bg_grey = sWindow.cget('bg')
sWindow.title("Setup Menu - Spelling Trainer")

text = ScrolledText(sWindow, width=20, height=10)
text.grid(row=1,column=0)

# Load data (deserialize)
with open('vocabulary.pkl', 'rb') as handle:
    unserialized_data = pickle.load(handle)


vocabulary_choices = {}
for category in unserialized_data.keys():
    vocabulary_choices[category] = tk.BooleanVar()
    cb = tk.Checkbutton(text, text=category, bg='white', anchor='w', cursor='arrow',variable=vocabulary_choices[category])
    text.window_create('end', window=cb)
    text.insert('end', '\n')



a = tk.Button(text="Check Decisions",command = print_decisions) #command=spelling_test(var1,sWindow,vocabulary,bg_grey))
a.grid(row=0,column=0)

b = tk.Button(text="Start Spelling Training",command = start_spelltest) #command=spelling_test(var1,sWindow,vocabulary,bg_grey))
b.grid(row=2,column=0)

var1= tk.BooleanVar()
var1.set(False)
tk.Checkbutton(sWindow, text="randomize", variable=var1).grid(row=3,column=0)


sWindow.mainloop()
