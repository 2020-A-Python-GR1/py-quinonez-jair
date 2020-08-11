# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:33 2020

@author: qtand
"""
import pandas as pd
import os 

path = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.csv"

df1 = pd.read_csv(
    path)

#Definir columnas que nostros queremos utilizar

columnas = ['id','artist','title',
            'medium', 'year',
            'acquisitionYear','height','width','units'
            ]

df2 = pd.read_csv(path,
                  
                  usecols=columnas)
df3 = pd.read_csv(path,
                  usecols=columnas,
                  index_col='id')

path_guardado = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.pickle"
#debe ser .pickle
df3.to_pickle(path_guardado)
#leer el pickle 
df5 = pd.read_pickle(path_guardado)