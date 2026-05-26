import networkx as nx

#计算逻辑边富余度
def Lredundancy(pweight,Lweight=10):
    result=(pweight-Lweight)/Lweight
    return result
#计算方差
def calculate_variance(lst):
    '''
    检查点
    print(lst)
    '''
    mean = sum(lst) / len(lst)
    squared_diffs = [(x - mean) ** 2 for x in lst]
    variance = sum(squared_diffs) / len(lst)
    return 1/(variance+1)
#计算适应度
def calculate_fitness(pweights):
    #默认逻辑需求全为10
    Lweight=10
    list=[]
    for edge in pweights:
        list.append(Lredundancy(pweights[edge],Lweight))
    fitness=calculate_variance(list)
    return fitness
if __name__=="__main__":
    import networkx as nx
    from zhituhanshu import luojitu
    peizhitu=nx.Graph()
    peizhitu.add_edges_from(luojitu.edges)
    nx.set_edge_attributes(peizhitu,30,"weight")
    fitness=calculate_fitness(peizhitu)
    print(fitness)