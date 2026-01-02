import numpy as np
import matplotlib.pyplot as plt

# define the gauß function
def C(x,y,z,H,u,disp_cat):
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
    return Quellterm*exp_y*exp_z