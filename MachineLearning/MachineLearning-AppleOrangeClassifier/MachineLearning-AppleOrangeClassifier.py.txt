#Python - Machine Learning - Apple/Orange Classifier
#Based on https://www.youtube.com/watch?v=cKxRvEZd3Mw

import numpy as np
from sklearn import tree

print("Machine Learning Demo - Apple/Orange classifier")
print("Based on - https://www.youtube.com/watch?v=cKxRvEZd3Mw\n")

print("Training Data")
#0 = Bumpy, 1=Smooth
features = [[140,1],[130,1],[150,0],[170,0]]
print (np.matrix(features),"\n")

print("Training Labels")
labels = ["apple","apple","orange","orange"]
print(np.matrix(labels),"\n")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print("Classsifier Input:")
print("Weight(grams): 155")
print("Surface: 1","\n")

print("Classifier Output:")
print(clf.predict([[155,1]]),"\n")

print("Classsifier Input:")
print("Weight(grams): 155")
print("Surface: 0","\n")

print("Classifier Output:")
print(clf.predict([[155,0]]),"\n")

print("Classsifier Input:")
print("Weight(grams): 135")
print("Surface: 0","\n")

print("Classifier Output:")
print(clf.predict([[135,0]]),"\n")