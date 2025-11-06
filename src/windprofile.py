"""
All functions and plots are stored and created here for the wind profiles
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# define constants
z0=1
g=9.81
p0=1013
R=287.1
cp=1005
kappa=0.41

# define height
z=np.linspace(0,1000,10)

# define potential temperature
data['theta']=data['T']*(data['p']/p0)**(R/cp)

# define fluctuations and so on
data['u_fluc']=data['u']-np.mean(data['u'])
data['v_fluc']=data['v']-np.mean(data['v']
data['w_fluc']=data['w']-np.mean(data['w'])

# kinematic heat and momentum fluxes
uw=np.mean(data['u_fluc']*data['w_fluc'])
uv=np.mean(data['u_fluc']*data['v_fluc'])
thetaw=np.mean(data['theta']*data['w_fluc']))

# define shear stress rate and characteristic temperature
u_star=((np.mean(uw))**2+(np.mean(uv))**2)**(1/4)
theta_star=-(np.mean(thetaw)/u_star)

# obukhov-length and vertical coordinate zeta
L=(u_star)**3/(kappa*g/data['theta']*np.mean(thetaw))
data['zeta']=z/L

# define X and X_0
X=(1-15*(data['zeta']))**(-1/4)
X_0=(1-15*(z_0/(L)))**(-1/4)

def u_speed(z):
    """
    function which computes the wind speed in direction of u depending on the stability
    :param z: height in meters
    :return: u_speed
    """
    if data['zeta']<=0:
        u_speed=u_star/kappa*(np.log(z/z0)-2*np.log((1+X)/1+X_0)-np.log((1+X**2)/1+X_0**2)+2*np.arctan2(X)-2*np.arctan2(X_0))
    elif data['zeta']>=0 and data['zeta']<0.5:
        u_speed=u_star/kappa*(np.log(z/z0)+5*(z-z0/L))
    elif data['zeta']>=0.5 and data['zeta']<10:
        u_speed=u_star/kappa*(8*np.log(2*z/L)+4.25*(z/L)**(-1)-0.5*(z/L)**(-2)-np.log(2*z0/L)-5*(z0/L)-4)
    else:
        u_speed=u_star/kappa*(0.7585*(z/L)+8*np.log(20)-11.165-np.log(2*z0/L)-5*(z0/L))
    return u_speed











