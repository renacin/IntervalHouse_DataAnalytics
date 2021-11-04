# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import dendrogram, linkage

# ----------------------------------------------------------------------------------------------------------------------


class DataPrep:
    """ Prepare data for K-Means Clustering """


    def filter_data(data_path: str, focus_variables: list) -> "Pandas Dataframe":
        """
        This class method imports the CSV file as a pandas dataframe and filters it
        based on the fields the user wants to focus on.
        """

        try:
            df = pd.read_csv(data_path)
        except PermissionError:
            print("Files Currently Open In Another Program")

        return df[focus_variables]


    def max_norm(df: "Pandas Dataframe", skip_col: str) -> "Pandas Dataframe":
        """
        This class method takes the provided pandas dataframe and normalizes
        al fields based on Min&Max values. New dataframe is returned
        """

        # Make a copy of the data to ensure non-destructive methods
        df_scaled = df.copy()
  
        # Apply Max Normalization For Each Column | Skip CT_UID
        for column in df_scaled.columns:

            if (column != skip_col):
                df_scaled[column] = df_scaled[column]  / df_scaled[column].max()

        df_scaled = df_scaled.fillna(0)
        return df_scaled



class Clustering:
    """ Conduct K-Means Clustering Of Data """


    def Elbow_chart(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Make Copy Just Incase
        df = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df.drop([col], axis=1, inplace=True)

        # Create New Plot For Data
        plt.plot()
        X = df.to_numpy() 

        # Iterate Through Max Num Of K For Elbow Chart
        WSCC = []
        K = range(2, 15)
        for k in K:
            kmeanModel = KMeans(n_clusters=k, max_iter=150, random_state=0)
            kmeanModel.fit(X)
            WSCC.append(kmeanModel.inertia_)

        # Plot The Elbow Chart
        plt.plot(K, WSCC, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Overall Distortion (WCSSE)")
        plt.title("Elbow Chart: Finding Optimal K-Value")
        plt.show()


    def Silhouette_chart(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Given K numbers of clusters, determine the silouette scores for each iteration,
        render a silouette score chart informing the user of the optimal number of clusters
        for a K-Means analysis
        """

        # Make Copy Just Incase
        df = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df.drop([col], axis=1, inplace=True)

        # Create New Plot For Data
        plt.plot()
        X = df.to_numpy() 

        # Run K-Means Analysis & Calculate Silhouette Score For Each K Iteration
        sil_score = []
        K = range(2, 15)
        for k in K:
            kmeanModel = KMeans(n_clusters=k, max_iter=150, random_state=0)
            kmeanModel.fit(X)
            score = silhouette_score(X, kmeanModel.labels_)
            sil_score.append(score)

        # Find K Iteration With Highest Score
        max_k = (sil_score.index(max(sil_score))) + 2

        # Plot The Elbow Chart
        plt.plot(K, sil_score, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Silhouette Score (Euclidean Distance)")
        plt.title("Silhouette Score Chart: Finding Optimal K-Value")
        plt.axvline(max_k, linestyle="--")
        plt.show()


    def Dendrogram(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Create a dendrogram to help the user identify the optimal number of clusters for thier clustering attempt
        """

        # Make Copy Just Incase
        df = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df.drop([col], axis=1, inplace=True)

        # Find Distance Between Values
        Z = linkage(df, 'ward')

        # Plot The Dendrogram
        plt.plot()
        plt.xlabel("Clusters")
        plt.ylabel("Distance (Ward)")

        # Make the dendrogram | Do not render x-axis, too many labels
        dendrogram(Z, labels=df.index, leaf_rotation=90)
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        plt.show()



    def K_Means(df: "Pandas Dataframe", k : "Number Of Clusters", drop_col: list):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Drop Unneeded Columns
        for col in drop_col:
            df.drop([col], axis=1, inplace=True)

        # Dataframe To Numpy Array For Clustering
        X = df.to_numpy()

        # Perform K-Means Analysis
        kmeanModel = KMeans(n_clusters=k, max_iter=150)
        kmeanModel.fit(X)

        # Return Cluster Membership & Centroid Locations
        return [kmeanModel.cluster_centers_, kmeanModel.labels_]


    