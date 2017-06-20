#### Instalamos virtualenv
#### Instalamos python3

Tras esto, hacemos:

```
> virtualenv -p python3 Entrega1
> sudo apt-get install python-pip
```
una vez tengamos esto hacemos:
```
> source bin/activate dentro de la carpeta de ssbw de virtualenv
> pip install python
> pip freeze  ; mostrara las libreriaspip
```

extraemos las librerias que tenemos instalados con
```
> pip freeze > requeriments.txt
```

luego si queremos instalar todo podremos hacer
```
> pip install -(nombrearchivo)
```

Instalamos Django

pip install django
django-admin startproject entrega1
cd entrega1
python manage.py runserver
python manage.py startapp restaurantes

mkdir templates
mkdir static

> ahora apuntamos en entrega1/settings.py a la carpeta de templates
```
TEMPLATES = [
{
'DIRS':[os.path.join(BASE_DIR, 'templates')]
...
 +++++++
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
 +++++++
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurantes',
]
```
Ahora podemos iniciar la bases de datos SQL que usaremos para los datos autentificación y registro de usuarios, para los restaurantes seguimos usando mongoDB
$ python manage.py migrate

Esto habrá que hacerlo cada vez que hagamos cambios en la BD SQL

Creamos ahora un administrador de la BD
$ python manage.py createsuperuser

usuario por defecto pablo... sin escribir nada.. contraseña asd12614

y tendremos acceso a la aplicación de administración de la BD en:
 http://localhost:8000/admin
