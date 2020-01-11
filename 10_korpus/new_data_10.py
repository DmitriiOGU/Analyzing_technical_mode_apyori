# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:11:11 2019

@author: Dima
"""

import os
import pandas as pd
import form_date
os.chdir("./10")

#read
CaF2=pd.read_excel("CaF2 _ 10 корпус.xls")
MgF2=pd.read_excel("MgF2 _ 10 корпус.xls")
AE=pd.read_excel("АЭ _ 10 корпус.xls")
Dlitelnost_viplavki=pd.read_excel("Длительность выливки _ 10 корпус.xls")
Doza_glinozema=pd.read_excel("Доза глинозема _ 10 корпус.xls")
KO=pd.read_excel("КО _ 10 корпус.xls")
Kol_glinozema__cherez_APG=pd.read_excel("Кол глинозема через АПГ _ 10 корпус.xls")
Kol_doz_APG_automate=pd.read_excel("Кол. доз АПГ в автом. режиме _ 10 корпус.xls")
Kol_doz_APG_nedopitok=pd.read_excel("Кол. доз АПГ в недопитке _ 10 корпус.xls")
Kol_doz_APG_nominal=pd.read_excel("Кол. доз АПГ в номинале _ 10 корпус.xls")
Kol_doz_APG_perepitok=pd.read_excel("Кол. доз АПГ в перепитке _ 10 корпус.xls")
Kol_doz_APG_test=pd.read_excel("Кол. доз АПГ в тесте _ 10 корпус.xls")
Kol_rab_el_ov=pd.read_excel("Кол. работающих эл-ров _ 10 корпус.xls")
Kol_podernutih_anodov=pd.read_excel("Количество поддернутых анодов _ 10 корпус.xls")
Napryazhenie_ASUTP=pd.read_excel("Напряжение АСУТП _ 10 корпус.xls")
Napryazhenie_dobavka=pd.read_excel("Напряжение добавка _ 10 корпус.xls")
Napryazhenie_oshinovki=pd.read_excel("Напряжение ошиновки _ 10 корпус.xls")
Napryazhenie_privedennoe=pd.read_excel("Напряжение приведенное _ 10 корпус.xls")
Napryazhenie_celevoe=pd.read_excel("Напряжение целевое _ 10 корпус.xls")
Obratnaya_EDS=pd.read_excel("Обратная ЭДС _ 10 корпус.xls")
Otnoshenie_skorosti=pd.read_excel("Отношение скорости _ 10 корпус.xls")
RMPR=pd.read_excel("РМПР _ 10 корпус.xls")
RMPR_dlit_VIRA=pd.read_excel("РМПР длительность ВИРА _ 10 корпус.xls")
RMPR_dlit_MAINA=pd.read_excel("РМПР длительность МАЙНА _ 10 корпус.xls")
RMPR_kol_VIRA=pd.read_excel("РМПР кол ВИРА _ 10 корпус.xls")
RMPR_kol_MAINA=pd.read_excel("РМПР кол МАЙНА _10 корпус.xls")
Sred_vrem_dobavka=pd.read_excel("Средняя временная добавка _ 10 корпус.xls")
Sred_dobavka_po_shumam=pd.read_excel("Средняя добавка по шумам _ 10 корпус.xls")
Srok_slujbi=pd.read_excel("Срок службы _ 10 корпус.xls")
Temperatura_electrolita=pd.read_excel("Температура электролита _ 10 корпус.xls")
Uroven_metala=pd.read_excel("Уровень металла _ 10 корпус.xls")
Ustanovka_APG=pd.read_excel("Уставка АПГ _ 10 корпус.xls")
Ftorid_alumin_ves_dozi=pd.read_excel("Фторид алюминия вес дозы _ 10 корпус.xls")
Ftorid_alumin_kol_doz=pd.read_excel("Фторид алюминия кол доз _ 10 корпус.xls")
Shum=pd.read_excel("Шум _ 10 корпус.xls")
Elektrolit=pd.read_excel("Электролит _ 10 корпус.xls")
#diff
Sila_toka_KPP=pd.read_excel("Сила тока серии (КПП) - 10 корпус.xls")



#normalize
CaF2=form_date.date_normalize(CaF2)
MgF2=form_date.date_normalize(MgF2)
AE=form_date.date_normalize(AE)
Dlitelnost_viplavki=form_date.date_normalize(Dlitelnost_viplavki)
Doza_glinozema=form_date.date_normalize(Doza_glinozema)
KO=form_date.date_normalize(KO)
Kol_glinozema__cherez_APG=form_date.date_normalize(Kol_glinozema__cherez_APG)
Kol_doz_APG_automate=form_date.date_normalize(Kol_doz_APG_automate)
Kol_doz_APG_nedopitok=form_date.date_normalize(Kol_doz_APG_nedopitok)
Kol_doz_APG_nominal=form_date.date_normalize(Kol_doz_APG_nominal)
Kol_doz_APG_perepitok=form_date.date_normalize(Kol_doz_APG_perepitok)
Kol_doz_APG_test=form_date.date_normalize(Kol_doz_APG_test)
Kol_rab_el_ov=form_date.date_normalize(Kol_rab_el_ov)
Kol_podernutih_anodov=form_date.date_normalize(Kol_podernutih_anodov)
Napryazhenie_ASUTP=form_date.date_normalize(Napryazhenie_ASUTP)
Napryazhenie_dobavka=form_date.date_normalize(Napryazhenie_dobavka)
Napryazhenie_oshinovki=form_date.date_normalize(Napryazhenie_oshinovki)
Napryazhenie_privedennoe=form_date.date_normalize(Napryazhenie_privedennoe)
Napryazhenie_celevoe=form_date.date_normalize(Napryazhenie_celevoe)
Obratnaya_EDS=form_date.date_normalize(Obratnaya_EDS)
Otnoshenie_skorosti=form_date.date_normalize(Otnoshenie_skorosti)
RMPR=form_date.date_normalize(RMPR)
RMPR_dlit_VIRA=form_date.date_normalize(RMPR_dlit_VIRA)
RMPR_dlit_MAINA=form_date.date_normalize(RMPR_dlit_MAINA)
RMPR_kol_VIRA=form_date.date_normalize(RMPR_kol_VIRA)
RMPR_kol_MAINA=form_date.date_normalize(RMPR_kol_MAINA)
Sred_vrem_dobavka=form_date.date_normalize(Sred_vrem_dobavka)
Sred_dobavka_po_shumam=form_date.date_normalize(Sred_dobavka_po_shumam)
Srok_slujbi=form_date.date_normalize(Srok_slujbi)
Temperatura_electrolita=form_date.date_normalize(Temperatura_electrolita)
Uroven_metala=form_date.date_normalize(Uroven_metala)
Ustanovka_APG=form_date.date_normalize(Ustanovka_APG)
Ftorid_alumin_ves_dozi=form_date.date_normalize(Ftorid_alumin_ves_dozi)
Ftorid_alumin_kol_doz=form_date.date_normalize(Ftorid_alumin_kol_doz)
Shum=form_date.date_normalize(Shum)
Elektrolit=form_date.date_normalize(Elektrolit)
#diff
Sila_toka_KPP=form_date.date_normalize(Sila_toka_KPP)
#write
os.chdir("../new_10")
CaF2.to_excel('CaF2.xlsx',index=False)
MgF2.to_excel('MgF2.xlsx',index=False)
AE.to_excel('AE.xlsx',index=False)
Dlitelnost_viplavki.to_excel('Dlitelnost_viplavki.xlsx',index=False)
Doza_glinozema.to_excel('Doza_glinozema.xlsx',index=False)
KO.to_excel('KO.xlsx',index=False)
Kol_glinozema__cherez_APG.to_excel('Kol_glinozema__cherez_APG.xlsx',index=False)
Kol_doz_APG_automate.to_excel('Kol_doz_APG_automate.xlsx',index=False)
Kol_doz_APG_nedopitok.to_excel('Kol_doz_APG_nedopitok.xlsx',index=False)
Kol_doz_APG_nominal.to_excel('Kol_doz_APG_nominal.xlsx',index=False)
Kol_doz_APG_perepitok.to_excel('Kol_doz_APG_perepitok.xlsx',index=False)
Kol_doz_APG_test.to_excel('Kol_doz_APG_test.xlsx',index=False)
Kol_rab_el_ov.to_excel('Kol_rab_el_ov.xlsx',index=False)
Kol_podernutih_anodov.to_excel('Kol_podernutih_anodov.xlsx',index=False)
Napryazhenie_ASUTP.to_excel('Napryazhenie_ASUTP.xlsx',index=False)
Napryazhenie_dobavka.to_excel('Napryazhenie_dobavka.xlsx',index=False)
Napryazhenie_oshinovki.to_excel('Napryazhenie_oshinovki.xlsx',index=False)
Napryazhenie_privedennoe.to_excel('Napryazhenie_privedennoe.xlsx',index=False)
Napryazhenie_celevoe.to_excel('Napryazhenie_celevoe.xlsx',index=False)
Obratnaya_EDS.to_excel('Obratnaya_EDS.xlsx',index=False)
Otnoshenie_skorosti.to_excel('Otnoshenie_skorosti.xlsx',index=False)
RMPR.to_excel('RMPR.xlsx',index=False)
RMPR_dlit_VIRA.to_excel('RMPR_dlit_VIRA.xlsx',index=False)
RMPR_dlit_MAINA.to_excel('RMPR_dlit_MAINA.xlsx',index=False)
RMPR_kol_VIRA.to_excel('RMPR_kol_VIRA.xlsx',index=False)
RMPR_kol_MAINA.to_excel('RMPR_kol_MAINA.xlsx',index=False)
Sred_vrem_dobavka.to_excel('Sred_vrem_dobavka.xlsx',index=False)
Sred_dobavka_po_shumam.to_excel('Sred_dobavka_po_shumam.xlsx',index=False)
Srok_slujbi.to_excel('Srok_slujbi.xlsx',index=False)
Temperatura_electrolita.to_excel('Temperatura_electrolita.xlsx',index=False)
Uroven_metala.to_excel('Uroven_metala.xlsx',index=False)
Ustanovka_APG.to_excel('Ustanovka_APG.xlsx',index=False)
Ftorid_alumin_ves_dozi.to_excel('Ftorid_alumin_ves_dozi.xlsx',index=False)
Ftorid_alumin_kol_doz.to_excel('Ftorid_alumin_kol_doz.xlsx',index=False)
Shum.to_excel('Shum.xlsx',index=False)
Elektrolit.to_excel('Elektrolit.xlsx',index=False)
#diff
Sila_toka_KPP.to_excel('Sila_toka_KPP.xlsx',index=False)
