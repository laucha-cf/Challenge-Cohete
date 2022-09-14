import pandas as pd
from read_files import create_dataframes, read_files
from normalize_data import normalize_museos, normalize_cines, normalize_bibliotecas


if __name__ == '__main__':
    #Extraemos y almacenamos los datos
    dataframes = create_dataframes()
    read_files(list_dataframes=dataframes)
    
    #Cargamos los datos
    df_cines = pd.read_csv('cines/2022-September/cines-14-09-22')
    df_museos = pd.read_csv('museos/2022-September/museos-14-09-22')
    df_bibliotecas = pd.read_csv('bibliotecas/2022-September/bibliotecas-14-09-22')
    
    #Normalizamos las tablas
    df_cines = normalize_cines(df_cines.copy())
    df_museos = normalize_museos(df_museos.copy())
    df_bibliotecas = normalize_bibliotecas(df_bibliotecas.copy())

    #Creamos tabla única
    df_master = pd.concat([df_cines, df_museos, df_bibliotecas], axis=0)