from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, <b>World</b>'

@app.route('/untextoplano/<todo>')
def hello_world_txt(todo):
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data("Pepe <b>eres un </b>"+todo);
    return response

@app.route('/archivo')
def enviar_archivo():
    response = Response()
    f = open('facturon.jpg', 'rb')
    imagen = f.read()
    response.headers['Content-Type'] = 'image/jpg'
    response.set_data(imagen);
    return response

@app.route('/archivo')
def enviar_archivo2():
    response = Response()
    f = open('facturon.jpg', 'rb')
    imagen = f.read()
    response.headers['Content-Type'] = 'image/jpg'
    response.set_data(imagen);
    return response

@app.route('/sitio')
def sitio():
    usuarios = []
    usuarios.append({'name':"Pablo", 'dni':"1472"})
    usuarios.append({'name':'Pablo2', 'dni':'123'})
    usuarios.append({'name':'Pablo3', 'dni':'1111'})
    return render_template('hola.html', var='esto', usuarios='usuarios')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
