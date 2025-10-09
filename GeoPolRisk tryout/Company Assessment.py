import importlib.util
import os
from src.geopolrisk.assessment.main import *
from src.geopolrisk.assessment.database import database

############### Company-specific assessment
ProductionQuantity, hhi = HHI("Titanium", 1995, "Company")
Num_Company, TotalTrade_Company, Price_Company = importrisk_company("Titanium", 1995)

Values_Company = GeoPolRisk(
    Num_Company,
    TotalTrade_Company,
    Price_Company,
    ProductionQuantity,
    hhi
)

df = createresultsdf()
df["DBID"] = ["Company"]
df["Country [Economic Entity]"] = ["Company"]
df["Raw Material"] = ["Titanium"]
df["Year"] = ["1995"]
df["GeoPolRisk Score"] = [Values_Company[0]]
df["GeoPolRisk Characterization Factor [eq. Kg-Cu/Kg]"] = [Values_Company[1]]
df["HHI"] = [hhi]
df["Import Risk"] = [Values_Company[2]]
df["Price"] = [Price_Company]

excel_path = databases.directory + "/output/results_company_2.xlsx"
df.to_excel(excel_path, index=False)
writetodb(df)