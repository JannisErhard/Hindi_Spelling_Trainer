import random
import tkinter as tk
from button_file import buttons

def generate_checkboxes(dictionary, text):
    checkboxes, choices = [], {}
    for category in dictionary.keys():
        choices[category] = tk.BooleanVar()
        cb = tk.Checkbutton(text, text=category, bg='white', anchor='w', cursor='arrow',variable=choices[category])
        text.window_create('end', window=cb)
        text.insert('end', '\n')
        checkboxes.append(cb)
    return checkboxes, choices

def select_all(checkboxes):
# selects all entries in tickable list
    for checkbox in checkboxes:
        checkbox.select()

def deselect_all(checkboxes):
# deselects all entries in tickable list
    for checkbox in checkboxes:
        checkbox.deselect()


def generate_English_to_Hindi_vocabulary(vocabulary_choices, unserialized_data, randomize):
# goes through decisions and appends them to list which will then be used for tests
    vocabulary = []
    for decision in vocabulary_choices.keys():
        if vocabulary_choices[decision].get():
            for item in unserialized_data[decision][0:]:
                for alternative in item[1]:
                    vocabulary.append([alternative, item[0]])
    if randomize.get():
        random.shuffle(vocabulary)
    return vocabulary 

def generate_Hindi_to_English_vocabulary(vocabulary_choices, unserialized_data, randomize):
# goes through decisions and appends them to list which will then be used for tests
    vocabulary = []
    for decision in vocabulary_choices.keys():
        if vocabulary_choices[decision].get():
            for item in unserialized_data[decision][0:]:
                for alternative in item[0]:
                    vocabulary.append([alternative, item[1]])
    if randomize.get():
        random.shuffle(vocabulary)
    return vocabulary

def make_keyboard(Frame, press):
    for i,row in enumerate(buttons):
        for j,key in enumerate(row):
            tk.Button(Frame,text=key,font=('Times', 24),width=6,height=2,relief='raised',command=lambda x=key:press(x),bd=6).grid(row=i+4,column=j)

