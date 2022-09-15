import pandas as pd
import numpy as np

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
    df['espacio_INCAA'].replace(to_replace='0', value=np.nan, inplace=True)
    df['espacio_INCAA'].replace(to_replace='SI', value='si', inplace=True)
    
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
