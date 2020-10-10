import csv
import matplotlib.pyplot as plt

filename = 'subscribers.csv'
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            datay.append(int(datarow[1]))  # 数据集中读取的数据为字符串，需要转换为int型

xa = list(range(1, len(datay)+1))
plt.scatter(xa, datay, s=50, c='r', marker='o', alpha=0.5)
plt.show()