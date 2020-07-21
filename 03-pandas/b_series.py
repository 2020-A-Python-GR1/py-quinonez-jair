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

svc_cuadrado = np.square(serie_valores_ciudad)
ciudades_uno = pd.Series({
    "Montañita": 300,
    "Guayaquil": 10000,
    "Quito": 2000
    })
ciudades_dos = pd.Series({
    "Loja":300,
    "Guayaquil": 10000
    })
ciudades_uno["Loja"] = 0
print(ciudades_uno + ciudades_dos)
ciudades_add = ciudades_uno.add(ciudades_dos)
ciudad_concat = pd.concat([
    ciudades_uno,ciudades_dos
    ])
ciudad_concat_verify = pd.concat([
    ciudades_uno,ciudades_dos],
    verify_integrity=False)
#sub()
#mul()
#div
ciudad_concat_verify = ciudades_uno.append(
    ciudades_dos,verify_integrity=False)
#obtener maximo y minimo
print(ciudades_uno.max())
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))

print(ciudades_uno.min())
print(pd.Series.min(ciudades_uno))
print(np.min(ciudades_uno))

#Media, mediana.
print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))

print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))

print(ciudades_uno.sort_values(
    ascending=False).head(2))
print(ciudades_uno.sort_values().tail(2))

#0- 1000 5%
#1001 - 50000 10%
#5001 - 20000 15%

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 15
    if(valor_serie > 1000 and valor_serie <= 5000 ):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15
ciudad_calculada = ciudades_uno.map(calcular)

#if else 
#cuando no se cumple la condicion

resultado = ciudades_uno.where(ciudades_uno < 1000,
                   ciudades_uno * 1.05)
print(resultado)

series_numeros = pd.Series(['1.0','2',-3])
print(pd.to_numeric(series_numeros))
#Se peude elegir INteger, signed, unsigned, flotantes 
print(pd.to_numeric(series_numeros, downcast='integer'))
series_numeros_err = pd.Series(['1.0','2',-3,'no tiene'])
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))















