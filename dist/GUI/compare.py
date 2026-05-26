import os
import tkinter as tk
from tkinter import Canvas, font
from PIL import ImageTk
import pickle
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
class Compare(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.font_1 = font.Font(family='楷体', size=18, weight='bold')
        self.font_2 = font.Font(family='微软雅黑', size=32, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.title = tk.Label(self, text="攻击设置", font=self.font_2, foreground="#072717", bg="#F8D8E8")
        self.canvas.create_window(450, 27, width=200, height=50, window=self.title)

        self.input_igraph= tk.Button(self, text="导入原始图形", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.igraph)
        self.canvas.create_window(105, 25, width=200, height=40, window=self.input_igraph)

        self.disable_edges = tk.Label(self, text="失效边：", font=self.font_1, foreground="#F7D787", bg="#082888")
        # 创建一个输入框
        self.entry_edge = tk.Entry(self, font=self.font_1)

        self.get_edges = tk.Button(self, text="输入", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                   command=self.get_input_edge)
        self.canvas.create_window(100, 70, width=150, height=40, window=self.disable_edges)
        self.canvas.create_window(275, 70, width=200, height=40, window=self.entry_edge)
        self.canvas.create_window(400, 70, width=50, height=40, window=self.get_edges)

        self.i_peizhitu_show = tk.Label(self, text="原路由选择", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(200, 550, width=125, height=40, window=self.i_peizhitu_show)

        self.run = tk.Button(self, text="开始运行", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.run)
        self.canvas.create_window(700, 25, width=200, height=40, window=self.run)

        self.disable_nodes = tk.Label(self, text="失效点：", font=self.font_1, foreground="#F7D787", bg="#082888")
        self.entry_node = tk.Entry(self, font=self.font_1)
        self.get_nodes = tk.Button(self, text="输入", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                   command=self.get_input_node)
        self.canvas.create_window(100, 110, width=150, height=40, window=self.disable_nodes)
        self.canvas.create_window(275, 110, width=200, height=40, window=self.entry_node)
        self.canvas.create_window(400, 110, width=50, height=40, window=self.get_nodes)

        self.af_attack_show = tk.Label(self, text="攻击后路由", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(700, 550, width=125, height=40, window=self.af_attack_show)

    def igraph(self):
        with open(os.getcwd() + r"\GUI\generatedata\inherit_I.pkl", 'rb') as file:
            self.read_inherit = pickle.load(file)
        with open(os.getcwd() + r"\GUI\generatedata\direct_I.pkl", 'rb') as file:
            self.read_direct = pickle.load(file)
        self.i_attack_fig_d = Figure(figsize=(3, 1.5), dpi=100)
        ax_d = self.i_attack_fig_d.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(self.read_direct)
        nx.draw(self.read_direct, pos, ax=ax_d, node_color='skyblue', with_labels=True)

        '''# 更改指定边的颜色
        nx.draw_networkx_edges(self.read_inherit, pos, ax=ax, edgelist=self.input_edge, edge_color='red', width=4)
        print(self.input_edge)'''
        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.i_canvas_widget_d = FigureCanvasTkAgg(self.i_attack_fig_d, master=self.canvas)
        self.i_canvas_widget_d.draw()
        self.i_canvas_widget_d.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(25, 150, anchor=tk.NW, window=self.i_canvas_widget_d.get_tk_widget())

        # 创建工具栏，并将其放置在Frame中
        self.i_toolbar_d = NavigationToolbar2Tk(self.i_canvas_widget_d, self.root)
        self.i_toolbar_d.update()
        self.canvas.create_window(25, 300, anchor=tk.NW, window=self.i_toolbar_d)


        self.i_attack_fig_i = Figure(figsize=(3, 1.5), dpi=100)
        ax_i = self.i_attack_fig_i.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(self.read_inherit)
        nx.draw(self.read_inherit, pos, ax=ax_i, node_color='skyblue', with_labels=True)

        '''# 更改指定边的颜色
        nx.draw_networkx_edges(self.read_inherit, pos, ax=ax, edgelist=self.input_edge, edge_color='red', width=4)
        print(self.input_edge)'''
        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.i_canvas_widget_i = FigureCanvasTkAgg(self.i_attack_fig_i, master=self.canvas)
        self.i_canvas_widget_i.draw()
        self.i_canvas_widget_i.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(25, 350, anchor=tk.NW, window=self.i_canvas_widget_i.get_tk_widget())

        # 创建工具栏，并将其放置在Frame中
        self.i_toolbar_i = NavigationToolbar2Tk(self.i_canvas_widget_i, self.root)
        self.i_toolbar_i.update()
        self.canvas.create_window(25, 500, anchor=tk.NW, window=self.i_toolbar_i)

        self.run_situation_d = tk.Label(self.root,
                                        text=f"直接选路：\n完备性{self.read_direct.fitness1}",
                                        wraplength=200)

        self.run_situation_i = tk.Label(self.root,
                                        text=f"遗传选路：\n完备性{self.read_inherit.fitness1}",
                                        wraplength=200)

        self.canvas.create_window(375, 225, width=100, height=150, window=self.run_situation_d)

        self.canvas.create_window(375, 425, width=100, height=150, window=self.run_situation_i)
    def get_input_edge(self):
        # 获取输入框中的内容
        string_list = self.entry_edge.get().replace('（', '(').replace('）', ')').replace('，', ',').split('),(')
        if len(string_list) > 1:
            self.input_edge = [tuple(map(int, item.replace('(', '').replace(')', '').split(','))) for item in string_list]
        elif len(string_list)==1:
            self.input_edge = [tuple(map(int, string_list[0].replace('(', '').replace(')', '').split(',')))]
        else:
            return

    def get_input_node(self):
        # 获取输入框中的内容
        string_list = self.entry_node.get().replace('，', ',').split(',')
        if len(string_list) >=1:
            self.input_node = list(map(int,string_list))
        else:
            return

    def run(self):
        #直接
        self.af_attack_fig_d = Figure(figsize=(3, 2), dpi=100)
        ax = self.af_attack_fig_d.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(self.read_direct)
        nx.draw(self.read_direct, pos, ax=ax, node_color='skyblue', with_labels=True)

        # 更改指定边的颜色
        nx.draw_networkx_edges(self.read_direct, pos, ax=ax, edgelist=self.input_edge, edge_color='red', width=4)
        nx.draw_networkx_nodes(self.read_direct, pos, ax=ax, nodelist=self.input_node, node_color='red')
        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.af_canvas_widget_d = FigureCanvasTkAgg(self.af_attack_fig_d, master=self.canvas)
        self.af_canvas_widget_d.draw()
        self.af_canvas_widget_d.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(500, 50, anchor=tk.NW, window=self.af_canvas_widget_d.get_tk_widget())

        # 创建工具栏，并将其放置在Frame中
        self.af_toolbar = NavigationToolbar2Tk(self.af_canvas_widget_d, self.root)
        self.af_toolbar.update()
        self.canvas.create_window(500, 250, anchor=tk.NW, window=self.af_toolbar)

        #遗传
        self.af_attack_fig_i = Figure(figsize=(3, 2), dpi=100)
        ax = self.af_attack_fig_i.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(self.read_inherit)
        nx.draw(self.read_inherit, pos, ax=ax, node_color='skyblue', with_labels=True)

        # 更改指定边的颜色
        nx.draw_networkx_edges(self.read_inherit, pos, ax=ax, edgelist=self.input_edge, edge_color='red', width=4)
        nx.draw_networkx_nodes(self.read_inherit, pos, ax=ax, nodelist=self.input_node, node_color='red')
        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.af_canvas_widget_i = FigureCanvasTkAgg(self.af_attack_fig_i, master=self.canvas)
        self.af_canvas_widget_i.draw()
        self.af_canvas_widget_i.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(500, 300, anchor=tk.NW, window=self.af_canvas_widget_i.get_tk_widget())

        # 创建工具栏，并将其放置在Frame中
        self.af_toolbar_i = NavigationToolbar2Tk(self.af_canvas_widget_i, self.root)
        self.af_toolbar_i.update()
        self.canvas.create_window(500, 500, anchor=tk.NW, window=self.af_toolbar_i)

        self.read_direct.attack_find_delect_path(self.input_edge,self.input_node)
        self.read_inherit.attack_find_delect_path(self.input_edge, self.input_node)
        zong_d=len(self.read_direct.peizhipaths)
        zong_i=len(self.read_inherit.peizhipaths)
        yewu_zhu_d=len(self.read_direct.delet_yewu_zhu)
        yewu_zhu_i = len(self.read_inherit.delet_yewu_zhu)
        yewu_zhubei_d=len(self.read_direct.delet_yewu_zhubei)
        yewu_zhubei_i = len(self.read_inherit.delet_yewu_zhubei)
        self.run_situation_d = tk.Label(self.root, text=f"直接选路：\n被破坏业务数{yewu_zhu_d}\n可切换业务数{yewu_zhu_d-yewu_zhubei_d}\n鲁棒性{1-yewu_zhubei_d/zong_d}", wraplength=200)


        self.run_situation_i = tk.Label(self.root, text=f"遗传选路：\n被破坏业务数{yewu_zhu_i}\n可切换业务数{yewu_zhu_i-yewu_zhubei_i}\n鲁棒性{1-yewu_zhubei_i/zong_i}", wraplength=200)


        self.canvas.create_window(850, 150, width=110, height=200, window=self.run_situation_d)

        self.canvas.create_window(850, 400, width=110, height=200, window=self.run_situation_i)


    def i_peizhitu_show(self):
        pass

    def af_attack_show(self):
        pass

    def random(self):
        pass