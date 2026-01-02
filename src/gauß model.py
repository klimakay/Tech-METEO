import numpy as np
import matplotlib.pyplot as plt

#define constants for effective plum heights up to 50 m
F={"I":1.294,"III/2":0.695}
G={"I":0.241,"III/2":0.165}
f={"I":0.718,"III/2":0.807}
g={"I":0.662,"III/2":0.996}

#define the distance from the source
x=np.linspace(0,1000,100)

disp_cat=["I", "III/2"]

heights=[10,20,30,40,50]

# define the gauß function
def c(x,y,z,H,u,disp_cat):
    """

    :param x: longitude coordinate
    :param y: lateral coordinate
    :param z: height above ground in meters
    :param H: effective plume height in meters
    :param u: wind speed in m/s
    :param disp_cat: dispersion category
    :return: concentration of a substance at a certain distance of a source
    """
    sigma_y=F[disp_cat]*(x/1)**f[disp_cat]
    sigma_z=G[disp_cat]*1*(x/1)**g[disp_cat]
    Quellterm=100/(u*2*np.pi*sigma_y*sigma_z)
    exp_y=np.exp(-(y**2)/2*sigma_y**2)
    exp_z=np.exp(-0.5*(z-H/sigma_z)**2)+np.exp(-0.5*(z+H/sigma_z)**2)
    c=Quellterm*exp_y*exp_z
    return c

# for next time: wind speed from wind profile for heights