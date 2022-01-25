from bottle import get, route, run, request, template,error
import os

@route('/')
def login():
	return template('login')

def verificar_login (nome_usuario, senha):
	d = {'Marcelo': '123456', 'Grogu': '123456', 'Anakin': '123456'}
	if nome_usuario in d.keys() and d[nome_usuario] == senha:
		return True
	return False


@route('/login', method='POST')
def executar_login():
	nome_usuario = request.forms.get('nome_usuario')
	senha = request.forms.get('senha')
	return template('verificacao_login', sucesso=verificar_login(nome_usuario, senha), nome=nome_usuario)

@error(404)
def error404(error):
	return template('pagina404')

if __name__ == "__main__":
	if os.environ.get('APP_LOCATION') == 'heroku':
		run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
	else:
		run(host='localhost', port=8080, debug=True, reloader=True)