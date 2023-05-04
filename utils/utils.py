import numpy as np

def int_tostring(input_int:int, output_length:int=7):
    '''
    convert an integer input to a string with specified string length.
    input param: 
                input_int:int: the intger input
                output_length:int: the desired length of the output img

    output:
                :string: the integer input outputed with the desired length 
    
    Note: why on this project? because the UVtools 
    sees a .sl1s file and in that file, only files with
    ordered names can be accepted. img001, img002, ... img999.
    A bug could be images with names like img1.png, img2.png,...img999.png
    the length of these images are not equal. So this function is 
    applied in here. This function is helpful for that purpose...

    >>> int_tostring(1, 3)
    '001'
    >>> int_tostring(87, output_str_length=3)
    '087'
    '''
    
    input_len = len(str(input_int))
    assert(input_len<=output_length)

    if (input_len < output_length):
        return '0'*(output_length-input_len) + str(input_int)

def copy_file(original_file, target_file):
    import shutil
    shutil.copyfile(original_file, target_file)

def copy_folder(original_file, target_file):
    import shutil
    shutil.copytree(original_file, target_file, symlinks=False, 
                    ignore=None, ignore_dangling_symlinks=False, 
                    dirs_exist_ok=False)
def clear_folder(dirpath):
    import shutil
    import os
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)

def dummy(point):
    '''a helper function to test sdf'''
    x, y, z = point
    return (x-y)

def sphere(point):
    '''a helper function to test sdf'''
    x, y, z = point
    r = 5
    return (x-r)**2+(y-r)**2+(z-r)**2 - (r)**2

def primitive(point):
    '''a helper function to test sdf'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    x*=3
    y*=3
    z*=3
    return np.cos(x) + np.cos(y) + np.cos(z) 
    
def sdf(point, func):
    '''The Sign Distance function
    This function is recieves a function as an input argument and 
    for every point in that function produces a value <0, >0 or =0 values 
    for that point input. Mathematically speaking, SDF: (X, func)--> func(X)
    and in this case X==point.

    >>> point = (1, 0.5, 2)
    >>> sdf(point, func=sphere)
    20.25
    >>> sdf((0.5,-0.5,-0.5), func=primitive)
    -3.0
    '''
    return func(point)




