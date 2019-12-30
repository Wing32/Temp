import numpy as np
import time
import matplotlib.pyplot as plt

# 这个是用来做测试到底哪个指数会使得我们的鲲 增长最快
# 总体增长率 用变化量/变化次数

def rule(num, rate):
    # 这个是每次磨炼的规则
    # 每一次磨炼 有成功和失败
    # 如果成功的话，就会增加num*rate 那么多
    # 如果失败的话，就会减少num*(rate)的数量
    this_rate = np.random.rand(1)
    if this_rate >= rate:
        total_num = num * (1 + rate)
    else:
        total_num = num * (1 - rate)
    return total_num

# 初始化数据
num = 1000.0
rate = 0.40
print(rate)
# 磨炼次数 
MAX = 1000
for i in range(MAX):
    num = rule(num,rate)
    print(i,num,'\r',end= '')
    time.sleep(0.01)


