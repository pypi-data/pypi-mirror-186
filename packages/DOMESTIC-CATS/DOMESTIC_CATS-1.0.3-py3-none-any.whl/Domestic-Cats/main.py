import pandas as pd
from os import listdir
from os.path import isfile, join
import warnings
warnings.filterwarnings("ignore")


#Read in data files
from ReadData import OIDs, OIDs_df
#FEATURE FUNCTION
from features import gal_lat, sgscore, first_mag, loop_color


#FUNCTION TO RUN FEATURE FUNCTIONS
def get_features(event_df,type_str,file_str): #input: ZTF names df, file name
    #Get the features
    features = [first_mag(event_df['ZTF Name']),gal_lat(event_df),sgscore(event_df['ZTF Name']),loop_color(event_df['ZTF Name'],file_str)]
    #Name the feautre files
    features_string = ['FirstMag','GalacticLatitude','SGScore','Color']
    return features, features_string
    
#FUNCTION TO SAVE DATA
def save(filename,df_name):
    df_name.to_csv('Data_Output/'+filename+'.csv', sep=',',index=False)
    
#RUN FEATURE FUNCTIONS
features, features_string = get_features(OIDs_df,'UKNOWN','Data_Input/OIDs.csv')

for i in range(0,len(features)):
    save(features_string[i],features[i])

#FUNCTION TO MERGE FEATURES
from merge_features import all_features
print (all_features)


#FUNCTION TO RUN RFC
import RFC

print("\a")
