from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
datax = [str(x) for x in range(1995, 2010)]  # 横坐标必须是字符串
datay = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]

line.add_xaxis(datax)
line.add_yaxis('Price', datay, is_step=True)

line.set_global_opts(
    title_opts=opts.TitleOpts(title='美国邮费阶梯图'),
    yaxis_opts=opts.AxisOpts(min_=0.3, max_=0.45)
)

line.render('step.html')