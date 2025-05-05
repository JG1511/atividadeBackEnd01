from flask import Blueprint, request, render_template,redirect,url_for
from database.usuario import USUARIO,MUSICA

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

@usuario_route.route('/perfil/<nome>', methods = ['GET','POST'])
def perfil(nome):
    
    musica_editada = None

    musica_id = request.args.get('musica_id') # O args consulta(query parameters) na URL. Parâmetros que vem depois da ? na url 
    
    if musica_id:
        musica_editada = next((m for m in MUSICA if m['id'] == int(musica_id)),None)
    
    if request.method == 'POST':

        nomeDaMusica = request.form.get('nome')

        if musica_editada:
            musica_editada['nome'] = nomeDaMusica
        else:
            nova_musica = {
                "id": len(MUSICA) + 1,
                "nome" : nomeDaMusica
            }

            MUSICA.append(nova_musica)

        return redirect(url_for('usuario.perfil', nome = nome))

    return render_template('lista_musica.html',nome = nome, musicaLista = MUSICA, musicaEditada=musica_editada)

@usuario_route.route('/<int:musica_id>/delete', methods = ['DELETE'])
def deletarMusica(musica_id):
    global MUSICA
    MUSICA = [musica for musica in MUSICA if musica['id'] != musica_id]
    return '', 204

# @usuario_route.route('/<int:musica_id>/edit')
# def form_editar_musica(musica_id):
#     musica = None

#     for m in MUSICA:
#         if m['id'] == musica_id:
#             musica = m
    
#     return render_template('lista_musica.html',musica = musica)

# @usuario_route.route('/<int:musica_id>/update', methods = ['PUT'])
# def atualizar_musica(musica_id):
#     musica_editado = None

#     # data = request.json
#     data = request.form.get('nome')

#     for m in MUSICA:
#         if m['id'] == musica_id:
#             m['nome'] = data['nome']

#             musica_editado = m
    
#     return render_template('lista_musica.html', musica = musica_editado)

@usuario_route.route('/logout')
def logout():
    return redirect(url_for('usuario.login_usuario'))