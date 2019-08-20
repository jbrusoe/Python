#Python demo of Support Vector Machine
#Written by: Jeff Brusoe
#Last Updated: January 23, 2019

#Data taken from https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28original%29

import numpy as np
from sklearn import preprocessing, neighbors, svm
from sklearn.model_selection import train_test_split
import pandas as pd

TestSize = 0.2 #1-TestSize = % of data used for training
InputFile = "C:/Users/jbrus/Google Drive/Documents/ProgrammingMeritBadge/CodeSamples/Python/SupportVectorMachineDemo/Data/Cancer2.csv"

#Read and process data from file
CancerData = pd.read_csv(InputFile)

#A question mark indicates missing data in file
CancerData.replace('?',-99999, inplace=True)

#Drop unique ID field so it's not used in predictions
CancerData.drop(['id'], 1, inplace=True)
#End of file processing

#Array of data
X = np.array(CancerData.drop(['class'], 1))

#Array of results (Benign/Malignant)
y = np.array(CancerData['class'])

#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
print("Splitting data into training and test data")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = TestSize) 

#Generate Model
Model = svm.SVC()
Model.fit(X_train, y_train)
Accuracy = Model.score(X_test, y_test)
print("Training Data Accuracy: ", "{:.2%}".format(Accuracy))

#Make predition with new data
NewData = np.array([[4,3,2,1,1,2,3,2,1]])
print("\nNew Data: ", NewData)

prediction = Model.predict(NewData)

if prediction == 2:
    print("Prediction: Benign")
else:
    print("Prediction: Malignant")