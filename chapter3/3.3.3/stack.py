from pyecharts.charts import Bar
import pyecharts.options as opt
import csv

bar = Bar()
filename = 'hot-dog-places.csv'
datax = []
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        datax.append(datarow)
x = datax[0]
y1 = [float(x) for x in datax[1]]
y2 = [float(x) for x in datax[2]]
y3 = [float(x) for x in datax[3]]

bar.add_xaxis(x)
bar.add_yaxis('A', y1, stack=1)
bar.add_yaxis('B', y2, stack=1)
bar.add_yaxis('C', y3, stack=1)
bar.set_series_opts(label_opts=opt.LabelOpts(is_show=False))

bar.render('stack.html')
