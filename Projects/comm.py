import time
import threading
from tkinter import *
import serial

ser = serial.Serial('/dev/cu.usbmodem1421')

stop_serial_thread = False

class serial(threading.Thread):
    def __init__(self, name, input, monitor, autoscroll):
      threading.Thread.__init__(self)
      self.name = name
      self.input = input
      self.monitor = monitor
      self.autoscroll = autoscroll
      self.TimeCounter = time.time()
      self.LineCounter = 0
            
    def receive(self):
        chr = ser.read()
        self.monitor.config(state=NORMAL)
        self.monitor.insert(END,chr)
        if self.autoscroll.get() == True:
            self.monitor.see("end")
        self.monitor.config(state=DISABLED)
        
    # def receive(self): #Mocked
        # if((time.time() - self.TimeCounter) > 0.1):
        #     newLine = f"new line #{self.LineCounter}\n"
        #     self.monitor.config(state=NORMAL)
        #     self.monitor.insert(END,newLine)
        #     if self.autoscroll.get() == True:
        #         self.monitor.see("end")
        #     self.monitor.config(state=DISABLED)
        #     self.TimeCounter = time.time()
        #     self.LineCounter += 1
        
    def run(self):
        print ("Starting " + self.name)
        while(stop_serial_thread == False):
            self.receive()
        print("Ending " + self.name)
        
        
def transmitt(entry):
    str = entry.get()
    if str != "":
        ser.write(str.encode('ascii'))