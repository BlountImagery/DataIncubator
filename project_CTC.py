# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:47:12 2017

@author: Chris
"""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

filelocation = "C:\Users\Chris\Desktop\incubator\Project\git\CTC.csv"

names = ['CyclistsNames','TripName','Tagline','No.ofriders','Male/Female','Nationalities','Start','Finish','Duration(months)','Ongoing','Costperperson(originalcurrency)','Costperperson(GBP£)','Totaldistancekm','Totaldistancemiles','"Averagemonthlydistance(km,calculated)"','Costperkm','Costpermonth(calculated)','Typeofbike','Bicyclemake/model','Gears','Handlebars','Brakes','Wheelsize','Luggage','Whatfootwear/pedalsdidyouuse?','Europe','Africa','Australasia','NorthAmerica','SouthAmerica','Asia','PartsofAsia','Round-the-world','Website','Routemap','Kitlist','Titles','Buy(UK)','Buy(World)']
dataset = pd.read_csv(filelocation, names=names)
      
def main():   
        
    #print(dataset.shape)
    #print(dataset.head(1))
    #print(dataset.describe())
    #print(dataset.groupby('No. of riders').size())

#Figure 1       
    d1 = {'distance' : dataset.Totaldistancemiles[1:], 'type' : dataset.Typeofbike[1:]}
    df1 = pd.DataFrame(d1)
    df1[['type', 'distance']] = df1[['type', 'distance']].astype(str)
    df1['type'] = df1['type'].str.lower()
    df1.distance = pd.to_numeric(df1.distance, errors='coerce').fillna(0).astype(np.int64)
    df1['count'] = 1
    
    
    type_comp = df1.groupby('type').sum()
    type_comp['dist_per_ride'] = type_comp['distance'] / type_comp['count']
   
    #print type_comp
    graph = type_comp.plot(y=['dist_per_ride', 'count'], secondary_y=['count'], kind='bar', legend=True)
    graph.set_xlabel("Bike type")
    graph.set_ylabel("Distance traveled (miles)")
    graph.right_ax.set_ylabel("Number of rides per bike type")

#Figure 2 
    d2 = {'cost' : dataset.Costperkm[1:], 'length' : dataset.Totaldistancekm[1:]}
    df2 = pd.DataFrame(d2).dropna().astype(float)
    
    #print df2
    
    graph2 = df2.plot(x=['cost'], y=['length'], kind='scatter', legend=True)
    graph2.set_xlabel("Cost per km traveled")
    graph2.set_ylabel("Distance traveled (km)")
       
    
    #Boilplate calling main
if __name__ == '__main__':
    main()