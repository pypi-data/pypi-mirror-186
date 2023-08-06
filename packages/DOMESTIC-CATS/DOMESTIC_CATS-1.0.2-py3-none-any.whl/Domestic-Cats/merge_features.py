import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
pd.set_option('display.max_rows', 1000)

def save(filename,df_name):
    df_name.to_csv('Data_Output/'+filename+'.csv', sep=',',index=False)
    

GalacticLatitude = pd.read_table("Data_Output/GalacticLatitude.csv", delimiter =",")
firstmag = pd.read_table("Data_Output/firstmag.csv", delimiter =",")
SGSCORE = pd.read_table("Data_Output/SGSCORE.csv", delimiter =",")
Colors = pd.read_table("Data_Output/Color.csv", delimiter =",")



FMDec = pd.merge(firstmag,GalacticLatitude, left_on='ZTF Name', right_on='ZTF Name')

#Merge First Magnitude and Galactic Latitude and SG Score
FMDec_SG = FMDec.merge(SGSCORE,how='left', left_on='ZTF Name', right_on='ZTF Name')

#Merge First Magnitude and Galactic Latitude and SG Score and Colors
all_features = FMDec_SG.merge(Colors,how='left', left_on='ZTF Name', right_on='ZTF Name')


save('merge_features/all_features',all_features)


