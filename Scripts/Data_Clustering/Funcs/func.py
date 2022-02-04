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
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA
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


    @staticmethod
    def corr_data(df_raw: "Pandas Dataframe", csv_path=False) -> "CSV If User Wants It":
        """
        This class method takes the provided pandas dataframe provides a correlation
        matrix for each variable
        """

        # Make a copy of the data to ensure non-destructive methods
        df_copy = df_raw.copy()

        # Correlation Matrix formation | Methods: pearson, kendall, spearman
        corr_matrix = df_copy.corr(method='pearson')

        # Check To See If User Wants To Write Correlation Data
        if csv_path is not False:
            corr_matrix.to_csv(csv_path)

        #Using heatmap to visualize the correlation matrix
        sns.heatmap(corr_matrix, annot = True, cmap = 'coolwarm')
        plt.show()


    @staticmethod
    def describe_data(df_raw: "Pandas Dataframe"):
        """
        This function returns basic data description information.
        Histograms, Scatterplots, Mean, Standard Deviation Etc...
        """

        # Make Copy Just Incase
        df_copy = df_raw.copy()

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
        return [kmean_model.cluster_centers_, kmean_model.labels_]


    @staticmethod
    def mean_shift(df_raw: "Pandas Dataframe"):
        """
        Run Mean-Shift analysis to identify clusters in data.
        How do I determine the accuracy of a Mean Shift analysis?
        """

        # Make Copy Just Incase
        df_raw = df_raw.copy()

        # Dataframe To Numpy Array For Clustering
        training_data = df_raw.to_numpy()

        # # Bandwidth is found automatically with
        # bandwidth = estimate_bandwidth(training_data, quantile=0.0001, n_jobs= -1)

        # Run the algorithm
        mean_shift_model = MeanShift(bandwidth = 10, bin_seeding = True)
        mean_shift_model.fit(training_data)
        labels = mean_shift_model.labels_
        cluster_centers = mean_shift_model.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters = len(labels_unique)

        # Return Cluster Membership & Centroid Locations
        print(f"Mean Shift Clusters Found: {n_clusters}")
        return cluster_centers, labels



class ComponentAnalysis():
    """ This class stores all functions related to component analysis """


    @staticmethod
    def principle_component_analysis(df_raw: "Pandas Dataframe"):
        """
        Perform a principle component analysis and determine gourping of variables and possible underlying factors
        """

        # Make Copy Just Incase
        df_copy = df_raw.copy()
        df_copy_cols = list(df_copy.columns)

        # Dataframe To Numpy Array For Clustering | Store Data In Dictionary | Grab Original Column Names
        pca_dict = {}
        training_data = df_copy.to_numpy()

        # Perform PCA
        pca = PCA()
        pca.fit_transform(training_data)
        pca_data = pca.transform(training_data)

        # Basic Analysis
        pca_dict["ComponentNumber"] = list(range(1, pca.n_components_ + 1))
        pca_dict["Eigenvalues"] = pca.explained_variance_
        pca_dict["Explained_Variance"] = pca.explained_variance_ratio_ * 100
        pca_dict["Cummulative_Explained_Variance"] = np.cumsum((pca.explained_variance_ratio_ * 100))

        # Eigenvalues Above 1
        eigenvalues = pca.explained_variance_
        e_df = pd.DataFrame(eigenvalues)
        eigen_values_g1 = [x for x in e_df[0].tolist() if x > 1]

        # Print Variable Importance In Each Component | Magnitude Indicates The Influence On The Component (In Abs Terms)
        pca_comp_df = pd.DataFrame(pca.components_)
        transposed_pca_comp_df = pca_comp_df.transpose()

        new_cols = [f"PC_{x}" for x in range(1, pca.n_components_ + 1)]
        transposed_pca_comp_df.columns = new_cols

        transposed_pca_comp_df["Variables"] = df_copy_cols
        transposed_pca_comp_df.set_index("Variables", inplace = True)

        main_pcs = new_cols[0 : len(eigen_values_g1)]
        transposed_pca_comp_df = transposed_pca_comp_df[main_pcs]

        # # Iterate Through Dataframe & Supress Values Between 0.300 & -0.300
        supress_val = 0.3
        for col in main_pcs:
            transposed_pca_comp_df.loc[(transposed_pca_comp_df[col] <= supress_val) & (transposed_pca_comp_df[col] >= -supress_val), col] = ""

        # Return Principle Component Information As Pandas DF
        pca_df = pd.DataFrame(pca_dict)

        # Priciple Component Data For Each Row As Pandas DF
        pc_row_data = pd.DataFrame(pca_data)
        pc_row_data.columns = new_cols

        return transposed_pca_comp_df, pca_df, pc_row_data[main_pcs]
