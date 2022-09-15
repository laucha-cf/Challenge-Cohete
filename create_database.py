from email.policy import default
from sqlalchemy import create_engine, Column, Integer, DECIMAL, String, Date, Time
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import declarative_base


def create_dbms(dbms, user, password, host, port, db_name):
    """Crea la base de datos y las tablas
    
    params:
        dbms: Motor de base de datos
        user: Usuario
        password: Contraseña
        host: Host
        port: Puerto
        db_name: Nombre de la base de datos
    return:
        None
    """
    #Creamos el engine y la base de datos
    engine = create_engine(f'{dbms}://{user}:{password}@{host}:{port}/{db_name}')
    if not database_exists(engine.url):
        create_database(engine.url)
    
    #Se utiliza para declarar y crear las tablas
    Base = declarative_base()
    
    #Tabla Maestra
    class TablaUnica(Base):
        __tablename__ = 'tabla_unica'
        id_row = Column(Integer, primary_key=True)
        cod_localidad = Column(Integer)
        id_provincia = Column(Integer)
        id_departamento = Column(Integer)
        categoria = Column(String(50))
        provincia = Column(String(80))
        localidad = Column(String(80)) 
        nombre = Column(String(80))
        domicilio = Column(String(80))
        codigo_postal = Column(String(50))
        num_telefono = Column(String(80))
        mail = Column(String(80))
        web = Column(String(80))
    #Tabla con cantidad de registros por fuente
    class RegistrosFuente(Base):
        __tablename__ = 'registros_por_fuente'
        id_row = Column(Integer, primary_key=True, autoincrement=True)
        fuente = Column(String(50), default=None)
        cantidad = Column(Integer)
    #Tabla con cantidad de registros por categoría
    class RegistrosCategoria(Base):
        __tablename__ = 'registros_por_categoria'
        id_row = Column(Integer, primary_key=True, autoincrement=True)
        categoria = Column(String(80))
        cantidad = Column(Integer)
    #Tabla con cantidad de registros por provincia y categoría
    class RegistrosProvinciaCat(Base):
        __tablename__ = 'registros_por_provincia_categoria'
        id_row = Column(Integer, primary_key=True, autoincrement=True)
        provincia = Column(String(80))
        categoria = Column(String(80))
        cantidad = Column(Integer)
    #Tabla con datos sobre salas de cine
    class DataCinema(Base):
        __tablename__ = 'data_cinema'
        id_row = Column(Integer, primary_key=True, autoincrement=True)
        provincia = Column(String(80))
        pantallas = Column(Integer)
        butacas = Column(Integer)
        espacio_INCAA = Column(Integer)
        
    Base.metadata.create_all(engine)
    
    #Cerramos la conexión
    engine.dispose()

def fill_table(dataframe, name, engine):
    """Puebla una tabla
    
    params:
        dataframe: DataFrame a utilizar para poblar.
    return:
        None
    """
    dataframe.to_sql(name, engine, if_exists='replace', index=False, method='multi')

def load_db(to_load, dbms, user, password, host, port, db_name):
    """Carga las tablas de la base de datos en este orden
        df_master, 
        registros_por_categoria, 
        registros_por_fuente, 
        registros_provincia_categoria, 
        datos_cine_por_prov
    
    params:
        to_load: Lista con dataframes a cargar
        dbms: Motor de base de datos
        user: Usuario
        password: Contraseña
        host: Host
        port: Puerto
        db_name: Nombre de la base de datos
    return:
        None
    """
    #Genera la conexión con la base de datos
    engine = create_engine(f'{dbms}://{user}:{password}@{host}:{port}/{db_name}')
    connection = engine.connect()
    
    #Lista con los nombres de las tablas a poblar
    list_names = ['tabla_unica', 
                  'registros_por_categoria', 
                  'registros_por_fuente', 
                  'registros_por_provincia_categoria', 
                  'data_cinema']
    list_dataframes = to_load
    
    for i, name in enumerate(list_names):
        fill_table(list_dataframes[i], name, engine)
    
    #Cerramos la conexión
    connection.close()
    engine.dispose()
    
