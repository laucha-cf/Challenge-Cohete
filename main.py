import pandas as pd
from modules.read_files import create_dataframes, extract_files, load_files
from modules.normalize_data import normalize_museos, normalize_cines, normalize_bibliotecas, normalize_master
from modules.new_tables import create_master_table, create_new_table, data_cinema_table
from modules.create_database import create_dbms, load_db
import logging
from decouple import config


# - CREDENCIALES - #
DBMS = config('DBMS')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = config('PORT')
DB_NAME = config('DB_NAME')

#Establecemos el formato para los loggings
logging.FileHandler(filename='app_logs.log', mode='w')
logging.basicConfig(filename='app_logs.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

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
    df_master = create_master_table([df_cines, df_museos, df_bibliotecas])
    
    #Creamos nuevas tablas
    registros_por_categoria = create_new_table(
                                            df_master.copy(),
                                            ['categoria']
                                        )
    registros_por_fuente = create_new_table(
                                            df_master.copy(), 
                                            ['fuente']
                                        )
    registros_provincia_categoria = create_new_table(
                                            df_master.copy(), 
                                            ['provincia','categoria']
                                            )
    
    datos_cine_por_prov = data_cinema_table( df_cines=df_cines.copy() )
    
    #Normalizamos la tabla única para su carga
    df_master = normalize_master( df_master.copy() )
    
    #Creamos la base de datos
    create_dbms( DBMS, USER, PASSWORD, HOST, PORT, DB_NAME )
    
    #Seleccionamos los dataframes a cargar
    dataframes_to_load = [df_master,
                          registros_por_categoria,
                          registros_por_fuente,
                          registros_provincia_categoria,
                          datos_cine_por_prov]
    #Cargamos los datos a las tablas
    load_db( dataframes_to_load, DBMS, USER, PASSWORD, HOST, PORT, DB_NAME )