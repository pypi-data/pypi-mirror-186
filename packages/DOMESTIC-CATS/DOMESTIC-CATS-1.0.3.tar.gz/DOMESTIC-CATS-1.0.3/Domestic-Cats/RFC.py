import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
pd.set_option('display.max_rows', 1000)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


#Read in Table of Merged Features
known_transients = pd.read_csv("Data_Input/Known_Transient_Types.csv", delimiter =",")
firstmag_mean,GL_mean,SGSCORE_mean,color_mean = np.mean(known_transients)

#Random Forest Classifier
feature_names = ['First Mag','Galactic Latitude','SGSCORE','Color']
X=known_transients[feature_names]
y=known_transients['Type']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

clf=RandomForestClassifier(n_estimators=50)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
feature_imp = pd.Series(clf.feature_importances_,index=feature_names).sort_values(ascending=False)
print (feature_imp)

#print ("Accuracy for training set data only:",metrics.accuracy_score(y_test, y_pred))


# On new unknown data

#Fill NA Values with Mean values from training data
new_transients = pd.read_csv("Data_Output/merge_features/all_features.csv", delimiter =",")
new_transients['First Mag'].fillna((firstmag_mean),inplace = True)
new_transients['Galactic Latitude'].fillna((GL_mean),inplace = True)
new_transients['SGSCORE'].fillna((SGSCORE_mean),inplace = True)
new_transients['Color'].fillna((color_mean),inplace = True)

new_transients.to_csv('Data_Output/merge_features/all_features_fillNA.csv', sep=',',index=False)

#make new prediction 
prediction = []
for i in range(0,len(new_transients)):
    prediction.append(clf.predict([[new_transients['First Mag'][i],new_transients['Galactic Latitude'][i],new_transients['SGSCORE'][i],new_transients['Color'][i]]])[0])


d = {'ZTF Name': new_transients['ZTF Name'], 'RFC Prediction': prediction}
predictions = pd.DataFrame(data=d)


print (predictions)

predictions.to_csv('Data_Output/predictions.csv', sep=',',index=False)
