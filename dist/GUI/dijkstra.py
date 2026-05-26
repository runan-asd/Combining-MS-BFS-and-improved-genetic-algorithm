import tkinter as tk
from tkinter import Canvas, font, ttk
from PIL import ImageTk
import os

class Dijkstra(tk.Frame):

    def __init__(self, root):

        super().__init__(root)

        self.font_1 = font.Font(family='楷体', size=18, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=32, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.title = tk.Label(self, text="MMBFS与Dijkstra算法的比较", font=self.font_2, foreground="#072717",
                              bg="#F8D8E8")
        self.canvas.create_window(450, 50, width=550, height=50, window=self.title)

        self.run = tk.Button(self, text="同时运行程序", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.run)
        self.canvas.create_window(800, 90, width=150, height=40, window=self.run)

        self.frame_1 = ttk.Frame(self.canvas)
        self.chart_1 = ttk.Treeview(self.frame_1, show="headings",
                                    columns=("1", "2", "3", "4", "5", "6", "7", "8", "9"))
        self.chart_1.column("1", width=40, anchor="center")
        self.chart_1.heading("1", text="编号")
        self.chart_1.column("2", width=100, anchor="center")
        self.chart_1.heading("2", text="逻辑网络边起点")
        self.chart_1.column("3", width=100, anchor="center")
        self.chart_1.heading("3", text="逻辑网络边终点")
        self.chart_1.column("4", width=100, anchor="center")
        self.chart_1.heading("4", text="主/备份链路标记")
        self.chart_1.column("5", width=100, anchor="center")
        self.chart_1.heading("5", text="配置速率(Gbps)")
        self.chart_1.column("6", width=100, anchor="center")
        self.chart_1.heading("6", text="物理网络节点1")
        self.chart_1.column("7", width=100, anchor="center")
        self.chart_1.heading("7", text="物理网络节点2")
        self.chart_1.column("8", width=100, anchor="center")
        self.chart_1.heading("8", text="物理网络节点3")
        self.chart_1.column("9", width=100, anchor="center")
        self.chart_1.heading("9", text="物理网络节点4")
        self.chart_1.pack(fill="both", expand=True)
        self.canvas.create_window(450, 225, window=self.frame_1)

        self.frame_2 = ttk.Frame(self.canvas)
        self.chart_2 = ttk.Treeview(self.frame_2, show="headings", columns=("1", "2", "3"))
        self.chart_2.column("1", width=240, anchor="center")
        self.chart_2.heading("1", text="参数比较")
        self.chart_2.column("2", width=300, anchor="center")
        self.chart_2.heading("2", text="MMBFS算法")
        self.chart_2.column("3", width=300, anchor="center")
        self.chart_2.heading("3", text="Dijkstra算法")
        self.chart_2.insert("", tk.END, values=("运行时间"))
        self.chart_2.insert("", tk.END, values=("负载均衡"))
        self.chart_2.insert("", tk.END, values=("网络阻塞率"))
        self.chart_2.insert("", tk.END, values=("链路利用率"))
        self.chart_2.pack(fill="both", expand=True)
        self.canvas.create_window(450, 475, window=self.frame_2)

    def run(self):
        for row in self.chart_1.get_children():
            self.chart_1.delete(row)
        self.chart_1.insert("", tk.END, values=(5, 6, [5, 26], [5, 6, 26]))
        self.chart_1.insert("", tk.END, values=(11, 26, [11, 7, 26], [11, 10, 26]))
        self.chart_1.insert("", tk.END, values=(22, 26, [22, 17, 23, 26], [22, 12, 10, 26]))
        self.chart_1.insert("", tk.END, values=(22, 24, [22, 17, 24], [22, 15, 24]))
        self.chart_1.insert("", tk.END, values=(19, 24, [19, 23, 24], [19, 21, 24]))
        self.chart_1.insert("", tk.END, values=(3, 5, [3, 1, 5], [3, 2, 5]))
        self.chart_1.pack(fill="both", expand=True)
        for row in self.chart_2.get_children():
            self.chart_2.delete(row)
        self.chart_2.insert("", tk.END, values=("运行时间"))
        self.chart_2.insert("", tk.END, values=("负载均衡"))
        self.chart_2.insert("", tk.END, values=("网络阻塞率"))
        self.chart_2.insert("", tk.END, values=("链路利用率"))

