from pyecharts.charts import Page
from pyecharts.charts import Bar
import pyecharts.options as opt
import csv

page = Page()

bar1 = Bar()
filename1 = 'hot-dog-contest-winners.csv'
data1x = []
data1y = []
with open(filename1) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            data1y.append(float(datarow[2]))  # 数据集中读取的数据为字符串，需要转换为float型
            data1x.append(datarow[0])  # pyrcharts中横坐标要求为字符串，故不进行转换
bar1.add_xaxis(data1x)
bar1.add_yaxis('A', data1y, label_opts=opt.LabelOpts(is_show=False))
bar1.set_global_opts(
    title_opts=opt.TitleOpts(title='柱状图示例'),
)

bar2 = Bar()
filename = 'hot-dog-places.csv'
data2x = []
data2y = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        data2x.append(datarow)
x2 = data2x[0]
y21 = [float(x) for x in data2x[1]]
y22 = [float(x) for x in data2x[2]]
y23 = [float(x) for x in data2x[3]]

bar2.add_xaxis(x2)
bar2.add_yaxis('A', y21, stack=1)
bar2.add_yaxis('B', y21, stack=1)
bar2.add_yaxis('C', y21, stack=1)
bar2.set_series_opts(label_opts=opt.LabelOpts(is_show=False))

page.add(bar1)
page.add(bar2)

page.render('page.html')
