from flask import Flask
from routes.usuario import usuario_route

app = Flask(__name__)

app.register_blueprint(usuario_route)

@app.route('/')
def teste():
    return 'olá Mundo'

app.run(debug=True)