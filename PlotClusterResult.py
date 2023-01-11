import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import argparse
import matplotlib.colors as mcolors


def Plot(df):
    # plotting clusters
    plt.figure(num=None, figsize=(16*3, 9*3), dpi=500)

    x = dict()
    y = dict()
    c = dict()

    colors = list(mcolors.cnames.keys())
    k = len(df.Cluster.value_counts())
    for i in range(k):
        x[i] = df[df.Cluster == i]['lon']
        y[i] = df[df.Cluster == i]['lat']
        c[i] = pl.scatter(x[i], y[i], c=colors[i], marker='o', alpha=0.4)
        print('Cluster', i, ',Size:', '%5d'%len(x[i]), ', Color: ',colors[i])


    pl.xlabel('Longitude')
    pl.ylabel('Latitude')
    pl.title('Result of Clustering')
    pl.savefig("ResultOfClusterImg.png")
    pl.show()

if __name__ == '__main__':
    df = pd.read_csv('ResultOfCluster.csv')
    Plot(df)

    