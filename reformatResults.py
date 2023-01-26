# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:33:20 2023

@author: Katie Salvati
"""

import pandas as pd


#%%
path = 'Y:/Salvati/strada/KAS_CRISPR/All_HRM_results/2023_01_23/'
NormFile = pd.read_csv(path + 'HRM genotyping_meltregionnormalizeddata.csv')
TempFile = pd.read_csv(path + 'HRM genotyping_meltregiontemperaturedata.csv')

## Sort RFU values Primer Temps
guide6_PP1 = NormFile[NormFile['Target']=='guide6 #1']
guide6_PP2 = NormFile[NormFile['Target']=='guide 6 #2']
guide4_PP1 = NormFile[NormFile['Target']=='guide 4 #1']
guide4_PP2 = NormFile[NormFile['Target']=='guide 4 #2']
guide8_PP1 = NormFile[NormFile['Target']=='guide 8 #1']
#guide8_PP2 = NormFile[NormFile['Target']=='guide 8 #2']

## Sort Primer Temps
guide6_PP1_T = TempFile[TempFile['Target']=='guide6 #1']
guide6_PP2_T = TempFile[TempFile['Target']=='guide 6 #2']
guide4_PP1_T = TempFile[TempFile['Target']=='guide 4 #1']
guide4_PP2_T = TempFile[TempFile['Target']=='guide 4 #2']
guide8_PP1_T = TempFile[TempFile['Target']=='guide 8 #1']
#guide8_PP2_T = TempFile[TempFile['Target']=='guide 8 #2']

## Eliminate No Template Control
avoid_wells = ['A11', 'A12', 'B11', 'B12', 'C2', 'C12', 'D11', 'D12', 'E11', 'E12', 'F11', 'F12', 'G11', 'G12', 'H11', 'H12']

guide6_PP1_T = guide6_PP1_T[~guide6_PP1_T['Well Location'].str.contains('|'.join(avoid_wells))] 
guide6_PP2_T = guide6_PP2_T[~guide6_PP2_T['Well Location'].str.contains('|'.join(avoid_wells))] 
guide4_PP1_T = guide4_PP1_T[~guide4_PP1_T['Well Location'].str.contains('|'.join(avoid_wells))] 
guide4_PP2_T = guide4_PP2_T[~guide4_PP2_T['Well Location'].str.contains('|'.join(avoid_wells))]  
guide8_PP1_T = guide8_PP1_T[~guide8_PP1_T['Well Location'].str.contains('|'.join(avoid_wells))] 
#guide8_PP2_T = guide8_PP2_T[~guide4_PP2_T['Well Location'].str.contains('|'.join(avoid_wells))] 

guide6_PP1 = guide6_PP1[~guide6_PP1['Well Location'].str.contains('|'.join(avoid_wells))] 
guide6_PP2 = guide6_PP2[~guide6_PP2['Well Location'].str.contains('|'.join(avoid_wells))] 
guide4_PP1 = guide4_PP1[~guide4_PP1['Well Location'].str.contains('|'.join(avoid_wells))] 
guide4_PP2 = guide4_PP1[~guide4_PP1['Well Location'].str.contains('|'.join(avoid_wells))] 
guide8_PP1 = guide4_PP1[~guide4_PP1['Well Location'].str.contains('|'.join(avoid_wells))] 
#uide8_PP2 = guide4_PP1[~guide4_PP1['Well Location'].str.contains('|'.join(avoid_wells))] 

#%% Average Column Temp for all guides

g6_PP1_meanT = guide6_PP1_T.iloc[:,4:].mean(axis=0)
g6_PP2_meanT = guide6_PP2_T.iloc[:,4:].mean(axis=0)
g4_PP1_meanT = guide4_PP1_T.iloc[:,4:].mean(axis=0)
g4_PP2_meanT = guide4_PP2_T.iloc[:,4:].mean(axis=0)
g8_PP1_meanT = guide8_PP1_T.iloc[:,4:].mean(axis=0)
#g8_PP2_meanT = guide8_PP2_T.iloc[:,4:].mean(axis=0)

#%% Transpose RFU Data Frames
g6_PP1_RFUs = guide6_PP1.iloc[:,4:].T
g6_PP2_RFUs = guide6_PP2.iloc[:,4:].T

g4_PP1_RFUs = guide4_PP1.iloc[:,4:].T
g4_PP2_RFUs = guide4_PP2.iloc[:,4:].T

g8_PP1_RFUs = guide8_PP1.iloc[:,4:].T
#g8_PP2_RFUs = guide8_PP2.iloc[:,4:].T

#%% Add Transposed mean T column to RFU dataframes
idx = 0

new_col = [g6_PP1_meanT, g6_PP2_meanT, g4_PP1_meanT, g4_PP2_meanT, g8_PP1_meanT] #, g8_PP2_meanT]

g6_PP1_RFUs.insert(loc=idx, column='Temp', value = new_col[0])
g6_PP2_RFUs.insert(loc=idx, column='Temp', value = new_col[1])

g4_PP1_RFUs.insert(loc=idx, column='Temp', value = new_col[2])
g4_PP2_RFUs.insert(loc=idx, column='Temp', value = new_col[3])

g8_PP1_RFUs.insert(loc=idx, column='Temp', value = new_col[4])
#g8_PP2_RFUs.insert(loc=idx, column='Temp', value = new_col[5])

#%% Save each dataframe as a .csv file

g6_PP1_RFUs.to_csv(path + 'g6_PP1_control.csv')
g6_PP2_RFUs.to_csv(path + 'g6_PP2_control.csv')
g4_PP1_RFUs.to_csv(path + 'g4_PP1_control.csv')
g4_PP2_RFUs.to_csv(path + 'g4_PP2_control.csv')
g8_PP1_RFUs.to_csv(path + 'g8_PP1_control.csv')
#g8_PP2_RFUs.to_csv(path + 'g8_PP2_control.csv')











