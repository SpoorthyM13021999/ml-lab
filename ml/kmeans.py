# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:15:02 2019

@author: Administrator
"""

from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target)
model =KMeans(n_clusters=3)
model.fit(X_train,y_train)
metrics.accuracy_score(y_test,model.predict(X_test))

#-------Expectation and Maximization----------
from sklearn.mixture import GaussianMixture
model2 = GaussianMixture(n_components=3)
model2.fit(X_train,y_train)
score=model2.score(X_test,y_test)
print("Score is:",score)
accuracy=metrics.accuracy_score(y_test,model.predict(X_test))
print("Accuracy:",accuracy)