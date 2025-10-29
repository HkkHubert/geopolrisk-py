import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

"""Data to build the a dataframe that can be used for the stacked bar chart generation"""
#######
AC_models = ["EXACT A320", "Howe's A320", "A330", "B777", "B787", "A350"]
Manganese = [38.85656888,48.97762179,161.1389014,116.880915,72.09966592,72.06039102]
Copper = [1384.171257,913.0609604,2513.371138,2825.039634,1082.565334,875.9629683]
Nickel = [6964.277016,283.9915901,19812.82372,5943.729474,12843.6373,21379.08083]
Vanadium = [1378.157375,744.3113666,326.0912801,3401.124482,7846.357414,12575.07746]
Aluminium = [8990.223254,13105.11323,35081.89764,51629.43816,15164.02264,15769.75185]
Magnesium = [6.225524166,6.57726504,17.44237295,31.3784674,4.350184269,4.561960682]
Titanium = [8161.769897,4551.568348,16647.24388,20535.98667,39830.49318,41776.33159]
Beryllium = [525.3973629,0,0,0,0,0]
Cobalt = [1160.997597,0,0,0,749.230719,0]
Tungsten = [291.3825299,0,128.5327318,0,0,759.3230804]
Lanthanum = [3.383340546,0,0,0,0,0]
Niobium = [2337.263847,0,2140.100454,717.6138237,0,0]
Tantalum = [172.9091354,0,3577.599564,0,0,0]
Cerium = [6.06085733,0,0,0,0,0]
Lithium = [0,0,0,0,5107.80557,5356.464632]
Op_empty_masses = [44928,34420,105448,134800,129000,142400]

Materials = np.array([Manganese, Copper, Nickel, Vanadium, Aluminium, Magnesium, Titanium,
                     Beryllium, Cobalt, Tungsten, Lanthanum, Niobium, Tantalum, Cerium, Lithium])
Column_names = ["Aircraft model", "Manganese", "Copper", "Nickel", "Vanadium", "Aluminium", "Magnesium", "Titanium",
                     "Beryllium", "Cobalt", "Tungsten", "Lanthanum", "Niobium", "Tantalum", "Cerium", "Lithium"]
########

### Looping through the lists to assign the correct values to each aircraft model ###
Data_columns = []
for i, Aircraft in enumerate(AC_models):
    Values_per_AC = [Aircraft]
    for M in Materials:
        Values_per_AC.append(M[i])
    Data_columns.append(Values_per_AC)

### Assembling the dataframe that can be plotted ###
Bar_chart_data = pd.DataFrame(Data_columns, columns = Column_names)

### Plotting functions ###
Bar_chart_data.plot(x= "Aircraft model", kind = "bar", stacked = True, figsize = (14,4), colormap = "tab20b")
plt.ylabel("Aircraft Criticality (kf of Cu eq. mass)")
plt.xticks(rotation = 0)
plt.scatter(Bar_chart_data["Aircraft model"],Op_empty_masses, marker = "x", color = "black", label = "OEM (kg)")
plt.legend(loc = "upper left", ncols = 2)

### Saving the figure as an svg file for optimal use in the report
plt.savefig("G:/Studenten/PLM/HubertHakk/Python Projects/Stacked_chart.svg")
plt.show()

### Making the standard bar chart for crit. material masses
Absolute_crit_mat_masses = [22075.08451,25346.099,73548.04,100940.1324,47185.62,51031.3704]
plt.figure(figsize = (14,4))
plt.scatter(Bar_chart_data["Aircraft model"],Op_empty_masses, marker = "x", color = "black", label = "OEM")
plt.legend(loc = "best")
plt.bar(AC_models, Absolute_crit_mat_masses, label = Bar_chart_data["Aircraft model"])
plt.ylabel("Mass of critical materials (kg)")
plt.xlabel("Aircraft models")
plt.savefig("G:/Studenten/PLM/HubertHakk/Python Projects/Absolute_mass_chart.svg")
plt.show()