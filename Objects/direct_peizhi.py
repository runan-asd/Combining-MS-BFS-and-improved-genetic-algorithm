from direct_lujing import *
from mmbfs import mmbfs
from zhituhanshu import Zhitu
from Peizhitu import Peizhitu

def get_lujingtotle(luojitu,wulitu,NUMBER):
    a, lj1 = mmbfs(luojitu, wulitu, NUMBER, mode=1)
    # a=0,失败；返回未完成的需求图
    b, lj2 = mmbfs(lj1, wulitu,NUMBER, mode=2)
    # b=1,成功；返回模式1的补充
    c, lj3 = mmbfs(luojitu, wulitu,NUMBER, mode=3)
    # c=0,失败；返回模式1得到的残缺路径集
    lj3.update(lj2)
    return lj3

def pp(luojitu,wulitu,NUMBER):
    lujingtotle =get_lujingtotle(luojitu,wulitu,NUMBER)
    paths = {}
    for edge in lujingtotle:
        i,j=edge
        if i>j:
            edge=(j,i)
        path = xuanlu(edge, lujingtotle)
        if path == 0:
            print(edge)
        else:
            paths[edge] = path
    return paths
if __name__=="__main__":
    import time

    tu = Zhitu(r"C:\Users\30282\Desktop\软件\软件\物理数据.xlsx", r"C:\Users\30282\Desktop\软件\软件\逻辑数据.xlsx")

    start = time.perf_counter()
    peizhipaths=pp( tu.luojitu,tu.wulitu,3)
    endtime = time.perf_counter()
    print('运行时间为：{}秒'.format(endtime - start))

    print(peizhipaths)
    peishow=Peizhitu()
    peishow.crI_by_peizhipaths(peizhipaths,tu.wulitu)
    print(peishow.fitness1)