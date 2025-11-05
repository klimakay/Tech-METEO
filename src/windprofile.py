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

# define potential temperature
data['theta']=data['T']*(data['p']/p0)**(R/cp)

# define fluctuations and so on
data['u_fluc']=data['u']-np.mean(data['u'])
data['v_fluc']=data['v']-np.mean(data['v']
data['w_fluc']=data['w']-np.mean(data['w'])

# kinematic heat and momentum fluxes
data['uw']=np.mean(data['u_fluc']*data[w_fluc])
data['uv']=np.mean(data['u_fluc']*data['v_fluc'])
data['thetaw']=np.mean(data['theta']*data['w_fluc']))

# define shear stress rate and characteristic temperature
data['u_star']=((np.mean(data['uw']))**2+(np.mean(data['uv']))**2)**(1/4)
data['theta_star']=-(np.mean(data['thetaw'])/data['u_star'])

# obukhov-length and vertical coordinate zeta
data['L']=(data['u_star'])**3 /(kappa*g/data['theta']*np.mean(data['thetaw']))
data['zeta']=data['z']/data['L']

# define X and X_0
data['X']=(1-15*(data['zeta']))**(-1/4)
data['X_0']=(1-15*(z_0/(data['L'])))**(-1/4)










