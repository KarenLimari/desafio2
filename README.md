# Proyecto Django: Desafío - Django acceso de datos

Se solicita un proyecto de administración de tareas, donde tendremos Tareas y SubTareas.
Las tareas deben tener un identificador autonumérico, descripción y estado, las subtareas tienen los mismos campos, más una relación a Tareas. El proyecto debe contar con un archivos de servicios donde estará la lógica de aplicación sobre los modelos. Se podrá presentar utilizando SQLite3 o Postgresql.

El proyecto se llama **desafio2** y contiene una aplicación llamada **desafioadl**. Se ha configurado para crear y gestionar tablas `desafioadl`, además de utilizar las tablas generadas automáticamente por Django.

## Requerimientos Técnicos

- **Motor de base de datos:** PostgreSQL
- **Framework web:** Django
- **Entorno de Python:** Virtual environment (opcional, pero recomendado)

## Instrucciones de Desarrollo

### 1. Instalación y configuración del motor de base de datos PostgreSQL

1. Instalar PostgreSQL en el sistema.
2. Crear una base de datos llamada `desafio2_bd`:
   ```sql
   CREATE DATABASE "desafio2_bd";
   ```

### 2. Configuración del Proyecto Django

1. Crear el proyecto Django
```sql
django-admin startproject desafio2
```
2. Crear la aplicación dentro del proyecto:
```sql
python manage.py startapp desafioadl
```
3. Configurar la conexión a PostgreSQL en el archivo settings.py
```sql
DATABASES = {
 'default': {
 'ENGINE':'django.db.backends.postgresql',
 'NAME': os.getenv('BD_NAME'),
 'USER': os.getenv('BD_USER'),
 'PASSWORD': os.getenv('BD_PASSWORD'),
 'HOST': os.getenv('BD_HOST','127.0.0.1'),
 'PORT': os.getenv('BD_PORT','5432'),
 }
}
```
### 3. Creación del Modelo y Migraciones

1. Definir el archivo services.py de la aplicación desafioadl.

2. Generar las migraciones:

```sql
python manage.py makemigrations
```

3. Aplicar las migraciones:

```sql
python manage.py migrate
```

### 4.Verificación en consola de Django

1. Acceder a manage.py Shell y verificar Cada función que opere sobre los modelos, luego de actualizar, debe devolver un
arreglo con las tareas y subtareas

2. La función imprimir_en_pantalla debe ser capaz de recibir ese arreglo e imprimir las
tareas y subtareas de forma ordenada.

3. Captura: Se incluye imagenes de la vista, con lo solicitado.

## 5. Capturas  

Las capturas solicitadas están en la carpeta capturas.

## Autor  
**Karen Limarí**
