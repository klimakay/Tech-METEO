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
#define fluctuations and so on
data['u_fluc']=data['u']-np.mean(data['u'])
data['v_fluc']=data['v']-np.mean(data['v']
data['w_fluc']=data['w']-np.mean(data['w'])

# define potential temperature
data['theta']=data['T']*(data['p']/p0)**(R/cp)

