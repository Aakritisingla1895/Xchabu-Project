import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.messagebox import *

   
def block():
    bedx = bedl.get()
    bedy= bed.get()
    bed1=bedx*10/4/100
    bed2=bedy*10/2/100
    
    kitx = kitchenl.get()
    kity= kitchen.get()
    kit1=kitx*10/4/100
    kit2=kity*10/2/100

    toix = toiletl.get()
    toiy= toilet.get()
    toi1=toix*10/4/100
    toi2=toiy*10/2/100

    drawx = halll.get()
    drawy= hall.get()
    dra1=drawx*10/4/100
    dra2=drawy*10/2/100

    dinx = diningl.get()
    diny= dining.get()
    din1=dinx*10/4/100
    din2=diny*10/2/100

    otsx = otsl.get()
    otsy= ots.get()
    ots1=otsx*10/4/100
    ots2=otsy*10/2/100

    stox = storel.get()
    stoy= store.get()
    sto1=stox*10/4/100
    sto2=stoy*10/2/100

    stax = stairsl.get()
    stay= stairs.get()
    sta1=stax*10/4/100
    sta2=stay*10/2/100

    foyx = foyerl.get()
    foyy= foyer.get()
    foy1=foyx*10/4/100
    foy2=foyy*10/2/100
    print("bed length ",bed1)
    print("bed width",bed2)
    print("kitchen length ",kit1)
    print("kitchen width",kit2)
    

    
root = Tk()
root.title('Xchabu')
root.geometry('1366x600')

bed = IntVar()
bedl = IntVar()
kitchen = IntVar()
kitchenl = IntVar()
toilet = IntVar()
toiletl = IntVar()
ots= IntVar()
otsl= IntVar()
store = IntVar()
stairs = IntVar()
hall = IntVar()
dining = IntVar()
storel = IntVar()
stairsl = IntVar()
halll = IntVar()
diningl = IntVar()
foyer= IntVar()
foyerl= IntVar()
xx= IntVar()
l = Label(root,text="bed width")
l.grid(row=0,column=0)
length =Entry(root,width=20,textvariable =bed)
length.grid(row=0,column=2)
l = Label(root,text="bed length")
l.grid(row=1,column=0)
bed1 =Entry(root,width=20,textvariable =bedl)
bed1.grid(row=1,column=2)

l = Label(root,text="kticheb length")
l.grid(row=3,column=0)
bed1 =Entry(root,width=20,textvariable =kitchen)
bed1.grid(row=3,column=2)

l = Label(root,text="kitchen width")
l.grid(row=4,column=0)
bed1 =Entry(root,width=20,textvariable =kitchenl)
bed1.grid(row=4,column=2)

l = Label(root,text="Toilet length")
l.grid(row=5,column=0)
bed1 =Entry(root,width=20,textvariable =toiletl)
bed1.grid(row=5,column=2)

l = Label(root,text="Toilet width")
l.grid(row=6,column=0)
bed1 =Entry(root,width=20,textvariable =toilet)
bed1.grid(row=6,column=2)

l = Label(root,text="drawing length")
l.grid(row=7,column=0)
bed1 =Entry(root,width=20,textvariable =halll)
bed1.grid(row=7,column=2)

l = Label(root,text="drawing width")
l.grid(row=8,column=0)
bed1 =Entry(root,width=20,textvariable =halll)
bed1.grid(row=8,column=2)

l = Label(root,text="dining length")
l.grid(row=9,column=0)
bed1 =Entry(root,width=20,textvariable =diningl)
bed1.grid(row=9,column=2)

l = Label(root,text="dining width")
l.grid(row=10,column=0)
bed1 =Entry(root,width=20,textvariable =dining)
bed1.grid(row=10,column=2)

l = Label(root,text="Staris length")
l.grid(row=11,column=0)
bed1 =Entry(root,width=20,textvariable =stairsl)
bed1.grid(row=11,column=2)

l = Label(root,text="stairs width")
l.grid(row=12,column=0)
bed1 =Entry(root,width=20,textvariable =stairs)
bed1.grid(row=12,column=2)

l = Label(root,text="OTS length")
l.grid(row=13,column=0)
bed1 =Entry(root,width=20,textvariable =otsl)
bed1.grid(row=13,column=2)

l = Label(root,text="OTS width")
l.grid(row=14,column=0)
bed1 =Entry(root,width=20,textvariable =ots)
bed1.grid(row=14,column=2)

l = Label(root,text="Store length")
l.grid(row=15,column=0)
bed1 =Entry(root,width=20,textvariable =storel)
bed1.grid(row=15,column=2)

l = Label(root,text="store width")
l.grid(row=16,column=0)
bed1 =Entry(root,width=20,textvariable =store)
bed1.grid(row=16,column=2)


l = Label(root,text="Foyer length")
l.grid(row=17,column=0)
bed1 =Entry(root,width=20,textvariable =foyerl)
bed1.grid(row=17,column=2)

l = Label(root,text="Foyer width")
l.grid(row=18,column=0)
bed1 =Entry(root,width=20,textvariable =foyer)
bed1.grid(row=18,column=2)






button1 = tk.Button(root, text="Sumbit",command=block)
button1.config( height = 2, width = 30 )
button1.grid(row=25,column=10)

root.mainloop()