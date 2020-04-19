import tkinter as tk

window = tk.Tk()
window.title("尺度")
window.geometry("200x200")

l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()

def print_selection(v):
    l.config(text="当前选择的值是：" + v)   #V就是传入值也是获取的长度

s = tk.Scale(window,label="想要多少台",from_=1,to=20,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval=4,resolution=1,command=print_selection)   #HORIZONTAL横向,length的单位是像素,resolution单位是取小数还是取整
s.pack()

window.mainloop()