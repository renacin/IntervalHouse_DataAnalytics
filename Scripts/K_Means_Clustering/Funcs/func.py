# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

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
        all fields based on Min&Max values. New dataframe is returned
        """

        # Make a copy of the data to ensure non-destructive methods
        df_scaled = df.copy()
  
        # Apply Max Normalization For Each Column | Skip CT_UID
        for column in df_scaled.columns:
            if (column != skip_col):
                df_scaled[column] = df[column]  / df[column].max()

        return df_scaled



class K_Means:
    """ Conduct K-Means Clustering Of Data """


    def elbow_chart(df: "Pandas Dataframe", drop_col: list):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Drop Unneeded Columns
        for col in drop_col:
            df.drop([col], axis=1, inplace=True)

        # Create New Plot For Data
        plt.plot()
        X = df.to_numpy() 

        # Iterate Through Max Num Of K For Elbow Chart
        distortions = []
        K = range(1, 15)
        for k in K:
            kmeanModel = KMeans(n_clusters=k, max_iter=150)
            kmeanModel.fit(X)
            distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, "euclidean"), axis=1)) / X.shape[0])

        # Plot The Elbow Chart
        plt.plot(K, distortions, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Overall Distortion (WCSSE)")
        plt.title("Elbow Chart: Finding Optimal K-Value")
        plt.show()


    def clustering(df: "Pandas Dataframe", k : "Number Of Clusters", drop_col: list):
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


    