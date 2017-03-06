# Tarea 1
### Aplicación con flask

> Autor: Juan Pablo González

>Tarea: Realizar una aplicación web con un microframework (flask), que deje iniciar sesión a un usuario por medio de un formulario. Se debe hacer con templates de flask (jinja2) y estos templates con preferiblemente con alguna libreria de css como bootstrap. Al tratarse de inicios de sesión se puede utilizar las variables de sesión que el navegador permite.

### Implementación

Para la implementación se han creado dos archivos. Uno en la carpeta tempates llamado index.html que contendrá la pagina principal con su plantilla y otro llamado t1.py que será el encargado de ejecutar los scripts que se van a utilizar.

##### Index.html

Este documento contiene las web en html junto con jinja2 para mostrar variables de flask.
```
 <label>{{session['user']}}</label>
```
Para redireccionar formularios o enlaces a scripts se hace por medio de la funcion url_for
``` action="{{ url_for('login') }}"```
Al inciar login, buscará en el script en ejecución la función login en /login, ejecutando el código que contenga.

##### t1.py

En este documento aparecen varios tipos de funciones como prueba, como mostrar imagenes, texto plano, texto html y por supuesto iniciar sesiones.

```
@app.route('/')
def sitio():
    usuarios = []
    usuarios.append({'name':'Pablo2', 'dni':'123'})
    usuarios.append({'name':'Pablo3', 'dni':'1111'})
    return render_template('index.html', var='esto', usuarios=usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
    return redirect(url_for('sitio'))
    #return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('sitio'))
```
En el trozo de código anterior se ve como primero en la ruta / se lanza la funcion sitio() que crea una rray con usuarios y renderiza la plantilla index.html, pasando 2 variables.

Las funciones de login y logout modifican la variable de sesión user y redireccionan a la url para sitio , es decir, al index.

