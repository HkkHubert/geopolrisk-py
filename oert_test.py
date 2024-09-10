# _price = instance.price
# _wgi = instance.wgi
# Resource = "Nickel"
# HS = "260400"
# HS_price = 2604
# Country = "Germany"
# ISO = "276"
# Year = "2020"

# regions()
# TradeData, priceif = worldtrade(year = Year, country = ISO, commodity = HS)
# ProductionData = ProductionData(Resource, Country)
# WTAData = weightedtrade(Year, TradeData = TradeData, PIData = _wgi, scenario = 0, recyclingrate = 0.00)

# YearlyAveragePrice = 10203.98
# # Optional - A database already exists that can be used to fetch the price data.
# YearlyAveragePrice =  _price[Year].tolist()[_price.HS.to_list().index(HS_price)]
# result = GeoPolRisk(ProductionData, WTAData, Year, YearlyAveragePrice)

# print(result)
# print("\n")

# -------------------------²----------------------------------------

# test main_comlete()


# the main_complete()-function gets an error, because the copied price-table from Libray.db
# has different HS-Codes - see different HS and HS_price definition on the top test example

ListofMetals = [
    260400,
    261000,
    260300,
    283691,
    282200,
]
regions = {'Trial' : [
    "Austria",
    "Belgium",
    "Belgium-Luxembourg",
    "Bulgaria",
    "Croatia"
],}

ListofCountries = [
    36,
    124,
    251,
    276,
    392,
    826,
    842,
]
ListofYear = [2018, 2019, 2020]


from geopolrisk.assessment.main import gprs_calc
# from geopolrisk.assessment.geopolrisk import gprs_calc

gprs_calc(ListofYear,ListofCountries, ListofMetals)


# -----------------------------------------------------------------
