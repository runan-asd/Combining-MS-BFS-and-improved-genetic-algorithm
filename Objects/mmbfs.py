'''
作者：Asd
一种针对多点对生成链路分离度高的路径集算法
'''
import networkx as nx
#寻边函数
def findedge(i,j):
    if i>j:
        return (j,i)
    return (i,j)

def mmbfs(Luojitu,Wulitu,number,limit=4,mode=1):
    '''
    :param Luojitu NetworkX graph为逻辑图
    :param Wulitu  NetworkX graph为物理图
    :param number  int           为单点对要求的路径数量
    :param limit   int           为单点向下最大搜索次数
    :param mode    int           为模式
        1：不允许以其他逻辑节点为中转点
        2：允许以其他逻辑节点为中转点
        3：同模式 1 返回（~，路径集）
    :return (int 1,dict)/(int 2,NetworkX graph)
            完成路径需求 ：（1,路径集）
          未完成路径需求 ：（2,未满足的逻辑需求图）
    '''
    L=Luojitu.copy()
    W=Wulitu.copy()
    #前驱总编
    predecessorstotle=dict()
    #当前节点总编
    dangqiantotle=dict()
    #路径总编
    lujingtotle=dict()

    #初始化
    Luoji=tuple(L.nodes)
    for i in L.edges():
        a,b=i
        if a>b:
            a,b=b,a
        h=(a,b)
        lujingtotle[h]=[]
    for i in L.nodes:
        predecessorstotle[i]={i:None}
        dangqiantotle[i]=set([i])
    #遍历程序
    count=0
    while L.edges :
        '''
        检查点一
        print(L.nodes)
        '''
        if count>=limit:
            if mode==3:
                return 0,lujingtotle
            else:
                return 0,L
        count+=1
        #每个根节点
        for i in L.nodes:
            tuple1=tuple(L[i])
            '''
            检查点二
            print(tuple1)
            '''
            #向下进行一轮搜索
            p=dangqiantotle[i].copy()
            dangqiantotle[i].clear()
            for source in p:
                for node in W[source]:
                    #不重复搜索
                    if node in predecessorstotle[i]:
                        continue
                    if mode==1 or mode==3:
                    # 不以逻辑节点为中转点
                        if node in tuple1 and count==1 and i<node:
                            lujingtotle[(i,node)].append([i,node])
                        if node in Luoji:
                            continue
                    #设置当前节点前驱
                    predecessorstotle[i][node]=source
                    #检查是否产生路径
                    for j in tuple1:
                        if node in dangqiantotle[j]:
                            #返回路径
                            paths = []
                            currents = node
                            while currents is not None:
                                paths.append(currents)
                                currents = predecessorstotle[i][currents]
                             # 将路径反转，使其按起始节点到目标节点的顺序排列
                            paths.reverse()
                            pathe=[]
                            currente = predecessorstotle[j][node]
                            while currente is not None:
                                 pathe.append(currente)
                                 currente = predecessorstotle[j][currente]
                            path=paths+pathe
                            if mode==2 and not( nx.is_simple_path(W, path)):#保证模式2不出现多余路径
                                continue
                            #标准化
                            if i>j:
                                path.reverse()
                            edge=findedge(i,j)
                            lujingtotle[edge].append(path)
                            #除去已满足路径需要的逻辑边
                            if len(lujingtotle[edge])==number:
                                L.remove_edge(i,j)
                    #将此节点加入当前节点
                    dangqiantotle[i].add(node)
        #检查逻辑节点是否还有度
        remove=[]
        for i in L.nodes:
            if len(L[i])==0:
                remove.append(i)
        L.remove_nodes_from(remove)
    return 1,lujingtotle

if __name__=="__main__":
    import sys
    import os
    import matplotlib.pyplot as plt

    sys.path.append(os.getcwd() + "/GUI")
    sys.path.append(os.getcwd() + "/Objects")
    from zhituhanshu import Zhitu
    tu = Zhitu(r"C:\Users\30282\Desktop\软件\软件\物理数据.xlsx",r"C:\Users\30282\Desktop\软件\软件\逻辑数据.xlsx")
    wulitu,luojitu=tu.wulitu, tu.luojitu
    import time

    start = time.perf_counter()
    a, lj1 = mmbfs(luojitu, wulitu, 3, mode=1)
    print(a,lj1.edges)#a=0,失败；返回未完成的需求图
    b, lj2 = mmbfs(lj1, wulitu, 3, mode=2)
    print(b,len(lj2))#b=1,成功；返回模式1的补充
    print(lj2[(22,26)])
    c, lj3 = mmbfs(luojitu, wulitu, 3, mode=3)
    print(c,len(lj3))#c=0,失败；返回模式1得到的残缺路径集
    print(lj3[(22,26)])
    lj3.update(lj2)
    print(lj3[(22,26)])#更新成功完成需求
    print(lj3)
    #或者选用完整路径完成需求
    '''h=list(nx.all_simple_paths(wulitu,22,26,4))
    l = tuple(luojitu.nodes)
    for path in h:
        for i in l:
            if i in path[1:-1]:
                continue
        print(path)'''
    end = time.perf_counter()
    print('运行时间为：{}秒'.format(end - start))