# drawchart
Simple chart drawing class for Python 2.7 and samples

The goals are:
- create a library to draw a charts (lines) use at hosting service, where a few python libraries are enabled
- auto-scale the data to use maximum of the space (defaul resoulution is 800x600)
- add test labels
- add title
- support re-sizing 

PREREQUISITE
1) pillow graphic library (https://pillow.readthedocs.io/en/stable/)
  import PIL
  from PIL import Image, ImageFont, ImageDraw

2) Functions creating iterators for efficient looping  (https://docs.python.org/3/library/itertools.html)
from itertools import izip  

3)  Standard operators as functions (https://docs.python.org/3/library/operator.html)
import operator

4) Configuration file from the project (config.py)
import config


Approach:
First, you need to create an object of the class to store all data
Second, you need to add lines (list of coordinates (x,y)) to be drawn
Then you can add text label
Then you can configure Axis (by default - no axis)
Finally you should call the Render method to render all data and save image to file.

COORDINATES:
(0,0) is the LEFT BOTTOM corner of the image.

Text labels.
- can be created in ABSOLUTE coordinates, where (x,y) are equal to pixel offsets from the left bottom corner of the image.
- can be created in RELATIVE coordinates, where (x,y) are % offsets, calculated from the size of the render area
- can be created in DATA  coordinates (DEFAULT), where (x,y) are the actual data from the lines. In this case coordinates will be normalized (scaled) according to the data before rendering.

Text labels alignment
- (horizontal,vertical)
- horisontal:  left, middle, right
- vertical: top,middle, bottom
By default text label render alignment is ('left','top').
Alignment is applied to render coordinates (x,y) of the text. 
Horizontal alignment
- 'left' mean that the left border of the text will be aligne with the 'x' coordinate
- 'right' mean that the right border of the text will be aligne with the 'x' coordinate
- 'middle' mean that the middle point of the text will be aligne with the 'x' coordinate
Vertical alignment
- 'top' mean that the text will be rendered ON TOP of the 'y' coordinate
- 'bottom' mean that the text will be rendered BELOW of the 'y' coordinate
- 'middle' mean that the CENTER of the text will be rendered at the 'y' coordinate

Margin:
Added in the config file to make some visual space around the drawing area. 
Axis are drawin in the margin area

Axis:
To draw a axis lines.
Vertical axis could be drawn and the "left" side of the screen or at the "right" side of the screen.
Vertical axis could be "floating" and render at some data point.

The same approach for horizontal axis.  It coult be on "top", "bottom" or "floating"
DEFAULT: "left","bottom"

NOTE: 'float" mode is to be implemented.

CONFIG
Most of configuration parametes are listed in the config.py file. 


SAMPLES:
1) Line with text to show alingment modes
![lines](https://user-images.githubusercontent.com/22292864/141677704-b113f683-b304-4b0e-ba71-7eeb133ae79d.png)

2) draw two graphics in different colors with text labels and axis
![square](https://user-images.githubusercontent.com/22292864/141677732-86098edc-d20f-40b1-a95d-d9d1e0dfa521.png)
