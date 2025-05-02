from flask import Blueprint, request
from database.usuario import USUARIO

usuario_route = Blueprint('usuario',__name__)

@usuario_route.route('/login', methods = ['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        return validacaoLogin
    else:
        pass 
    
def validacaoLogin():
    pass