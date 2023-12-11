import tkinter as tk
from read_data import read_dictionary 
from utils import generate_checkboxes, select_all, deselect_all, generate_English_to_Hindi_vocabulary, generate_Hindi_to_English_vocabulary, make_keyboard
from tkinter.scrolledtext import ScrolledText
from us_grades import grade
from flashcard import flashcard

root=tk.Tk()
root.title('Selfcontained')
root.geometry("400x400")


class Main():
    def __init__(self, master):
        var_1 = ''
        self.dictionary=read_dictionary()
        self.window=master
        self.Frame=tk.LabelFrame(self.window, text="")
        self.start_menue()
        self.k, self.nright, self.nwrong = 0, 0, 0
        self.state = True
    
    def press(self, value):
        # only way to carry variables over
        length=len(self.l2.get())
        if (value=='Erase'):
            self.l2.delete(length-1,length)
            length=length-1
        elif value=='Space':
            self.l2.insert(length,' ')
        else:
            self.l2.insert(length,value)

    def Enter(self):
        if self.state:
            if self.l2.get() ==self. vocab[1]:
                self.nright+=1
                tk.Label(self.Frame,text=' '*80,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13,pady=3)
                tk.Label(self.Frame,text='Correct',fg='green', font=('Times', 24), height=2).grid(row=2,column=0,columnspan=13,pady=3)
            else :
                self.nwrong+=1
                tk.Label(self.Frame,text=' '*80,fg='red', font=('Times', 24)).grid(row=2,column=0,columnspan=13)
                tk.Label(self.Frame,text='Incorrect. Proper Solution: '+self.vocab[1],fg='red', font=('Times', 24), height=2).grid(row=2,column=0,columnspan=13)
            self.state = False
        else:
            if self.k == len(self.vocabulary)-1:
                print("great, its done")
                self.start_menue()
            else:
                self.k+=1
                self.vocab = self.vocabulary[self.k]
                self.l2 = flashcard(self.Frame, self.nright, self.nwrong, self.vocab, grade)
                self.l2.delete(0,'end')
                self.state = True
    
    def start_menue(self):
        # overhead 
        self.Frame.destroy()
        self.Frame = tk.LabelFrame(self.window, text="Choose Vocabulary", padx=4, pady=5)
        self.Frame.pack()

        # generate ... menue # self.Frame
        scroll_text = ScrolledText(self.Frame, width=20, height=10)
        checkboxes, self.choices = generate_checkboxes(self.dictionary, scroll_text)
        scroll_text.grid(row=0,sticky="NESW")
       
        # set up buttons
        button_deselect = tk.Button(self.Frame, text="Deselect All", command =lambda *args: deselect_all(checkboxes))
        button_deselect.grid(row=1,column=0,sticky="NESW")

        button_select = tk.Button(self.Frame, text="Select All", command =lambda *args: select_all(checkboxes))
        button_select.grid(row=1,column=1,sticky="NESW")

        button_start_english_to_hindi = tk.Button(self.Frame, text="Translate English to Hindi", command = self.english_to_hindi)
        button_start_english_to_hindi.grid(row=2,column=0,sticky="NESW")

        button_start_hindi_to_english = tk.Button(self.Frame, text="Translate Hindi to English", command = self.hindi_to_english)
        button_start_hindi_to_english.grid(row=2,column=1,sticky="NESW")


    def hindi_to_english(self):
        # overhead
        self.Frame.destroy()
        self.Frame = tk.LabelFrame(self.window, text="Here is text", padx=4, pady=5)
        self.Frame.pack()
        root.geometry(f"{root.winfo_screenwidth()//12*5}x{root.winfo_screenheight()//5*2}")
        # pick out words 
        self.vocabulary = generate_Hindi_to_English_vocabulary(self.choices, self.dictionary)
        self.vocab = self.vocabulary[self.k]
        # design of flashcard
        self.l2 = flashcard(self.Frame, self.nright, self.nwrong, self.vocab, grade)
        enter_button = tk.Button(self.Frame, text=" Enter ", font=('Times', 24),width=6,height=2, relief='raised', command = self.Enter)
        enter_button.grid(row=3,column=0,sticky="NESW")


    def english_to_hindi(self):
        # overhead
        self.Frame.destroy()
        self.Frame = tk.LabelFrame(self.window, text="Here is text", padx=4, pady=5)
        self.Frame.pack()
        root.geometry(f"{root.winfo_screenwidth()//12*11}x{root.winfo_screenheight()//5*4}")
        # pick out words 
        self.vocabulary = generate_English_to_Hindi_vocabulary(self.choices, self.dictionary)
        # design flashcard
        self.vocab = self.vocabulary[self.k]
        # design keyboard
        Keyboard_Frame = tk.LabelFrame(self.Frame, text="Hindi Keyboard", padx=4, pady=5)
        Keyboard_Frame.grid(row=3,column=0,sticky="NESW")
        make_keyboard(Keyboard_Frame, self.press)
        enter_button = tk.Button(Keyboard_Frame, text=" ↵ ", font=('Times', 24),width=6,height=2, relief='raised', command = self.Enter)
        enter_button.grid(row=5,column=12,sticky="NESW")
        # make flashcard
        self.l2 = flashcard(self.Frame, self.nright, self.nwrong, self.vocab, grade)
    


    def sub_menue(self):
        # overhead
        self.Frame.destroy()
        self.Frame = tk.LabelFrame(self.window, text="Here is text", padx=4, pady=5)
        self.Frame.pack()
        l1=tk.Label(self.Frame,text='b'*80,fg='red', font=('Times', 24), height=2)
        l1.grid(row=0,column=0,columnspan=1,sticky="NEWS")
        button1 = tk.Button(self.Frame, text="Start Start", command = self.start_menue)
        button1.grid(row=1,column=0,columnspan=1,sticky="NEWS")


Main = Main(root)
root.mainloop()
