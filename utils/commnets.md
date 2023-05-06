# Comments:
 - I have to select the same length for intger numbering of .png files: img001, img002, ...,img401 not img1, img2...img401
      numbering shold start from 0 (if you have 401 (0 to 400) of .png files ---> in '.ini' file numFast = 401 
      should be set.). 'numFast=' should be set to a numer that represents the number of layers (z axis), and 
     display_pixels_x = 5760
      display_pixels_y = 3600
     these last two are Anycubic X 6k resolution configurations.


 - I have to use *555 as I shown above. It is only working with absolute 0 and 1.
 - When I put the .png files in a folder, then i need a 'config.ini' and 'pursasclicer.ini' files and a folder
      to for 'thumbnail' that is used for showing on the printer screen. After putting all of these in a single file 
 - I must compress them into .zip file and then 'righ click+rename+.sls1'(remove .zip). the process of zipping 
      should not be run on a parent folder. I must select .ini files and thumbnail folder and zip them and the rest (
      it killed my time for hours to accidentally understand that...damnit).
 - I should now open the this .sl1s file in uvtools and convert it to .pwmb if I'm wokring on Anycube Mono X 6k. 
 - I need to define pngs with Width=5760, Height=3600 to be compatible with my printer (Anycub mono x 6K). otherwise
      I have to modify display_pixels_x (Width) and display_pixels_y (Height).
      I also need to 
 - You might run out of memery, if you consider a 3d np.ndarray for holding .pngs. the best practice is 
 to work on one .png and save it, then go to another layer and work on another .png file...
