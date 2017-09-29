#!/usr/bin/env python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score as accuracy


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# Cutting data to speed up stuff:
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

t0 = time()
# Classifier init and learn
classy=SVC(C=10000.0,kernel="rbf",gamma='auto')
classy.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1=time()
# Predict
pred=classy.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

# Test accuracy, entries, no of Chris entries, etc
print "accuracy is ", accuracy(pred,labels_test)
print pred[10], pred[26], pred[50]
print pred.tolist().count(1)

#########################################################


