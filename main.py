
import sys
sys.path.insert(0, './utils/')
sys.path.insert(0, './src/')

from slicer import slicer
 
from  utils import (int_tostring, sdf, primitive, dummy, 
                    copy_file, copy_folder, clear_folder,
                    count_content_in_folder,
                    update_file, zipFilesInDir,
                    rename_file, convert
                    )
def main():

    # clear the path
    import shutil

    # clear the folder
    clear_folder('./data/')

    # FIXME: its best if I consider a .json file and read from that...
    layerHeight = 0.05

    slicer(func=primitive,
           func_x_domain =[0,1],
           func_y_domain =[-1,1],
           func_z_domain =[0,1],
           size_x=5, # in mm
           size_y=5, # in mm
           size_z=0.5,  # in mm 
           layerHeight = layerHeight, # in mm  
           path="./data/",
           file_name='img',
        )

    # copy .ini files in specified location    
    copy_file('./src/prusaslicer.ini','./data/prusaslicer.ini')
    copy_file('./src/config.ini','./data/config.ini')   
    copy_folder('./src/thumbnail', './data/thumbnail')

    # copy a file from .png into thumnail
    # to be done...

    # edit config and prusaslicer.ini based on the number of .png files
    # how many files in ./data folder
    num_files = count_content_in_folder('./data')
    print(num_files, ' number of .png files exists in folder')
    update_file('./data/config.ini', 'layerHeight', str(layerHeight))
    
    # update config file based on the slicing process
    # 3 files added config.ini, parser.init and thubmnail folder
    update_file('./data/config.ini', 'numFast', str(num_files-3)) 


    
    # zip the entire files in the domain:
    # to be done...
    zipFilesInDir('./data/', './sample') # sample.zip will be created 


    # rename the zip file to .sl1s:
    rename_file('sample.zip', 'sample.sl1s')

    # run ./UVtoolsCMD convert input.sl1s pwmb output.pwmb
  
    print("=========:")
    convert('sample.sl1s', 'sample.pwmb', type='pwmb')
    print("=========:")

if __name__ == '__main__':
    main()
