# Título del Proyecto

Biblioteca simple.

## Descripción

Proyecto básico que funciona como una libreria/tienda de libros, articulos o archivos.

## Getting Started

### Dependencias

* Libreria `django-phonenumber-field`
* Instalar dependencias a traves del archivo `requerimientos.txt`
  

### Instalación

* Instalar todas las dependencias en entorno virtual
```
pip install -r ../path/to/requerimientos.txt
```

## Ayuda

Si la dependencia `django-phonenumber-field` no se puede instalar con el comanado anterior, entonces ejecutar:
```
pip install django-phonenumber-field[phonenumbers]
```

# NOTAS

## Para crear el entorno virtual
    - python -m venv 'name'

## Para iniciar el entorno virtual:
        - .\venv\Scripts\activate

## Correr proyecto:
Tienes que posicionarte en la ruta del proyecto

    - py manage.py runserver
    
### Crear nueva aplicacion
    - py manage.py startapp core

### Crear migracion de datos
    - py manage.py makemigrations

### Correr la migracion
    - py manage.py migrate

### Crear usuario
    - py manage.py createsuperuser

### Crear modelo
    - Dentro de models.py crear clases para las tablas

<!-- 
## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie) -->

