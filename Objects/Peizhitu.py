import networkx as nx
from fitness import calculate_fitness

'''binarysize==3'''
class Peizhitu(nx.Graph):
    def __init__(self, incoming_graph_data=None,**attr):
        super().__init__(incoming_graph_data=None, **attr)
        self.weights=[10,15,20]
        self.peizhipaths ={}
        self.pweights={}
        self.bluojiedges=[]#未完成的逻辑边
        self.delet_yewu_zhu = []
        self.delet_yewu_zhubei = []
    def __add_nedge(self, nedge, weight):
        '''
        :param G: 作用的图
        :param nedge: 将添加的边
        :param weight: nedge的权重
        :return: None
        '''
        i, j = nedge
        if i >j:
            i,j=j,i
        if (i,j) not in self.edges:
            self.add_edge(i,j, weight=weight)
        else:
            # 获取边缘数据
            edge_data = self.get_edge_data(i, j)
            # 更新边缘数据
            edge_data['weight'] += weight
        '''
        使用示例：
        # 创建一个空的无向图
        G = nx.Graph()
        # 添加两次相同的边，并更新边缘数据
        G.add_edge(1, 2, weight=3)
        add_nedge(G, (1, 2), 2)
        # 打印更新后的边缘数据
        print(G[i][j])
        '''
    def __add_npath(self, npath, weight):
        e=zip(npath[0:-1],npath[1:])
        for nedge in e:
            #print(nedge)
            self.__add_nedge( nedge, weight)
    def translate(self,edge,binary, paths,weights):
        weight=weights[int(binary[-1:])]
        self.peizhipaths[edge]=[]
        self.pweights[edge]=weight
        for i in range(len(binary)-1):
            if binary[i]=="1":
                self.peizhipaths[edge].append(paths[i])
                self.__add_npath(paths[i],weight)
    def attack_find_delect_path(self,edges,nodes):
        self.delet_yewu_zhu = []
        self.delet_yewu_zhubei = []
        for yewu in self.peizhipaths:
            flag=0
            zhu=self.peizhipaths[yewu][0]
            bei=self.peizhipaths[yewu][1]
            for i in zhu:
                if i in nodes:
                    flag=1
                    break
            zhue = zip(zhu[0:-1], zhu[1:])
            for i in zhue:
                if i in edges:
                    flag=1
                    break
                a,b=i
                i=(b,a)
                if i in edges:
                    flag=1
                    break
            if flag==1:
                beie=zip(bei[0:-1],bei[1:])
                for j in beie:
                    if j in edges:
                        flag=2
                        break
                    a,b=j
                    j=(b,a)
                    if j in edges:
                        flag=2
                        break
                for j in bei:
                    if j in nodes:
                        flag=2
                        break
            if flag>=1:
                self.delet_yewu_zhu.append(yewu)
            if flag==2:
                self.delet_yewu_zhubei.append(yewu)
    def crI_by_peizhipaths(self,peizhipaths,wulitu):
        self.wulitu=wulitu
        self.peizhipaths=peizhipaths
        for edge in self.peizhipaths:
            for path in self.peizhipaths[edge]:
                self.__add_npath(path,10)
        self.fitnessone()
    def creatIndividual(self,DNA,lujingtotle,wulitu):
        self.lujingtotle=lujingtotle
        self.wulitu=wulitu
        edges = [edge for edge in self.lujingtotle]
        '''binarysize==3'''
        for i in range(len(DNA) // 4):  # 针对以4位2进制组成的基因
            binary=DNA[(i * 4): (i + 1) * 4]
            edge=edges[i]
            self.translate(edge,binary,self.lujingtotle[edge],self.weights)
        self.fitnessone()
        self.fitnesstwo()
        self.fitnessthree()
    def fitnessone(self):
        '''完备性指标'''
        self.find_graphs()
        fitness1=1-len(self.bluojiedges)/len(self.peizhipaths)
        if fitness1==0:
            fitness1=0.0001
        self.fitness1=fitness1
        '''wuli=nx.get_edge_attributes(wulitu, "weight")
        peizhi=nx.get_edge_attributes(self, "weight")
        fitness2=0
        for edge in peizhi:
            try:
                if peizhi[edge]>wuli[edge]:
                    continue
            except:
                i,j=edge
                exedge=(j,i)
                if peizhi[edge]>wuli[exedge]:
                    continue
            fitness2+=1
        self.fitness2=fitness2/len(peizhi)'''
    def fitnesstwo(self):
        '''总代价指标'''
        sum=0
        for edge in self.pweights:
            sum+=self.pweights[edge]-10
        self.fitness2=sum/len(self.pweights)
    def fitnessthree(self):
        '''边均衡度指标'''
        fitness3=calculate_fitness(self.pweights)
        self.fitness3=fitness3
    def find_graphs(self):
        wuli = nx.get_edge_attributes(self.wulitu, "weight")
        peizhi = nx.get_edge_attributes(self, "weight")
        bedges=[]
        for edge in peizhi:
            try:
                if peizhi[edge] > wuli[edge]:
                    bedges.append(edge)
            except:
                i, j = edge
                exedge = (j, i)
                if peizhi[edge] > wuli[exedge]:
                    bedges.append(edge)
        for luojiedge in self.peizhipaths:
            count=0
            for path in self.peizhipaths[luojiedge]:
                e = zip(path[0:-1], path[1:])
                if count==1:
                    break
                for edge in e:
                    if edge in bedges:
                        self.bluojiedges.append(luojiedge)
                        count=1
                        break
    '''def return_DNA(self,new_lujingtotle):
        i=0
        for edge in self.lujingtotle:'''

if __name__=="__main__":
    from zhituhanshu import luojitu
    from zhituhanshu import wulitu
    from mmbfs import mmbfs
    import random
    import time

    start = time.perf_counter()

    def get_lujingtotle(wulitu, luojitu):
        a, lj1 = mmbfs(luojitu, wulitu,3, mode=1)
        # a=0,失败；返回未完成的需求图
        b, lj2 = mmbfs(lj1, wulitu, 3, mode=2)
        # b=1,成功；返回模式1的补充
        c, lj3 = mmbfs(luojitu, wulitu, 3, mode=3)
        # c=0,失败；返回模式1得到的残缺路径集
        lj3.update(lj2)
        return lj3
    def r_generate_binary(n, p):
        binary = ["0" for i in range(n)]  # 初始化一个四位的二进制数
        ones = 0  # 记录已经生成的1的个数
        while ones < p:
            index = random.randint(0, n - 1)  # 随机选择一个位置
            if binary[index] == '0':
                binary[index] = '1'
                ones += 1
        return ''.join(binary)


    def generate_binary(h, n, p, weightlen):
        result = ""
        for i in range(h):
            result += r_generate_binary(n, p) + str(random.randint(0, weightlen - 1))
        return result

    p=Peizhitu()
    lj3 = get_lujingtotle(wulitu, luojitu)
    DNA = "11001100"+generate_binary(10, 3, 2, 1)+"1100"+generate_binary(2, 3, 2, 1)+"1010"
    p.creatIndividual(DNA, lj3,wulitu)


