# -*- coding: utf-8 -*-
"""Knn Algorthim.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17FagFvSguRrd-ajHjeXdF0M1Ru5kj6wQ
"""

#import libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

iris=load_iris() #load iris dataset

# Convert dataframe for better visualization
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# print first 5 rows of the dataset
print(df.head())

#separate features (x) and the target(y)
x = iris.data
y = iris.target

#Split the data into training and testing stes
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

# predict on the test data
y_pred = knn.predict(x_test)

# evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# print the classification report
print(classification_report(y_test, y_pred))