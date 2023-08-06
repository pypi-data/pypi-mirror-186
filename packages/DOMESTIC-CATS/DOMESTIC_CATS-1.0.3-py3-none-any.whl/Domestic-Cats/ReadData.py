import pandas as pd
from alerce.core import Alerce
alerce = Alerce()
from ned_extinction_calc import request_extinctions

# Let's user choose if they just want to enter the details for one single object, or classify a list of transients through a CSV File.

obj_or_file = input("Single Object or CSV File? (Enter 'object' or 'file')?: ")

#For a single Object which the User will enter the details of in the terminal.
#Creates a CSV file with just the one single object so you can keep track of what was done. :)
if obj_or_file == 'object':
    newtrans = []
    yse_name = input("YSE Name: ")
    yse_ra = input("RA: ")
    yse_dec = input("Dec: ")
    na = ''
    YSE_object_dict = {'ZTF Name': str(yse_name),'classification':na ,'transient_RA': [yse_ra], 'transient_Dec': [yse_dec]}
    YSE_object_df = pd.DataFrame(data = YSE_object_dict)
    print (YSE_object_df)
    YSE_object_df.to_csv('Data_Input/object_'+yse_name+'.csv',index=False)
    newtrans = pd.read_csv('Data_Input/object_'+yse_name+'.csv')


#For a list of objects in a file for which the user will enter the filename (inclduing extension).
if obj_or_file == 'file':
    file_name = input("Enter Name of YSE Query File: ")
    newtrans = pd.read_csv('Data_Input/'+file_name) #from query
    


#find and save OIDs
dataframe=[]
for i in range(0,len(newtrans)):
    dataframe.append(alerce.query_objects(
      ra=newtrans['transient_RA'][i],
      dec=newtrans['transient_Dec'][i],
      radius=1.5,
      format="pandas"))


    new_oids,ra,dec=[],[],[]
    for i in range(0,len(dataframe)):
        if len(dataframe[i]) != 0:
            new_oids.append(dataframe[i]['oid'][0])
            ra.append(newtrans['transient_RA'][i])
            dec.append(newtrans['transient_Dec'][i])
    newOIDs_dict = {'ZTF Name': new_oids, 'ra': ra,'dec':dec}
    OIDs_df = pd.DataFrame(data=newOIDs_dict)

#GET AV Values with NED Extinction Calculator


def getAV(ra,dec):
    filts = ['Landolt V']
    AV=[]
    for i in range(0,len(ra)):
        AV.append(request_extinctions(ra[i], dec[i], filters=filts)[0])
    return AV

OIDs_df['AV'] = getAV(OIDs_df['ra'],OIDs_df['dec'])
OIDs_df.sort_values('ZTF Name').to_csv('Data_Input/'+'OIDs.csv', sep=',',index=False)

OIDs_df.to_csv('Data_Input/OIDs.csv',index=False)

OIDs_df = OIDs_df

OIDs = (OIDs_df['ZTF Name'])

print (OIDs_df)
