# Cohete Challenge
Para desplegar el proyecto en un entorno virtual (virtualenv) deberá concretar los siguientes pasos:

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