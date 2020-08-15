# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:23 2020

@author: qtand
"""

import pandas as pd
path_guardado = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.pickle"
df = pd.read_pickle(path_guardado)

#loc Acceder a grupo fila y columnas x LABEL (ARR TRUE)


#primero = df.loc[1035] #serie se trae toda la fila 
#print(primero)

filtrado_horizontal = df.loc[1015] #Serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indices columnas

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index) 

#filtrado por el indice 
df_1035 = df[df.index == 1035]
segundo = df.loc[1035] #Filtrar por indice(1)

segundo = df.loc[[1035,1036]] #filtrar pot arr indice (2)

segundo = df.loc[3:5] #filtrdo desde x indice hatsta y indice (3)
segundo = df.loc[df.index == 1035] #Filtrar por arreglo Arreglo true and false(4)

segundo = df.loc[1035, ['artist','medium']] #varios indices


#print(df.loc[0]) Indice dentro del Dataframe
#print(df[0])Incie dentro del DataFrame


#ILOC - Acceder a grupo fila y columnas x INDICEs basados en 0 
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]
#filtrado de indices por rango de indices 0:4
tercero = df.iloc[0:10, 0:4]

########################
datos = {
    "nota 1":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "nota 2":{
        "Pepito": 7,
        "Juanita": 8,
        "Maria": 9
        },
    "disciplina":{
        "Pepito": 4,
        "Juanita": 9,
        "Maria":2
        },
    }
notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] > 7
condicion_nota2 = notas["nota 2"] > 7
condicion_disciplina = notas["disciplina"] > 7

mayores_siete = notas.loc[condicion_nota, ["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota2][condicion_disciplina]
notas.loc["Maria", "disciplina"] = 7
#Cambiar a todos 
notas.loc[:,"disciplina"] = 7

##Promedio de las 3 notas#################

notas["promedio"]= notas.mean([1][0])

