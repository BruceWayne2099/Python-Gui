import tkinter as tk

window = tk.Tk()
window.title("点选按钮功能")
window.geometry("200x200")

var1 = tk.StringVar()
l = tk.Label(window,bg='pink',width=10,text="空")
l.pack()    #把l吸附上去

def print_selection():
    l.config(text="你选择了"+var1.get())  #使用config功能去改变原有l的参数,把text变成了提取var1里的值
r1 = tk.Radiobutton(window,text="2核4G",variable=var1,value='A',command=print_selection) #如果选择此项，将会给var1传入值A，同时执行函数print_selection
r1.pack()   #把r1吸附上去

r2 = tk.Radiobutton(window,text="2核8G",variable=var1,value='B',command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text="4核8G",variable=var1,value='C',command=print_selection)
r3.pack()

r4 = tk.Radiobutton(window,text="4核16G",variable=var1,value='D',command=print_selection)
r4.pack()

window.mainloop()