#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:36:54 2022

@author: likith
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import plot_confusion_matrix

data = pd.read_csv("Dataset.csv")
df = pd.DataFrame(data)

df=df.drop(['ID','Sensors','Sensor_values','Sensor_status'], axis = 1)

columnsToEncode = list(df.select_dtypes(include=['category','object']))
le = LabelEncoder()
for feature in columnsToEncode:
    try:
        df[feature] = le.fit_transform(df[feature])
    except:
        print('Error encoding '+feature)

X = df.drop(['Activity'],axis=1)
y = df.iloc[:,-1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
    
neighbors = np.arange(2, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over K values
K = -1
acc = 0.0
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train.values.ravel())
    # print(knn.predict([[1,1398701533664495097,0,12,79]]))
    # Compute training and test data accuracy
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)
    if(test_accuracy[i]>acc):
        acc=test_accuracy[i]
        K=k
print(train_accuracy)
print(test_accuracy)
    
# knn = KNeighborsClassifier(n_neighbors=K)
# knn.fit(X_train, y_train.values.ravel())
# y_pred = knn.predict(X_test)