import pandas as pd
import numpy as np
import datetime as dt
import logging

def create_master_table(list_dataframes):
    """Crea una tabla única con una list_dataframes
    
    params:
        list_dataframes: Lista con el/los DataFrames a concatenar.
    return:
        DataFrame único.                            
    """
    df_master = pd.concat(list_dataframes, axis=0)
    df_master.insert(loc=0, column='id_row', value=range(len(df_master)))
    
    logging.info('Master table created.')
    
    return df_master

def create_new_table(df_master, columnas):
    """Retorna un DataFrame con la cantidad de registros 
    totales por una o varias columnas especificadas.
    
    params:
        df_master: DataFrame a utilizar
        columnas: Lista de columna/s por las cuáles filtrar
    return:
        df: DataFrame con la cantidad de registros totales
    """
    #Cantidad de registros totales por categoría
    df = df_master.groupby(by=columnas)['id_row'].count()
    df = pd.DataFrame(df).reset_index()
    df.rename(columns={
        'id_row': 'cantidad'
    }, inplace=True)
    #Agregamos fecha de carga
    df['fecha_carga'] = dt.datetime.now()
    
    logging.info('New table created. Filtered by {}.'.format(columnas))
    
    return df

def data_cinema_table(df_cines):
    """Retorna un DataFrame con
        o Provincia
        o Cantidad de pantallas
        o Cantidad de butacas
        o Cantidad de espacios INCAA
        o Fecha de carga
    
    params:
        df_cines: DataFrame de cines de los cuáles procesa los datos.
    return:
        datos_por_provincia: DataFrame con datos.
    """
    #Agrupamos por provincia
    df_cines_por_provincia = df_cines.groupby(by=['provincia'])
    #Cantidad de pantallas y butacas
    df_pantallas_y_butacas = df_cines_por_provincia[['pantallas', 'butacas']].sum()
    df_pantallas_y_butacas.reset_index(inplace=True)
    #Cantidad de espacios INCAA
    df_espacios_incaa = df_cines_por_provincia[['espacio_INCAA']].count()
    df_espacios_incaa.reset_index(inplace=True)

    #Agrupamos los datos en una sola tabla
    datos_por_provincia = pd.concat([
        df_pantallas_y_butacas,
        df_espacios_incaa['espacio_INCAA']
    ], axis=1)
    #Agregamos timestamp de carga
    datos_por_provincia['fecha_carga'] = dt.datetime.now()
    
    logging.info('Table with info about Cines created.')
    
    return datos_por_provincia