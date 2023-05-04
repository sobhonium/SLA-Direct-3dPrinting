import numpy as np
from PIL import Image
import sys

sys.path.insert(0, '../utils/')
from utils import int_tostring, sdf, primitive, dummy

def add_config_files_():
    '''adds printers files in ../data folder'''
    pass

'''
The given function should receive 3 values, mathematically it is 
#  func:(x,y,z) --> func(x,y,z)
and this function is func: R^3 --> R for any point defined in the domain.
size_x, size_y, size_z are the length of shape in each standard
catesian coordinate that should be printed. that and 
layerHeight is very important as it specifies the number of layers. 
size_z/layerHeight == number of layers.
'''
def slicer(func, 
           func_x_domain =[0,1],
           func_y_domain =[0,1],
           func_z_domain =[0,1],

           size_x=30, 
           size_y=30, 
           size_z=30,
           
           layerHeight = 0.05,   
           path="../data/",
           file_name='img',
           start_layer=1,
           printer='AnyCubeMonoX6K'):
   
    # check weather the printer's configuraion .ini fils existed
    #  ....to be coded....

    #must assure that values are integer

    # must replaced. read from a config file.
    display_pixels_x = 5760 # num pixels
    display_pixels_y = 3600 # num pixel
    
    display_width    = 198.15  # means that in each mm we have 29.069 (5760/198.15) pixels.
    display_height   = 123.84
    max_print_height = 245

    size_x_in_pixel = int(size_x*(5760/198.15))
    size_y_in_pixel = int(size_y*(3600/123.84))

    max_layer_num = int(size_z/layerHeight)
    assert(max_layer_num < max_print_height/layerHeight)

    print('max_layer_num=', max_layer_num)
    for z in range(1, max_layer_num+1, 20): # layers. From 1 because we have no 0-layer
        v_holder = np.zeros((display_pixels_y, display_pixels_x)) # width and heigh are reveresed in here
        print('rendering layer z=',z,'/',max_layer_num, '...')
        for width in range(display_pixels_x//2-size_x_in_pixel//2, 
                           display_pixels_x//2+size_x_in_pixel//2):
            for height in range(display_pixels_y//2-size_y_in_pixel//2, 
                                display_pixels_y//2+size_y_in_pixel//2):
                # point = (0,0,0)    
                point = (func_x_domain[1]-func_x_domain[0])/(size_x_in_pixel//2 *2)*(width-(display_pixels_x//2-size_x_in_pixel//2)), (func_y_domain[1]-func_y_domain[0])/(size_y_in_pixel//2 *2)*(height-(display_pixels_y//2-size_y_in_pixel//2)), (func_z_domain[1]-func_z_domain[0])/(max_layer_num)*(z-1)

                # if z>0:
                #     print(point)
                sdf_value = sdf(point, func=func)
                if sdf_value<0: 
                    # print (point,sdf_value)
                    v_holder[height, width] = 1 # reversed in here
        
        image = Image.fromarray(v_holder.astype('uint8')*255)
        image.save(path+file_name+int_tostring(z-1, 8)+'.png')     # number start from 0, other wise it is errrosome

# from functools import partial
# slicer(partial(func=primitive, x=(0,1), y=(0,1)))

if __name__=='__main__':
    slicer(func=primitive,
           func_x_domain =[0,1],
           func_y_domain =[0,1],
           func_z_domain =[0,1],
           size_x=50, # in mm
           size_y=50, # in mm
           size_z=50,  # in mm 
           layerHeight = 0.05,   
           path="../data/",
           file_name='img',
        )