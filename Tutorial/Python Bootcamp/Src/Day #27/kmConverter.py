from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

window = Tk()
window.title("kmConverter")
window.minsize(600, 600)

label = Label(text = "I am a label")
label.pack()

def buttonClicked():
    label["text"] = textInput.get()

button = Button(text = "Click me", command=buttonClicked)
button.pack()

textInput = Entry()
textInput.pack()

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item
combo.pack()

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.config(state=ACTIVE)
txt.insert(INSERT,'You text goes here')
txt.config(state=DISABLED)
txt.pack()

window.mainloop()