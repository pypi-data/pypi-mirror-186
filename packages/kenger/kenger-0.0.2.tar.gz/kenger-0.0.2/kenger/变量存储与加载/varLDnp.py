import numpy as np


#设置递归深度，为了解决数据存储问题
import sys
sys.setrecursionlimit(10000)




def loadData(filePath):
    data=np.load(filePath)
    return data

def saveData(data, filePath):
    np.save(data, filePath)


if __name__ == '__main__':
    x =[i for i in range(100)]
    np.save('x.npy', x)

    b = np.load('x.npy')
    print(b)