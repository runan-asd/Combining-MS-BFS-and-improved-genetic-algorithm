import os
import tkinter as tk
from tkinter import Canvas, font, filedialog
from PIL import ImageTk,Image
from zhituhanshu import Zhitu
import pickle
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
class Attack_random(tk.Frame):

    def __init__(self, root):

        super().__init__(root)

        self.font_1 = font.Font(family='楷体', size=18, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=32, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.title = tk.Label(self, text="图像设置", font=self.font_2, foreground="#072717", bg="#F8D8E8")
        self.canvas.create_window(450, 50, width=200, height=50, window=self.title)

        self.physics_chart = tk.Label(self, text="物理表导入：", font=self.font_1, foreground="#F7D787", bg="#082888")
        self.physics_name = tk.Text(self, font=self.font_1, wrap="none")
        self.physics_name.bind("<KeyPress>", lambda e: "break")
        self.physics_find = tk.Button(self, text="选择", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                      command=self.physics)
        self.canvas.create_window(100, 125, width=150, height=40, window=self.physics_chart)
        self.canvas.create_window(425, 125, width=500, height=40, window=self.physics_name)
        self.canvas.create_window(700, 125, width=50, height=40, window=self.physics_find)

        self.physics_note = tk.Label(self, text="物理表浏览", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(200, 550, width=125, height=40, window=self.physics_note)

        self.logic_chart = tk.Label(self, text="逻辑表导入：", font=self.font_1, foreground="#F7D787", bg="#082888")
        self.logic_name = tk.Text(self, font=self.font_1, wrap="none")
        self.logic_name.bind("<KeyPress>", lambda e: "break")
        self.logic_find = tk.Button(self, text="选择", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                    command=self.logic)
        self.canvas.create_window(100, 175, width=150, height=40, window=self.logic_chart)
        self.canvas.create_window(425, 175, width=500, height=40, window=self.logic_name)
        self.canvas.create_window(700, 175, width=50, height=40, window=self.logic_find)

        self.logic_note = tk.Label(self, text="逻辑表浏览", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(700, 550, width=125, height=40, window=self.logic_note)
        self.run = tk.Button(self, text="录入数据", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.run)
        self.canvas.create_window(800, 90, width=150, height=40, window=self.run)

        if self.run == 1:
            self.run_note = tk.Label(self, text="参数导入成功", font=self.font_1, foreground="#371707", bg="#D8F8F8")
            self.canvas.create_window(400, 550, width=125, height=40, window=self.run_note)

    def physics(self):
        self.path_wuli = filedialog.askopenfilename(filetypes=[("物理表", [".xls", ".xlsx"])])
        if self.path_wuli:
            self.physics_name.delete(1.0, tk.END)
            self.physics_name.insert(tk.END, self.path_wuli)
            self.read_wuli = Zhitu(self.path_wuli, [])

            self.phsics_image = Image.open("物理图.jpg")
            self.phsics_photo = ImageTk.PhotoImage(self.phsics_image.resize((400, 300)))
            self.canvas.create_image(25, 200, anchor=tk.NW, image=self.phsics_photo)
        try:
            return self.read_wuli.wulitu
        except:
            pass

    def logic(self):
        self.path_luoji = filedialog.askopenfilename(filetypes=[("逻辑表", [".xls", ".xlsx"])])
        if self.path_luoji:
            self.logic_name.delete(1.0, tk.END)
            self.logic_name.insert(tk.END, self.path_luoji)
            self.read_luoji = Zhitu([], self.path_luoji)

            self.logic_image = Image.open("逻辑图.jpg")
            self.logic_photo = ImageTk.PhotoImage(self.logic_image.resize((400, 300)))
            self.canvas.create_image(500, 200, anchor=tk.NW, image=self.logic_photo)
        try:
            return self.read_luoji.luojitu
        except:
            pass

    def run(self):
        if self.path_luoji and self.path_wuli:
            self.read = Zhitu(self.path_wuli, self.path_luoji)
        try:
            return 1
        except:
            pass

    def random(self):
        pass

class Attack_point(tk.Frame):

    def __init__(self, root):

        super().__init__(root)
        self.root=root
        self.font_1 = font.Font(family='楷体', size=18, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=32, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.title = tk.Label(self, text="攻击设置", font=self.font_2, foreground="#072717", bg="#F8D8E8")
        self.canvas.create_window(450, 50, width=200, height=50, window=self.title)

        self.disable_edges = tk.Label(self, text="失效边：", font=self.font_1, foreground="#F7D787", bg="#082888")
        # 创建一个输入框
        self.entry_edge = tk.Entry(self,font=self.font_1)

        self.get_edges = tk.Button(self, text="输入", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                      command=self.get_input_edge)
        self.canvas.create_window(100, 125, width=150, height=40, window=self.disable_edges)
        self.canvas.create_window(425, 125, width=500, height=40, window=self.entry_edge)
        self.canvas.create_window(700, 125, width=50, height=40, window=self.get_edges)

        self.i_peizhitu_show = tk.Label(self, text="原路由选择", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(200, 550, width=125, height=40, window=self.i_peizhitu_show)

        self.disable_nodes = tk.Label(self, text="失效点：", font=self.font_1, foreground="#F7D787", bg="#082888")
        self.entry_node = tk.Entry(self, font=self.font_1)
        self.get_nodes = tk.Button(self, text="输入", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                    command=self.get_input_node)
        self.canvas.create_window(100, 175, width=150, height=40, window=self.disable_nodes)
        self.canvas.create_window(425, 175, width=500, height=40, window=self.entry_node)
        self.canvas.create_window(700, 175, width=50, height=40, window=self.get_nodes)

        self.af_attack_show = tk.Label(self, text="攻击后路由", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(700, 550, width=125, height=40, window=self.af_attack_show)

    def get_input_edge(self):
        with open(os.getcwd() + r"\GUI\generatedata\inherit_I.pkl", 'rb') as file:
            self.read = pickle.load(file)
        # 获取输入框中的内容
        string_list = self.entry_edge.get().replace('（', '(').replace('）', ')').split('), (')
        self.input_edge= [tuple(map(int, item.split('，'))) for item in string_list]
        # 创建一个matplotlib图形
        self.af_attack_fig = Figure(figsize=(4, 3), dpi=100)
        ax = self.af_attack_fig.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(self.read)
        nx.draw(self.read, pos, ax=ax, node_color='skyblue', with_labels=True)

        # 更改指定边的颜色
        nx.draw_networkx_edges(self.read, pos, edgelist=self.input_edge, edge_color='red', width=4)

        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.canvas_widget = FigureCanvasTkAgg(self.af_attack_fig, master=self.canvas)
        self.canvas_widget.draw()
        self.canvas_widget.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(25, 200, anchor=tk.NW, window=self.canvas_widget.get_tk_widget())

        # 创建工具栏，并将其放置在Frame中
        self.toolbar = NavigationToolbar2Tk(self.canvas_widget, self.root)
        self.toolbar.update()

        self.canvas.create_window(25, 500, anchor=tk.NW, window=self.toolbar)
    def get_input_node(self):
        with open(os.getcwd() + r"\GUI\generatedata\inherit_I", 'rb') as file:
            self.read = pickle.load(file)
        # 获取输入框中的内容
        self.input_node = self.entry_node.get()
    def i_peizhitu_show(self):
        pass
    def af_attack_show(self):
        pass
    def random(self):
        pass