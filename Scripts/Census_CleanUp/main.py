# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
from Census_Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of Census Data Cleaner
def main():

    # Differences Beteen CT, DA Files
    geo_types = ["CT", "DA"]
    geo_ids = ["ALT_GEO_CODE", "GEO_NAME"]
    geo_ranges = [(535000100, 535080202), (35200000, 35205000)]


    # # Filter Toronto Census Tract & Dissemination Area Data From Main Census File
    # for tract_type, id_type, geo_range in zip(geo_types, geo_ids, geo_ranges):
    #     census_data_path = r"C:\Users\renac\Downloads\\" + tract_type + "_CensusData_2016.csv"
    #     filtered_data_path = r"C:\Users\renac\Downloads\FILTR_" + tract_type + "_CensusData_2016.csv"
    #     CensusDataPrep.isolate_data(census_data_path, filtered_data_path, geo_range, id_type, tract_type)
    #
    #
    # # Remove Unneeded Data
    # for tract_type in geo_types:
    #     filtered_data_path = r"C:\Users\renac\Downloads\FILTR_" + tract_type + "_CensusData_2016.csv"
    #     rm_data_path = r"C:\Users\renac\Downloads\RMV_" + tract_type + "_CensusData_2016.csv"
    #     CensusDataPrep.remove_data(filtered_data_path, rm_data_path)
    #
    #
    # # Transpose Data For Easier Data Analysis
    # for tract_type, id_type in zip(geo_types, geo_ids):
    #     rm_data_path = r"C:\Users\renac\Downloads\RMV_" + tract_type + "_CensusData_2016.csv"
    #     transpose_data_path = r"C:\Users\renac\Downloads\TRNSP_" + tract_type + "_CensusData_2016.csv"
    #     CensusDataPrep.transpose_data(rm_data_path, transpose_data_path, id_type)
    #
    #
    # # Final Data Clean Up
    # for tract_type in geo_types:
    #     transpose_data_path = r"C:\Users\renac\Downloads\TRNSP_" + tract_type + "_CensusData_2016.csv"
    #     altr_output_data = r"C:\Users\renac\Downloads\ALTR_" + tract_type + "_CensusData_2016.csv"
    #     CensusDataPrep.altr_for_shp(transpose_data_path, altr_output_data, tract_type)


    # Parse Data For Specific Variables
    for tract_type in geo_types:
        altr_output_data = r"C:\Users\renac\Downloads\ALTR_" + tract_type + "_CensusData_2016.csv"
        spc_output_data = r"C:\Users\renac\Downloads\SPC_" + tract_type + "_CensusData_2016.csv"
        data_range = [741, 758]
        CensusDataPrep.specifc_columns(altr_output_data, spc_output_data, tract_type, data_range)




# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
