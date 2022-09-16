import pandas as pd
import numpy as np
import datetime as dt

def normalize_cines(df):
    """Normaliza los campos del dataframe Cines.
    
    params:
        df: DataFrame Cines
    return:
        df: DataFrame normalizado
    """
    df = df[['Cod_Loc', 'IdProvincia', 'IdDepartamento',
            'Categoría', 'Provincia', 'Localidad', 'Nombre',
            'Dirección', 'CP', 'Teléfono', 'Mail', 'Web', 'Fuente',
            'Pantallas', 'Butacas', 'espacio_INCAA']]
    df.columns = ['cod_localidad','id_provincia','id_departamento',
                'categoria','provincia','localidad','nombre',
                'domicilio','codigo_postal','num_telefono','mail',
                'web', 'fuente', 'pantallas', 'butacas', 'espacio_INCAA']
    #Normalizamos los datos dentro de la columna espacio_INCAA
    df.loc[df['espacio_INCAA']=='0', 'espacio_INCAA'] = np.nan
    df.loc[df['espacio_INCAA']=='SI', 'espacio_INCAA'] = 'si'
    
    return df

def normalize_museos(df):
    """Normaliza los campos del dataframe Museos.
    
    params:
        df: DataFrame Museos
    return:
        df: DataFrame normalizado
    """
    df = df[['Cod_Loc', 'IdProvincia', 'IdDepartamento',
            'categoria', 'provincia', 'localidad', 'nombre',
            'direccion', 'CP', 'telefono', 'Mail', 'Web', 'fuente']]
    df.columns = ['cod_localidad','id_provincia','id_departamento',
                'categoria','provincia','localidad','nombre',
                'domicilio','codigo_postal','num_telefono','mail',
                'web', 'fuente']
    return df

def normalize_bibliotecas(df):
    """Normaliza los campos del dataframe Bibliotecas.
    
    params:
        df: DataFrame Bibliotecas
    return:
        df: DataFrame normalizado
    """
    df = df[['Cod_Loc', 'IdProvincia', 'IdDepartamento',
            'Categoría', 'Provincia', 'Localidad', 'Nombre',
            'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web', 'Fuente']]
    df.columns = ['cod_localidad','id_provincia','id_departamento',
                'categoria','provincia','localidad','nombre',
                'domicilio','codigo_postal','num_telefono','mail',
                'web', 'fuente']
    return df

def normalize_master(df_master):
    """Selecciona las columnas relevantes para la carga
    a la base de datos
    
    params:
        df_master: DataFrame a transformar.
    return:
        df_ready: DataFrame listo para la carga a la base de datos.
    """
    #Seleccionamos columnas
    df_ready = df_master[['id_row', 'cod_localidad', 'id_provincia',
             'id_departamento', 'categoria', 'provincia',
             'localidad', 'nombre', 'domicilio',
             'codigo_postal', 'num_telefono', 'mail', 
             'web']]
    #Agregamos timestamp de carga
    df_ready['fecha_carga'] = dt.datetime.now()
    
    return df_ready