# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:31:32 2020

@author: Sebastian_Tilaguy
"""
import pandas as pd
import numpy as np

path = 'C:/Users/Sebastian_Tilaguy/.spyder-py3/ProcessedData/'
filename = 'Processed_data_ref.csv'
df_ref = pd.read_csv(path+filename, sep="\t", header = 0)
filename = 'Processed_data_1.csv'
df = pd.read_csv(path+filename, sep="\t", header = 0)

# print(df_ref)
print(df)

#%%
# df.drop(df[df['Z']<=self.z_ref].index)
a = df_ref['high'].drop(df_ref[df_ref['high']==0.0].index)
b = df['high'].drop(df[df['high']==0.0].index)

e_h = (a.values-b.values)**2
e_rms = np.sqrt(np.mean(e_h))
print('Error de altura')
print(e_rms)
e_h = (a.values-b.values)/a.values
print(np.mean(e_h))

#%%
a = df_ref['D_tree'].drop(df_ref[df_ref['D_tree']==0.0].index)
b = df['D_tree'].drop(df[df['D_tree']==0.0].index)
avg_dt_ref = a.mean()
avg_dt = b.mean()

e_dt = (avg_dt-avg_dt_ref)/avg_dt_ref*100
print('Error de distancia entre arboles')
print(avg_dt_ref,avg_dt)
print(e_dt)

#%%
a = df_ref['D_groove'].drop(df_ref[df_ref['D_groove']==0.0].index)
b = df['D_groove'].drop(df[df['D_groove']==0.0].index)
avg_dg_ref = a.mean()
avg_dg = b.mean()

e_dg = (avg_dg-avg_dg_ref)/avg_dg_ref*100
print('Error de distancia entre surcos')
print(avg_dg_ref,avg_dg)
print(e_dg)

#%%
a = df_ref['Dimeter'].drop(df_ref[df_ref['Dimeter']==0.0].index)
b = df['Dimeter'].drop(df[df['Dimeter']==0.0].index)

e_d = (a.values-b.values)**2
e_rms = np.sqrt(np.mean(e_d))
print('Error de diametro')
print(e_rms)
e_h = (a.values-b.values)/a.values
print(np.mean(e_h))