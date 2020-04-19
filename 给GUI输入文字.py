#简单的gui界面，搭配按钮点击
import tkinter as tk

#先做一个大窗体
window = tk.Tk()
window.title("购买阿里云服务器")   #窗体的标题
window.geometry("500x750")  #宽X长

e = tk.Entry(window,show=None)  #如果是密码，那就是show='*',
e.pack()

def insert_point():
    var = e.get()   #获取e里的内容
    t.insert('insert',var)  #插入到光标所在的地方

def insert_end():
    var = e.get()
    t.insert("end",var) #插入到尾部,如果给end加上坐标就是具体位置，第几行第几位

b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)  #这个button是在window这个载体上运行的，点击之后会执行hit_me这个函数
b1.pack()

b2 = tk.Button(window,text="insert end",command=insert_end)
b2.pack()

t=tk.Text(window,height=10)
t.pack()
window.mainloop()   #不断的循环刷新