'''
作者：Asd
一种直接选择主备路径的算法
'''

def xuanlu(edge,lujingtotle):
    '''
    :param edge (int,int)        标准边，前点小于后点
    :param lujingtotle dict      包含标准边的路径集字典
    :return:            成功：主备路径元组
                        失败：(0,0)
    '''
    count=0
    l=lujingtotle[edge]
    while count < len(l):
        p=l[count]
        for i in range(count+1,len(l)):
            path=l[i]
            for node in path[1:-1]:#保证物理分离
                if node in p[1:-1]:
                    break
            else:
                return [p,path]
        count+=1
    return 0

if __name__=="__main__":
    lujingtotle={ (16, 20): [ [16, 21, 20],[16, 21, 19, 20], [16, 24, 23, 19, 20]]}
    paths={}
    for edge in lujingtotle:
        path=xuanlu(edge,lujingtotle)
        if path==0:
            print(edge)
        else:
            paths[edge] =path
    print(paths)


