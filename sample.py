from drawchart import cDrawChart
from itertools import izip
from math import sin

def Sin1_X():
    x = []
    y = []

    for i in range(-400, 401):
        d = i * 0.1
        x.append(d)
        if 0 == d:
            continue
        y.append( sin(1/d))
    result = list(izip(x, y))
    return result


def SinX_X():
    x = []
    y = []

    for i in range(-400, 401):
        d = i * 0.1
        x.append(d)
        if 0 == d:
            continue
        y.append( sin(d) / d)
    result = list(izip(x, y))
    return result

draw = cDrawChart()
draw.AddTexts('Simple graphics. Samples',(50,2),mode='pixel_r',alignment=('middle','middle'),color=(255,0,0,255),font_size=22)


draw_list = SinX_X()
draw.AddLine(draw_list,(60,160,60,255))
draw.AddTexts('Sin(x)/x',(10,10),mode='pixel_r',alignment=('left','top'),color=(60,160,60,255),font_size=16)

draw_list = Sin1_X()
draw.AddLine(draw_list,(0,0,255,255))
draw.AddTexts('Sin(1/x)',(10,14),mode='pixel_r',alignment=('left','top'),color=(0,0,255,255),font_size=16)


draw.ConfigAxis() #default axis - left/bottom
draw.RenderData()
draw.SaveImageToFile('square.png',path='./')

draw.Resize((1920,1080))
draw.RenderData()
draw.SaveImageToFile('square1920.png',path='./')
del draw

draw = cDrawChart()
draw_color=(60,160,60,255)
x = []
y = []
x.append(0)
y.append(700)
x.append(100)
y.append(700)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('LEFT_BOTTOM_TEXT',(0,700),mode='data',alignment=('left','bottom'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(0)
y.append(400)
x.append(100)
y.append(400)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('LEFT_MIDDLE_TEXT',(0,400),mode='data',alignment=('left','middle'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(0)
y.append(200)
x.append(100)
y.append(200)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('LEFT_TOP_TEXT',(0,200),mode='data',alignment=('left','top'),color=draw_color,font_size=16)
del x[:]
del y[:]

#to have a scale from (0,0)
x.append(0)
y.append(0)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,(0,0,0,255))
del x[:]
del y[:]

#----------
draw_color=(160,60,60,255)
x.append(300)
y.append(700)
x.append(400)
y.append(700)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('MIDDLE_BOTTOM_TEXT',(300,700),mode='data',alignment=('middle','bottom'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(300)
y.append(400)
x.append(400)
y.append(400)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('MIDDLE_MIDDLE_TEXT',(300,400),mode='data',alignment=('middle','middle'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(300)
y.append(200)
x.append(400)
y.append(200)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('MIDDLE_TOP_TEXT',(300,200),mode='data',alignment=('middle','top'),color=draw_color,font_size=16)
del x[:]
del y[:]

#----------
draw_color=(60,60,160,255)
x.append(600)
y.append(700)
x.append(700)
y.append(700)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('RIGHT_BOTTOM_TEXT',(600,700),mode='data',alignment=('right','bottom'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(600)
y.append(400)
x.append(700)
y.append(400)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('RIGHT_MIDDLE_TEXT',(600,400),mode='data',alignment=('right','middle'),color=draw_color,font_size=16)
del x[:]
del y[:]

x.append(600)
y.append(200)
x.append(700)
y.append(200)
draw_line = list(izip(x, y))
draw.AddLine(draw_line,draw_color)
draw.AddTexts('RIGHT_TOP_TEXT',(600,200),mode='data',alignment=('right','top'),color=draw_color,font_size=16)
del x[:]
del y[:]

draw.RenderData()
draw.SaveImageToFile('lines.png',path='./')

