from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'chave-secreta'

# - - Parte sessões

# - Criar sessão
@app.route('/sessao', methods=['GET', 'POST'])
def iniciar_sessao():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        return redirect(url_for('iniciar_sessao'))
    nome = session.get('nome') 
    return render_template('sessao.html', nome=nome)

# - Remover da sessão
@app.route('/limpar_sessao')
def limpar_sessao():
    session.pop('nome', None)
    return redirect(url_for('iniciar_sessao'))

# - - Parte cookies

# - Criar cookies

