#Python MachineLearning - Using Scikit-Learn
#Written by: Jeff Brusoe
#Last Updated: February 12, 2019
#Based on the following videos: 
#1. https://www.youtube.com/watch?v=RXFnwCRb-is
#2. https://www.youtube.com/watch?v=MFpgsy_7_YM

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectPercentile
from sklearn.linear_model import LogisticRegression

cancer = load_breast_cancer()

rng = np.random.RandomState(42)

noise = rng.normal(size=(len(cancer.data),50))

X_w_noise = np.hstack([cancer.data,noise])

X_train, X_test, y_train, y_test = train_test_split(X_w_noise,cancer.target,random_state=0,test_size=0.5)

select = SelectPercentile(percentile=50)
select.fit(X_train,y_train)

X_train_selected = select.transform(X_train)

print("X_train.shape: {}".format(X_train.shape))
print("X_train_selected.shape: {}".format(X_train_selected.shape))

mask = select.get_support()
print(mask)
plt.matshow(mask.reshape(1,-1),cmap="gray_r")
plt.show()
