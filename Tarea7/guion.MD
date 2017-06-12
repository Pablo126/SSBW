http://patternhatch.com/2016/07/06/a-primer-on-the-react-ecosystem-part-1-of-3/

Empezamos creando el directorio de trabajo

`mkdir Tarea7`
`npm init -y`

editamos el package.json
```
{
  "name": "Tarea7",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "JPG",
  "license": "ISC"
}
```

Creamos index.html,index.js y ponemos lo que dice

Ahora instalamos el webpack y veremos como lo añade a package.json

Podriamos borrar el directorio node_modules y luego solo con poner npm install, ya volveria a instalar lo que teniamos.


Cremos el webpack.config.js con el codigo e la webpack

Y ahora ejecutamos
`node node_modules/webpack/bin/webpack.js`


Ahora seguimos añadiendo lo que quede en el webpack.config.js


Bueno despues de acabar este tutorial vemos el otro que lo compara con JQuery. Este trabaja sobre jsbin




Hay un fallo con las versiones del as dependencias... asi que miramos en lgithub que está actualizado y vemos cuales son las versiones.

ahora nos compilará automaticamente el código de nuestra fuente, dando como resultado en la carpeta dist a lo que es el archivo que se presentará (no es desarrollo)
