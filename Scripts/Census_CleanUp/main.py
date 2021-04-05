# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
from Census_Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of Census Data Cleaner
def main():

    # # Filter Toronto Census Tract & Dissemination Area Data From Main Census File
    # ct_census_data_path = r"C:\Users\renac\Downloads\CT_CensusData_2016.csv"
    # ct_filtered_data_path = r"C:\Users\renac\Downloads\FILTR_CT_CensusData_2016.csv"
    # ct_range = (535000100, 535080202)
    # CensusDataPrep.isolate_data(ct_census_data_path, ct_filtered_data_path, ct_range, "ALT_GEO_CODE", "CT")
    #
    # da_census_data_path = r"C:\Users\renac\Downloads\DA_CensusData_2016.csv"
    # da_filtered_data_path = r"C:\Users\renac\Downloads\FILTR_DA_CensusData_2016.csv"
    # da_range = (35200000, 35205000)
    # CensusDataPrep.isolate_data(da_census_data_path, da_filtered_data_path, da_range, "GEO_NAME", "DA")


    # Remove Unneeded Data
    for tract_type in ["CT", "DA"]:
        filtered_data_path = r"C:\Users\renac\Downloads\FILTR_" + tract_type + "_CensusData_2016.csv"
        transpose_data_path = r"C:\Users\renac\Downloads\RMV_" + tract_type + "_CensusData_2016.csv"
        CensusDataPrep.remove_data(filtered_data_path, transpose_data_path)


    # Transpose Data For Easier Data Analysis

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
