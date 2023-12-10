import tkinter as tk
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
import pickle
from spelling_test import spelling_test as sp


cbs = []
vocabulary_choices = {}
var1 = False 

with open('vocabulary.pkl', 'rb') as handle:
    unserialized_data = pickle.load(handle)
    unserialized_data = dict(sorted(unserialized_data.items()))

def select_all():
# selects all entries in tickable list
    for i in cbs:
        i.select()

def deselect_all():
# deselects all entries in tickable list
    for i in cbs:
        i.deselect()

def print_decisions():
# function for debugging purposes
    for decision in vocabulary_choices.keys():
        print(decision, ":" , vocabulary_choices[decision].get())

def start_English_to_Hindi(sWindow, bg_grey):
# goes through decisions and appends them to list which will then be used for tests
    vocabulary = []
    for decision in vocabulary_choices.keys():
        if vocabulary_choices[decision].get():
            for item in unserialized_data[decision][0:]:
                vocabulary.append([item[1], item[0]])
    sp(var1,sWindow,vocabulary,bg_grey)

def start_Hindi_to_English(sWindow, bg_grey):
# goes through decisions and appends them to list which will then be used for tests
    vocabulary = []
    for decision in vocabulary_choices.keys():
        if vocabulary_choices[decision].get():
            for item in unserialized_data[decision][0:]:
                vocabulary.append([item[0], item[1]])
    sp(var1,sWindow,vocabulary,bg_grey)


def Main():
    sWindow = ctk.CTk()
    bg_grey = sWindow.cget('bg')
    sWindow.title("Setup Menu - Hindi Language Trainer")
    
    text = ScrolledText(sWindow, width=20, height=10)
    text.grid(row=1,columnspan=2,sticky="NESW")
    
    # Load data (deserialize)
    
    
    for category in unserialized_data.keys():
        vocabulary_choices[category] = tk.BooleanVar()
        cb = tk.Checkbutton(text, text=category, bg='white', anchor='w', cursor='arrow',variable=vocabulary_choices[category])
        text.window_create('end', window=cb)
        text.insert('end', '\n')
        cbs.append(cb)
    
    
    
    
    #a = tk.Button(text="Check Decisions",command = print_decisions) #command=spelling_test(var1,sWindow,vocabulary,bg_grey))
    #a.grid(row=0,column=0)
    
    button_start_english_to_hindi = tk.Button(text="Translate English to Hindi",command = lambda *args: start_English_to_Hindi(sWindow,bg_grey)) 
    button_start_english_to_hindi.grid(row=2,column=0,sticky="NESW")
    
    button_start_hindi_to_english = tk.Button(text="Translate Hindi to English",command =lambda *args: start_Hindi_to_English(sWindow,bg_grey)) 
    button_start_hindi_to_english.grid(row=2,column=1,sticky="NESW")
    
    button_start_english_to_hindi = tk.Button(text="Deselect All",command = deselect_all) 
    button_start_english_to_hindi.grid(row=0,column=0,sticky="NESW")
    
    button_start_hindi_to_english = tk.Button(text="Select All",command = select_all) 
    button_start_hindi_to_english.grid(row=0,column=1,sticky="NESW")
    
    tk.Checkbutton(sWindow, text="randomize", variable=var1).grid(row=3,column=0,sticky='N')
    
    sWindow.grid_columnconfigure(0,weight=1)
    sWindow.grid_rowconfigure(0,weight=1)
    sWindow.grid_rowconfigure(1,weight=1)
    sWindow.grid_rowconfigure(2,weight=1)
    sWindow.grid_rowconfigure(3,weight=1)
    
    sWindow.mainloop()


Main()


# see https://www.reddit.com/r/learnprogramming/comments/y6opmu/python3what_is_an_intvar/ for explanation on wtf these Tkinter variables are ...
