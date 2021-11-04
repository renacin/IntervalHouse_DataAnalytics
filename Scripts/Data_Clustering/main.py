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
    focus_rows = []
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Flower_IRIS_Data.csv"
    df = DataPrep.filter_data(raw_data_path, focus_rows)

    # Normalize Data
    df_scaled = DataPrep.max_norm(df, "species")

    # For Debugging
    print(df_scaled.info())
    print(df_scaled.head())

    # # Determine Optimal Number Of Clusters
    # Clustering.Elbow_chart(df_scaled, ["species"])
    # Clustering.Silhouette_chart(df_scaled, ["species"])
    # Clustering.Dendrogram(df_scaled, ["species"])

    # # Perform K Means Analysis & Determine Cluster Memberships
    # # centroids, labels = Clustering.K_Means(df_scaled, 7, ["species"])




# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
