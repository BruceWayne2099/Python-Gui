#简单的gui界面，搭配按钮点击
import tkinter as tk

#先做一个大窗体
window = tk.Tk()
window.title("购买阿里云云资源")   #窗体的标题
window.geometry("500x750")  #宽X长

var1 = tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

def point_selection():
    value = lb.get(lb.curselection())   #选择的值作为value
    var1.set(value)

b1 = tk.Button(window,text="请选择下面的功能",width=15,height=2,command=point_selection)  #这个button是在window这个载体上运行的，点击之后会执行hit_me这个函数
b1.pack()

var2 = tk.StringVar()
var2.set(("yaoming","james","wade","bosh","kobe","curry","durant")) #传入一个元祖

sb = tk.Scrollbar(window)  #垂直滚动条组件
sb.pack(side="right",fill="y")  #设置滚动条的位置

lb = tk.Listbox(window,listvariable=var2,yscrollcommand=sb.set) #将var2传入到list里,把垂直滚动条set添加到listbox里
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)   #将1234添加到尾部
lb.insert(1,"shaq")
lb.insert(2,"Dirk Nowitzki")    #插入
#lb.delete(2)    #删除第二位

lb.pack(fill="both")    #充满，side="left"意思是lb框在左边，
sb.config(command=lb.yview)
window.mainloop()   #不断的循环刷新