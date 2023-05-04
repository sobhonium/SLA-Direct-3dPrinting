
import sys
sys.path.insert(0, './utils/')
sys.path.insert(0, './src/')

from slicer import slicer
 
from  utils import int_tostring, sdf, primitive, dummy, copy_file, copy_folder, clear_folder
def main():

    # clear the path
    import shutil

    clear_folder('./data/')

    # slicer(func=primitive,
    #        func_x_domain =[0,1],
    #        func_y_domain =[0,1],
    #        func_z_domain =[0,1],
    #        size_x=50, # in mm
    #        size_y=50, # in mm
    #        size_z=50,  # in mm 
    #        layerHeight = 0.05,   
    #        path="./data/",
    #        file_name='img',
    #     )

    # copy .ini files in specified location    
    copy_file('./src/prusaslicer.ini','./data/prusaslicer.ini')
    copy_file('./src/config.ini','./data/config.ini')   
    copy_folder('./src/thumbnail', './data/thumbnail')

    # copy a file from .png into thumnail
    # to be done...

    # edit config and prusaslicer.ini based on the number of .png files
    # to be done.

    # zip the entire files in the domain:
    # to be done...

    # rename the zip file to .sl1s:
    # to be done...

    # run ./UVtoolsCMD convert input.sl1s pwmb output.pwmb
    # to be done

if __name__ == '__main__':
    main()
