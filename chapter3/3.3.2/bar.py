from pyecharts.charts import Bar
import pyecharts.options as opt
import csv

bar = Bar()
filename = 'hot-dog-contest-winners.csv'
datax = []
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            datay.append(float(datarow[2]))  # 数据集中读取的数据为字符串，需要转换为float型
            datax.append(datarow[0])  # pyrcharts中横坐标要求为字符串，故不进行转换
bar.add_xaxis(datax)
bar.add_yaxis('A', datay, label_opts=opt.LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=opt.TitleOpts(title='柱状图示例'),
)
bar.render('bar.html')