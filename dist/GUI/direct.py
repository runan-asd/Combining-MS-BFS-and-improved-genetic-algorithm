import os
import pickle
import pandas as pd
import tkinter as tk
from tkinter import Canvas,font,filedialog,ttk
from PIL import ImageTk
from Peizhitu import Peizhitu
from direct_peizhi import pp
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import networkx as nx
class Direct(tk.Frame):

    def __init__(self, root):

        super().__init__(root)
        self.root=root

        self.font_1 = font.Font(family='楷体', size=18, weight='bold')

        self.canvas = Canvas(self, width=923, height=600)
        self.photo = ImageTk.PhotoImage(file=os.getcwd() + r"\GUI\basephoto\程序背景.gif")
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.pack()

        self.frame = ttk.Frame(self.canvas)
        self.chart = ttk.Treeview(self.frame, show="headings", columns=("1", "2", "3", "4"))
        self.chart.column("1", width=60, anchor="center")
        self.chart.heading("1", text="节点1")
        self.chart.column("2", width=60, anchor="center")
        self.chart.heading("2", text="节点2")
        self.chart.column("3", width=120, anchor="center")
        self.chart.heading("3", text="主路径")
        self.chart.column("4", width=120, anchor="center")
        self.chart.heading("4", text="备用路径")
        self.chart.pack(fill="both", expand=True)
        self.canvas.create_window(200, 350, window=self.frame)

        self.out_chart = tk.Label(self, text="输出地址：", font=self.font_1, foreground="#F7D787", bg="#082888")
        self.out_name = tk.Text(self, font=self.font_1, wrap="none")
        self.out_name.bind("<KeyPress>", lambda e: "break")
        self.out_find = tk.Button(self, text="选择", font=self.font_1, foreground="#072717", bg="#F8D8E8",
                                    command=self.shuchu)
        self.canvas.create_window(100, 175, width=150, height=40, window=self.out_chart)
        self.canvas.create_window(425, 175, width=500, height=40, window=self.out_name)
        self.canvas.create_window(700, 175, width=50, height=40, window=self.out_find)

        self.run = tk.Button(self, text="运行程序", font=self.font_1, foreground="#F7D787", bg="#082878",
                             command=self.run_)
        self.canvas.create_window(100, 50, width=100, height=40, window=self.run)
        self.logic_note = tk.Label(self, text="逻辑表浏览", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(700, 557, width=125, height=40, window=self.logic_note)

        self.logic_note = tk.Label(self, text="输出数据浏览", font=self.font_1, foreground="#371707", bg="#D8F8F8")
        self.canvas.create_window(200, 557, width=250, height=40, window=self.logic_note)

    def shuchu(self):
        self.path_ = filedialog.askdirectory()
        if self.path_:
            self.out_name.delete(1.0, tk.END)
            self.out_name.insert(tk.END, self.path_)

            '''nx.draw(self.read, with_labels=True, node_size=1000, edgecolors="black")
            plt.show()'''

            '''self.logic_image = Image.open("逻辑图.jpg")
            self.logic_photo = ImageTk.PhotoImage(self.logic_image.resize((400, 300)))
            self.canvas.create_image(500, 200, anchor=tk.NW, image=self.logic_photo)'''
        try:
            return 1
        except:
            pass

    def run_(self):
        with open(os.getcwd() + r"\GUI\generatedata\s_read.pkl", 'rb') as file:
            self.read = pickle.load(file)
        self.wulitu, self.luojitu = self.read.wulitu, self.read.luojitu
        self.zhubei = pp(self.luojitu, self.wulitu,3)
        peishow = Peizhitu()
        peishow.crI_by_peizhipaths(self.zhubei, self.wulitu)
        # 指定存储路径
        file_path = os.getcwd() + r"\GUI\generatedata\direct_I.pkl"
        # 确保文件夹存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 将实例序列化并保存到文件
        with open(file_path, 'wb') as file:
            pickle.dump(peishow, file)


        df = pd.DataFrame(self.zhubei)
        p = df.T
        p.to_excel(self.path_ + '/直接主备路径选择.xlsx')
        print(self.zhubei)
        for item in self.zhubei:
            s, e = item
            tuple1 = tuple([s, e] + self.zhubei[item])
            self.chart.insert("", tk.END, values=tuple1)
        self.chart.pack(fill="both", expand=True)

        # 创建一个matplotlib图形
        self.peizhi_fig = Figure(figsize=(4, 3), dpi=100)
        ax = self.peizhi_fig.add_subplot(111)
        # 绘制Networkx图
        pos = nx.spring_layout(peishow )
        nx.draw(peishow , pos, ax=ax, with_labels=True)

        # 将matplotlib图形嵌入到Tkinter Canvas中
        self.canvas_widget_peizhi = FigureCanvasTkAgg(self.peizhi_fig, master=self.canvas)
        self.canvas_widget_peizhi.draw()
        self.canvas_widget_peizhi.get_tk_widget().pack()

        # 使用create_window将matplotlib画布嵌入到Tkinter Canvas中
        self.canvas.create_window(500, 200, anchor=tk.NW, window=self.canvas_widget_peizhi.get_tk_widget())

        # 添加工具栏，实现放大、缩小和移动功能
        self.toolbar_peizhi = NavigationToolbar2Tk(self.canvas_widget_peizhi, self.root)
        self.toolbar_peizhi.update()
        '''self.canvas_widget_logic.get_tk_widget().pack(side=tk.RIGHT,  expand=False)'''
        self.canvas.create_window(500, 500, anchor=tk.NW, window=self.toolbar_peizhi)