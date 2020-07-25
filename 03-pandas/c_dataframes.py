# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:48:24 2020

@author: qtand
"""

#c_dataframes.py
import numpy as np 
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)
df1 = pd.DataFrame(arr_pand)
s1 = df1[0]#devuelve una serie 

#operaciones con la serie. 
s2 = df1[1]
s3 = df1[2]

df1[3] = s1 
 
df1[4] = s1 * s2 
datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura',
        'Peso',
        'Edad'],
    index = [
        'Jair',
        'Andres'])
#Acceder por indice y columna
#serie_peso = datos_fisicos_uno['Edad']
#print(serie_peso['Jair'])

#edicion de index y columns 
df1.index = ['Test','Testing']
df1.index = ['Test2','Testing2']
df1.columns = ['A','B','C','D','E']

