"""
All functions and plots are stored and created here for the wind profiles
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# define the output path for the plots
BASE_DIR = Path(__file__).resolve().parent.parent
output_path = BASE_DIR / 'output'
# if directory is not there
output_path.mkdir(parents=True, exist_ok=True)

# define the output plots
output_file_land = "windprofil land.png"
output_file_city = "windprofil city.png"
output_file_land_height = "windprofil land height.png"
output_file_city_height = "windprofil city height.png"

# define constants
# more information for chosen wind speed in reference height u_A is given in the report
u_A= {"10": 3.0, "50": 6.0, "150":7.5}
z_A=[10,50,150]

# define dictionaries for roughness in rural and city areas only for considered atmospheric conditions
m_rural = {"I": 0.37, "III/2": 0.18}
m_city = {"I": 0.52, "III/2": 0.31}

# define the dispersion categories
disp_cat=["I", "III/2"]

# define the height for the wind profile
z=np.linspace(0,200,50)

def u(u_A,z,z_A,m):
    """
    function for calculation of the wind speed in different heights
    :param u_A: wind speed in reference height in m/s
    :param z: height in m
    :param z_A: reference height in m
    :param m: Ausbreitungsklasse
    :return: wind speed in m/s
    """
    u=u_A*(z/z_A)**m
    return u
# initialize the functions
u_ru = {}
u_ci = {}

# defining the concrete functions for different heights and stability criteria
for height in z_A:
    u_ru[height]= {}
    u_ci[height]= {}
    for disp in disp_cat:
        u_ru[height][disp] = u(u_A[str(height)],z,height,m_rural[disp])
        u_ci[height][disp] = u(u_A[str(height)],z,height,m_city[disp])

# print the wind speed for specific heights for later input for the gauß-model
u_32 = {}
for hoehe in [10,20,30,40,50]:
    u_direct = u(u_A["150"],hoehe,150,m_rural["III/2"])
    print(u_direct)
# Output: [10: 4.61, 20: 5.22, 30: 5.61, 40: 5.91, 50: 6.15]

# Plot only for stable/neutral conditions
plt.figure(1, figsize=(10,5), dpi=300)
plt.plot(u_ru[10]["I"],z,label="Land,I")
plt.plot(u_ru[10]["III/2"],z,label="Land,III/2")
plt.xlabel("Windgeschwindigkeit in m/s")
plt.ylabel("Höhe über Grund in m")
plt.legend()
plt.grid()
plt.savefig(output_path/output_file_land)

plt.figure(2, figsize=(10,5), dpi=300)
plt.plot(u_ci[10]["I"],z,label="Stadt,I")
plt.plot(u_ci[10]["III/2"],z,label="Stadt,III/2")
plt.xlabel("Windgeschwindigkeit in m/s")
plt.ylabel("Höhe über Grund in m")
plt.legend()
plt.grid()
plt.savefig(output_path/output_file_city)

plt.figure(3, figsize=(10,5), dpi=300)
plt.plot(u_ru[150]["I"],z,label="Stadt,I")
plt.plot(u_ru[150]["III/2"],z,label="Stadt,III/2")
plt.xlabel("Windgeschwindigkeit in m/s")
plt.ylabel("Höhe über Grund in m")
plt.legend()
plt.grid()
plt.savefig(output_path/output_file_land_height)

plt.figure(4, figsize=(10,5), dpi=300)
plt.plot(u_ci[150]["I"],z,label="Stadt,I")
plt.plot(u_ci[150]["III/2"],z,label="Stadt,III/2")
plt.xlabel("Windgeschwindigkeit in m/s")
plt.ylabel("Höhe über Grund in m")
plt.legend()
plt.grid()
plt.savefig(output_path/output_file_city_height)