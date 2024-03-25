# Hindi_Spelling_Trainer
## Prerequisites
requires  python3, tkinter and Customtkinter to run. Ubuntu, bash:

`sudo apt-get install python3`\
`pip install tk`\
`pip install Customtkinter`

## Usage
run:\
`python3 Main.py`

# Update vocabulary 
Go into `TMP`, run the preformatter `sh pre_formatter.sh > war`, then run the formatter `python3 format.py war` and move the generated file `vocabulary.pkl` up into the parent folder. 


## Plans
re-think the enter key hook -> this is boileplate code that should be written only once. problem enter invisible to flashcard function\
introduce a progression system that also allows the addition of new vocabulary\
allow for alternative answers\
introduce declenation exercises
