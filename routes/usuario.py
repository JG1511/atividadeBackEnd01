from flask import Blueprint, request, render_template
from database.usuario import USUARIO

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/login', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        return validacaoLogin()
    else:
        return render_template('forms.html')

def validacaoLogin():
    email = request.form.get('email')
    senha = request.form.get('senha')

    for usuario in USUARIO:
        if usuario['email'] == email and usuario['senha'] == int(senha):
            return render_template('teste.html', usuarioLogado=usuario)
    
    
    return render_template('forms.html', erro="Email ou senha incorretos")
