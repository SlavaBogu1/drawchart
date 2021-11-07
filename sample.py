from drawchart import cDrawChart
from itertools import izip

x = []
y = []

for i in range(-10, 10):
    d = i * 0.1
    x.append(d)
    y.append(d*d)

draw = cDrawChart()

draw.AddTexts('TITLE',(50,0),mode='pixel_r',alignment=('middle','middle'),color=(255,0,0,255),font_size=22)

draw_list = list(izip(x, y))
draw.AddLine(draw_list,(0,255,0,255))

draw.RenderData()
draw.SaveImageToFile('square.png',path='./')
