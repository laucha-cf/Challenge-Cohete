# Cohete Challenge
### **Creación y activación de un entorno virtual (virtualenv)**

- Abrir la consola de comandos (cmd). Una vez en la misma ejecutar:

1) Actualizar pip (por si acaso):
```
py -m pip install --upgrade pip
```

2) Instalar virtualenv:
```
pip install virtualenv
```

3) Crear el entorno virtual:
```
py -m venv "nombre_entorno"
```
Donde **"nombre_entorno"** es el nombre que le quieras poner al entorno.

4) Activar el entorno virtual.
Nos dirigimos a la carpeta donde hemos creado el entorno. Dentro de la misma ejecutamos el siguiente comando:
```
/Scripts/activate.bat
```
5) Asegurarse de haber activado el entorno. Para esto, debe ver que antes de la dirección donde se encuentra, aparezca entre paréntesis el nombre del entorno virtual.
De esto...
```
UnaDirección/algoMas
```
Pasaría a lo siguiente
```
("nombre_entorno") UnaDirección/algoMas
```
6) Instalar las librerías dentro de el archivo **requirements.txt**.
```
pip install -r /dirección/requirements.txt
```
7) Verificar que se hayan instalado correctamente. 
```
pip list
```
o
```
pip freeze
```
### **Ejecución del Proyecto**

1) Establecemos las credenciales correspondientes a nuestra base de datos.
Creamos un archivo **.env** con el siguiente formato:
```
DBMS = 'postgres'
USER = Usuario de nuestro gestor de bases de datos. Por defecto es 'postgres'.
PASSWORD = Contraseña de nuestro gestor de bases de datos. Por defecto es 'postgres'.
HOST = 'localhost'
PORT = Por defecto es *5432*.
DB_NAME = Nombre a elección para nuestra base de datos.
```

2) Ejecutamos el proyecto.
Nos dirigimos a la terminal de comandos, siempre con el entorno virtual activo.
Ejecutamos:
```
py main.py
```

