import importlib.util
import os
from src.geopolrisk.assessment.main import gprs_calc
from src.geopolrisk.assessment.database import database

########## For the "company" assessment
from geopolrisk.assessment.core import HHI, importrisk_company, GeoPolRisk
from geopolrisk.assessment.utils import createresultsdf
##########

Years = [2022]
Countries = [ "EU", "Airbus"]
Materials = ["Aluminium","Titanium","Titanium Metal", "Titanium Metal Unwrought", "Copper", "Nickel", "Cobalt", "Rare earth", "Niobium", "Beryllium", "Manganese", "Tantalum", "Magnesite", "Tungsten", "Lithium"]
AirbusCountriesDict = {
    "Airbus": ["France", "Germany", "United Kingdom", "Spain"],
    "EU": database.regionslist["EU"]
}

trial = gprs_calc(Years, Countries, Materials, region_dict=AirbusCountriesDict)

