# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

class CensusDataPrep:
    """This class will help store methods that will efficiently parse, reorganize, and append Census data to a shapefile."""

    def isolate_data(in_path, out_path, geo_range, geoname, geo_type):

        """
        This class method imports the CSV containing Census data and writes another CSV with only the rows
        within the range specified. Data is filtered this way as it is too intensive to continuously read, and filter
        through the original Census profile.

        This function takes:
            + IN_PATH:
                - Leadings to the original CSV file containing all census data for a certain geographic scale of measurement
            + OUT_PATH:
                - Leadings to the place where a filtered dataframe will be written as a CSV
            + GEO_RANGE:
                - The range of geographic areas you would like to parse from the main dataset
            + GEO_NAME:
                - The column name in the Census dataset that shows

        Notes:
            + In Census Tract Census Data ALT_GEO_CODE == CTUID
            + In Dissemination Area Census GEO_NAME == DAUID
        """

        # Init temporary dataframe; set chunksize to 1'000'000 lines
        temp_df = pd.DataFrame()
        chunksize = 10 ** 6

        # Filter rows; must be within range defined by user. Append to new dataframe
        counter = 1
        for chunk in pd.read_csv(in_path, chunksize=chunksize, low_memory=False):

            chunk = chunk[pd.to_numeric(chunk[geoname], errors="coerce").notnull()]
            chunk[geoname] = chunk[geoname].astype(int)
            temp_focus_df = chunk[chunk[geoname].between(geo_range[0], geo_range[1])]
            frames = [temp_df, temp_focus_df]
            temp_df = pd.concat(frames)

            print(f"Chunk {counter}: Lines Parsed: {len(temp_focus_df)}, Total Lines In Output File: {len(temp_df)}")
            counter += 1

        # Write temporary dataframe to out_path
        complete_outpath = f"{out_path}/{geo_type}_CensusData2016.csv"
        temp_df.to_csv(complete_outpath, index=False)
