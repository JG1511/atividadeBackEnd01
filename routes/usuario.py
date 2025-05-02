from flask import Blueprint, request, render_template,redirect,url_for
from database.usuario import USUARIO

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/login', methods=['GET', 'POST'])
def login_usuario():
    # Se a requisição for do método post, ele irá chamar a função de validação do login
    if request.method == 'POST':
        return validacaoLogin() 
    else:
        return render_template('forms.html')

def validacaoLogin():
    # email e senha vão pegar os dados do forms, por isso a utilização do ".form.get"
    email = request.form.get('email')
    senha = request.form.get('senha')
    # laço de repetição para percorrer a lista de discionário e comparar com os dados armazenados do forms e armazenar o nome
    for usuario in USUARIO:
        if usuario['email'] == email and usuario['senha'] == int(senha):
            nome = usuario['nome']
            # O redirect além de rederecionar também manda o nome para '/perfil/<nome>''
            return redirect(url_for('usuario.perfil', nome = nome))
    
    
    return render_template('forms.html', erro="Email ou senha incorretos")

@usuario_route.route('/perfil/<nome>')
def perfil(nome):
    return render_template('lista_musica.html',nome = nome)