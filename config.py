root_path = "./"

metall_name = {
        'A33':'Palladium',
        'A76':'Platinum',
        'A98':'Gold',
        'A99':'Silver'
}

#TODO  error with drawing. top and bottom are mixedup instead of scaling chart is just shifting. 
#workaround: Use equal numbers by now.
margin_l = 5
margin_r = 5
margin_t = 5
margin_b = 5

pixel_scale = 1 #sensitivity to data visualisation. 1 - every pixel, 2 - two pixels, 3 - three ... 

chart_width = 800
chart_height = 600
chart_color = (0,0,255,255)  #blue, non-transparent
axes_color = (128,128,128,255)  #gray, non-transparent
text_color = (0,0,0,255)  #black, non-transparent

chart_pen_width = 2

#chart_font_type = "./font/arial.ttf"
#chart_font_type = "./font/Guru-Regular.otf"
chart_font_type = root_path + "font/GothamSSm-Book.otf"
chart_font_size = 16

