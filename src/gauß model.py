import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# define the output path for the plots
BASE_DIR = Path(__file__).resolve().parent.parent
output_path = BASE_DIR / 'output'
# if directory is not there
output_path.mkdir(parents=True, exist_ok=True)

#define constants for effective plum heights up to 50 m
F={"I":1.294, "II": 0.801, "III/1": 0.640, "III/2":0.695, "IV": 0.876, "V": 1.503}
G={"I":0.241, "II": 0.264, "III/1": 0.215, "III/2":0.165, "IV": 0.127, "V": 0.151}
f={"I":0.718, "II": 0.754, "III/1": 0.784, "III/2":0.807, "IV": 0.823, "V": 0.833}
g={"I":0.662, "II": 0.774, "III/1": 0.885, "III/2":0.996, "IV": 1.108, "V": 1.219}

# wind speed for all heights. for real values see windprofile.py
# u for land
u = {
    "I": [3.0,3.0,4.5,4.5,4.5],
    "II": [3.0,4.5,4.5,4.5,4.5],
    "III/1": [3.0,4.5,4.5,4.5,6.0],
    "III/2": [4.5,4.5,6.0,6.0,6.0],
    "IV": [4.5,6.0,6.0,6.0,6.0],
    "V": [6.0,6.0,6.0,6.0,6.0]}


# u for city
#u = {
    #"I": [2.0,3.0,3.0,3.0,4.5],
     #"II": [2.0,3.0,3.0,4.5,4.5],
    #"III/1": [3.0,4.5,4.5,4.5,4.5],
    #"III/2": [3.0,4.5,4.5,4.5,4.5],
    #"IV": [3.0,4.5,4.5,4.5,4.5],
     #"V": [4.5,4.5,6.0,6.0,6.0]}

#define the distance from the source
x=np.linspace(1,1000,100)

#disp_cat=["I", "II", "III/1", "III/2", "IV", "V"]
disp_cat=["III/2"]
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
    Quellterm=1/(u*2*np.pi*sigma_y*sigma_z)
    exp_y=np.exp(-(y**2) / (2*sigma_y**2))
    exp_z=np.exp(-0.5*((z-H) / sigma_z)**2)+np.exp(-0.5*((z+H) /sigma_z)**2)
    c=Quellterm*exp_y*exp_z
    return c

# plot over all heights for all dispersion categories
plt.rc('legend', fontsize=8)
for disp in range(len(disp_cat)):
    cat = disp_cat[disp]
    # new variable to ensure a correct file path to save the plot
    name_cat = str(cat).replace("/","_")
    for height in range(len(heights)):
        H = heights[height]
        u_neu = u[cat][height]
        plt.plot(x,c(x,0,0,H, u_neu,cat)*1e6, label=f"{H} m Emissionshöhe")
        plt.title(f"Ausbreitungsklasse {cat}")
        plt.xlabel("Entfernung von der Quelle in m")
        plt.ylabel("Emittierte Konzentration in Millionstel")
    plt.legend()
    #plt.savefig(output_path/f"Ausbreitungskategorie {name_cat} mit verschiedenen Emissionshöhen.png", dpi=300)

# plot the distribution of the emissions
# define the lateral coordinate
x=np.linspace(1,2100)
y=np.linspace(-400,401)
X,Y=np.meshgrid(x,y)

for height in range(len(heights)):
    H_new = heights[height]
    cat_new = "III/2"
    u_new = u[cat_new][height]
    C = c(X, Y, 0, H_new, u_new, cat_new)*1e6
    plt.figure()
    contours = plt.contour(X, Y, C, levels=[1,2,3,4,8,12], colors='k')
    plt.clabel(contours, inline=True, fontsize=8, fmt='%.1f')
    plt.xlabel("Entfernung x von der Quelle in Windrichtung in m")
    plt.ylabel("Entfernung y von der Quelle senkrecht zur Windrichtung in m")
    plt.title(f"{cat_new}, Höhe {H_new} m")
    plt.grid()
    plt.show()
