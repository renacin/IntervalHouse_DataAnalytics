# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
from Census_Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of Census Data Cleaner
def main():

    try:
        # Filter Toronto Census Tract Data From Main Census File
        ct_census_data_path = r"C:\Users\renac\Downloads\CT_CensusData_2016.csv"
        ct_filtered_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Data\CensusData\CensusToronto_CT_2016"
        ct_range = (535000100, 535080202)
        CensusDataPrep.isolate_data(ct_census_data_path, ct_filtered_data_path, ct_range, "ALT_GEO_CODE", "CT")
    except FileNotFoundError:
        print("CT File Not Found")

    try:
        # Filter Toronto Dissemination Area Data From Main Census File
        da_census_data_path = r"C:\Users\renac\Downloads\DA_CensusData_2016.csv"
        da_filtered_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Data\CensusData\CensusToronto_DA_2016"
        da_range = (35200000, 35205000)
        CensusDataPrep.isolate_data(da_census_data_path, da_filtered_data_path, da_range, "GEO_NAME", "DA")
    except FileNotFoundError:
        print("DA File Not Found")

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
