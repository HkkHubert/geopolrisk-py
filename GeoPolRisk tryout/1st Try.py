import importlib.util
import os
from src.geopolrisk.assessment.main import *
from src.geopolrisk.assessment.database import database

Years = [2022]
Countries = ["Germany"]
Materials = ["Aluminium"]

trial = gprs_calc(Years,Countries, Materials)