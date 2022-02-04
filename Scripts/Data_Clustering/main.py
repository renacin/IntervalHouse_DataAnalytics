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
    focus_rows = []
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Census_CleanedData_Focus.csv"
    df_filtered = DataTransform.filter_data(raw_data_path, focus_rows)

    # Normalize Data & Describe
    # S_CTUID_Data = df_filtered["S_CTUID"].tolist()
    df_filtered.drop("S_CTUID", axis=1, inplace=True)
    df_scaled = DataTransform.scaled_z(df_filtered)

    # DataTransform.describe_data(df_scaled)
    # DataTransform.corr_data(df_scaled, r"C:\Users\renac\Desktop\Coor_Matrix.csv")

    # Determine Optimal Number Of Clusters
    DataClustering.elbow_chart(df_scaled)
    DataClustering.silhouette_chart(df_scaled)
    DataClustering.dendrogram_plot(df_scaled)

    # Perform K Means Analysis & Determine Cluster Memberships
    centroids, labels = DataClustering.k_means(df_scaled, 13)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
