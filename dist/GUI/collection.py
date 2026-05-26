import tkinter as tk
import pickle
import os
from tkinter import Canvas, font, ttk
from PIL import ImageTk
from mmbfs import mmbfs
class Collection(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.font_1 = font.Font(family='楷体', size=18, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.frame = ttk.Frame(self.canvas)
        self.chart = ttk.Treeview(self.frame, show="headings", columns=("1", "2", "3", "4", "5", "6", "7"))
        self.chart.column("1", width=60, anchor="center")
        self.chart.heading("1", text="节点1")
        self.chart.column("2", width=60, anchor="center")
        self.chart.heading("2", text="节点2")
        self.chart.column("3", width=120, anchor="center")
        self.chart.heading("3", text="路径1")
        self.chart.column("4", width=120, anchor="center")
        self.chart.heading("4", text="路径2")
        self.chart.column("5", width=120, anchor="center")
        self.chart.heading("5", text="路径3")
        self.chart.column("6", width=120, anchor="center")
        self.chart.heading("6", text="路径4")
        self.chart.column("7", width=120, anchor="center")
        self.chart.heading("7", text="路径5")
        self.chart.pack(fill="both", expand=True)
        self.canvas.create_window(460, 300, window=self.frame)

        self.run = tk.Button(self, text="运行程序", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.run_)
        self.canvas.create_window(100, 100, width=100, height=40, window=self.run)

    def run_(self):
         # 从文件中恢复实例
        with open(os.getcwd() + r"\GUI\generatedata\s_read.pkl", 'rb') as file:
            self.read = pickle.load(file)
        wulitu, luojitu = self.read.wulitu, self.read.luojitu
        a, lj1 = mmbfs(luojitu, wulitu, 3, mode=1)
        b, lj2 = mmbfs(lj1, wulitu, 3, mode=2)
        c, lj3 = mmbfs(luojitu, wulitu, 3, mode=3)

        lj3.update(lj2)
        print(lj3)
        for item in lj3:
            s,e=item
            tuple1=tuple([s,e]+lj3[item])
            self.chart.insert("", tk.END, values=tuple1)

        self.chart.pack(fill="both", expand=True)
        # 指定存储路径
        file_path = os.getcwd() + r"\GUI\generatedata\lujingji.pkl"
        # 确保文件夹存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 将实例序列化并保存到文件
        with open(file_path, 'wb') as file:
             pickle.dump(self.read, file)
