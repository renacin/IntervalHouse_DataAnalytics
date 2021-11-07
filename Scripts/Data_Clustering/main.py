# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data K-Means Clustering
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of K-Means Clustering Attempt
def main():
    """ Main Logic Of Python Code """

    # Filter Only Income Data Fields For Now
    focus_rows = ["S_CTUID", "16", "17", "18", "19", "20", "21", "22", "40", "41", "42", "43", "44", "45", "46", "47"]
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Census_CleanedData.csv"
    df_filtered = DataTransform.filter_data(raw_data_path, focus_rows)

    # Normalize Data & Describe
    df_scaled = DataTransform.max_norm(df_filtered, "S_CTUID")
    # DataTransform.describe_data(df_scaled, "S_CTUID")
    DataTransform.corr_data(df_scaled, "S_CTUID")


    # # Determine Optimal Number Of Clusters
    # DataClustering.elbow_chart(df_scaled, ["S_CTUID"])
    # DataClustering.silhouette_chart(df_scaled, ["S_CTUID"])
    # DataClustering.dendrogram_plot(df_scaled, ["S_CTUID"])

    # # Perform K Means Analysis & Determine Cluster Memberships
    # centroids, labels = DataClustering.k_means(df_scaled, 3, ["﻿S_CTUID"])
    # centroids, labels = DataClustering.mean_shift(df_scaled, ["﻿S_CTUID"])



# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
