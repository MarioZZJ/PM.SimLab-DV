import csv
import matplotlib.pyplot as plt

filename = 'world-population.csv'
datax = []
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num !=1:
            print(reader.line_num, datarow)
            # 从csv文件中读取的数据为字符串，需要转换为int型
            datax.append(int(datarow[0]))
            datay.append(int(datarow[1]))
plt.plot(datax, datay)
plt.show()