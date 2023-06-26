''' 
The primary goal of slicers in resin printers' world is to 
render layers'pixels as 0 or 1 to specify whether 
a particular pixel should be printed or not. In other words, 
from a simplictic viewpoint, consider Resin printers as
machines that just understand 0 or 1 values for their 
operations. SDF functions, however, are returning 
floating point values and are not consistent with 
this printers' understandings. Adding a filter on sdf 
functions let us filter values to be 0 or 1. To shed 
light on it, one simple function that can be considered as 
filter function is the following indicating function:
f(x) = {0|if x<0, 1|if x>=0}
* indicating functions in math are those returning 0 and 1.
Applying this filter on sdf functions gives only 0/1 values.
This function is called binay_step_function in math which
is a simple function from indicating function families.
From a mathematical standpoint, if we define sdf function as
sdf and filter function as f, the fomula we binary step
function we mentioned already would be
f(sdf(point)) = {0|if sdf(point)<0, 1|if sdf(point)>=0}

* Appying other customized filter functions are also possible 
if you write your custom filter functions down bellow.
'''
import numpy as np

def binary_step_function(input_):
    '''it is 1 when input_>=0 and 0 when input_<0'''
    if input_>=0:
        return 1
    return 0

def custom_surface_filter(input_):
    '''it is inteded to return a very tiny surface
    (with thickness)
    '''
    thickness = 0.2
    if input_>-thickness and input_<thickness:
        return 1
    return 0

# def pyramid_filter(input_):

def custom_surface_filter2(input_):
    '''it is inteded to return a very tiny surface
    (with thickness)
    input_ is a 2d np.ndarray (as apposed to custom_surface_filter() functino
    that recieves only one value at a time)

    The condition should have & (not 'and')
    I wrote this for faster slicers that work with np.mgrid.
    '''
    
    # thickness = 0.2
    # condi  = (input_<thickness) & (input_>-thickness)
    # return np.where( condi, 1, 0)

    condi  = (input_>-0.2) & (input_<0.2)
    return np.where( condi, 1, 0)

