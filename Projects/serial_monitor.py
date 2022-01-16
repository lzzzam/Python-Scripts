from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import comm

window = Tk()
window.title("Serial Monitor")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

def clearOutput():
    monitor.config(state=NORMAL)
    monitor.delete('1.0', END)
    monitor.config(state=DISABLED)

input = Entry(window)
input.grid(row=0, column=0, padx=1, pady=1, sticky=N+EW)

Send = Button(text = "Send", width = 12 , command = lambda: comm.transmitt(input))
Send.grid(row=0, column=1,  padx=1, pady=1, sticky=EW)

Clear = Button(text = "Clear Output", command = clearOutput)
Clear.grid(row=2, column=1, sticky=E)

autoscroll_state = BooleanVar()
autoscroll_state.set(True)
autoscroll_chk = Checkbutton(window, width= 12, text='Autoscroll', var=autoscroll_state)
autoscroll_chk.grid(row=2, column=0, sticky = W)

monitor = scrolledtext.ScrolledText(window,state=DISABLED, wrap=WORD)
monitor.grid(row=1, column=0, columnspan=2, sticky=NSEW)

Serial = comm.serial("Serial Thread", input, monitor, autoscroll_state)
Serial.start()

def closeSerialMonitor():
    
    comm.stop_serial_thread = True
    comm.ser.close()

    window.destroy()

window.protocol("WM_DELETE_WINDOW", closeSerialMonitor)

window.update()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
rw = window.winfo_width()
rh = window.winfo_height()
window.minsize(rw, 233)
window.geometry(f'{rw}x{rh}+{int((sw-rw)/2)}+{int((sh-rh)/2)-30}')

window.mainloop()