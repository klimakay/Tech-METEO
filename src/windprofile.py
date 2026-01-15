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
m_rural = {"I": 0.37, "II": 0.32, "III/1": 0.26, "III/2": 0.18, "IV": 0.14, "V": 0.12}
m_city = {"I": 0.52, "II": 0.48, "III/1": 0.31, "III/2": 0.31, "IV": 0.31, "V": 0.20}

# define the dispersion categories
disp_cat=["I", "III/2"]
all_class=["I", "II", "III/1", "III/2", "IV", "V"]

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
print(round(u(u_A[str(10)],50,10,m_rural["I"]),2))
print(round(u(u_A[str(10)],50,10,m_rural["III/2"]),2))
print(round(u(u_A[str(10)],50,10,m_city["I"]),2))
print(round(u(u_A[str(10)],50,10,m_city["III/2"]),2))

# print the wind speed for specific heights for later input for the gauß-model
u_all = {}
for hoehe in [10,20,30,40,50,150]:
    u_all[hoehe] = {}
    for all in all_class:
        u_all[hoehe][all] = round(u(u_A["150"],hoehe,150,m_rural[all]),2)
        print(u_all)
# Output land: 10: {'I': 2.75, 'II': 3.15, 'III/1': 3.71, 'III/2': 4.61, 'IV': 5.13, 'V': 5.42},
# 20: {'I': 3.56, 'II': 3.94, 'III/1': 4.44, 'III/2': 5.22, 'IV': 5.66, 'V': 5.89},
# 30: {'I': 4.13, 'II': 4.48, 'III/1': 4.94, 'III/2': 5.61, 'IV': 5.99, 'V': 6.18},
# 40: {'I': 4.6, 'II': 4.91, 'III/1': 5.32, 'III/2': 5.91, 'IV': 6.23, 'V': 6.4},
# 50: {'I': 4.99, 'II': 5.28, 'III/1': 5.64, 'III/2': 6.15, 'IV': 6.43, 'V': 6.57},
# 150: {'I': 7.5, 'II': 7.5, 'III/1': 7.5, 'III/2': 7.5, 'IV': 7.5, 'V': 7.5}
# Output stadt : {10: {'I': 1.83, 'II': 2.04, 'III/1': 3.24, 'III/2': 3.24, 'IV': 3.24, 'V': 4.36},
# 20: {'I': 2.63, 'II': 2.85, 'III/1': 4.02, 'III/2': 4.02, 'IV': 4.02, 'V': 5.01},
# 30: {'I': 3.25, 'II': 3.46, 'III/1': 4.55, 'III/2': 4.55, 'IV': 4.55, 'V': 5.44},
# 40: {'I': 3.77, 'II': 3.98, 'III/1': 4.98, 'III/2': 4.98, 'IV': 4.98, 'V': 5.76},
# 50: {'I': 4.24, 'II': 4.43, 'III/1': 5.34, 'III/2': 5.34, 'IV': 5.34, 'V': 6.02},
# 150: {'I': 7.5, 'II': 7.5, 'III/1': 7.5, 'III/2': 7.5, 'IV': 7.5, 'V': 7.5}}

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
plt.plot(u_ru[150]["I"],z,label="Land,I")
plt.plot(u_ru[150]["III/2"],z,label="Land,III/2")
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