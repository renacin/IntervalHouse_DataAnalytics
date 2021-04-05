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
        through the original Census profile. Note in Census Tract Census Data ALT_GEO_CODE == CTUID, and in
        Dissemination Area Census GEO_NAME == DAUID
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
        temp_df.to_csv(out_path, index=False)



    def remove_data(in_path, out_path):
        """
        This class method imports a CSV containing filtered Census data (for a certain geography only), and removes
        unneeded columns in an effort to reduce the size of the file. The resulting output file is then written to
        a CSV. Note that only total population data will be focused on.
        """

        # Drop unneeded columns
        census_data = pd.read_csv(in_path, low_memory=False)
        col2remove = ["CENSUS_YEAR", "GEO_LEVEL", "GNR", "GNR_LF",
                      "DATA_QUALITY_FLAG",
                      "Notes: Profile of Dissemination Areas (2247)",
                      "Notes: Profile of Census Tracts (2247)",
                      "Dim: Sex (3): Member ID: [2]: Male",
                      "Dim: Sex (3): Member ID: [3]: Female"]

        for col in col2remove:
            try:
                census_data = census_data.drop(columns=[col])
            except KeyError:
                pass

        census_data.to_csv(out_path, index=False)



    def transpose_data(in_path, out_path, id_type):
        """
        This class method imports a CSV containing filtered Census data (for a certain geography only), and transposes
        it and writes the cleaned data as a CSV. Data are transposed as it is not sutable for analysis or geo-visualizations
        in its current form. Note that this function will parse all 2247 unique columns within the Census Profile.
        """

        # Grab names for columns; clean up, Get Unique UIDs as list from first tract observation
        cleaned_census_data = pd.read_csv(in_path, low_memory=False)
        for col in ["DIM: Profile of Dissemination Areas (2247)", "DIM: Profile of Census Tracts (2247)"]:
            try:
                unq_census_fields = list(cleaned_census_data[col][0:2247])
            except KeyError:
                pass

        # Create New Column Names With Col Names Parsed; Ensure Readability
        columns_list = []
        for idx, field in enumerate(unq_census_fields):
            toreplace = [" ", "_", ",", "-", "..."]
            for char in toreplace:
                field = field.replace(char, "")
            columns_list.append(str(idx + 1) + "_" + field)


        # Grab unique rows & begin writting data to temp lists
        unq_da = list(cleaned_census_data[id_type].unique())
        rows_list = []
        start_idx = 0
        end_idx = 2247

        for idx, da in enumerate(unq_da):
            idx += 1
            if idx != 1:
                start_idx += 2247
                end_idx += 2247

            rows_list.append(list(cleaned_census_data["Dim: Sex (3): Member ID: [1]: Total - Sex"][start_idx:end_idx]))

        # Create a new DF with parsed data
        cleaned_df = pd.DataFrame(rows_list, columns = columns_list)
        cleaned_df.insert(loc=0, column=id_type, value=unq_da)
        cleaned_df.to_csv(out_path, index=False)
