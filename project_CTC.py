# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:47:12 2017

@author: Chris
"""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

        
#load libraries
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

   #Load data
#filelocation = "C:\Users\mbcx9cb4\Downloads\Coefficients-multiples.csv"
#names = ['co0', 'co1', 'co2', 'co3', 'species']
#names = ['co0', 'co1', 'co2', 'co3', 'co4', 'co5','co6','co7', 'co8', 'co9', 'co10', 'species']

filelocation = "C:\Users\Chris\Desktop\Data incubator python\Project\CTC.csv"



names = ['CyclistsNames','TripName','Tagline','No.ofriders','Male/Female','Nationalities','Start','Finish','Duration(months)','Ongoing','Costperperson(originalcurrency)','Costperperson(GBP£)','Totaldistance(km)','Totaldistancemiles','"Averagemonthlydistance(km,calculated)"','Costperkm(calculated)','Costpermonth(calculated)','Typeofbike','Bicyclemake/model','Gears','Handlebars','Brakes','Wheelsize','Luggage','Whatfootwear/pedalsdidyouuse?','Europe','Africa','Australasia','NorthAmerica','SouthAmerica','Asia','PartsofAsia','Round-the-world','Website','Routemap','Kitlist','Titles','Buy(UK)','Buy(World)']
dataset = pd.read_csv(filelocation, names=names)
  
    
def main():   
        
    #print(dataset.shape)
    #print(dataset.head(1))
    #print(dataset.describe())
    #print(dataset.groupby('No. of riders').size())
        
    d1 = {'distance' : dataset.Totaldistancemiles[1:], 'type' : dataset.Typeofbike[1:]}
    df1 = pd.DataFrame(d1)
    df1[['type', 'distance']] = df1[['type', 'distance']].astype(str)
    df1['type'] = df1['type'].str.lower()
    df1.distance = pd.to_numeric(df1.distance, errors='coerce').fillna(0).astype(np.int64)
    df1['count'] = 1
    
    
    type_comp = df1.groupby('type').sum()
    type_comp['dist_per_ride'] = type_comp['distance'] / type_comp['count']
   
    #print type_comp
    type_comp.plot(y=['dist_per_ride', 'count'], secondary_y=['count'], kind='bar', legend=True)
    
 
    
    #Boilplate calling main
if __name__ == '__main__':
    main()