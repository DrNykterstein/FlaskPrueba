#importo el framework flask
from flask import Flask, render_template

#objeto que nos devuelve el framework y nos ayuda a crear las rutas y se guarda en la variable app
app = Flask(__name__)

#creo ruta para la pagina web principal
@app.route('/')
def index():
	return render_template('home.html')

#creo otra ruta
@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
#con el metodo run, corro la apliacion
	app.run(debug=True)