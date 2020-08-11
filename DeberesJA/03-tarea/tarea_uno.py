# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:16:20 2020

@author: qtand
"""


import xlsxwriter
import pandas as pd 
import numpy as np
path_guardado = "E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data.pickle"
df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519,:].copy()

data = sub_df['artist'].value_counts()
print(data)
rango_celdas = 'B2:B{}'.format(len(data.index)+1)
cuaderno = xlsxwriter.Workbook('E://EPN//Python//ReposPY//py-quinonez-jair//03-pandas//data//artwork_data_tarea.xlsx')
hoja_grafico = cuaderno.add_worksheet('Grafico')

hoja_grafico.write_column('B1', data)
hoja_grafico.write_column('A1', data.index)
#hoja_grafico.add_table('A1:B1', {'data': data,
#                              'columns': [{'header': 'Types'},
#                                         {'header': 'Number'}]}
#)

# Create a new chart object.
chart = cuaderno.add_chart({'type': 'bar'})


chart.add_series({
    'name': 'ARTISTS',		
    'categories': '=Grafico!$A$1:$A$85',
    				
    'values':     '=Grafico!$B$1:$B$85',
})

#chart.set_title ({'name': 'Artists '})
#chart.set_x_axis({'name': 'Artist'})
#chart.set_y_axis({'name': 'Number of times'})


hoja_grafico.insert_chart('D2', chart)

cuaderno.close()