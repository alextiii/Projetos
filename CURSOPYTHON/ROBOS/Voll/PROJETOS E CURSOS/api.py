from flask import Flask, jsonify

app = Flask(__name__)

# Rota para o endpoint principal
@app.route('/')
def index():
    return 'Bem-vindo à sua API simples!'

# Rota para um endpoint que retorna dados em formato JSON
@app.route('/api/exemplo', methods=['GET'])
def exemplo():
    dados = {'mensagem': 'Isso é um exemplo de retorno JSON.'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
python app.py
