# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:41 2020

@author: qtand
"""


import pandas as pd
path_guardado = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.pickle"
df = pd.read_pickle(path_guardado)
serie_artisstas_dup = df['artist']

artistas = pd.unique(serie_artisstas_dup)
print(type(artistas)) #numpy array 
print(artistas.size)

blake = df['artist'] == 'Blake, William' #Serie
print(blake.value_counts())
df_blake = df[blake] #DataFrame