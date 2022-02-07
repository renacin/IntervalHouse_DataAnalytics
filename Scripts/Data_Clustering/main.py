# Name:                                            Renacin Matadeen
# Date:                                               02/04/2022
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data K-Means Clustering
#
# ----------------------------------------------------------------------------------------------------------------------
from Funcs.func import *
# ----------------------------------------------------------------------------------------------------------------------

# Define Main Logic Of K-Means Clustering Attempt
def main():
    """ Main Logic Of Python Code """

    # Import & Export Paths
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Census_CleanedData_Focus.csv"
    export_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Membership.csv"

    # Filter Data If Needed, But Better To Filter In CSV First!
    focus_rows = []
    df_filtered = DataTransform.filter_data(raw_data_path, focus_rows)

    # Normalize Data & Describe
    stuid_data = df_filtered["S_CTUID"].tolist()
    df_filtered.drop("S_CTUID", axis=1, inplace=True)
    df_scaled = DataTransform.scaled_z(df_filtered)

    # # Determine Optimal Number Of Clusters
    # DataClustering.elbow_chart(df_scaled)
    # DataClustering.silhouette_chart(df_scaled)
    # DataClustering.dendrogram_plot(df_scaled)

    # Perform K Means Analysis & Determine Cluster Memberships
    labels_ = DataClustering.k_means(df_scaled, 5)

    # Create New Pandas Dataframe & Export Data
    final_df_data = {"S_CTUID": stuid_data, "Membership": labels_}
    final_df = pd.DataFrame.from_dict(final_df_data)
    final_df.to_csv(export_data_path, index = False)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
