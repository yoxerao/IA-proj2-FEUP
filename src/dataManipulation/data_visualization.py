import pandas as pd
import data_analysis as da
import seaborn as sb
from matplotlib import pyplot as plt


def visualize_data(df):
    """ M = df[df.diagnosis == 1] #Diagnosis transfers all values of M to M data
    B = df[df.diagnosis == 0] #Diagnosis transfers all values of B to B data

    plt.scatter(M.radius_mean,M.smoothness_se, label = "Malignant", alpha = 0.3)
    plt.scatter(B.radius_mean,B.smoothness_se,label = "Benign", alpha = 0.3)

    plt.xlabel("radius_mean")
    plt.ylabel("smoothness_se")

    plt.legend()
    plt.show() """

    plt.figure(figsize=(20,20))
    sb.heatmap(df.corr(),cbar=True,annot=True,cmap='Oranges')
    plt.show()

visualize_data(da.get_data())