# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:37:03 2019

@author: Kritartha Patowary
"""

from sklearn.datasets import load_boston
data = load_boston()

#print a histogram of the quantity to predict: price
import matplotlob.pyplot as plt
plt.figure(figsize=(4,3))
plt.hist(data.target)
plt.xlabel('price ($1000s)')
plt.ylabel('count')
plt.tight_layout()
plt.show()

for index, feature_name in enumerate(data.feature_names):
    plt.figure(figsize=(4,3))
    plt.scatter(data.data[:,index], data.target)
    plt.ylabel('Price', size=15)
    plt.xlabel(feature_name, size=15)
    plt.tight_layout()
 #plt.show()
from sklearn.linear_model import LinearRegression
from  sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target
clf = LinearRegression()
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
expected = y_test

plt.figure(figsize=(4,3))
plt.scatter(expected, predicted)
plt.plot([0, 50], [0, 50], '--k)
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')
plt.tight_layout()
plt.show()
