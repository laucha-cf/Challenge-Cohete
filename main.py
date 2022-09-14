import pandas as pd
from read_files import create_dataframes, extract_files, load_files
from normalize_data import normalize_museos, normalize_cines, normalize_bibliotecas


if __name__ == '__main__':
    #Extraemos y almacenamos los datos
    empty_dataframes = create_dataframes()
    extract_files(list_dataframes=empty_dataframes)
    
    #Cargamos los datos
    df_museos, df_cines, df_bibliotecas = load_files()
    
    #Normalizamos las tablas
    df_cines = normalize_cines(df_cines.copy())
    df_museos = normalize_museos(df_museos.copy())
    df_bibliotecas = normalize_bibliotecas(df_bibliotecas.copy())

    #Creamos tabla única
    df_master = pd.concat([df_cines, df_museos, df_bibliotecas], axis=0)