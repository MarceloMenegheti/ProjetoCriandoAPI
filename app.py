#APi - é um lugar para disponibilar recursos ou funcionalidades

# 1. Objetivo - Criar um api de disponibiliza a consulta, criação, edição e exclusão de livros 

# 2. URL base - localHost

# 3. EndPoints - 
    # - localHost/livros (GET)
    # - localHost/livros (POST)
    # - localHost/livros/id (GET)
    # - localHost/livros/id (PUT)
    # - localHost/livros/id (DELETE)

# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'Titulo':'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tokkien'
    },
    {
        'id':2,
        'Titulo':'Harry Potter e a pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id':3,
        'Titulo':'James Clear',
        'autor': 'Hábitos Atômicos'
    }
]

# consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_Id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_um_livro_id(id):
    request.get_json()
    for i,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livro_alterado)
            return jsonify(livros[i])

# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for i,livro in enumerate(livros):
        if livro.get(id) == id:
            del livros[i]
    return jsonify(livros)


app.run(port=5000,host='localHost',debug=True)