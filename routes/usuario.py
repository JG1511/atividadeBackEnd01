from flask import Blueprint

usuario_route = Blueprint('usuario',__name__)

@usuario_route.route('/')
def login_usuario():
    pass