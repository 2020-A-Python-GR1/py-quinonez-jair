# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:38 2020

@author: qtand
"""
import numpy as np 
import pandas as pd
lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_arreglos = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_arreglos)
series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Jair",
    None,
    (1),
    [2],
    {"nombre":"Jair"}
    ])
print(series_d[5])
lista_ciudades = ["Ambato",
                  "Cuenca",
                  "Loja",
                  "Quito"]
serie_ciudad = pd.Series(lista_ciudades,
                         index = ["A",
                                  "C",
                                  "L",
                                  "Q"])
print(serie_ciudad[3])
print(serie_ciudad["C"])

valores_ciudad = {
    "Ibarra":95000,
    "Guayaquil":10000,
    "Cuenca": 70000,
    "Quito":80000,
    "Loja":3000
    }
serie_valores_ciudad = pd.Series(valores_ciudad)

ciudades_menor_5k = serie_valores_ciudad < 5000

print(ciudades_menor_5k)
print(type(ciudades_menor_5k))
print(type(serie_valores_ciudad))

s5 = serie_valores_ciudad[ciudades_menor_5k]
print(s5)
serie_valores_ciudad = serie_valores_ciudad * 1.1
serie_valores_ciudad["Quito"] = serie_valores_ciudad["Quito"] - 50
print("Lima" in serie_valores_ciudad)





















