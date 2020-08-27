# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:28:57 2020

@author: qtand
"""
import pandas as pd
import numpy as np
import os
import sqlite3 
import xlsxwriter

#path_guardado = "./data/artworkdata.pickle"
path_guardado = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.pickle"
df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519,:].copy()

#artwork_data.xlsx
path_excel = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_excel.xlsx"
path_excel_indice = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_indice.xlsx"
path_excel_columnas = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_columnas.xlsx"
path_xlsx = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.xlsx"
columnas = ['artist','title','year']
sub_df.to_excel(path_excel)
sub_df.to_excel(path_excel_indice, index = False)
sub_df.to_excel(path_excel_columnas, columns=columnas)

#Multiples hojas de trabjo 
path_excel_mt = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_excel_mt.xlsx"
writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')
sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save()

#Formato condicional 

num_artist = sub_df['artist'].value_counts()
print(num_artist)
path_excel_colores = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_excel_colores.xlsx"
writer = pd.ExcelWriter(path_excel_colores, engine = 'xlsxwriter')
#Series
num_artist.to_excel(writer, 
                    sheet_name = 'Artistas')
#Seleccionando la hoja de trabajo
hojas_artistas = writer.sheets['Artistas']
ultimo_numero = len(num_artist.index) + 1
#rango de celdas
#rango_celdas = f'B2:B{ultimo_numero}'
rango_celdas = 'B2:B{}'.format(len(num_artist.index)+1)
#formato

formato_artista = {
    "type":"2_color_scale",
    "min_value":"1",
    "min_type": "percentible",
    "max_value":"99",
    "max_type":"percentible"
    }
hojas_artistas.conditional_format(rango_celdas,formato_artista)

writer.save()
#SQLITE
#with sqlite3.connect("bdd_artist.bdd") as conexion:
    #sub_df.to_sql('py_artistas', conexion)

#JSON
#sub_df.to_json('artista.json')
#sub_df.to_json('artista_tabla.json', orient='table')
    