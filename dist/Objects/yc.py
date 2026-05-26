from mmbfs import mmbfs
from zhituhanshu import Zhitu
from Peizhitu import Peizhitu


import numpy as np
import random
import copy
import time

def r_generate_binary(n,p):
    binary = ["0" for i in range(n)]  # 初始化一个四位的二进制数
    ones = 0  # 记录已经生成的1的个数
    while ones < p:
        index = random.randint(0, n-1)  # 随机选择一个位置
        if binary[index] == '0':
            binary[index] = '1'
            ones += 1
    return ''.join(binary)
def generate_binary(h,n,p,weightlen):
    result=""
    for i in range(h):
        result+=r_generate_binary(n,p)+str(random.randint(0,weightlen-1 ))
    return result

class Pop():
    def __init__(self, POP_SIZE1,POP_SIZE2,POP_SIZE3, NUMBER,BINARY_SIZE, CROSSOVER_RATE, N_GENERATIONS1,N_GENERATIONS2,N_GENERATIONSm, wulitu, luojitu):
        self.POP_SIZE1 = POP_SIZE1
        self.POP_SIZE2=POP_SIZE2
        self.POP_SIZE3=POP_SIZE3
        self.NUMBER = NUMBER
        self.BINARY_SIZE=BINARY_SIZE
        self.CROSSOVER_RATE =CROSSOVER_RATE
        self.N_GENERATIONS1 =N_GENERATIONS1
        self.N_GENERATIONS2=N_GENERATIONS2
        self.N_GENERATIONSm=N_GENERATIONSm
        self.wulitu = wulitu
        self.luojitu = luojitu
        self.H=1
        self.Individuals=[]#以DNA形式储存
        self.fitness=[]
        self.key_luojiedges = []

        self.get_DNA_SIZE()
        self.get_lujingtotle()
    def get_lujingtotle(self):
        a, lj1 = mmbfs(self.luojitu,self.wulitu, self.NUMBER, mode=1)
        # a=0,失败；返回未完成的需求图
        b, lj2 = mmbfs(lj1, self.wulitu, self.NUMBER, mode=2)
        # b=1,成功；返回模式1的补充
        c, lj3 = mmbfs(self.luojitu, self.wulitu, self.NUMBER, mode=3)
        # c=0,失败；返回模式1得到的残缺路径集
        lj3.update(lj2)
        self.lujingtotle=lj3
    def get_DNA_SIZE(self):
        self.DNA_SIZE = len(self.luojitu.edges)
    def new_pop(self):
        new_pop = copy.copy(self)
        new_pop.Individuals = []
        new_pop.fitness = []
        new_pop.key_luojiedges = []
        return new_pop

    def generate_Individual1(self, DNA):
        Individual = Peizhitu()
        Individual.creatIndividual(DNA, self.lujingtotle, self.wulitu)
        self.Individuals.append(DNA)
        self.fitness.append(Individual.fitness1)
        self.key_luojiedges.extend(Individual.bluojiedges)
    def generate_Individual2(self,DNA,nlujingtotle):
        Individual = Peizhitu()
        Individual.creatIndividual(DNA, nlujingtotle,self.wulitu)
        self.Individuals.append(DNA)
        self.fitness.append(Individual.fitness1)
    def generate_pop1(self):
        #self.generate_Individual("110011001010110010101010110011001100110011001100101001101010")
        #self.generate_Individual("110011001010110010101010110011001100110011001100101010101010")
        while len(self.Individuals) < self.POP_SIZE1:
            DNA = generate_binary(self.DNA_SIZE, self.BINARY_SIZE, 2, 1)
            self.generate_Individual1(DNA)
    def generate_pop2(self,nlujingtotle):
        while len(self.Individuals) < self.POP_SIZE2:
            DNA = generate_binary(len(nlujingtotle), self.BINARY_SIZE, 2, 1)
            self.generate_Individual2(DNA,nlujingtotle)
    def generate_pop3(self,nlujingtotle):
        while len(self.Individuals) < self.POP_SIZE3:
            DNA = generate_binary(len(nlujingtotle), self.BINARY_SIZE, 2, 1)
            self.generate_Individual2(DNA,nlujingtotle)
    def generate_pop4(self,nlujingtotle,peizhi1,peizhi2):
        while len(self.Individuals) < self.POP_SIZE3:
            idx1=random.choices(range(len(peizhi1)))[0]
            idx2=random.choices(range(len(peizhi2)))[0]
            DNA =peizhi1[idx1]+peizhi2[idx2]
            self.generate_Individual2(DNA,nlujingtotle)
        '''idx = max(range(self.POP_SIZE1), key=lambda x: self.fitness[x])
        best = self.Individuals[idx]
        fitness = self.fitness[idx]
        count = 0
        for i in self.fitness:
            if i == 1:
                count += 1
        Individual = Peizhitu()
        Individual.creatIndividual(best, self.lujingtotle, self.wulitu)
        print(best, fitness, count)'''
        new_pop = self.new_pop()
        for i in range(len(self.Individuals)):
            if self.fitness[i] ==1:
                new_pop.fitness.append(self.fitness[i])
                new_pop.Individuals.append(self.Individuals[i])
        self = new_pop
        return self.Individuals
    def calculate_fitness(self,Individual):
        return Individual.fitness1+self.H*Individual.fitness2

    def select(self):  # nature selection wrt pop's fitness
        # s=sum(self.fitness)
        # prop=[f/s for f in self.fitness]
        f = []
        for i in self.fitness:
            if i > 0.6:
                f.append(i)
            else:
                f.append(0.0001)

        idx = random.choices(range(len(self.fitness)), weights=self.fitness)
        for i in idx:
            return i

    def mutation(self,child, MUTATION_RATE=0.3):
        if np.random.rand() < MUTATION_RATE:  # 以MUTATION_RATE的概率进行变异
            mutate_point = np.random.randint(0, self.DNA_SIZE - 1)  # 随机产生一个实数，代表要变异基因的位置
            e = random.randint(0, self.BINARY_SIZE)
            mutate = [1 for i in range(self.BINARY_SIZE+1)]
            mutate[e] = 0
            return child[:mutate_point * (self.NUMBER + 1)] + ''.join(list(map(str,mutate))) + child[(mutate_point+1) * (self.NUMBER + 1):]
        elif np.random.rand() < MUTATION_RATE:
            mutate_point = np.random.randint(0, self.DNA_SIZE - 1)  # 随机产生一个实数，代表要变异基因的位置
            e = random.randint(0,2)
            return child[:mutate_point * (self.NUMBER + 1)+3] + str(e) + child[(mutate_point + 1) * (self.NUMBER + 1):]
        else:
            return child
    def L_crossover_and_mutation1(self):
        #new_pop = self.new_pop()
        new_pop = copy.copy(self)
        new_pop.Individuals = []
        new_pop.fitness = []
        new_pop.key_luojiedges = []
        while len(new_pop.fitness) < self.POP_SIZE1:
            idx = self.select()
            father = self.Individuals[idx]
            child = father
            if np.random.rand() < self.CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
                mother = self.Individuals[self.select()]  # 再种群中选择另一  个个体，并将该个体作为母亲
                cross_points = np.random.randint(0, self.DNA_SIZE - 1)  # 随机产生交叉的点
                child = father[:cross_points * (self.NUMBER + 1)] + mother[cross_points * (self.NUMBER + 1):]  # 孩子得到位于交叉点后的母亲的基因
            child = self.mutation(child)  # 每个后代有一定的机率发生变异
            new_pop.generate_Individual1(child)

            if len(new_pop.fitness) < self.POP_SIZE1 and np.random.rand() < 0.05:  # 以0.05的概率引入新个体
                DNA = generate_binary(self.DNA_SIZE, self.BINARY_SIZE, 2, 3)
                new_pop.generate_Individual1(DNA)
        return new_pop
    def L_crossover_and_mutation2(self,nlujingtotle):
        new_pop = self.new_pop()
        while len(new_pop.fitness)<self.POP_SIZE2:
            idx=self.select()
            father=self.Individuals[idx]
            child=father
            if np.random.rand() < self.CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
                mother = self.Individuals[self.select()]  # 再种群中选择另一  个个体，并将该个体作为母亲
                cross_points = np.random.randint(0, len(nlujingtotle) - 1)  # 随机产生交叉的点
                child=father[:cross_points * (self.NUMBER + 1)] + mother[cross_points * (self.NUMBER + 1):]  # 孩子得到位于交叉点后的母亲的基因
            #child = self.mutation(child)  # 每个后代有一定的机率发生变异
            new_pop.generate_Individual1(child)

            if len(new_pop.fitness)<self.POP_SIZE2 and np.random.rand() < 0.05:  # 以0.05的概率引入新个体
                DNA = generate_binary(len(nlujingtotle), self.BINARY_SIZE, 2, 3)
                new_pop.generate_Individual2(DNA,nlujingtotle)
        return new_pop
    def L_crossover_and_mutation3(self,nlujingtotle):
        new_pop = self.new_pop()
        while len(new_pop.fitness)<self.POP_SIZE3:
            idx=self.select()
            father=self.Individuals[idx]
            child=father
            if np.random.rand() < self.CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
                mother = self.Individuals[self.select()]  # 再种群中选择另一  个个体，并将该个体作为母亲
                cross_points = np.random.randint(0, len(nlujingtotle) - 1)  # 随机产生交叉的点
                child=father[:cross_points * (self.NUMBER + 1)] + mother[cross_points * (self.NUMBER + 1):]  # 孩子得到位于交叉点后的母亲的基因
            #child = self.mutation(child)  # 每个后代有一定的机率发生变异
            new_pop.generate_Individual1(child)

            if len(new_pop.fitness)<self.POP_SIZE3 and np.random.rand() < 0.05:  # 以0.05的概率引入新个体
                DNA = generate_binary(len(nlujingtotle), self.BINARY_SIZE, 2, 1)
                new_pop.generate_Individual2(DNA,nlujingtotle)
        return new_pop
    def evolve1(self):
        self.generate_pop1()
        for _ in range(self.N_GENERATIONS1):
            self=self.L_crossover_and_mutation1()
            #print(sum(self.fitness)/self.POP_SIZE1)
        '''idx=max(range(self.POP_SIZE1),key=lambda x: self.fitness[x])
        best=self.Individuals[idx]
        fitness=self.fitness[idx]
        count=0
        for i in self.fitness:
            if i ==1:
                count+=1
        Individual = Peizhitu()
        Individual.creatIndividual(best, self.lujingtotle, self.wulitu)
        print(best,fitness,count)
        new_pop=self.new_pop()
        for i in range(len(self.Individuals)):
            if self.fitness[i]>0.5:
                new_pop.fitness.append(self.fitness[i])
                new_pop.Individuals.append(self.Individuals[i])
        self=new_pop'''
    def evolve2(self,nlujingtotle):
        self.generate_pop2(nlujingtotle)
        for _ in range(self.N_GENERATIONS2):
            self=self.L_crossover_and_mutation2(nlujingtotle)
        '''idx=max(range(self.POP_SIZE2),key=lambda x: self.fitness[x])
        best=self.Individuals[idx]
        fitness=self.fitness[idx]
        count = 0
        for i in self.fitness:
            if i == 1:
                count += 1
        print(best,fitness,count)
        #检验'''
        new_Individuals=[]
        for i in range(len(self.fitness)):
            if self.fitness[i]==1:
                new_Individuals.append(self.Individuals[i])
        return new_Individuals
    def evolve3(self,nlujingtotle,peizhi1,peizhi2):
        self.generate_pop4(nlujingtotle,peizhi1,peizhi2)
        for _ in range(self.N_GENERATIONS3):
            self=self.L_crossover_and_mutation3(nlujingtotle)
        '''idx=max(range(self.POP_SIZE3),key=lambda x: self.fitness[x])
        best=self.Individuals[idx]
        fitness=self.fitness[idx]
        count = 0
        for i in self.fitness:
            if i == 1:
                count += 1
        print(best,fitness,count)
        #检验'''
        new_Individuals = []
        for i in range(len(self.fitness)):
            if self.fitness[i] == 1:
                new_Individuals.append(self.Individuals[i])
        return new_Individuals
    def key_graph(self):
        self=self.new_pop()
        self.evolve1()
        k=len(self.key_luojiedges)//self.POP_SIZE1-2
        #print(k)
        luojiedges= random.sample(self.key_luojiedges,k=k)
        #print(luojiedges)
        nlujingtotle1= {}
        nlujingtotle2={}
        nlujingtotle3={}
        for edge in self.lujingtotle:
            if edge in luojiedges:
                nlujingtotle1[edge] = self.lujingtotle[edge]
                nlujingtotle3[edge] = self.lujingtotle[edge]
            else:
                i,j=edge
                nedge=i,j
                if nedge in luojiedges:
                    nlujingtotle1[edge]=self.lujingtotle[edge]
                    nlujingtotle3[edge] = self.lujingtotle[edge]
        for edge in self.lujingtotle:
            if edge in luojiedges:
                continue
            i, j = edge
            nedge = i, j
            if nedge in luojiedges:
                continue
            nlujingtotle2[edge]=self.lujingtotle[edge]
            nlujingtotle3[edge]=self.lujingtotle[edge]
        '''print(len(nlujingtotle1))
        print(len(nlujingtotle2))
        print(len(nlujingtotle3))'''
        self=self.new_pop()
        peizhi1=self.evolve2(nlujingtotle1)
        #print(peizhi1)
        self=self.new_pop()
        peizhi2=self.evolve2(nlujingtotle2)
        self=self.new_pop()

        #self.evolve3(nlujingtotle3,peizhi1,peizhi2)
        base=self.generate_pop4(nlujingtotle3, peizhi1, peizhi2)
        self = self.new_pop()
        self.lujingtotle=nlujingtotle3
        for DNA in base:
            self.generate_Individualm(DNA)
        for i in range(self.N_GENERATIONSm):
            for DNA in self.Individuals:
                DNA=self.mutationm(DNA)
                self.generate_Individualm(DNA)
        sorted_id1 = sorted(range(len(self.fitness)), key=lambda k: self.fitness[k], reverse=True)
        new_pop=self.new_pop()
        new_pop.lujingtotle=nlujingtotle3
        for id in sorted_id1[:100]:
            if (self.fitness[sorted_id1[0]] - self.fitness[id]) > 5:
                break
            new_pop.generate_Individualend(self.Individuals[id])
        sorted_id2 = sorted(range(len(new_pop.fitness)), key=lambda k: new_pop.fitness[k], reverse=True)
        best=new_pop.Individuals[sorted_id2[-1]]
        Individual = Peizhitu()
        Individual.creatIndividual(best, self.lujingtotle, self.wulitu)
        return Individual.fitness1,Individual.fitness2,Individual.fitness3,Individual.peizhipaths,Individual.pweights,Individual
    def generate_Individualm(self,DNA):
        Individual = Peizhitu()
        Individual.creatIndividual(DNA, self.lujingtotle, self.wulitu)
        if Individual.fitness1==1:
            self.Individuals.append(DNA)
            self.fitness.append(Individual.fitness2)
    def generate_Individualend(self,DNA):
        Individual = Peizhitu()
        Individual.creatIndividual(DNA, self.lujingtotle, self.wulitu)
        if Individual.fitness1==1:
            self.Individuals.append(DNA)
            self.fitness.append(Individual.fitness3)
    def mutationm(self,DNA):
        for i in range(3):
            mutate_point = np.random.randint(0, self.DNA_SIZE - 1)  # 随机产生一个实数，代表要变异基因的位置
            e = random.randint(0,2)
            DNA=DNA[:mutate_point * (self.NUMBER + 1)+3] + str(e) + DNA[(mutate_point + 1) * (self.NUMBER + 1):]
        return DNA

class Yichuan():
    def __init__(self, wulitu, luojitu):
        NUMBER = 3
        BINARY_SIZE = 3
        POP_SIZE1 = 300
        POP_SIZE2 = 1000
        POP_SIZE3 = 3000
        CROSSOVER_RATE = 0.5
        N_GENERATIONS1 = 10
        N_GENERATIONS2 = 10
        N_GENERATIONSm = 10


        self.pop = Pop(POP_SIZE1, POP_SIZE2, POP_SIZE3, NUMBER, BINARY_SIZE, CROSSOVER_RATE, N_GENERATIONS1, N_GENERATIONS2,
                  N_GENERATIONSm, wulitu, luojitu)
    def run(self):
        self.answer=self.pop.key_graph()
        return self.pop.key_graph()[3]
    def show(self):
        return self.pop.key_graph()[-1]
if __name__ == '__main__':
    tu = Zhitu(r"C:\Users\30282\Desktop\软件\软件\物理数据.xlsx",r"C:\Users\30282\Desktop\软件\软件\逻辑数据.xlsx")
    yiyic=Yichuan(tu.wulitu, tu.luojitu)
    answer=yiyic.run()
    print (answer)

