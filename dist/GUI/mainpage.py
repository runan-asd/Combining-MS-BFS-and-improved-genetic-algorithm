import os
from collection import Collection
from compare import Compare
from direct import Direct
from inherit import Inherit
from dijkstra import Dijkstra
from attack import Attack_point#,Attack_random
from k import K
from set import Set

import tkinter as tk
from tkinter import Canvas, font
from PIL import ImageTk



class MainPage:

    def __init__(self, master):
        self.root = master
        self.font_1 = font.Font(family='宋体', size=36, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=18, weight='normal')
        self.root.geometry('923x600')
        self.root.resizable(0, 0)
        self.root.title('联合多源 BFS 与改进遗传算法的主备路由选择系统 V1.0')

        self.popup_menu = tk.Menu(self.root, tearoff=0)
        self.popup_menu.add_command(label="退出", command=self.root.destroy)

        self.root.bind('<Button-3>', self.on_right_click)

        self.canvas = Canvas(self.root, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.create_page()

    def create_page(self):
        self.collection = Collection(self.root)
        self.direct = Direct(self.root)
        self.inherit = Inherit(self.root)
        self.compare=Compare(self.root)
        #self.Dj = Dijkstra(self.root)
        #self.attack_random =Attack_random(self.root)
        #self.attack_point = Attack_point(self.root)
        #self.k = K(self.root)
        self.set = Set(self.root)

        self.menubar = tk.Menu(self.root)

        self.function_chart = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_command(label='图像设置', command=self.Parameter_set)

        #self.function_chart.add_command(label='生成随机图', command=self.Parameter_random)
        self.menubar.add_command(label='  路径集  ', command=self.Path_collection)

        self.function_path = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='主备路径', menu=self.function_path)
        self.function_path.add_command(label='直接选出', command=self.Count_direct)
        self.function_path.add_command(label='遗传算法', command=self.Count_inherit)

        self.function_compare = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_command(label='算法比较', command=self.Path_compare)
        '''self.menubar.add_cascade(label='算法比较', menu=self.function_compare)
        self.function_compare.add_command(label='Dijkstra算法', command=self.Compare_Dijkstra)
        self.function_compare.add_command(label='k最短路径算法', command=self.Compare_k)'''

        '''self.attack_set = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='攻击演示', menu=self.attack_set)
        #self.attack_set.add_command(label='随机攻击', command=self.Attack_random)
        self.attack_set.add_command(label='指定攻击', command=self.Attack_point)
        '''
        self.root['menu'] = self.menubar

    def forget(self):
        self.canvas.pack_forget()
        self.collection.pack_forget()
        self.direct.pack_forget()
        self.inherit.pack_forget()
        #self.Dj.pack_forget()
        #self.k.pack_forget()
        self.set.pack_forget()
        self.compare.pack_forget()
        #self.attack_random.pack_forget()
        #self.attack_point.pack_forget()
    def Path_collection(self):
        self.forget()
        self.collection.pack()
    def Path_compare(self):
        self.forget()
        self.compare.pack()
    def Count_direct(self):
        self.forget()
        self.direct.pack()

    def Count_inherit(self):
        self.forget()
        self.inherit.pack()

    def Compare_Dijkstra(self):
        self.forget()
        self.Dj.pack()
    '''
    def Attack_random(self):
        self.forget()
        self.attack_random.pack()
        '''
    def Attack_point(self):
        self.forget()
        self.attack_point.pack()
    def Compare_k(self):
        self.forget()
        self.k.pack()

    def Parameter_set(self):
        self.forget()
        self.set.pack()

    def Parameter_random(self):
        Set.random(self.root)

    def on_right_click(self, event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()

