from flask import Flask, Response, url_for, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
@app.route('/hello')
def hello():
    return 'Hello, <b>World</b>'

@app.route('/untextoplano/<todo>')
def hello_world_txt(todo):
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data("Pepe <b>eres un </b>"+todo);
    return response

# @app.route('/archivo')
# def enviar_archivo():
#     response = Response()
#     f = open('facturon.jpg', 'rb')
#     imagen = f.read()
#     response.headers['Content-Type'] = 'image/jpg'
#     response.set_data(imagen);
#     return response

@app.route('/archivo')
def archivo():
    return render_template('archivo.html')

@app.route('/texto')
def texto():
    usuarios = []
    usuarios.append({'name':'Pablo2', 'dni':'123'})
    usuarios.append({'name':'Pablo3', 'dni':'1111'})
    return render_template('texto.html', var='esto', usuarios=usuarios)

@app.route('/')
def sitio():
    return render_template('index.html')

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


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
