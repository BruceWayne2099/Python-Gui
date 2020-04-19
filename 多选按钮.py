import tkinter as tk

window = tk.Tk()
window.title("多选按钮")
window.geometry("500x500")

l = tk.Label(window,width=30,height=10,bg="yellow",text="Choose,plz...")
l.pack()

def print_selection():
    if (var1.get() ==1) & (var2.get() ==0):
        l.config(text = "i choose redis!")
    if (var1.get() == 0) & (var2.get() == 1):
        l.config(text = "i choose memcache!")
    if (var1.get() == 0) & (var2.get() == 0):
        l.config(text = "no,thanks!")
    if (var1.get() == 1) & (var2.get() == 1):
        l.config(text = "i need both!")

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window,text="redis",variable=var1,onvalue=1,offvalue=0,command=print_selection) #选中的时候value被赋值成1,同时赋值给var1
c2 = tk.Checkbutton(window,text="memcache",variable=var2,onvalue=1,offvalue=0,command=print_selection)

c1.pack()
c2.pack()

window.mainloop()