import pandas as pd
import datetime as dt
import os

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

    
def read_files(list_dataframes):
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
    list_categories = ['museos', 'cines', 'bibliotecas']

    for i, sheet_id in enumerate(list_spreadsheet_id):
        url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
        url = url.format(sheet_id, list_categories[i])
        list_dataframes[i] = pd.read_csv(url)
        #Crea el path donde se almacenará
        path = create_path(list_categories[i])
        #Crea el nuevo directorio donde se almacenará
        list_path = path.split('/')
        new_dir = f'{list_path[0]}/{list_path[1]}'
        os.makedirs(new_dir)
        #Guarda el archivo en el directorio creado
        list_dataframes[i].to_csv(path, index=False)
        


if __name__ == '__main__':
    dataframes = create_dataframes()
    read_files(list_dataframes=dataframes)