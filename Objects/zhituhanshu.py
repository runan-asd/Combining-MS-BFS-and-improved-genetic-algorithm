import networkx as nx
import pandas as pd

class Zhitu():

    def __init__(self,physics,logic):
        # 绘制图形
        #nx.draw(G, with_labels=True)
        if physics != []:self.wulitu=self.zhitu(physics)
        if logic != []:self.luojitu=self.zhitu(logic)

    def zhitu(self,path):
    #读取表格数据
        self.df = pd.read_excel(path)
        self.df = self.df.iloc[:, 1:]
        self.arr=self.df.values.tolist()


    # 创建一个空的无向图
        self.G = nx.Graph()

    # 添加节点和边
        n=len(self.arr)
        for i in range(n):
            for j in range(n):
                if self.arr[i][j] >= 10:
                    self.G.add_nodes_from([i+1,j+1])
                    self.G.add_edge(i+1, j+1,weight=self.arr[i][j])
        return(self.G)
Z=Zhitu([],[])
wulitu=Z.zhitu(r"C:\Users\30282\Desktop\软件\1116启动\物理数据.xlsx")