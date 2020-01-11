# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:44:24 2019

@author: Dima
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
import numpy as np
#matplotlib.style.use('ggplot')
data=pd.read_excel('9_korpus.xlsx')
#((data['CaF2']-data['CaF2'].mean())/data['CaF2'].std()).plot.kde()
#data['KO'].plot.kde(bw_method=0.3)
'''
data['CaF2'].plot.kde()#seem to normal
data['MgF2'].plot.kde()#seem to normal and x-square, more to gauss
data['AE'].plot.kde()#categories
data['Dlitelnost_viplavki'].plot.kde() #may be normal may be not
data['Doza_glinozema'].plot.kde() #seem to gaussian mixture 
data['KO'].plot.kde()#seem to gaussian
data['Kol_doz_APG_automate'].plot.kde() #unknown
data['Kol_doz_APG_nedopitok'].plot.kde() #seem to gauss
data['Kol_doz_APG_nominal'].plot.kde()#seem to gaussian and xi square, more to gauss
data['Kol_doz_APG_perepitok'].plot.kde()  #seem to gauss and xi square, more to gauss
data['Kol_doz_APG_test'].plot.kde()  #chi square 
data['Kol_rab_el_ov'].plot.kde()#need to category  because of text data
data['Kol_podernutih_anodov'].plot.kde()#ready to category  
data['Napryazhenie_ASUTP'].plot.kde()#seem to be gauss or chi square   
data['Napryazhenie_dobavka'].plot.kde()    # seem to chi square
data['Napryazhenie_oshinovki'].plot.kde()#strange but may be gauss 
data['Napryazhenie_privedennoe'].plot.kde()     # seem to chi square
data['Napryazhenie_celevoe'].plot.kde()#chi squa     
data['Obratnaya_EDS'].plot.kde()#gausiian   
data['Otnoshenie_skorosti'].plot.kde() #gaussian may be chi
data['RMPR'].plot.kde() #80 % gauss may be chi
data['RMPR_dlit_VIRA'].plot.kde() #seem to chi 
data['RMPR_dlit_MAINA'].plot.kde()# seem to chi 
data['RMPR_kol_VIRA'].plot.kde() #unknown but seem to chi
data['RMPR_kol_MAINA'].plot.kde()  #unknown but seem to chi 
data['Sred_vrem_dobavka'].plot.kde()   #chi square
data['Sred_dobavka_po_shumam'].plot.kde() #chi square
data['Srok_slujbi'].plot.kde() # seem to gauss but maybe unknown
data['Temperatura_electrolita'].plot.kde() #may be gauss
data['Uroven_metala'].plot.kde() #may be gauss
data['Ustanovka_APG'].plot.kde()#seem to gaussian mixture,but may be unknown 
data['Ftorid_alumin_ves_dozi'].plot.kde() #unknown
data['Ftorid_alumin_kol_doz'].plot.kde() #chi but may be unknown
data['Shum'].plot.kde() # may be chi may be gauss
data['Elektrolit'].plot.kde()# may be gauss may be not
'''
'''
for i in data.columns[7:8]:
    print(i)
    jimbo_data=(data[i]-data[i].mean())/data[i].std()
    jimbo_data=jimbo_data[np.invert(pd.isnull(jimbo_data))]
    print(len(jimbo_data))
    jimbo_data.plot.kde(ind=80513)
    print(jimbo_data)
    #a = np.random.normal(0, 1, size=80513)
    k2, p = stats.normaltest(jimbo_data,nan_policy='omit')
    print(p)
    alpha = 1e-3
    if p < alpha:  # null hypothesis: x comes from a normal distribution
        print("The null hypothesis can be rejected")
    else:    
        print("The null hypothesis cannot be rejected")
'''
#data['Kol_rab_el_ov'].replace({'раб':0,'откл':1,'обж':2},inplace=True)
data.quantile([.25,.5,.75,1])

