import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

filename = 'unemployment-rate-1948-2010.csv'
ya = []
xa = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        for datarow in reader:
            if reader.line_num != 1:
                ya.append(float(datarow[3]))
                xa.append(int(datarow[1]))
except:
    print('Error reading csv file')
    sys.exit(-1)
plt.figure()  # 创建一个图像
'''
在图像上画一个散点图，其中：
s：size，点的大小；
c：color，点的颜色；
marker：点的形状；
alpha：点的透明度；
'''
plt.scatter(xa[:], ya[:], s=10, c='g', marker='o', alpha=0.5)
'''
在图像上画一条拟合曲线，其中：
np.polyfit用于求拟合函数；
deg：拟合的多项式阶次；
np.polyval根据拟合函数求出对应的拟合曲线；
'''
poly = np.polyfit(xa, ya, deg=3)
plt.plot(xa, np.polyval(poly, xa))
plt.show()