from collections import OrderedDict
color=OrderedDict([('color','red'),('color2','green'),('color3','yellow')])
print(color)
color.update({'color4':'orange'})
color.move_to_end('color4',last='False')
print(color)