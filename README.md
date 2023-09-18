# SLA-Direct-3dPrinting
A python tool for producing a ```.pwmb``` file from a function for my printer (AnyCubic Photon Mono X 6K)

#####

![image](./docs/images/direct_printing.png)

#####

## Auto Setup

Run install.sh to download the required tools and packages.
> ./install.sh





When installed, **tools**  and **data** folders (if not existed) are generated in the rool directory (this folder would contain all 3rd party codes for conversion between file formats and other usefull tools). 

run in the root directory 
> python3 main.py

You only need to define a function in main.py and set other parameters in slicer() function to slice and produce a ```.pwmb``` file for your parinting machine (AnyCube Phonton Mono X 6K is the defualt).

## Manually Setup
If you want to manually produce a .pwmb file follow this instruction:
- First, you need ```.png``` files (let's say ```img``` is the root name, you start from ```0000``` to ```XXXX``` with the equal name length). The accepted files names are like bellow:
    * ```img0000.png```, ```img0001.png```, ..., ```img0400.png```,         
These .png files should be put in ./data folder and size/resolution should be in consistence with your printers' display. For   AnyCube Phonton Mono X 64 this is ```5670*3600```.      

- Now, you need to copy and paste **./src/*.ini** files and **thubmnail** in ./data folder. 

- zip all files and folder in ./data and rename it **sample.sl1s**.
- Download https://github.com/sn4k3/UVtools/releases/download/v3.13.1/UVtools_linux-x64_v3.13.1.zip (for linux users) and upzip it in ```./tools``` folder. You need to find **UVtoolsCmd** and call
> ./tools/UVtoolsCmd convert sample.s1 sample.pwmb pwmb

## User Manual

In order to print an SDF function you need its math formula ```f(x,y,z)``` to be added/defined. As an example for an sdf function like gyroid you need to define:
```
def gyroid(point):
    '''a helper function to test sdf'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    return np.sin(x)*np.cos(y) + np.sin(y)*np.cos(z) + np.sin(z)*np.cos(x) 
```
This function returns a real value since this sdf function is ```f: (x,y,z) --> R```. The printer only works with ```0/1``` int values, so you need to filter sdf values into ```0/1``` with something like this:

```
def binary_step_function(input_):
    '''it is 1 when input_>=0 and 0 when input_<0'''
    if input_>=0:
        return 1
    return 0
```
or any desired filter function. After that you can slice the function into layers to be printed. But at this step you need to indicate the domain of function for each ```x,y``` and ```z``` axis. Here I'm showing ```0<= x,y,z <=1```. You also need to specify the size of your function (in ```mm```) to convert the abstract values into a real life unit-based measurements (here 100mm for each ```x,y,z```). So, the slicer would be:

```
slicer(func=gyroid,
           func_x_domain=[0,1],
           func_y_domain=[0,1],
           func_z_domain=[0,1],
           
           size_x=100, # in mm
           size_y=100, # in mm
           size_z=100,  # in mm
           
           filter_func= binary_step_function,
        )
```
For setting other print variable like   ```layerHeight```, ```raft_layers```,  ```gap``` and others read on from the functions' doc strings.

## Extension
I already set/check things based on Anycube Mono X 6K. If you want to add more SLA ptiners you only need to define and put the specks of your printer(s) in files like:
