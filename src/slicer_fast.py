__author__ = 'SBN'
__date__ = 'June 2023'

# this version of slicer is a lot faster that the current slicer that 
# upgrade: for loops are replaced with np.mgrid

import numpy as np
from PIL import Image
import sys

sys.path.insert(0, '../utils/')
from sdf_functions import  sdf, primitive, dummy, gyroid, pyarmaid_function
from filter_functions import binary_step_function, custom_surface_filter, custom_surface_filter2
from utils import int_tostring
from printers import AnyCubeMonoX6K

def add_config_files_():
    '''adds printers files in ../data folder'''
    pass


def slicer(func, 
           
           # defines the domain in each axis.
           func_x_domain =[0,1],
           func_y_domain =[0,1],
           func_z_domain =[0,1],
           
           # in mm
           size_x=10, 
           size_y=10, 
           size_z=10,
           
        
           filter_func = custom_surface_filter2,

           layerHeight = 0.05,   
           path="../data/",
           file_name='img',
           raft_layers=8, #  number of layers for raft
           good_gap = 200, # to let structure be obove the raft 
           printer='AnyCubeMonoX6K'):
    '''
    By default, func() is defined over [0,1]*[0,1]*[0,1] where x,y,z \in [0,1].
     
    filter_func is the 'indicator function' i.e. it recieves values as inputs
    and ouput 0 and 1. In slicing we need all matrix slice values to be 0 or 1.
    In direct function printing in sla printers, filter_func applies 
    to the sdf function and specifies 0 and 1 out of this. The default
    value for filter_func is the binary step function, as mostly >0 are
    of interests for printing. Other costume functions, however,
    can also be defined and used alternatively. 
    size_x, size_y, size_z are the length of shape in each standard
    cartesian coordinate that should be printed. that and 
    layerHeight is very important as it specifies the number of layers. 
    size_z/layerHeight == number of layers.
    '''
    
    # FIXIIT(SBN) : check weather the printer's configuraion .ini fils existed
    #  ....to be coded....

    # FIXIIT(SBN) : must assure that values are integer

    # FIXIIT(SBN) : must replaced. read from a config file.
    if printer == "AnyCubeMonoX6K":
        display_pixels_x = AnyCubeMonoX6K.display_pixels_x # num pixels
        display_pixels_y = AnyCubeMonoX6K.display_pixels_y # num pixel
        
        display_width    = AnyCubeMonoX6K.display_width  
        display_height   = AnyCubeMonoX6K.display_height
        max_print_height = AnyCubeMonoX6K.max_print_height
    
        # Note: for anycub6k means that in each mm we have 29.069 (5760/198.15) pixels. 
    else:
        sys.exit("errors! you need to define your "+ printer  + " printer first!")
        
    # it is highly important to know the size of object (in terms of num pixels)
    # for each width and height  
    size_x_in_pixel = int(size_x*(display_pixels_x/display_width))
    size_y_in_pixel = int(size_y*(display_pixels_y/display_height))


    max_layer_num = int(size_z/layerHeight)
    assert(max_layer_num+raft_layers+good_gap < max_print_height/layerHeight)

    start_x_pixel = display_pixels_x//2-size_x_in_pixel//2
    end_x_pixel   = display_pixels_x//2+size_x_in_pixel//2

    start_y_pixel = display_pixels_y//2-size_y_in_pixel//2
    end_y_pixel   = display_pixels_y//2+size_y_in_pixel//2
    
    x = np.arange(start_x_pixel, end_x_pixel, 1)
    y = np.arange(start_y_pixel, end_y_pixel, 1)
    width, height = np.meshgrid(x, y)
    
    point_x = (func_x_domain[1]-func_x_domain[0])/(size_x_in_pixel//2 *2)*(width-start_x_pixel)+func_x_domain[0]
    point_y = (func_y_domain[1]-func_y_domain[0])/(size_y_in_pixel//2 *2)*(height-start_y_pixel)+func_y_domain[0]
    point_hw = point_x, point_y



    print('max_layer_num=', max_layer_num)
    # layers. From 1 because we have no 0-layer
    for z in range(1, max_layer_num+1+raft_layers+good_gap, 1): 
        

        # width and heigh are reveresed in here
        v_holder = np.zeros((display_pixels_y, display_pixels_x)) 
        print('rendering layer z=',z,'/',max_layer_num+raft_layers+good_gap, '...')
        
   
        # for width in range(start_x_pixel, end_x_pixel):
        #     for height in range(start_y_pixel, end_y_pixel):
                # point = (0,0,0)
        if z<=raft_layers:
            v_holder[height, width] = 1
            image = Image.fromarray(v_holder.astype('uint8')*255)
            image.save(path+file_name+int_tostring(z-1, 8)+'.png') 
            continue
        elif z>raft_layers and z<=raft_layers+good_gap:
            v_holder[height, width] = 0
            image = Image.fromarray(v_holder.astype('uint8')*255)
            image.save(path+file_name+int_tostring(z-1, 8)+'.png') 
            continue

        point = point_hw[0], point_hw[1], (func_z_domain[1]-func_z_domain[0])/(max_layer_num)*(z-1-(raft_layers+good_gap))+func_z_domain[0]
        # print(point[0].shape)
        sdf_value = sdf(point, func=func)
        # print(sdf_value)
        
        v_holder[height, width] = filter_func(sdf_value)
        
        # print(width.shape, height.shape)

        image = Image.fromarray(v_holder.astype('uint8')*255)
        image.save(path+file_name+int_tostring(z-1, 8)+'.png')     # number start from 0, other wise it is errrosome



if __name__=='__main__':
    slicer(func=pyarmaid_function,
           func_x_domain =[0,3],
           func_y_domain =[0,3],
           func_z_domain =[0,3],
           size_x=90, # in mm
           size_y=90, # in mm
           size_z=90,  # in mm 
           layerHeight = 0.05,
           filter_func=custom_surface_filter2,   
           path="../data/",
           file_name='img',
           good_gap=200,
           raft_layers=5
        )