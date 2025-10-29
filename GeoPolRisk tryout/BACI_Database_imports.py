import importlib.util
import os
import time

import numpy as np
import pandas as pd
from src.geopolrisk.assessment.main import *
from src.geopolrisk.assessment.database import database


###### Define the desired parameters
#Desired_year = "1995"


# Titanium metal products HS code: 810890
# Magnesite :251910
# Copper ores and concentrates: 260300
# Nickel ores and concentrates: 260400
# Aluminium ores and concentrates: 260600
# Aluminium metal?: 760110 (Aluminium, not alloyed, unwrought)
# Tungsten ores and concentrates: 261100
# Titanium ores and concentrates: 261400
# Niobium, tantalum, Vanadium: 261590
# Cobalt oxides and hydroxides: 282200
# Lithium carbonate: 283691
# REEs, Lanthanum, Scandium, (excl Cerium!?): 284690
#


#Provide the desired material HS code to perform the analysis
Resource = 810810

#Mapdf = databases.production["HS Code Map"]
#if Resource in Mapdf["Reference ID"].tolist():
#    mappedTableName = Mapdf.loc[Mapdf["Reference ID"] == Resource, "Sheet_name"]

### Create the arrays to assign the values to
#Year, Importer, Exporter, Material, Quantity, Value = [], [], [], [], [], []
Rows = []

### specify the timeframe to loop through
start, end = 2022, 2023

#### loop through all of the years to obtain the temporal data
start_time = time.time()
for y in range (start, end):

    path_to_BACI = databases.directory + "/BACI_HS92_V202501/BACI_HS92_Y" + str(y) + "_V202501.csv"

    Data = pd.read_csv(path_to_BACI)

    no_of_years = end - start

    for i in range(len(Data.k)):
        length = len(Data.k)
        if i % 50000 == 0:
            print((i / (length* no_of_years) + (y - start) / no_of_years)*100 , "% done", ", evaluated year = ", y) #### calculate the progress percentage to show to indicate how long the process will take
        if Data.k[i] == Resource:
            #Year.append(int(Data.t[i]))
            #Importer.append(int(Data.i[i]))
            #Exporter.append(int(Data.j[i]))
            #Material.append(int(Data.k[i]))
            #Quantity.append(Data.q[i])
            #Value.append(Data.v[i])
            Single_row = [int(Data.t[i]),int(Data.i[i]),int(Data.j[i]), int(Data.k[i]), Data.q[i], Data.v[i]]
            Rows.append(Single_row)
    print("----- time: %s  -----" % round((time.time() - start_time), 2))

Data = pd.DataFrame(Rows, columns = ["Year", "Importer", "Exporter", "Material", "Quantity", "Value"])
#Data = pd.DataFrame(np.transpose([Year, Importer, Exporter, Material, Quantity, Value], columns = ["Year", "Importer", "Exporter", "Material", "Quantity", "Value"])
print(Data.head())
print("number of material transactions =", len(Data))

path_to_results = databases.directory + "/databases/export_results_unwrought_Ti.xlsx"
with pd.ExcelWriter(path_to_results) as writer:
    Data.to_excel(writer, sheet_name = str(Resource))