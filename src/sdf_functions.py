import numpy as np

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

def double_gyroid(point):
    '''a helper function to test sdf'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    # x*=10
    # y*=10
    # z*=10
    return 2.75 * (np.sin(2.0 * x) * np.sin(z) * np.cos(y) +
		        np.sin(2.0 * y) * np.sin(x) * np.cos(z) +
		        np.sin(2.0 * z) * np.sin(y) * np.cos(x))-1.0  * (np.cos(2.0 * x) * np.cos(2.0 * y) + 
		        np.cos(2.0 * y) * np.cos(2.0 * z) +np.cos(2.0 * z) * np.cos(2.0 * x))     - 0.95

def pyarmaid_function(point):
    # be careful about the logical ands
    return np.where(np.logical_and(point[2]>=0 , point[2]<1), gyroid(point),
                    np.where((point[2]>=1) & (point[2]<2) & (point[1]>=0) & (point[1]<2) & (point[0]>=0) & (point[0]<2),gyroid(point),
                    np.where((point[2]>=2) & (point[2]<3) & (point[1]>=0) & (point[1]<1) & (point[0]>=0) & (point[0]<1),gyroid(point), 
                             -1000
                    ))
                    )


    return -1000          

# TODO(add a macro for positvie and negative values)
def gyroid_cylinder(point):
    '''a sampler function for gyroid cylinder.
            if the point is inside the cylinder, it checks for gyroids's surface
            if it's on the cylinder boundary, returns a positive value. if not negative.
            --> This is done as I'm using sdf values for returning 0, 1 for pos and neg
            in filter functions. 
       '''
    r_cylider = 5
    r_out = 5
    r_in = 4.9

    is_internal = (point[0]-r_cylider)**2+(point[1]-r_cylider)**2<=r_in**2
    is_cylinder_boundary =np.where(
                     ((point[0]-r_cylider)**2+(point[1]-r_cylider)**2>=r_in**2)
                     &  ((point[0]-r_cylider)**2+(point[1]-r_cylider)**2<=r_out**2),
                     0.01, # just a positive value is enough
                     -1000)
    return np.where(is_internal,  
                    gyroid(point),
                    is_cylinder_boundary
                    )

def elipsis(point):
    r = 2
    ax = 2
    by = 0.5
    cz = 2
    eps = 0.05
    condi = ((point[0]-r)**2/(ax**2)+
              (point[1]-r)**2/(by**2)+
              (point[2]-r)**2/(cz**2)<=1**2)
    condi2 =np.where(
                     (point[2]<r) &
                     ((r - eps) < point[1]) & 
                     ((r + eps) > point[1]) & 
                     (np.mod(np.floor(10*point[0]),5)==0) 
                     ,1,-1000)
    return np.where(condi, 1,
                   condi2
                    )


def diamond(point):
    '''diamond helper sdf function'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    sin_x, sin_y, sin_z = np.sin(x), np.sin(y), np.sin(z)
    cos_x, cos_y, cos_z = np.cos(x), np.cos(y), np.cos(z)

    return sin_x*sin_y*sin_z+  sin_x*cos_y*cos_z+ cos_x*sin_y*cos_z+ cos_x*cos_y*sin_z

def gyroid(point):
    '''a helper function to test sdf'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    return np.sin(x)*np.cos(y) + np.sin(y)*np.cos(z) + np.sin(z)*np.cos(x) 


def primitive(point):
    '''a helper function to test sdf'''
    x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    x*=3
    y*=3
    z*=3
    return np.cos(x) + np.cos(y) + np.cos(z) 

def gyroid_parimitive(point):
    '''a helper function to test sdf
    an interpolation between gyroid and primitive'''
    # x, y, z = 2*np.pi*point[0], 2*np.pi*point[1], 2*np.pi*point[2]
    return gyroid(point) + primitive(point)

def heart(point):
    '''a helper function to test sdf
    agyroid heart'''

 

    x = point[0]- 1.5
    y = point[1]- 1.5
    z = point[2]- 1.5

    Heart = (x**2+(9/4)*y**2+z**2-1)**3 - x**2*z**3 - (9/80)*y**2*z**3
    return  Heart 
   

 

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