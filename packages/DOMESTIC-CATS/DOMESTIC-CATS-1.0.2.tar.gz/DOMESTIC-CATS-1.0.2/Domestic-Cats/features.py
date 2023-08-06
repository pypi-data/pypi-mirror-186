import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from alerce.core import Alerce
alerce = Alerce()


""" SG SCORE """

def sgscore(event_name):
    event, name = [],[]
    for i in range(0,len(event_name)):
        name.append(event_name[i])
    sgscore_arr,sgscore_val,names = [],[],[]
    for i in range(0,len(name)):
        try:
            if alerce.query_feature(name[i], 'sgscore1', format='json') != []:
                sgscore_arr.append(alerce.query_feature(name[i], 'sgscore1', format='json'))
                names.append(name[i])
        except:
            sgscore_arr = None
    for i in range(0,len(sgscore_arr)):
        sgscore_val.append((sgscore_arr)[i][0]['value'])
    d = {'ZTF Name': names,'SGSCORE': sgscore_val}
    event_scores = pd.DataFrame(data=d)
    event_scores = event_scores[event_scores.SGSCORE != 0.500000]
    return event_scores.drop_duplicates()
    

""" GALACTIC LATITUDE """
    
from astropy.coordinates import SkyCoord
import astropy.units as u
from ReadData import OIDs_df
def gal_lat(event_df):
    ra_icrs = event_df['ra']
    dec_icrs = event_df['dec']
    b=[]
    for i in range(0,len(ra_icrs)):
        coord_icrs = SkyCoord(ra=ra_icrs[i]*u.degree, dec=dec_icrs[i]*u.degree, frame='icrs')
        coord_galactic = coord_icrs.transform_to('galactic').to_string()
        split_string= coord_galactic.split()
        #galactic latitude
        b.append(float(split_string[1]))
        
    d = {'ZTF Name': OIDs_df['ZTF Name'],'Galactic Latitude': b}
    gal_lat = pd.DataFrame(data=d)
    return gal_lat


""" FIRST MAGNITUDE """

def first_mag(event_name):
    first_mag_arr =[]
    for i in range(0,len(event_name)):
        try:
            first_mag = alerce.query_magstats(event_name[i],format="pandas")['magfirst'][0]
            first_mag_arr.append(first_mag)
        except:
            pass
    firstmag_df = pd.DataFrame(data=first_mag_arr)
    d = {'ZTF Name': event_name, 'First Mag': firstmag_df[0]}
    df = pd.DataFrame(data=d)

    return df.drop_duplicates()






""" FIRST COLOR """

#First "clean" data by removing anything with too few detections in either band:

def clean(event_names,AV_path):
    names_list = event_names.values.tolist() #to keep the names of the event.
    AV = pd.read_csv(AV_path)['AV'].values.tolist() #to keep AV of the event
    
    det = []
    for i in range(0,len(event_names)):
        try:
            det.append(alerce.query_detections(event_names[i],format="pandas")[['fid','mjd','diffmaglim']].head(5))
        except:
            pass
            
    arrg,arrr=[],[]
    for i in range(0,len(det)):
        arrg.append(np.bincount(det[i]['fid'])[1]) #counts numbers of "1" in each detection dataframe "det"
    for i in range(0,len(det)):
        arrr.append(len(det[i]) - arrg[i])
        
    remove =[]
    for i in range(0,len(det)):
        if arrr[i] < .2 or arrg[i] < .2:
            remove.append(i) #tells what dataframes need to be removed from det
    for ele in sorted(remove, reverse = True):
        #removes events with too few detections in either band. If a band has less than 2 data points, interpolation can't be done.
        del det[ele]
        del names_list[ele]
        del AV[ele]
        
    remove2 = []  #will remove anything where first g and r point are too far away in time
    for i in range(0,len(det)):
        green = det[i].loc[det[i]['fid'] == 1]
        red =  det[i].loc[det[i]['fid'] == 2] #separates r from g band
        
        red1=red['mjd'].iloc[0]
        green1=green['mjd'].iloc[0] #gets first value in r and g bands in days

        if green1-red1 > 1 or red1-green1 > 1: #which dataframes have r and g vlues more than .5 days apart
            remove2.append(i)

    for ele in sorted(remove2, reverse = True):
        del det[ele]
        del names_list[ele]
        del AV[ele]

    
    return det,names_list,AV


# Next, correct the colors for galactic extinction:
from dust_extinction.parameter_averages import F99
import astropy.units as u
import math as m

model=F99
Rvalue=3.1 #for the milkyway
extF99Rv3p1=model(Rv=Rvalue)
def extinction(band,mag,AV):
    if band == 'g':
        lambdaSDSS = 4702.5
    if band == 'r':
        lambdaSDSS = 6175.58
    wavcenter=lambdaSDSS*0.0001*u.micron #in micron
    AV_SDSS=extF99Rv3p1(wavcenter)*AV  #extF99Rv3p1(wavcenter) is Alambda/A_V
    extcorrmag= mag-AV_SDSS #we apply here the extinction correction

    return extcorrmag
    

#Finally, clean the data, correct for ext., and find the color with the g-r bands.
def loop_color(event_names,AV_path):
    det,clean_names,AV = clean(event_names,AV_path)
    therange = range(0,len(det))
    #therange = range(0,5)
    
    green_dfs,red_dfs = [],[]
    for i in therange:
        green_dfs.append(det[i].loc[det[i]['fid'] == 1])
        red_dfs.append(det[i].loc[det[i]['fid'] == 2])
    
    g_uncorrectedmag,r_uncorrectedmag = [],[]
    for i in therange:
        g_uncorrectedmag.append(green_dfs[i]['diffmaglim'].iloc[0])
        r_uncorrectedmag.append(red_dfs[i]['diffmaglim'].iloc[0])
    
    
    #preform extinction correction function
    green_extcorr,red_extcorr = [],[]
    
    for i in therange:
        try:
            green_extcorr.append(extinction('g',g_uncorrectedmag[i],float(AV[i])))
            red_extcorr.append(extinction('r',r_uncorrectedmag[i],float(AV[i])))
        except:
            pass
        

    names_list,first_colors = [],[]
    for i in range(0,len(green_extcorr)):
        first_colors.append(green_extcorr[i]-red_extcorr[i])
        names_list.append(clean_names[i])
        

    d = {'ZTF Name': names_list,'Color': first_colors}
    colors = pd.DataFrame(data=d)
    
    
    return colors.drop_duplicates()
