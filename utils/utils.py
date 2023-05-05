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

def log(text):
    print(text + '... is done!')

def copy_file(original_file, target_file):
    import shutil
    shutil.copyfile(original_file, target_file)
    log('copy file from ' + original_file + ' to ' +  target_file)

def copy_folder(original_file, target_file):
    import shutil
    shutil.copytree(original_file, target_file, symlinks=False, 
                    ignore=None, ignore_dangling_symlinks=False, 
                    dirs_exist_ok=False)
    log('copy folder from ' + original_file + ' to ' +  target_file)

def clear_folder(dirpath):
    import shutil
    import os
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)
    log('folder ' + dirpath + ' cleaned ' )


def count_content_in_folder(dirpath):
    import os
    log('number of contents in ' + dirpath + ' calculated ' )
    return len([entry for entry in os.listdir(dirpath)])
    



def rename_file(old_file_name, new_file_name):
    import os
    os.rename(old_file_name, new_file_name)
    log('file ' + old_file_name + ' renamed to '+ new_file_name )


# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName):
    import os
    import glob
    from os.path import basename
    from zipfile import ZipFile
    import shutil
   # create a ZipFile object
    # with ZipFile(zipFileName, 'w') as f:
    #     for file in glob.glob(dirName+'*'):
    #         f.write(file)
    shutil.make_archive(zipFileName, 'zip', dirName)
    log('all content in  ' + dirName + ' zipped ' )

def update_file(file_name, variable, new_value ):
    import re

    # remove_commas = re.compile("House")
    import configparser
    import pathlib

    config = configparser.ConfigParser()
    config.optionxform = str
    # only works with absolute path
    config_path = pathlib.Path(file_name).absolute() 
        
    config.read(config_path)
    for ele in config['DEFAULT']:
        if ele==variable:
            config.set('DEFAULT', variable, new_value)
            # print(ele)

    cfgfile = open(config_path, 'w')
    # config.set('DEFAULT', variable, new_value)
    config.write(cfgfile)
    cfgfile.close()
    log(variable + ' in file ' + file_name + ' updated' )
    
    

        
def convert(input_file, output_file, type='pwmb'):
    import os
    import pathlib
    tool_path = pathlib.Path('tools/UVtools_linux-x64_v3.13.1/UVtoolsCmd').absolute()
    # os.system('ls ../tools/')
    os.system(f'{tool_path} convert {input_file} {output_file} {type}')
    log( input_file+ ' converted to ' + output_file )
    # this one also does the same:
    # import os
    # os.system(f'./tools/UVtools_linux-x64_v3.13.1/UVtoolsCmd convert sample.sl1s sample.pwmb pwmb')


def dummy(point):
    '''a helper function to test sdf'''
    x, y, z = point
    return (x-y)

def sphere(point):
    '''a helper function to test sdf'''
    x, y, z = point
    r = 1
    val = (x-1)**2+(y-1)**2+(z-1)**2
    if ( val- (r)**2 <0 and val-(r-0.4)**2>0 ):
        return -44
    return +44

def heart(point):
    '''a helper function to test sdf'''
    x, y, z = point
    return ((x-3)**2+ (9/4)*(y-3)**2+(z-3)**2 -1)**3 - (x-3)**2*(z-3)**3 - (9/80)*(y-3)**2*(z-3)**3


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




