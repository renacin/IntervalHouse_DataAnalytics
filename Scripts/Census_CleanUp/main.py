# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
from Census_Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of Census Data Cleaner
def main():

    # Filter Toronto Census Tract Data From Main Census File
    ct_census_data_path = r"C:\Users\renac\Downloads\CT_CensusData_2016.csv"
    ct_filtered_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Data\CensusData\CensusToronto_CT_2016"
    ct_range = [535_000_100, 535_080_202]
    CensusDataPrep.isolate_data(ct_census_data_path, ct_filtered_data_path, ct_range, "ALT_GEO_CODE", "CT")

    # Filter Toronto Dissemination Area Data From Main Census File
    ct_census_data_path = r"C:\Users\renac\Downloads\CT_CensusData_2016.csv"
    ct_filtered_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Data\CensusData\CensusToronto_CT_2016"
    ct_range = [535_000_100, 535_080_202]
    CensusDataPrep.isolate_data(ct_census_data_path, ct_filtered_data_path, ct_range, "ALT_GEO_CODE", "CT")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
