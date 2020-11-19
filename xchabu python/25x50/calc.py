import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.messagebox import *

   
def block():
    bedx = bedl.get()
    bedy= bed.get()
    bedx1=bedx*2
    bed1 =bedx1/100
    bedx2=bedy*4
    bed2= bedx2/100
    
    
    print("length ",bed1)
    print("width",bed2)
    
    

    
root = Tk()
root.title('Xchabu')
root.geometry('1366x600')

bed = IntVar()
bedl = IntVar()

l = Label(root,text="bed width")
l.grid(row=0,column=0)
length =Entry(root,width=20,textvariable =bed)
length.grid(row=0,column=2)
l = Label(root,text="bed length")
l.grid(row=1,column=0)
bed1 =Entry(root,width=20,textvariable =bedl)
bed1.grid(row=1,column=2)






button1 = tk.Button(root, text="Sumbit",command=block)
button1.config( height = 2, width = 30 )
button1.grid(row=25,column=10)

root.mainloop()
