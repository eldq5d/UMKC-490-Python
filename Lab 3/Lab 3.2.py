import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

income = []
spending_score = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            income.append(int(row[0]))
            spending_score.append(int(row[1]))
    return

get_data("Customers (1).csv")

incomenp = np.array(income)
ssnp = np.array(spending_score)

X = np.column_stack((incomenp, ssnp))

kmeans = KMeans(n_clusters=5, init='k-means++')
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[:,0], X[:,1], c=y_kmeans)
plt.title("K Means for Customers")
plt.show()
