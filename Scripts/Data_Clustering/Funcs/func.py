# Name:                                            Renacin Matadeen
# Date:                                               10/31/2021
# Title           Interval House Data Analytics Project: Canadian Census Data K-Means Clustering Attempt
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# ----------------------------------------------------------------------------------------------------------------------


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
    num_k = range(2, 15)
    for k in num_k:
        kmean_model = KMeans(n_clusters=k, max_iter=150, random_state=0)
        kmean_model.fit(training_data)
        wscc.append(kmean_model.inertia_)

    # Plot The Elbow Chart
    plt.plot(num_k, wscc, "bx-")
    plt.xlabel("Number Of Clusters (K)")
    plt.ylabel("Overall Distortion (WCSSE)")
    plt.title("Elbow Chart: Finding Optimal K-Value")
    plt.show()


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
        kmean_model = KMeans(n_clusters=k, max_iter=150, random_state=0)
        kmean_model.fit(training_data)
        score = silhouette_score(training_data, kmean_model.labels_)
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



def k_means(df_raw: "Pandas Dataframe", k : "Number Of Clusters", drop_col: list):
    """
    Run K number of K-Means analyses to identify optimal K value. Plot distortions
    via a simple line chart for user.
    """

    # Drop Unneeded Columns
    for col in drop_col:
        df_raw.drop([col], axis=1, inplace=True)

    # Dataframe To Numpy Array For Clustering
    training_data = df_raw.to_numpy()

    # Perform K-Means Analysis
    kmean_model = KMeans(n_clusters=k, max_iter=150)
    kmean_model.fit(training_data)

    # Return Cluster Membership & Centroid Locations
    return [kmean_model.cluster_centers_, kmean_model.labels_]



def mean_shift(df_raw: "Pandas Dataframe", drop_col: list):
    """
    Run Mean-Shift analysis to identify clusters in data.
    How do I determine the accuracy of a Mean Shift analysis?
    """

    # Drop Unneeded Columns
    for col in drop_col:
        df_raw.drop([col], axis=1, inplace=True)

    # Return Cluster Membership & Centroid Locations
    return 1
