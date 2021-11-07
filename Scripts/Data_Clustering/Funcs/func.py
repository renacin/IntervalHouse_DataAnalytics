# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

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
        except PermissionError:
            print("Files Currently Open In Another Program")

        if len(focus_variables) != 0:
            return df_filtered[focus_variables]

        return df_filtered


    @staticmethod
    def max_norm(df_raw: "Pandas Dataframe", skip_col: str) -> "Pandas Dataframe":
        """
        This class method takes the provided pandas dataframe and normalizes
        al fields based on Min&Max values. New dataframe is returned
        """

        # Make a copy of the data to ensure non-destructive methods
        df_scaled = df_raw.copy()

        # Apply Max Normalization For Each Column | Skip CT_UID
        for column in df_scaled.columns:
            if column != skip_col:
                df_scaled[column] = df_scaled[column]  / df_scaled[column].max()

        df_scaled = df_scaled.fillna(0)
        return df_scaled


    @staticmethod
    def describe_data(df_raw: "Pandas Dataframe", skip_col: str):
        """
        This function returns basic data description information.
        Histograms, Scatterplots, Mean, Standard Deviation Etc...
        """

        # Make Copy Just Incase
        df_copy = df_raw.copy()

        # Drop Identifier Col
        df_copy.drop([skip_col], axis=1, inplace=True)

        # Return Basic Field Description
        print(df_copy.info())

        # Return Basic Data Description
        print(df_copy.describe())

        # Render Basic Scatter & Histogram Chart
        sns.pairplot(df_copy, plot_kws=dict(marker="+", linewidth=0.5), diag_kws=dict(fill=False), corner=True)
        plt.show()



class DataClustering():
    """ This class stores all functions related to the process of clustering data """


    @staticmethod
    def elbow_chart(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Make Copy Just Incase
        df_copy = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df_copy.drop([col], axis=1, inplace=True)

        # Create New Plot For Data
        plt.plot()
        training_data = df_copy.to_numpy()

        # Iterate Through Max Num Of K For Elbow Chart
        wscc = []
        num_k = range(1, 15)
        for k in num_k:
            kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=300, n_init = 10, random_state=0)
            kmean_model.fit(training_data)
            wscc.append(kmean_model.inertia_)

        # Plot The Elbow Chart
        plt.plot(num_k, wscc, "bx-")
        plt.xlabel("Number Of Clusters (K)")
        plt.ylabel("Overall Distortion (WCSSE)")
        plt.title("Elbow Chart: Finding Optimal K-Value")
        plt.show()


    @staticmethod
    def silhouette_chart(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Given K numbers of clusters, determine the silouette scores for each iteration,
        render a silouette score chart informing the user of the optimal number of clusters
        for a K-Means analysis
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df_raw.drop([col], axis=1, inplace=True)

        # Create New Plot For Data
        plt.plot()
        training_data = df_raw.to_numpy()

        # Run K-Means Analysis & Calculate Silhouette Score For Each K Iteration
        sil_score = []
        num_k = range(2, 15)
        for k in num_k:
            kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=300, n_init = 10, random_state=0)
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
    def dendrogram_plot(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Create a dendrogram to help the user identify the optimal number of clusters for thier clustering attempt
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df_raw.drop([col], axis=1, inplace=True)

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
    def k_means(df_raw: "Pandas Dataframe", k : "Number Of Clusters", drop_col: list):
        """
        Run K number of K-Means analyses to identify optimal K value. Plot distortions
        via a simple line chart for user.
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Drop Unneeded Columns
        for col in drop_col:
            df_raw.drop([col], axis=1, inplace=True)

        # Dataframe To Numpy Array For Clustering
        training_data = df_raw.to_numpy()

        # Perform K-Means Analysis
        kmean_model = KMeans(n_clusters=k, init = 'k-means++', max_iter=300, n_init = 10, random_state=0)
        kmean_model.fit(training_data)

        # Return Cluster Membership & Centroid Locations
        return [kmean_model.cluster_centers_, kmean_model.labels_]


    @staticmethod
    def mean_shift(df_raw: "Pandas Dataframe", drop_col: list):
        """
        Run Mean-Shift analysis to identify clusters in data.
        How do I determine the accuracy of a Mean Shift analysis?
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Drop Unneeded Columns
        try:
            for col in drop_col:
                df_raw.drop([col], axis=1, inplace=True)
        except KeyError:
            pass

        # Dataframe To Numpy Array For Clustering
        training_data = df_raw.to_numpy()

        # Bandwidth is found automatically with
        bandwidth = estimate_bandwidth(training_data, quantile=0.2, n_samples=500)

        # Run the algorithm
        mean_shift_model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        mean_shift_model.fit(training_data)
        labels = mean_shift_model.labels_
        cluster_centers = mean_shift_model.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters = len(labels_unique)

        # Return Cluster Membership & Centroid Locations
        print(f"Mean Shift Clusters Found: {n_clusters}")
        return cluster_centers, labels
