import pandas as pd
import datetime as dt
import os
import shutil
import logging

list_categories = ['museos', 'cines', 'bibliotecas']

def create_dataframes():
    """Retorna una lista con tres objetos de tipo DataFrame. Uno por spreadsheet.
    params:
        None
    return:
        list_dataframes: lista de dataframes.
    """
    list_dataframes = []
    
    df_museos = pd.DataFrame()
    list_dataframes.append(df_museos)
    
    df_cines = pd.DataFrame()
    list_dataframes.append(df_cines)
    
    df_bibliotecas = pd.DataFrame()
    list_dataframes.append(df_bibliotecas)
    
    return list_dataframes

def create_path(name):
    """Retorna la dirección donde se guardará el archivo CSV
    
    params:
        name: Nombre del archivo
    return:
        path: Dirección
    """
    today = dt.date.today()
    month_string = today.strftime('%B')
    path = f"{name}/{today.year}-{month_string}/{name}-{today.strftime('%d-%m-%y')}"
    return path
   
def extract_files(list_dataframes):
    """Lee los tres archivos de tipo spreadsheet y los
    convierte a tipo CSV. Luego los almacena en el entorno local.
    
    params:
        list_dataframes: Lista de dataframes
    return:
        None 
    """
    list_spreadsheet_id = ['1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA',
                           '1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM',
                           '1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk']

    for i, sheet_id in enumerate(list_spreadsheet_id):
        url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
        url = url.format(sheet_id, list_categories[i])
        list_dataframes[i] = pd.read_csv(url)
        #Crea el path donde se almacenará el archivo (si no existe)
        path = create_path(list_categories[i])
        #Crea el nuevo directorio donde se almacenará
        list_path = path.split('/')
        new_dir = f'{list_path[0]}/{list_path[1]}'
        
        if os.path.exists(new_dir):
            shutil.rmtree(f'{list_categories[i]}/')

        os.makedirs(new_dir)
        logging.info('Directory {}/ created.'.format(list_categories[i]))
        
        #Guarda el archivo en el directorio creado
        list_dataframes[i].to_csv(path, index=False)
        logging.info('Dataframe {} saved.'.format(list_categories[i]))
               
def load_files():
    """Retorna los archivos previamente almacenados.
    
    params:
        None
    return:
        list_dataframes: DataFrames generados. Uno por categoría.
    """
    list_dataframes = create_dataframes()
    for i, category in enumerate(list_categories):
        path = create_path(category)
        list_dataframes[i] = pd.read_csv(path)
    return list_dataframes[0], list_dataframes[1], list_dataframes[2]
    