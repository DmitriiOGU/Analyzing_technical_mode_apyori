# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:21:40 2019

@author: Dima
"""

import os
import pandas as pd
import form_date
import numpy as np

def complicate(df):
    list1=[]
    for i in range(len(df)):
        for j in df.columns[1:]:
            list1.append(df.loc[i,j])
    return pd.Series(list1)
#change dir
os.chdir("./new_9")
#open data
CaF2=pd.read_excel('CaF2.xlsx',index=False)
MgF2=pd.read_excel('MgF2.xlsx',index=False)
AE=pd.read_excel('AE.xlsx',index=False)
Dlitelnost_viplavki=pd.read_excel('Dlitelnost_viplavki.xlsx',index=False)
Doza_glinozema=pd.read_excel('Doza_glinozema.xlsx',index=False)
KO=pd.read_excel('KO.xlsx',index=False)
#Kol_glinozema__cherez_APG=pd.read_excel('Kol_glinozema__cherez_APG.xlsx',index=False)
Kol_doz_APG_automate=pd.read_excel('Kol_doz_APG_automate.xlsx',index=False)
Kol_doz_APG_nedopitok=pd.read_excel('Kol_doz_APG_nedopitok.xlsx',index=False)
Kol_doz_APG_nominal=pd.read_excel('Kol_doz_APG_nominal.xlsx',index=False)
Kol_doz_APG_perepitok=pd.read_excel('Kol_doz_APG_perepitok.xlsx',index=False)
Kol_doz_APG_test=pd.read_excel('Kol_doz_APG_test.xlsx',index=False)
Kol_rab_el_ov=pd.read_excel('Kol_rab_el_ov.xlsx',index=False)
Kol_podernutih_anodov=pd.read_excel('Kol_podernutih_anodov.xlsx',index=False)
Napryazhenie_ASUTP=pd.read_excel('Napryazhenie_ASUTP.xlsx',index=False)
Napryazhenie_dobavka=pd.read_excel('Napryazhenie_dobavka.xlsx',index=False)
Napryazhenie_oshinovki=pd.read_excel('Napryazhenie_oshinovki.xlsx',index=False)
Napryazhenie_privedennoe=pd.read_excel('Napryazhenie_privedennoe.xlsx',index=False)
Napryazhenie_celevoe=pd.read_excel('Napryazhenie_celevoe.xlsx',index=False)
Obratnaya_EDS=pd.read_excel('Obratnaya_EDS.xlsx',index=False)
Otnoshenie_skorosti=pd.read_excel('Otnoshenie_skorosti.xlsx',index=False)
RMPR=pd.read_excel('RMPR.xlsx',index=False)
RMPR_dlit_VIRA=pd.read_excel('RMPR_dlit_VIRA.xlsx',index=False)
RMPR_dlit_MAINA=pd.read_excel('RMPR_dlit_MAINA.xlsx',index=False)
RMPR_kol_VIRA=pd.read_excel('RMPR_kol_VIRA.xlsx',index=False)
RMPR_kol_MAINA=pd.read_excel('RMPR_kol_MAINA.xlsx',index=False)
Sred_vrem_dobavka=pd.read_excel('Sred_vrem_dobavka.xlsx',index=False)
Sred_dobavka_po_shumam=pd.read_excel('Sred_dobavka_po_shumam.xlsx',index=False)
Srok_slujbi=pd.read_excel('Srok_slujbi.xlsx',index=False)
Temperatura_electrolita=pd.read_excel('Temperatura_electrolita.xlsx',index=False)
Uroven_metala=pd.read_excel('Uroven_metala.xlsx',index=False)
Ustanovka_APG=pd.read_excel('Ustanovka_APG.xlsx',index=False)
Ftorid_alumin_ves_dozi=pd.read_excel('Ftorid_alumin_ves_dozi.xlsx',index=False)
Ftorid_alumin_kol_doz=pd.read_excel('Ftorid_alumin_kol_doz.xlsx',index=False)
Shum=pd.read_excel('Shum.xlsx',index=False)
Elektrolit=pd.read_excel('Elektrolit.xlsx',index=False)

#complicate
date=form_date.date_creation()
spisok=[]
spisok1=[]
columns=CaF2.columns
columns=columns[1:]
for i in date:
    for j in range(len(columns)):
        spisok.append(i)
        spisok1.append(columns[j])
spisok1=pd.Series(spisok1)
spisok=pd.Series(spisok)
df=pd.DataFrame({'Data':spisok,'Vanna': spisok1})
#
df['CaF2']=complicate(CaF2)    
df['MgF2']=complicate(MgF2)    
df['AE']=complicate(AE)    
df['Dlitelnost_viplavki']=complicate(Dlitelnost_viplavki)    
df['Doza_glinozema']=complicate(Doza_glinozema)    
df['KO']=complicate(KO)    
df['Kol_doz_APG_automate']=complicate(Kol_doz_APG_automate)    
df['Kol_doz_APG_nedopitok']=complicate(Kol_doz_APG_nedopitok)    
df['Kol_doz_APG_nominal']=complicate(Kol_doz_APG_nominal)    
df['Kol_doz_APG_perepitok']=complicate(Kol_doz_APG_perepitok)    
df['Kol_doz_APG_test']=complicate(Kol_doz_APG_test)    
df['Kol_rab_el_ov']=complicate(Kol_rab_el_ov)    
df['Kol_podernutih_anodov']=complicate(Kol_podernutih_anodov)    
df['Napryazhenie_ASUTP']=complicate(Napryazhenie_ASUTP)    
df['Napryazhenie_dobavka']=complicate(Napryazhenie_dobavka)    
df['Napryazhenie_oshinovki']=complicate(Napryazhenie_oshinovki)    
df['Napryazhenie_privedennoe']=complicate(Napryazhenie_privedennoe)    
df['Napryazhenie_celevoe']=complicate(Napryazhenie_celevoe)    
df['Obratnaya_EDS']=complicate(Obratnaya_EDS)  
df['Otnoshenie_skorosti']=complicate(Otnoshenie_skorosti)  
df['RMPR']=complicate(RMPR)  
df['RMPR_dlit_VIRA']=complicate(RMPR_dlit_VIRA)  
df['RMPR_dlit_MAINA']=complicate(RMPR_dlit_MAINA)  
df['RMPR_kol_VIRA']=complicate(RMPR_kol_VIRA)    
df['RMPR_kol_MAINA']=complicate(RMPR_kol_MAINA)    
df['Sred_vrem_dobavka']=complicate(Sred_vrem_dobavka)    
df['Sred_dobavka_po_shumam']=complicate(Sred_dobavka_po_shumam)    
df['Srok_slujbi']=complicate(Srok_slujbi)    
df['Temperatura_electrolita']=complicate(Temperatura_electrolita)    
df['Uroven_metala']=complicate(Uroven_metala)    
df['Ustanovka_APG']=complicate(Ustanovka_APG)  
df['Ftorid_alumin_ves_dozi']=complicate(Ftorid_alumin_ves_dozi)  
df['Ftorid_alumin_kol_doz']=complicate(Ftorid_alumin_kol_doz)  
df['Shum']=complicate(Shum)  
df['Elektrolit']=complicate(Elektrolit)  
   
#output
os.chdir("../")
df.to_excel('9_korpus.xlsx',index=False)