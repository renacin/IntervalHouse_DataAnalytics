# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data K-Means Clustering
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of K-Means Clustering Attempt
def main():

    # Filter Only Income Data Fields For Now
    focus_rows = ["S_CTUID", "52"]
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\K_Means_Clustering\Data\Census_CleanedData.csv"
    df = DataPrep.filter_data(raw_data_path, focus_rows)

    # Normalize Data
    df_scaled = DataPrep.max_norm(df, "S_CTUID")

    # Determine Optimal Number Of Clusters
    Clustering.Elbow_chart(df_scaled, ["S_CTUID"])
    Clustering.Dendrogram(df_scaled, ["S_CTUID"])


    # Perform K Means Analysis & Determine Cluster Memberships
    # centroids, labels = Clustering.K_Means(df_scaled, 7, ["S_CTUID"])




# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
