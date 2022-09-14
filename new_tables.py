import pandas as pd


def create_master_table(list_dataframes):
    """Crea una tabla única con una list_dataframes
    
    params:
        list_dataframes: Lista con el/los DataFrames a concatenar.
    return:
        DataFrame único.                            
    """
    df_master = pd.concat(list_dataframes, axis=0)
    df_master.insert(loc=0, column='id_row', value=range(len(df_master)))
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
    
    return df

