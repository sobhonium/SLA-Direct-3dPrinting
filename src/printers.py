class AnyCubeMonoX6K():
    display_pixels_x = 5760 # num of pixels
    display_pixels_y = 3600 # num of pixel
    
    display_width    = 198.15 # mm (millimeter) 
    display_height   = 123.84 # mm
    max_print_height = 245    # mm

    pixel_size = 1/(29.069)  
    # 0.034 = 1/(29.069) is each pixle's size in mm.
    # This parameter is shown in 'Anycube photon Workshop' as 
    # 'XY-pixel size' in 'Machine' tab and it is calculated as
    #  XY-pixel size(um) = 34.400. 

# other printers can be added in here:...    