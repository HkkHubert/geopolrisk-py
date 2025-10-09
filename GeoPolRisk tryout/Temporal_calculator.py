import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.geopolrisk.assessment.main import *
#from src.geopolrisk.assessment.database import database
from geopolrisk.assessment.utils import (
    mapped_baci,)
import time

#### Code SNippet to export the GeoPolRisk material map
#mapping = mapped_baci()
#
#path_to_mapping = databases.directory + "/databases/material_map.xlsx"
#with pd.ExcelWriter(path_to_mapping) as writer:
#    mapping.to_excel(writer, sheet_name = "Material_map")

material_sheets = {"Titanium": "Ti metal", "Aluminium": "Al", "Copper": "Cu", "Nickel": "Ni", "Tungsten": "W", "Titanium O2": "Ti oxides", "Niobium": "Nb, Ta, V",
                   "Tantalum": "Nb, Ta, V", "Vanadium": "Nb, Ta, V", "Cobalt": "Co", "Lithium": "Li", "REEs": "REEs, La, Sc, (excl. Ce!)",
                   "Magnesium": "Mg"}


path_to_BACI_material = databases.directory + "/databases/export_results_1995_2022.xlsx"

Materials = ["Titanium", "Aluminium", "Copper", "Nickel", "Titanium O2", "Tungsten", "Niobium", "Cobalt", "Lithium"]

Material_trends = []

start_time = time.time()

### Check all of the years under observation
for Material in Materials:

    Data = pd.read_excel(path_to_BACI_material, sheet_name=material_sheets[Material])
    Yearly_avg_cost = []
    for Y in range(1995,2023):
        #initialize the counter for how much material was traded each year
        Material_quantity = 0
        Weighted_sum = 0


        for i in range(len(Data.Year)):
            if Data.Year[i] == Y and np.isnan(Data.Quantity[i]) != True:
                Weighted_sum += Data.Value[i] ### This total amount of money spent on the material (1000 $USD)
                Material_quantity += Data.Quantity[i]  ### Summing the amount of material volume (metric tons) to get the total material volume for each year


        Yearly_avg_cost.append(Weighted_sum / Material_quantity) ### Calculating the yearly average $1000 USD/ton ($USD/kg) value
        print("Year ", Y, " done with average:", Weighted_sum / Material_quantity)
        print("----- time: %s  -----" % round((time.time() - start_time), 2))
    Material_trends.append(Yearly_avg_cost)

fig, axs = plt.subplots(3,3, sharex=True)
for nn, ax in enumerate(axs.flat):
    plot_name = material_sheets[Materials[nn]]
    y = Material_trends[nn]
    line, = ax.plot(range(1995,2023), y)
    ax.set_title(plot_name)
fig.supxlabel("Year")
fig.supylabel("Average Cost of Material")
plt.show()

#axs[0,0].plot(range(1995,2023), Material_trends[0], label="Ti metal", color="blue")
#plt.title("Ti metal")
#axs[0,1].plot(range(1995,2023), Material_trends[1], label="Aluminium", color="red")
#plt.title("Aluminium")
#axs[0,2].plot(range(1995,2023), Material_trends[2], label="Copper", color="green")
#plt.title("Copper")
#axs[1,0].plot(range(1995,2023), Material_trends[3], label="Nickel", color="purple")
#plt.title("Nickel")
#axs[1,1].plot(range(1995,2023), Material_trends[4], label="Titanium O2", color="yellow")
#plt.title("Titanium O2")
#axs[1,2].plot(range(1995,2023), Material_trends[5], label="Tungsten", color="cyan")
#plt.title("Tungsten")
#plt.show()

