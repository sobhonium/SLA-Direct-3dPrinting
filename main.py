__author__ = 'SBN'
__date__ = 'May 2023'

import sys
sys.path.insert(0, './utils/')
sys.path.insert(0, './src/')

# if recall from slicer.py it's not fast
# but the slicer in slicer_fast.py is faster.
from slicer_fast import slicer 
 
from  utils import (copy_file, copy_folder, clear_folder,
                    count_content_in_folder,
                    update_file, zipFilesInDir,
                    rename_file, convert
                    )
from sdf_functions import (double_gyroid, diamond, gyroid, primitive, pyarmaid_function, 
                           gyroid_cylinder, gyroid_parimitive,heart,
                            elipsis)
from filter_functions import custom_surface_filter, custom_surface_filter2, binary_step_function
from src.printers import AnyCubeMonoX6K

def main():

    # FIXME: its best if I consider a .json file and read from that...
    layerHeight = 0.05
    printer = 'AnyCubeMonoX6K'
    path = './data/'
    img_file_name='img0'
    output_file_name = './sample'



    # clear the folder
    clear_folder(path)



    slicer(func=gyroid,
           func_x_domain=[0,1],
           func_y_domain=[0,1],
           func_z_domain=[0,1],
           size_x=5, # in mm
           size_y=10, # in mm
           size_z=5,  # in mm
           filter_func= custom_surface_filter2,
           raft_layers=0, # number of raft layers
           good_gap =0, # to let structure be obove the raft 
           layerHeight = layerHeight, # in mm  
           path=path,
           file_name=img_file_name,
           printer=printer
        )

    if printer=="AnyCubeMonoX6K":
        printer_machine = AnyCubeMonoX6K()
    else:
        sys.exit("errors! you need to define your "+ printer  + " printer first!")    

    # copy .ini files in specified location    
    copy_file('./src/prusaslicer.ini','./data/prusaslicer.ini')
    copy_file('./src/config.ini','./data/config.ini')   
    copy_folder('./src/thumbnail', './data/thumbnail')

    # copy a file from .png into thumnail
    # to be done...

    # edit config and prusaslicer.ini based on the number of .png files
    # how many files in ./data folder
    num_files = count_content_in_folder(path)
    print(num_files, ' number of .png files exists in folder')
    update_file('./data/config.ini', 'layerHeight', str(layerHeight))
    
    # update config file based on the slicing process
    # 3 files added config.ini, parser.init and thubmnail folder
    update_file('./data/config.ini', 'numFast', str(num_files-3)) 


    
    # zip the entire files in the domain:
    # to be done...
    zipFilesInDir(path, output_file_name) # sample.zip will be created 


    # rename the zip file to .sl1s:
    rename_file(output_file_name+'.zip', output_file_name+'.sl1s')

    # run ./UVtoolsCMD convert input.sl1s pwmb output.pwmb

    print("=========:")
    in_ = output_file_name+'.sl1s'
    out_ = output_file_name+ '.'+ printer_machine.file_format
    convert(in_, out_, type=printer_machine.file_format)
    # if you are using AnyCubeMonoX6K this is equally:
    # convert('sample.sl1s', 'sample.pwmb', type='pwmb')
    print("=========:")

if __name__ == '__main__':
    main()
