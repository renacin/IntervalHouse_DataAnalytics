# Authors:                                      Renacin M, Fazia M, Madeleine W
# Date:                                               02/04/2022
# Title                   Interval House Data Analytics Project: 2016 Canadian Census Data K-Means Clustering
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

sns.set(style="darkgrid")
# ----------------------------------------------------------------------------------------------------------------------


class DataTransform():
    """ This class stores all functions related to the transformation and description of data """


    @staticmethod
    def filter_data(data_path: str, focus_variables: list) -> "Pandas Dataframe":
        """
        This class method imports the CSV file as a pandas dataframe and filters it
        based on the fields the user wants to focus on.
        """

        try:
            df_raw = pd.read_csv(data_path)
            df_filtered = df_raw.copy()
            df_filtered = df_filtered.fillna(0)

            if len(focus_variables) != 0:
                return df_filtered[focus_variables]

            return df_filtered

        except PermissionError:
            print("Files Currently Open In Another Program")
            raise PermissionError


    @staticmethod
    def scaled_z(df_raw: "Pandas Dataframe") -> "Pandas Dataframe":
        """
        This class method takes the provided pandas dataframe and normalizes
        all fields based on Sklearn's built in scaler
        """

        # Make a copy of the data to ensure non-destructive methods
        df_copy = df_raw.copy()
        scaler = StandardScaler()
        np_scaled_data = scaler.fit_transform(df_copy)
        scaled_df = pd.DataFrame(np_scaled_data)
        scaled_df.columns = list(df_copy.columns)

        return scaled_df



class DataClustering():
    """ This class stores all functions related to the process of clustering data """


    @staticmethod
    def elbow_chart(df_raw: "Pandas Dataframe"):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Make Copy Just Incase
        df_copy = df_raw.copy()

        # Create New Plot For Data
        plt.plot()
        training_data = df_copy.to_numpy()

        # Iterate Through Max Num Of K For Elbow Chart
        wscc = []
        num_k = range(1, 30)
        for k in num_k:
            kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=500, n_init = 10, random_state=0)
            kmean_model.fit(training_data)
            wscc.append(kmean_model.inertia_)

        # Plot The Elbow Chart
        plt.plot(num_k, wscc, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Overall Distortion (WCSSE)")
        plt.title("Elbow Chart: Finding Optimal K-Value")
        plt.show()


    @staticmethod
    def silhouette_chart(df_raw: "Pandas Dataframe"):
        """
        Given K numbers of clusters, determine the silouette scores for each iteration,
        render a silouette score chart informing the user of the optimal number of clusters
        for a K-Means analysis
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Create New Plot For Data
        plt.plot()
        training_data = df_raw.to_numpy()

        # Run K-Means Analysis & Calculate Silhouette Score For Each K Iteration
        sil_score = []
        num_k = range(2, 30)
        for k in num_k:
            kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=500, n_init = 10, random_state=0)
            kmean_model.fit(training_data)
            score = silhouette_score(training_data, kmean_model.labels_, metric='euclidean')
            sil_score.append(score)

        # Find K Iteration With Highest Score
        max_k = (sil_score.index(max(sil_score))) + 2

        # Plot The Elbow Chart
        plt.plot(num_k, sil_score, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Silhouette Score (Euclidean Distance)")
        plt.title("Silhouette Score Chart: Finding Optimal K-Value")
        plt.axvline(max_k, linestyle="--")
        plt.show()


    @staticmethod
    def dendrogram_plot(df_raw: "Pandas Dataframe"):
        """
        Create a dendrogram to help the user identify the optimal number of clusters for their clustering attempt
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Find Distance Between Values | Make use of Ward's Linkage Method
        z_linkages = linkage(df_raw, 'ward')

        # Plot The Dendrogram
        plt.plot()
        plt.xlabel("Clusters")
        plt.ylabel("Distance (Ward)")
        plt.title("Hierarchical Clustering: Dendrogram - Combination Of Clusters")

        # Make the dendrogram | Do not render x-axis, too many labels
        dendrogram(z_linkages, labels=df_raw.index, leaf_rotation=90)
        plt_ax = plt.gca()
        plt_ax.get_xaxis().set_visible(False)
        plt.show()


    @staticmethod
    def k_means(df_raw: "Pandas Dataframe", k : "Number Of Clusters"):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Dataframe To Numpy Array For Clustering
        training_data = df_raw.to_numpy()

        # Perform K-Means Analysis
        kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=300, n_init = 10, random_state=0)
        kmean_model.fit(training_data)

        # Return Cluster Membership & Centroid Locations
        return kmean_model.labels_


# ----------------------------------------------------------------------------------------------------------------------
# Define Main Logic Of K-Means Clustering Attempt
def main():
    """ Main Logic Of Python Code """

    # FILL IN IMPORT & EXPORT PATHS
    raw_data_path = r"C:\Users\renac\Documents\Programming\Python\IntervalHouse_DataAnalytics\Scripts\Data_Clustering\Data\Census_CleanedData_Attempt3.csv"
    export_data_path = r"C:\Users\renac\Desktop\Attempt3.csv"

    # DEL UNNEEDED COL IN CSV FIRST BEFORE USING THIS FEATURE
    focus_rows = []
    df_filtered = DataTransform.filter_data(raw_data_path, focus_rows)

    # NORMALIZE DATA
    stuid_data = df_filtered["S_CTUID"].tolist()
    df_filtered.drop("S_CTUID", axis=1, inplace=True)
    df_scaled = DataTransform.scaled_z(df_filtered)

    # # HOW MANY CLUSTERS?
    # DataClustering.elbow_chart(df_scaled)
    # DataClustering.silhouette_chart(df_scaled)
    # DataClustering.dendrogram_plot(df_scaled)

    # PERFORM K MEANS WITH NUMBER_OF_CLUSTERS | UP TO USER TO CHANGE
    NUMBER_OF_CLUSTERS = 5
    labels_ = DataClustering.k_means(df_scaled, NUMBER_OF_CLUSTERS)

    # EXPORT DATA!
    final_df_data = {"S_CTUID": stuid_data, "Membership": labels_}
    final_df = pd.DataFrame.from_dict(final_df_data)
    final_df.to_csv(export_data_path, index = False)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
