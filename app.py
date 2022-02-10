from flask import Flask, g
import sqlite3
# da lib flask, me importe um element Flask (classe)
# hello abaixo é o nome do app
#flask run
DATABASE = "blog.bd"
SECRETE_KEY = "pudim"

app = Flask(__name__)
app.config.from_object(__name__)
#vai tirar as config d eum object,
# e é desse arquivo aqui, "__name__"

#bd - banco de dados
def conectar_bd():
    return sqlite3.connect(DATABASE)

#abrindo a conexao com o banco
@app.before_request
def antes_requisicao():
    #abrir conexao com banco e gravar numa variavel do flask
    g.bd = conectar_bd()
    #g --> recurso do flask (importado)

#teardown = desmonta; desmontaod a conexao
@app.teardown_request
#exc = exception // try, except, raise
def fim_requisicao(exc):
    g.bd.close()

@app.route("/")
#@app.route("/home")
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    # *maneira simples acima; isso acima é só uma string
    #return "Hello from Flask"
    cur = g.bd.execute(sql)
    #cur é alguma coisa do banco de dados
    entradas = []
    return str(entradas)


#@app.route("/pudim")
#def pudim():
#    return "I love pudim"
    