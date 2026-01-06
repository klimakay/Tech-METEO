import numpy as np
import matplotlib.pyplot as plt

#define constants for effective plum heights up to 50 m
F={"I":1.294, "II": 0.801, "III/1": 0.640, "III/2":0.695, "IV": 0.876, "V": 1.503}
G={"I":0.241, "II": 0.264, "III/1": 0.215, "III/2":0.165, "IV": 0.127, "V": 0.151}
f={"I":0.718, "II": 0.754, "III/1": 0.784, "III/2":0.807, "IV": 0.823, "V": 0.833}
g={"I":0.662, "II": 0.774, "III/1": 0.885, "III/2":0.996, "IV": 1.108, "V": 1.219}

# wind speed for all heights. for real values see windprofile.py
u = {
    "I": [3.0,4.5,4.5,4.5,4.5],
    "II": [3.0,3.0,4.5,4.5,4.5],
    "III/1": [3.0,3.0,4.5,4.5,4.5],
    "III/2": [3.0,3.0,3.0,4.5,4.5],
    "IV": [3.0,3.0,3.0,3.0,3.0],
    "V": [3.0,3.0,3.0,3.0,3.0]}

#define the distance from the source
x=np.linspace(0,1000,100)

disp_cat=["I", "II", "III/1", "III/2", "IV", "V"]

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

