from drawchart import cDrawChart
from itertools import izip
from math import sin

x = []
y = []

for i in range(-400, 401):
    d = i * 0.1
    x.append(d)
    if 0 == d:
        continue
    y.append( sin(d) / d)

draw = cDrawChart()

draw.AddTexts('TITLE',(50,0),mode='pixel_r',alignment=('middle','middle'),color=(255,0,0,255),font_size=22)

draw_list = list(izip(x, y))
draw.AddLine(draw_list,(0,255,0,255))

draw.RenderData()
draw.SaveImageToFile('square.png',path='./')
