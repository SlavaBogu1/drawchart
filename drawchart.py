import PIL
from PIL import Image, ImageFont, ImageDraw
from itertools import izip
import config
import operator


class cDrawChart(object):
    """convert data time from text labels
        calc deltas
    """
    def __init__(self,width=800,height=600,margin=config.margin,fg_color=(0,0,255,255),bg_color=(255,255,255,255)): #margin left,right,top,bottom
        self.lines = [] #( ((x[],y[]), color),..)
        self.texts = [] #( ('text',(x,y),text_size,mode,alignment,font_type,font_size,color), ..)   mode: pixel_a / pixel_r / data - how to calculate coordinates, alignment - ('left','top')
                        #      0     1      2        3       4          5       6        7
        self.data = []
        self.scale_x =0
        self.scale_y =0
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_x = 0
        self.margin = margin
        self.width = width
        self.height = height
        self.draw_color = fg_color
        self.bgc = bg_color
        self.image = 0
        self.draw_area = 0
        self.onscreen_texts = [] # ( ("text",(coor_x,coor_y),(scale_x,scale_y),align,font,size,color) , (...) )
                                 #       0           1              2            3    4    5     6        

    def Resize(self,size,margin='default'):
        if 'default' != margin:
            self.margin = margin
        self.width = size[0]
        self.height = size[1]
        
                                 
    def AddTexts(self,text,coor,mode='default',alignment='default',font_type='default',font_size=config.chart_font_size,color='default'):
        if 'default' == mode:
            mode = 'data'
        if 'default' == alignment:
            alignment = ('left','top') #coordinates are the left bottom corner of the text
        if 'default' == font_type:
            font_type = config.chart_font_type
        if 'default' == color:
            color = config.text_color

        #get font sizes
        chart_font = ImageFont.truetype(font_type, font_size)
        text_size = chart_font.getsize(text)
        

        #add into the list for rendering
        self.texts.append((text,coor,text_size,mode,alignment,font_type,font_size,color))
            
    def AddLine(self,data,color='default'):
        if 'default' == color:
            color = self.draw_color
        self.lines.append((data,color))
        return 0

    def RenderLines(self):
        for line in self.lines:
            x,y = zip(*line[0])
            #normilize x and y coordinates: substract the minimum x and y from all lines.
            xn = [self.min_x] * len(x)
            yn = [self.min_y] * len(y)
            draw_x = list(map(operator.sub,x,xn))
            draw_y = list(map(operator.sub,y,yn))
            #normilize x and y coordinates: multiply by scale to make them fit into the drawing area size.  Min_x = 0.0  Max_x = width-margin, same for y.
            xn = [self.scale_x] * len(x)
            yn = [self.scale_y] * len(y)
            draw_x = list(map(operator.mul,draw_x,xn))
            draw_y = list(map(operator.mul,draw_y,yn))
            #normilize x and y coordinates: add left margin (in pixels) to x and move move y to bottom of the screen
            xn = [self.margin[0]] * len(x)
            yn = [self.height + self.margin[3]] * len(y)
            draw_x = list(map(operator.add,draw_x,xn))
            draw_y = list(map(operator.sub,yn,draw_y))
            self.draw_area.line(list(izip(draw_x, draw_y)), fill=line[1], width=config.chart_pen_width)        

    def RenderTexts(self):
        # 0 - text to print
        # 1 - coordinates (can be in thre modes
        # 2 - size of text
        # 3 - coordinate calculation mode.  'data' - default - need to scale as a line, pixel_a - absolute pixel, pixel_r - pixel in % to size
        # 4 - alignment of text to the render coordinate,  left/middle,right top/middle/bottom
        # 5 - font type
        # 6 - font size
        # 7 - font color

        #calculate render coordinates with alignments
        for text in self.texts:
            if 'pixel_r' == text[3]:
                text_x = text[1][0] * 0.01 * (self.width - self.margin[0]- self.margin[2]) + self.margin[0]
                text_y = text[1][1] * 0.01 * (self.height - self.margin[2]- self.margin[3]) + self.margin[2]
            elif 'pixel_a' == text[3]:
                text_x = text[1][0]
                text_y = text[1][1]
            else: #'data' is default behavior
                text_x = self.margin[0] + (text[1][0] - self.min_x) * self.scale_x
                text_y = self.height - self.margin[3] - (text[1][1] - self.min_y) * self.scale_y
            #alignments
            if 'middle' == text[4][0]:
                a_x = -(text[2][0] >> 1)
            elif 'right' == text[4][0]:
                a_x = -text[2][0]
            else: #left is default
                a_x = 0
            if 'middle' == text[4][1]:
                a_y = -(text[2][1] >> 1)
            elif 'bottom' == text[4][1]:
                a_y = -text[2][1]
            else: #top is default
                a_y = 0
            text_x += a_x
            text_y += a_y
            #Syntax:  ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align='left')
            #Parameters:
            #   xy      - Top left corner of the text.
            #   text    - Text to be drawn. If it contains any newline characters, the text is passed on to multiline_text()
            #   fill    - Color to use for the text.
            #   font    - An ImageFont instance.
            #   spacing - If the text is passed on to multiline_text(), the number of pixels between lines.
            #   align   - If the text is passed on to multiline_text(), 'left', 'center' or 'right'.
            text_font = ImageFont.truetype(text[5],text[6])
            self.draw_area.text((text_x,text_y),text[0],text[7],font = text_font)        

    def RenderAxes(self):
        return 0

    def RenderData(self): #use lines and draw all of them
        self.image = Image.new('RGBA', (self.width, self.height), self.bgc)
        self.draw_area = ImageDraw.Draw(self.image)

        min_x =[]
        max_x =[]
        min_y =[]
        max_y =[]
        for line in self.lines:
            x,y = zip(*line[0])
            min_x.append(min(x))
            max_x.append(max(x))
            min_y.append(min(y))
            max_y.append(max(y))

        #this probably not needed anymore ... 
        self.min_x = min(min_x)
        self.max_x = max(max_x)
        dx = self.max_x - self.min_x
        self.min_y = min(min_y)
        self.max_y = max(max_y)
        dy = self.max_y - self.min_y

        self.scale_x = (self.width - self.margin[0] - self.margin[1]) / dx
        self.scale_y = (self.height - self.margin[2] - self.margin[3]) / dy

        self.RenderLines()
        self.RenderTexts()
        self.RenderAxes()

        return 0


    def SaveImageToFile(self, filename, path = config.root_path):
        self.image.save(path + filename)
