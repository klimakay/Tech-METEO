"""
All functions and plots are stored and created here for the wind profiles
"""

import numpy as np
import matplotlib.pyplot as plt

#define constants for now
u_A=3.0
z_A=10

# define dictionaries for roughness in rural and city areas only for considered atmospheric conditions
m_rural = {"I": 0.37, "III/2": 0.18}
m_city = {"I": 0.52, "III/2": 0.31}

# define the height for the wind profile
z=np.linspace(0,200,50)

def u(u_A,z,z_A,m):
    u=u_A*(z/z_A)**m
    return u

