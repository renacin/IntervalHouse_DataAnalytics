# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: Canadian Census Data Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------

class CensusDataPrep:
    """This class will help store methods that will efficiently parse, reorganize, and append Census data to a shapefile."""

    def isolate_data(in_path, out_path, geo_range=[0, 0], geoname):
        """
        This class method imports the CSV containing Census data and writes another CSV with only the rows
        within the range specified. Data is filtered this way as it is too intensive to continuously read, and filter
        through the original Census profile.

        This function takes:
            + IN_PATH:
                leading to the original CSV file containing all census data for a certain geographic scale of measurement
            + OUT_PATH:
                leading to the place where a filtered dataframe will be written as a CSV
            + GEO_RANGE:
                the range of geographic areas you would like to parse from the main dataset
        """

        temp_df = pd.DataFrame()

        # [1.] File Is Too Large To Hold In Memory, Read In 1'000'000 Line Chunks
        chunksize = 10 ** 6

        # [2.] Filter Geo Polygons Based On GEO_NAME, Append To New DF
        counter = 1
        for chunk in pd.read_csv(in_path, chunksize=chunksize):

            chunk = chunk[pd.to_numeric(chunk['GEO_NAME'], errors='coerce').notnull()]
            chunk['GEO_NAME'] = chunk['GEO_NAME'].astype(int)

            temp_focus_df = chunk[chunk["GEO_NAME"].between(35200000, 35205000)] # CoT DAs

            frames = [temp_df, temp_focus_df]
            temp_df = pd.concat(frames)

            print("Progress: Chunk {}/47".format(counter)) # Write To A CSV, This Takes Up Too Much Memory
            counter += 1

        # [3.] Write To CSV, Don't Repeat Intensive Processes
        temp_df.to_csv(out_path, index=False)








    def parse_data():
        pass

    def reorg_data():
        pass
