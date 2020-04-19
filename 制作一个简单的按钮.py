#简单的gui界面，搭配按钮点击
import tkinter as tk

window = tk.Tk()
window.title("购买阿里云服务器")   #窗体的标题
window.geometry("500x750")  #宽X长

var = tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)    #配置label
l.pack()    #place方法就是具体放置，需要指明坐标

on_hit = False
def hit_me():
    #print("olalalala")  #如果这么写就是在后台打印
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("你点到我了！")   #将label里的var赋值
    else:
        on_hit = False
        var.set("")

b = tk.Button(window,text="点我啊！",width=15,height=2,command=hit_me)  #这个button是在window这个载体上运行的，点击之后会执行hit_me这个函数

b.pack()
window.mainloop()   #不断的循环刷新
